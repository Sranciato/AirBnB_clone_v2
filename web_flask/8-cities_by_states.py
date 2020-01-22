#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(err):
    """removes current sqlalchemy Session"""
    storage.close()


@app.route('/cities_by_states')
def display_cities_by_states():
    """displays a template of all cities by matching states"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', storage=states.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
