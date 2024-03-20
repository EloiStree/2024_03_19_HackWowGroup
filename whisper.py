## python whisperTest.py your_api_key /path/to/input_audio_file.mp4 /path/to/output_transcription.txt


import argparse
from openai import OpenAI

def transcribe_audio(api_key, input_file, output_file):
    client = OpenAI(api_key=api_key)

    with open(input_file, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        transcription_text = transcription.text

    with open(output_file, "w") as output_file:
        output_file.write(transcription_text)

    print("Transcription saved to:", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio file using OpenAI API")
    parser.add_argument("api_key", help="Your OpenAI API key")
    parser.add_argument("input_file", help="Input audio file path")
    parser.add_argument("output_file", help="Output transcription file path")
    args = parser.parse_args()

    transcribe_audio(args.api_key, args.input_file, args.output_file)
