
# this class will start the app will communicate directly with the frontend and the route handler
from flask import Flask, render_template, request
from states import STATES
app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders initial HTML template. cssFile designates style used from static/css.
    """
    return render_template('index.html', states=STATES, cssFile='style.css')


@app.route('/get_trails', methods=['POST', 'GET'])
def get_trails():
    if request.method == "POST":
        city = request.form["city"]
        state = request.form["state"]
        return 'asdf' # This return statement just stops a 500 error from occuring
    else:
        form = request.form
        return 'asdf'  # This return statement just stops a 500 error from occuring


@app.route('/save_trail', methods=['POST'])
def save_trails():
    return None
    #todo add trail to database using model calls
