import replicate
import os

try:
    prediction = replicate.run(
        "victor-upmeet/whisperx:84d2ad2d6194fe98a17d2b60bef1c7f910c46b2f6fd38996ca457afd9c8abfcb",
        input={
            "audio_file": open("episode006-christoph-jentzsch.mp3", "rb"),  # File object
            "model": "large-v3",
            "language": "en",
            "diarization": True,
            "huggingface_access_token": os.environ.get('HF_TOKEN', ''),
            "batch_size": 8
        }
    )
    print("Prediction:", prediction)
except Exception as e:
    print("Error:", e)
