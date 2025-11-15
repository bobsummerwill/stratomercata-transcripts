#!/usr/bin/env python3
"""
AI transcript post-processor for Ethereum/blockchain content.
Batch process transcripts with multiple AI providers.
Supports: sonnet, chatgpt, gemini, llama, qwen.
"""

import os
import sys
import json
import time
from pathlib import Path
import argparse

# Import shared utilities
from common import (Colors, success, failure, skip, validate_api_key, 
                    load_people_list, load_terms_list, start_ollama, stop_ollama, cleanup_gpu_memory)


# ============================================================================
# Utility Functions
# ============================================================================


def extract_transcriber_from_filename(filepath):
    """Parse transcriber name from intermediate filename."""
    filename = Path(filepath).stem
    
    for service in ['whisperx', 'assemblyai', 'deepgram', 'openai']:
        if f'_{service}_raw' in filename:
            basename = filename.replace(f'_{service}_raw', '')
            return basename, service
    
    return filename, "whisperx"


def save_processed_files(output_dir, basename, transcriber, processor, content):
    """Save txt (clean) and md (with timestamps)."""
    import re
    
    output_path = Path(output_dir) / f"{basename}_{transcriber}_{processor}_processed.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Clean up content - remove code fences and continuation messages
    content_lines = [line.rstrip() for line in content.split('\n')]
    content_clean = '\n'.join(content_lines)
    
    # Remove markdown code fences (triple backticks)
    content_clean = re.sub(r'^```\s*$', '', content_clean, flags=re.MULTILINE)
    content_clean = re.sub(r'^```.*$', '', content_clean, flags=re.MULTILINE)
    
    # Remove continuation messages (with square brackets or parentheses)
    content_clean = re.sub(r'\[Transcript continues.*?\]', '', content_clean, flags=re.IGNORECASE)
    content_clean = re.sub(r'\(Transcript continues.*?\)', '', content_clean, flags=re.IGNORECASE)
    
    # Clean up multiple blank lines
    content_clean = re.sub(r'\n{3,}', '\n\n', content_clean)
    content_clean = content_clean.strip()
    
    # Save text version (NO timestamps, NO markdown formatting)
    text_lines = []
    for line in content_clean.split('\n'):
        # Remove timestamp pattern [MM:SS] or [HH:MM:SS] at start of line
        clean_line = re.sub(r'^\[\d{1,2}:\d{2}(?::\d{2})?\] ', '', line)
        # Remove markdown bold formatting from speaker labels
        clean_line = re.sub(r'^\*\*(SPEAKER_\d+):\*\*$', r'\1:', clean_line)
        text_lines.append(clean_line)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_lines))
    
    # Save markdown version (WITH timestamps, convert SPEAKER_ labels to bold if not already)
    md_path = output_path.with_suffix('.md')
    md_lines = []
    for line in content_clean.split('\n'):
        # Ensure speaker labels are bold (if not already)
        if re.match(r'^SPEAKER_\d+:$', line):
            line = f"**{line}**"
        md_lines.append(line)
    
    md_content = '\n'.join(md_lines)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return output_path


# ============================================================================
# Shared instruction template for all AI providers
# ============================================================================
SYSTEM_PROMPT = "You are an expert transcript editor specializing in Ethereum and blockchain technology."

INSTRUCTION_TEMPLATE = """You are an expert transcript editor specializing in Ethereum and blockchain technology.

Context - Ethereum Ecosystem Knowledge:
{context}

Raw Transcript (from speech recognition):
{transcript}

Your tasks:
1. Fix technical term spellings and capitalization (e.g., "etherium" → "Ethereum", "nfts" → "NFTs")
2. Correct proper names using the people list provided
3. Fix blockchain concept terminology to match standard usage
4. Use generic labels SPEAKER_01, SPEAKER_02, etc. (do not add actual names)
5. Improve punctuation and sentence structure for readability
6. Add paragraph breaks at natural conversation transitions
7. **CRITICAL: PRESERVE ALL TIMESTAMPS - DO NOT REMOVE THEM**
8. Maintain speaker label format: SPEAKER_XX: (not bold, just plain text with colon)

**TIMESTAMP PRESERVATION IS ABSOLUTELY MANDATORY:**

EVERY single line of dialogue in the input has a timestamp. You MUST keep all of them in the output.

Format specifications:
- Convert timestamps to [MM:SS] format if they're not already
- Use 2 digits for minutes and seconds: [00:05], [02:12], [15:47]
- Round decimal seconds to nearest whole second
- First minute is 00 (e.g., [00:15] for 15 seconds)
- Timestamps go at the START of each dialogue line

REQUIRED OUTPUT FORMAT:

SPEAKER_01:
[00:01] Welcome everyone to today's discussion.
[00:05] We're going to talk about Ethereum.

SPEAKER_02:
[00:12] Thanks for having me.
[00:14] I'm excited to share my perspective.

DO NOT use markdown formatting:
- NO triple backticks (```)
- NO bold formatting (**SPEAKER_01:**) - just plain SPEAKER_01:
- NO "Corrected Transcript" headers
- NO continuation messages like "(Transcript continues...)"

Critical rules:
- DO NOT wrap output in code fences
- DO NOT add any preamble or explanation
- DO NOT remove or skip any timestamps from the input
- DO NOT add metadata or notes
- Just output the corrected transcript directly

If the input has timestamps like [15.8s], convert to [00:16].
If the input has timestamps like [245.3s], convert to [04:05].

Start your output immediately with the first speaker label (no introduction needed)."""

def build_prompt(context, transcript):
    """Build complete prompt from template."""
    return INSTRUCTION_TEMPLATE.format(context=context, transcript=transcript)

def load_glossary():
    """Load ethereum_glossary.json if available."""
    glossary_file = Path("ethereum_glossary.json")
    
    if glossary_file.exists():
        with open(glossary_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {
        "people": [],
        "technical_terms": [],
        "projects": [],
        "abbreviations": {}
    }

def build_context_summary():
    """Build context summary from available resources."""
    import subprocess
    
    context_parts = []
    
    # Add glossary info if available
    glossary = load_glossary()
    if glossary["people"]:
        context_parts.append(f"Key People ({len(glossary['people'])}): {', '.join(glossary['people'][:30])}")
    if glossary["technical_terms"]:
        context_parts.append(f"Technical Terms ({len(glossary['technical_terms'])}): {', '.join(glossary['technical_terms'][:50])}")
    if glossary["projects"]:
        context_parts.append(f"Projects ({len(glossary['projects'])}): {', '.join(glossary['projects'][:20])}")
    
    # Try to load from separate files if glossary doesn't exist
    if not glossary["people"]:
        # Generate people list if it doesn't exist
        people_file = Path("intermediates/ethereum_people.txt")
        if not people_file.exists():
            extract_script = Path("scripts/extract_people.py")
            if extract_script.exists():
                try:
                    print("  Generating ethereum_people.txt...")
                    subprocess.run(["python3", str(extract_script)], 
                                 check=True, capture_output=True, text=True, cwd=Path.cwd())
                except subprocess.CalledProcessError:
                    pass  # Silent failure - file may not be critical
        
        people = load_people_list()
        if people:
            context_parts.append(f"Known People ({len(people)}): {', '.join(people[:30])}")
    
    if not glossary["technical_terms"]:
        # Generate technical terms if it doesn't exist
        terms_file = Path("intermediates/ethereum_technical_terms.txt")
        if not terms_file.exists():
            extract_script = Path("scripts/extract_terms.py")
            if extract_script.exists():
                try:
                    print("  Generating ethereum_technical_terms.txt...")
                    subprocess.run(["python3", str(extract_script)], 
                                 check=True, capture_output=True, text=True, cwd=Path.cwd())
                except subprocess.CalledProcessError:
                    pass  # Silent failure - file may not be critical
        
        terms = load_terms_list()
        if terms:
            context_parts.append(f"Technical Terms ({len(terms)}): {', '.join(terms[:50])}")
    
    return "\n\n".join(context_parts) if context_parts else "No additional context available."

def process_with_anthropic(transcript, api_key, context):
    """Process transcript using Claude Sonnet 4.5 with streaming."""
    try:
        import anthropic
    except ImportError:
        raise ImportError("anthropic package not installed. Install with: pip install anthropic")
    
    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Processing: ", end='', flush=True)
    
    result = ""
    chunk_count = 0
    
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=64000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            result += text
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def process_with_openai(transcript, api_key, context):
    """Process transcript using GPT-4o with streaming."""
    model = "gpt-4o"  # Using gpt-4o instead of chatgpt-4o-latest for better output capacity
    try:
        import openai
    except ImportError:
        raise ImportError("openai package not installed. Install with: pip install openai")
    
    client = openai.OpenAI(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Model: {model}")
    print(f"      Processing: ", end='', flush=True)
    
    result = ""
    chunk_count = 0
    
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=16384,  # gpt-4o supports up to 16K output tokens
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            result += chunk.choices[0].delta.content
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def process_with_gemini(transcript, api_key, context):
    """Process transcript using Gemini 2.5 Pro with streaming."""
    model = "gemini-2.5-pro"
    try:
        import google.generativeai as genai
    except ImportError:
        raise ImportError("google-generativeai package not installed")
    
    genai.configure(api_key=api_key)
    prompt = build_prompt(context, transcript)
    
    print(f"      Processing: ", end='', flush=True)
    
    model_instance = genai.GenerativeModel(model)
    result = ""
    chunk_count = 0
    
    response = model_instance.generate_content(prompt, stream=True)
    
    for chunk in response:
        if chunk.text:
            result += chunk.text
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def process_with_groq(transcript, api_key, context):
    """Process transcript using Llama 3.3 70B (via Groq) with streaming."""
    model = "llama-3.3-70b-versatile"
    try:
        import openai
    except ImportError:
        raise ImportError("openai package not installed")
    
    client = openai.OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
    prompt = build_prompt(context, transcript)
    
    print(f"      Model: {model}")
    print(f"      Processing: ", end='', flush=True)
    
    result = ""
    chunk_count = 0
    
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=8000,
        temperature=0.3,
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            result += chunk.choices[0].delta.content
            chunk_count += 1
            if chunk_count % 100 == 0:
                print(".", end='', flush=True)
    
    print(" ✓")
    return result

def estimate_tokens(text):
    """Estimate tokens (words × 1.3)."""
    return int(len(text.split()) * 1.3)

def process_with_qwen(transcript, context, ollama_process=None):
    """Process transcript using Qwen 2.5 14B (via Ollama)."""
    import subprocess
    import time
    
    try:
        import requests
        import json
    except ImportError:
        raise ImportError("requests package not installed")
    
    # Use 14B model (optimized for 12GB GPUs like RTX 5070)
    model = "qwen2.5:14b"
    print(f"      Model: {model}")
    
    started_ollama = False
    
    try:
        # Start Ollama if not running
        if ollama_process is None:
            ollama_process = start_ollama()
            if ollama_process is not None:
                started_ollama = True
        
        # Process transcript
        prompt = build_prompt(context, transcript)
        print(f"      Processing: ", end='', flush=True)
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": True,
                "options": {
                    "temperature": 0.3
                }
            },
            timeout=1800,
            stream=True
        )
        response.raise_for_status()
        
        result = ""
        chunk_count = 0
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                if "response" in chunk:
                    result += chunk["response"]
                    chunk_count += 1
                    if chunk_count % 50 == 0:
                        print(".", end='', flush=True)
                if chunk.get("done", False):
                    break
        
        print(" ✓")
        return result, ollama_process if started_ollama else None
        
    except Exception as e:
        print(f" {failure(f'Error: {e}')}")
        if started_ollama and ollama_process:
            ollama_process.terminate()
        return None, None

def process_single_combination(transcript_path, provider, api_keys, context, ollama_process=None):
    """Process single transcript with single provider."""
    start_time = time.time()
    
    # Load transcript
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    
    # Get output file paths for potential cleanup
    basename, transcriber = extract_transcriber_from_filename(transcript_path)
    output_txt = Path("outputs") / f"{basename}_{transcriber}_{provider}_processed.txt"
    output_md = Path("outputs") / f"{basename}_{transcriber}_{provider}_processed.md"
    
    # Process with appropriate provider
    corrected = None
    new_ollama_process = None
    
    try:
        if provider == "sonnet":
            corrected = process_with_anthropic(transcript, api_keys['sonnet'], context)
        elif provider == "chatgpt":
            corrected = process_with_openai(transcript, api_keys['chatgpt'], context)
        elif provider == "gemini":
            corrected = process_with_gemini(transcript, api_keys['gemini'], context)
        elif provider == "llama":
            corrected = process_with_groq(transcript, api_keys['llama'], context)
        elif provider == "qwen":
            corrected, new_ollama_process = process_with_qwen(transcript, context, ollama_process)
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"      {failure(f'Processing failed ({elapsed:.1f}s): {e}')}")
        
        # Clean up any partial files that may have been created
        for partial_file in [output_txt, output_md]:
            if partial_file.exists():
                try:
                    partial_file.unlink()
                    print(f"      → Deleted partial file: {partial_file.name}")
                except Exception as cleanup_error:
                    print(f"      ⚠ Could not delete {partial_file.name}: {cleanup_error}")
        
        return None, new_ollama_process, elapsed
    
    if not corrected:
        elapsed = time.time() - start_time
        print(f"      {failure(f'Processing failed ({elapsed:.1f}s): No output generated')}")
        
        # Clean up any partial files
        for partial_file in [output_txt, output_md]:
            if partial_file.exists():
                try:
                    partial_file.unlink()
                    print(f"      → Deleted partial file: {partial_file.name}")
                except Exception as cleanup_error:
                    print(f"      ⚠ Could not delete {partial_file.name}: {cleanup_error}")
        
        return None, new_ollama_process, elapsed
    
    # Save using utility function (basename/transcriber already extracted above)
    output_path = save_processed_files(
        "outputs",
        basename,
        transcriber,
        provider,
        corrected
    )
    
    elapsed = time.time() - start_time
    print(f"      ✓ Saved: {output_path} ({elapsed:.1f}s)")
    
    return output_path, new_ollama_process, elapsed

def main():
    parser = argparse.ArgumentParser(
        description="Post-process transcripts with multiple AI providers",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("transcripts", nargs='+', help="Transcript file path(s)")
    parser.add_argument("--processors", required=True,
                       help="Comma-separated list of processors (sonnet,chatgpt,gemini,llama,qwen)")
    
    args = parser.parse_args()
    
    # Clean up any dangling Ollama processes at startup
    try:
        import subprocess
        import requests
        
        # Check if Ollama is running
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=1)
            if response.status_code == 200:
                print("Stopping dangling Ollama process...")
                subprocess.run(['pkill', '-f', 'ollama serve'], 
                             stdout=subprocess.DEVNULL, 
                             stderr=subprocess.DEVNULL,
                             timeout=5)
                time.sleep(2)  # Give it time to stop
                print("✓ Cleared")
        except:
            pass  # Not running, nothing to clean up
    except Exception as e:
        # Non-fatal if cleanup fails
        print(f"⚠ Warning: Could not clean up dangling processes: {e}")
    
    # Parse processors
    processors = [p.strip() for p in args.processors.split(',')]
    valid_processors = {'sonnet', 'chatgpt', 'gemini', 'llama', 'qwen'}
    
    for proc in processors:
        if proc not in valid_processors:
            print(f"Error: Unknown processor '{proc}'")
            print(f"Valid options: {', '.join(sorted(valid_processors))}")
            sys.exit(1)
    
    # Check if Qwen requested on CPU-only system
    if 'qwen' in processors:
        try:
            import torch
            has_gpu = torch.cuda.is_available()
            
            if not has_gpu:
                # CPU-only system - skip Qwen with warning
                print()
                print(f"{Colors.YELLOW}⚠️  QWEN SKIPPED: GPU Required{Colors.RESET}")
                print()
                print("Qwen requires NVIDIA GPU with 12GB+ VRAM for transcript processing.")
                print("Current system: CPU-only")
                print()
                print("• Qwen 7B (CPU) is insufficient for complex transcript editing tasks")
                print("• Qwen 32B (GPU) would work excellently on RTX 5070 12GB or similar")
                print()
                print("Skipping Qwen processing - all other processors will continue normally.")
                print()
                
                # Remove qwen from processors list
                processors = [p for p in processors if p != 'qwen']
                
                if not processors:
                    print("Error: No processors remaining after skipping Qwen")
                    sys.exit(1)
        except ImportError:
            # If torch not available, can't use Qwen anyway
            print()
            print(f"{Colors.YELLOW}⚠️  QWEN SKIPPED: PyTorch not available{Colors.RESET}")
            print()
            processors = [p for p in processors if p != 'qwen']
            
            if not processors:
                print("Error: No processors remaining after skipping Qwen")
                sys.exit(1)
    
    # Check API keys using utility
    api_keys = {}
    skip_processors = []
    
    # Map processor names to their environment variable names
    key_mapping = {
        'sonnet': 'ANTHROPIC_API_KEY',     # Claude Sonnet 4.5 via Anthropic
        'chatgpt': 'OPENAI_API_KEY',       # ChatGPT-4o-latest via OpenAI
        'gemini': 'GOOGLE_API_KEY',        # Gemini 2.5 Pro via Google
        'llama': 'GROQ_API_KEY'            # Llama 3.3 70B via Groq
    }
    
    for proc in processors:
        if proc == 'qwen':
            # Qwen (local via Ollama) doesn't need an API key
            continue
        
        env_var = key_mapping.get(proc)
        if env_var:
            key, error = validate_api_key(env_var)
            if error:
                print(f"⊘ Skipping {proc}: {error}")
                skip_processors.append(proc)
            else:
                api_keys[proc] = key
    
    # Remove skipped processors
    processors = [p for p in processors if p not in skip_processors]
    
    if not processors:
        print("\nError: No processors available (all API keys missing)")
        sys.exit(1)
    
    # Build context once
    print("\nBuilding context from glossary...")
    context = build_context_summary()
    print(f"✓ Context built: {len(context)} characters")
    print()
    
    # Process all combinations
    total = len(args.transcripts) * len(processors)
    success_count = 0
    failed_count = 0
    combo_num = 0
    combo_times = []
    
    print("="*70)
    print(f"Processing {len(args.transcripts)} transcript(s) × {len(processors)} processor(s) = {total} combinations")
    print("="*70)
    print()
    
    ollama_process = None
    pipeline_start = time.time()
    
    try:
        for transcript_path in args.transcripts:
            if not Path(transcript_path).exists():
                print(f"✗ Transcript not found: {transcript_path}")
                failed_count += len(processors)
                continue
            
            for processor in processors:
                combo_num += 1
                print(f"[{combo_num}/{total}] {Path(transcript_path).name} + {processor}")
                
                result, new_ollama_process, elapsed = process_single_combination(
                    transcript_path, processor, api_keys, context, ollama_process
                )
                
                # Update Ollama process reference if it was started
                if new_ollama_process:
                    ollama_process = new_ollama_process
                
                if result:
                    success_count += 1
                    combo_times.append((Path(transcript_path).name, processor, elapsed))
                else:
                    failed_count += 1
                
                print()
    
    finally:
        # Clean up Ollama if we started it (using shared function)
        if ollama_process:
            stop_ollama(ollama_process)
    
    # Summary with timing
    pipeline_elapsed = time.time() - pipeline_start
    
    print("="*70)
    print("✓ Post-Processing Complete")
    print("="*70)
    print(f"Total combinations: {total}")
    print(f"Successful: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"Skipped: {len(skip_processors) * len(args.transcripts)}")
    print()
    print(f"Total time: {pipeline_elapsed:.1f}s ({pipeline_elapsed/60:.1f}min)")
    
    if combo_times:
        print()
        print("Per-combination timing:")
        for transcript, processor, elapsed in combo_times:
            print(f"  {transcript} + {processor}: {elapsed:.1f}s")
        
        if len(combo_times) > 1:
            avg_time = sum(t[2] for t in combo_times) / len(combo_times)
            print(f"\n  Average: {avg_time:.1f}s per combination")
    
    print()
    print("Output files in: ./outputs/")
    print("="*70)
    
    sys.exit(0 if failed_count == 0 else 1)

if __name__ == "__main__":
    main()
