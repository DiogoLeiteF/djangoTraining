import requests

# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, params={"product_id": 123}, json={"query":"hello world"})

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())



