import requests


def rika_chat_gpt(query):

    url = "https://api.aichatos.cloud/api/generateStream"

    headers = {
        "Content-Type": "application/json",
        "Referer": "https://dev.yqcloud.top/",
        "Origin": "https://dev.yqcloud.top",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    data = {
        "prompt": query,
        "userId": "#/chat/1699182167232",
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Request was successful")        
        pack = response.text

    return pack

