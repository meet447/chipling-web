from flask import Flask, render_template, redirect, request, json
from service.chat import create_chat, load_chats, get_chat
import uuid
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/chat/<id>')
def chat(id):
    data = get_chat(id=id)
    return render_template('chat.html', id=data)

@app.route("/create", methods=['GET'])
def create():
    
    return render_template("create.html")

@app.route('/create_chat', methods=['POST'])
def create_backbone():
    user = request.form['user']
    name = request.form['name']
    short_desc = request.form['short_desc']
    long_desc = request.form['long_desc']
    alias = request.form['alias']
    origin = request.form['origin']
    uui = uuid.uuid1()
    id = uui.hex
        
    create_chat(user=user, name=name, short_desc=short_desc, long_desc=long_desc, alias=alias, origin=origin, id=id)
        
    return redirect('/chat/'+id)

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data["text"]

    # Send the user's message to the external AI chatbot API
    url = "https://waifu4all.meetsonawane.repl.co/api/mai"
    response = requests.post(url, json={"text": user_message})
    
    print(response)

    try:
        response.raise_for_status()  # Check for HTTP errors
        if response.text.strip():  # Check if the response body is not empty
            result = response.json()
            if "response" in result:
                bot_response = result["response"]
                return json.dumps({"response": bot_response}), 200
            else:
                return json.dumps({"response": "Error: Invalid response format from the API"}), 500
        else:
            return json.dumps({"response": "Error: Empty response from the API"}), 500
    except requests.exceptions.HTTPError as http_err:
        return json.dumps({"response": f"HTTP error occurred: {http_err}"}), 500
    except requests.exceptions.RequestException as req_err:
        return json.dumps({"response": f"Request error occurred: {req_err}"}), 500
    except requests.exceptions.JSONDecodeError:
        return json.dumps({"response": "Error: Invalid JSON response from the API"}), 500
    except KeyError:
        return json.dumps({"response": "Error: Unexpected response format from the API"}), 500

app.run(debug=True)