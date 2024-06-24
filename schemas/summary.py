import requests
import os
import load_dotenv

load_dotenv.load_dotenv()
API_URL = "https://api-inference.huggingface.co/models/callmequan137/T5_xsum"
KEY = os.getenv("MODEL_KEY")


headers = {"Authorization": f"Bearer {KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

with open('schemas/test.txt', 'r', encoding='utf-8') as file:
    content = file.read()

output = query({
	"inputs": content,
})
print(output)