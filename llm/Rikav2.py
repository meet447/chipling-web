import requests

def Rikav2(query):
    
    print(query)

    url = "https://api.harpy.chat/llm/harpyai-huggingface"

    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IkFEZU90TFA0cXliZUxTWVYiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjk5MTcyNjU3LCJpYXQiOjE2OTkxNjkwNTcsImlzcyI6Imh0dHBzOi8vZWhncXh4b2V5cXNkZ3F1enpvbmQuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjMwZDc2OWQ2LTdhYzMtNDBlOC1iYzI2LTJjMjY0OGM2MGNkOSIsImVtYWlsIjoibWFvdXNlbnBhaTQ4QGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUFjSFR0Zmd0dGs0MWttNmZ5eUxpbHBLbTVnb3dwUjhqM3NnSjJRMkV5cTRyRlZ5PXM5Ni1jIiwiZW1haWwiOiJtYW91c2VucGFpNDhAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZ1bGxfbmFtZSI6Ik1hb3VTZW5wYWkiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoiTWFvdVNlbnBhaSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQWNIVHRmZ3R0azQxa202Znl5TGlscEttNWdvd3BSOGozc2dKMlEyRXlxNHJGVnk9czk2LWMiLCJwcm92aWRlcl9pZCI6IjEwNTk3MDkzMjEzMTIwMjIzODc2MiIsInN1YiI6IjEwNTk3MDkzMjEzMTIwMjIzODc2MiJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNjkxMzE3ODI1fV0sInNlc3Npb25faWQiOiI1ODI2NmY0Mi0yYWQ1LTQ3NzQtYThkNy1kOWQ2NDJkYmZkNmIifQ.cNIoYRzc2nK9s8h72s6Mqk5pki60_1ljxDJP0o_e_GI",
    "Content-Type": "application/json",
    "Origin": "https://harpy.chat",
    "Referer": "https://harpy.chat/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    payload = {
        "model": "llama-2-7b-chat",
        "max_new_token": 120,
        "messages": query,
        "temperature": 0.8,
    }

    response = requests.post(url, json=payload, headers=headers)

    print(f"Status Code: {response.status_code}")
    answer = response.json()
    
    print(answer)
    
    res = answer[0]['generated_text']
    
    return res
