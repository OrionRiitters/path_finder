
# this class will start the app will communicate directly with the frontend and the route handler
from flask import Flask, render_template, request, redirect
from states import STATES
import handlers.api_handler as api
import handlers.database_handler as db
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
        trails = api.get_trails_from_location(city, state)
        return trails # This return statement just stops a 500 error from occuring
    else:
        bucket_list = db.get_bucket_list()
        return bucket_list  # This return statement just stops a 500 error from occuring


@app.route('/save_trail', methods=['POST'])
def save_trails():
    id = request.form["id"]
    db.save_trails(id)
    redirect('/')
    #todo add trail to database using model calls