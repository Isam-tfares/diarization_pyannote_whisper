import whisper
from pyannote.audio import Pipeline
from utils import diarize_text

def diarize(audio_path):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                        use_auth_token="")
    model = whisper.load_model("tiny")

    asr_result = model.transcribe(audio_path)
    diarization_result = pipeline(audio_path)
    final_result = diarize_text(asr_result, diarization_result)

    for seg, spk, sent in final_result:
        line = f'{seg.start:.2f} {seg.end:.2f} {spk} {sent}'
        print(line)