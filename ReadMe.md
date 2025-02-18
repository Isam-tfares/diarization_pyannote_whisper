# Diarization Script

This script performs speaker diarization on an audio file.

## Requirements

Ensure you have Python installed along with the necessary dependencies.

## Installation

1. Clone the repository or download the script.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:
```bash
python main.py --audio <path_to_audio_file> --token <your_token>
```

### Example
```bash
python main.py --audio sample_audio.wav --token my_secret_token
```

## Output

The script will print the diarization result of the given audio file.

## Notes

- Ensure that the `model.py` file contains a function `diarize(audio_path, token)` that handles the diarization process.
- The script requires an audio file and an authentication token as input.

