import requests

url = "https://rika-web.meetsonawane.repl.co/api/rikav1" #rikav2 for faster and better api endpoint

data = {
    'text': 'who are you',
    'id': '2f2bd08f350b11eea28ce323b8e85112'#your charc id here 
}

# Send the POST request
response = requests.post(url, json=data)

data = response.json()

print(data)


