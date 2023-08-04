from flask import Flask, render_template, redirect, request, json

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

app.run(debug=True)