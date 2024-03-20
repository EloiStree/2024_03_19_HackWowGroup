from openai import OpenAI

api_key = "sk-"  # Replace this with your actual API key
client = OpenAI(api_key=api_key)

with open("/home/kali/Desktop/AncientJapanesePoem.mp4", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    # Get the transcription text
    transcription_text = transcription.text

# Define the path for the output text file
output_file_path = "/home/kali/Desktop/Transcription.txt"

# Write the transcription text to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(transcription_text)

print("Transcription saved to:", output_file_path)
