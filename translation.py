## python translation.py your_api_key /path/to/input_audio_file.mp3 /path/to/output_translation.txt


import argparse
from openai import OpenAI

def translate_audio(api_key, input_file, output_file):
    client = OpenAI(api_key=api_key)

    with open(input_file, "rb") as audio_file:
        translation = client.audio.translations.create(
            model="whisper-1", 
            file=audio_file
        )
        translation_text = translation.text

    with open(output_file, "w") as output_file:
        output_file.write(translation_text)

    print("Translation saved to:", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate audio file using OpenAI API")
    parser.add_argument("api_key", help="Your OpenAI API key")
    parser.add_argument("input_file", help="Input audio file path")
    parser.add_argument("output_file", help="Output translation file path")
    args = parser.parse_args()

    translate_audio(args.api_key, args.input_file, args.output_file)
