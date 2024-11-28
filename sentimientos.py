import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I hate you",
})

print(output)

#procesar este output en lugar de un json que devuelva el mensaje y lo que es mayormente