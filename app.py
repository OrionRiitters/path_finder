# this class will start the app will communicate directly with the frontend and the route handler
from flask import Flask, render_template, request
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
        return trails 
    else:
        bucket_list = db.get_all_trails()
        return bucket_list


@app.route('/save_trail', methods=['POST'])
def save_trails():
    form = request.json
    id = form["id"]
    db.save_trails(id)
    return "trail added successfully"


@app.route('/update_hiked', methods=['POST'])
def update_hiked():
    data = request.get_json(force=True)
    db.update_trail(data['id'])
    return db.get_all_trails()


if __name__ == '__main__':
    app.run(debug=True)
