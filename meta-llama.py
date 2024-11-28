from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B-Instruct", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message)