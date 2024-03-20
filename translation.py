from openai import OpenAI

api_key = "sk-"  # Replace this with your actual API key
client = OpenAI(api_key=api_key)

audio_file= open("/home/kali/Desktop/atoutalheure.mp3", "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
translation_text = translation.text

# Define the path for the output text file
output_file_path = "/home/kali/Desktop/translation.txt"

# Write the transcription text to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(translation_text)

print("Translation saved to:", output_file_path)
