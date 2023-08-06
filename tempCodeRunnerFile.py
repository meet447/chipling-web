from flask import Flask, render_template, redirect, request, json
from service.chat import create_chat, load_chats, get_chat
import uuid
import requests
from llm.rika import Rika 
from llm.Rikav2 import Rikav2
from service.character import character_builder

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
    id = data["id"]
    
    print(data)
    
    details = get_chat(id=id)
    
    print(details)
    
    name = details[0]["name"]
    desc = details[0]["long_desc"]
    
    scenario = "Her office, in the Public Safety building. . . <Start> \n"
    chat = "{{char}}: *you enter her office, she looks at you*\n\n\"Who are you?\"\n{{user}}:"

    print(user_message)
    print(name)
    print(desc)
    
    prompt = character_builder(name=name, description=desc, chat=chat, scenario=scenario)


    # Call your AI model here to generate the bot response
    response = Rikav2(query=prompt + user_message + "\n{{char}}:")
    
    print(response)

    return json.dumps({"response": response})
    
    
app.run(debug=True)

