﻿# Rika Web 

**Rika web** is a web application that allows users to create and share their own AI-powered chat characters on the [rika AI](https://rika-web.meetsonawane.repl.co) platform. The application provides a user-friendly interface for creating chat characters, browsing community-based AI models, and utilizing various AI services through APIs.

## Images
![IMG-20230809-WA0021](https://github.com/meet447/rika-web/assets/51074036/b7bec825-3364-4493-bb6c-7bc2b0185ffe)

## Features

- Create and Upload Chat Characters: Users can create and upload their own chat characters by providing information like name, description, chat text, and more.
- Browse Community-Based AI Models: Users can explore AI models created by the community and interact with them using natural language inputs.
- API Services: The application provides API endpoints for interacting with different AI models, including text-to-response and text-to-image functionalities.

## How to Use

1. **Clone the Repository**: `git clone https://github.com/meet447/rika-web.git`
2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using `pip install -r requirements.txt`.
3. **Configure AI Models**: Set up the AI models or endpoints you'll be interacting with, such as the `rika.ai` models or other AI services.
4. **Start the Application**: Run the Flask application using `python app.py`. The application will be accessible at `http://localhost:5000`.

## Routes

- `/home`: Browse and interact with community-based chat characters.
- `/create`: Create your own chat characters and upload them to the platform.
- `/status`: Check the status of the application.
- `/api`: API root endpoint.
- `/api/rikav1`: Interact with an AI model for text-to-response using the RikaV1 API.
- `/api/rikav2`: Interact with an AI model for text-to-response using the RikaV2 API.
- `/api/rikadel`: Interact with an AI model for text-to-image using the RikaDel API.

## API Endpoints

### POST `/api/rikav1`

Interact with the RikaV1 AI model for text-to-response functionality.

#### Request

```python
import requests

url = "http://127.0.0.1:5000/api/rikav1"#rikav2 for faster and better api endpoint

data = {
    'text': 'who are you',
    'id': '2f2bd08f350b11eea28ce323b8e85112'#your charc id here 
}

# Send the POST request
response = requests.post(url, json=data)

data = response.json()

print(data)
```

**Contributing**

We welcome contributions from the community! Feel free to open issues, submit pull requests, or suggest new features.


Simply create a `README.md` file in your project directory and paste this content into it. Adjust the URLs, placeholders, and details according to your application's specifics.
