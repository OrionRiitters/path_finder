# this class will start the app will communicate directly with the frontend and the route handler
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_trails', methods=['POST', 'GET'])
def get_trails():
    if request.method == "POST":
        city = request.form["city"]
        state = request.form["state"]
    else:
        form = request.form
        #todo get saved trails from database


@app.route('/save_trail', methods=['POST'])
def save_trails():
    return None
    #todo add trail to database using model calls
