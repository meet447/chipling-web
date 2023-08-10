import requests

url = "https://rika-web.meetsonawane.repl.co/api/rikandel" #rikav2 for faster and better api endpoint

data = {
    'text': 'girl rinding a bunny',
}

# Send the POST request
response = requests.post(url, json=data)

data = response.json()

print(data)


