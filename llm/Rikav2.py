import requests

def Rikav2(query):
    
    print(query)

    url = "https://api.harpy.chat/llm/harpyai-huggingface"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://harpy.chat",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
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
