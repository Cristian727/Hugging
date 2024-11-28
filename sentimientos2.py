import requests
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"

headers = {"Authorization": f"Bearer {TOKEN}"}

# Función para hacer la consulta a la API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Procesar la respuesta de la API para hacerla más comprensible
def procesar_sentimiento(texto):
    # Realizamos la consulta a la API
    output = query({
        "inputs": texto,
    })
    
    # Obtener el sentimiento desde la respuesta
    label = output[0]['label']  # 'LABEL_0', 'LABEL_1', 'LABEL_2'
    score = output[0]['score']  # Confianza en el sentimiento

    # Mapeo de las etiquetas a sentimientos más comprensibles
    sentimientos = {
        'LABEL_0': 'Negativo',
        'LABEL_1': 'Neutro',
        'LABEL_2': 'Positivo'
    }

    # Mostrar el resultado
    sentimiento = sentimientos.get(label, 'Desconocido')
    return f"El sentimiento de la frase '{texto}' es {sentimiento} con una confianza de {score:.2f}."

# Ejemplo de uso
texto = "I hate you"
resultado = procesar_sentimiento(texto)
print(resultado)
