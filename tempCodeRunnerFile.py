from flask import Flask, render_template, redirect, request, json
from service.chat import create_chat, load_chats

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/chat/<id>')
def chat(id):
    return render_template('chat.html', id=id)

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
        
    create_chat(user=user, name=name, short_desc=short_desc, long_desc=long_desc, alias=alias, origin=origin)
        
    return redirect('/home')


app.run(debug=True)