import requests

# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/products/11111111111111/"


# get_response = requests.get(endpoint, params={"product_id": 123}, json={"query":"hello world"})
get_response = requests.get(endpoint)

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
