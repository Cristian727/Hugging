from huggingface_hub import InferenceClient
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
promp = input("¿Qué quieres preguntar?")

client = InferenceClient(api_key=TOKEN)

messages = [
	{
		"role": "user",
		"content": promp
	}
]

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B-Instruct", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message)