import replicate
import os

os.environ['REPLICATE_API_TOKEN'] = ''

try:
    prediction = replicate.run(
        "victor-upmeet/whisperx:84d2ad2d6194fe98a17d2b60bef1c7f910c46b2f6fd38996ca457afd9c8abfcb",
        input={
            "audio_file": open("episode006-christoph-jentzsch.mp3", "rb"),  # File object
            "model": "large-v3",
            "language": "en",
            "diarization": True,
            "huggingface_access_token": "hf_" + os.environ.get('HF_TOKEN', ''),  # Add HF token prefix
            "batch_size": 8
        }
    )
    print("Prediction:", prediction)
except Exception as e:
    print("Error:", e)
