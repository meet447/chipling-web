from flask import Flask, render_template, redirect, request, json
from service.chat import create_chat, load_chats, get_chat
import uuid, requests, json
from llm.rika import Rika 
from llm.Rikav2 import Rikav2
from service.character import character_builder

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/home')

@app.route('/home')
def home():
    data = load_chats()
    return render_template('home.html', data=data)

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/chat/<id>')
def chat(id):
    data = get_chat(id=id)
    return render_template('chat.html', id=data)

@app.route("/info/<id>")
def info_page(id):
    data = get_chat(id=id)
    return render_template('info.html', data=data)

@app.route("/create", methods=['GET'])
def create():
    
    return render_template("create.html")

@app.route('/create_chat', methods=['POST'])
def create_backbone():
    user = request.form['user']
    name = request.form['name']
    short_desc = request.form['short_desc']
    long_desc = request.form['long_desc']
    scenario = request.form['scenario']
    origin = request.form['origin']
    chat = request.form['chat']
    image = request.form['image']
    uui = uuid.uuid1()
    id = uui.hex
        
    create_chat(user=user, name=name, chat=chat, short_desc=short_desc, long_desc=long_desc, scenario=scenario, origin=origin, id=id, image=image)
        
    return redirect('/chat/'+id)

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data["text"]
    id = data["id"]
        
    details = get_chat(id=id)
        
    name = details[0]["name"]
    desc = details[0]["long_desc"]
    scenario = details[0]["dialouge"]
    chat = details[0]["chat"]

    prompt = character_builder(name=name, description=desc, chat=chat, scenario=scenario)

    # Call your AI model here to generate the bot response
    response = Rikav2(query=prompt + user_message + "\n{{char}}:")
    
    print(response)

    return json.dumps({"response": response})


################################################AAAAAAAAAAAAAAPPPPPPPPPPPPPPPPIIIIIIII###########################################
    
@app.route('/api')
def api():
    return "API WORKING"

@app.route('/api/rikav1')
def rikav1():
    return
    
app.run(debug=True, host="0.0.0.0")

