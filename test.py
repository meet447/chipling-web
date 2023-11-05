import requests

url = "http://127.0.0.1:5000/api/rikav2"

data = {
    "text": "hello",
    "id": "02be4dd534fb11ee8f59c85acfdc7de9"
}

# Send a POST request to the API endpoint
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    result = response.json()
    print("API Response:", result)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response content:", response.text)