import requests

def rikadel(prompt):

    url = "https://www.kapwing.com/api/v2/generate/images?"

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
        "Content-Type": "application/json",
        "Cookie": "ssrSignedInCookie=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NGI1NTNhMjgzNDIxODAyM2MyNzcxYzQiLCJhY2NvdW50VHlwZSI6MCwibmFtZSI6Ik1hb3VTZW5wYWkiLCJlbWFpbCI6Im1hb3VzZW5wYWk0OEBnbWFpbC5jb20iLCJyb2xlIjoiZGVmYXVsdCIsImlhdCI6MTY4OTYwNTAyNiwiZXhwIjoxNzIxMTQxMDI2fQ.EoIHLlNcwfHg2gi3roeqr0eSRZZEH_2dfIzeuJQa-Gc",
        "Referer": "https://www.kapwing.com/64b553a43d5edc00105170dd/studio/editor",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-Access-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NGI1NTNhMjgzNDIxODAyM2MyNzcxYzQiLCJhY2NvdW50VHlwZSI6MCwibmFtZSI6Ik1hb3VTZW5wYWkiLCJlbWFpbCI6Im1hb3VzZW5wYWk0OEBnbWFpbC5jb20iLCJyb2xlIjoiZGVmYXVsdCIsImlhdCI6MTY4OTYwNTAyNiwiZXhwIjoxNzIxMTQxMDI2fQ.EoIHLlNcwfHg2gi3roeqr0eSRZZEH_2dfIzeuJQa-Gc"
    }

    parameter = { "prompt": prompt}

    response = requests.get(url, headers=headers, params=parameter)
    data = response.json()

    return data
    