# this class will start the app will communicate directly with the frontend and the route handler
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index')