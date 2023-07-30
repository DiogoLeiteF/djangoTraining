import requests

# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is required",
}

get_response = requests.post(endpoint, json=data)


print(get_response.json())
