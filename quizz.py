from openai import OpenAI

# Set up the OpenAI API client - change this to your API key
api_key = "sk-"  # Replace this with your actual API key
client = OpenAI(api_key=api_key)

fichier_texte = "/home/kali/Desktop/Transcription.txt"

# Ouvrir le fichier texte et lire son contenu
with open(fichier_texte, 'r') as file:
    prompt = file.read()

completion = client.chat.completions.create(

	model="gpt-3.5-turbo-1106",
	messages=[
		
		{"role":"system","content":"Tu es un créateur de Quizz / prof qui veut verifier que des eleves on bien lu et compris un texte "},
		{"role":"user","content":"Compose un quizz avec le texte suivant ta reponse doit commencer par VOICI UN QUIZZ parlant du sujet: " + prompt}
	]
)

message = completion.choices[0].message.content
with open("/home/kali/Desktop/Quizz.txt", "w") as output_file:
    output_file.write(message)
