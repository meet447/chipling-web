import requests

url = "http://127.0.0.1:5000/api/rikav1"

data = {
    'text': 'who are you',
    'id': '2f2bd08f350b11eea28ce323b8e85112'
}

# Send the POST request
response = requests.post(url, json=data)

data = response.json()

print(data)
