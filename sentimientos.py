import requests
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")


API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"


headers = {"Authorization": f"Bearer {TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "I love you", 
})

print(output)

#procesar este output para que en lugar de un json que devuelva el mensaje y lo que es mayormente, si positivo, neutro o negativo, que seamas humano