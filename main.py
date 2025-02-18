import argparse
from model import diarize

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="diarization of an audio file"
    )
    parser.add_argument("--audio", required=True, type=str)
    args = parser.parse_args()

    audio_path = args.audio

    print(diarize(audio_path))