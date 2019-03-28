
# this class will start the app will communicate directly with the frontend and the route handler
from flask import Flask, render_template, request
from states import STATES
import json
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
        res = json.dumps([{
            'id': 7000543,
            'name': 'Big Trail',
            'location': 'Boise, Idaho',
            'description': 'Biggest trail in the west! This good ol\' trail features ugly hills and the world\'s largest mall.',
            'difficulty': 'blueBack',
            'stars': 3.4,
            'longitude': -105.2755,
            'latitude': 39.9787,
            'length': 6.7,
            'imgMedium': 'https://cdn-files.apstatic.com/hike/7005382_medium_1435421346.jpg'
        },
            {'id': 7002243,
            'name': 'Small Trail',
            'location': 'Boise, Idaho',
            'description': 'Biggest trail in the west! This good ol\' trail features ugly hills and the world\'s largest mall.',
            'difficulty': 'blueBack',
            'stars': 3.4,
            'longitude': -104.2755,
            'latitude': 39.9767,
            'length': 6.7,
            'imgMedium': 'https://cdn-files.apstatic.com/hike/7005382_medium_1435421346.jpg'
        }])
        return res # Temporary response to test on front end
    else:
        return 'asdf'



@app.route('/save_trail', methods=['POST'])
def save_trails():
    return None
    #todo add trail to database using model calls
