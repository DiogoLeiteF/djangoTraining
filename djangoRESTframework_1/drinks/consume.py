import requests

base = "http://127.0.0.1:8000/drinks/"

response = requests.get(base)

print(response.json())