#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def start_server():
    """start server and display hello hbnb"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def display_hbnb():
    """HBNB route must return HBNB"""
    return ("HBNB")


@app.route('/c/<text>')
def display_c(text):
    """displays c followed by value of text variable"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    """displays python followed by value of text"""
    if (text == "is cool"):
        return("Python {}".format(text))
    else:
        return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def display_number(n):
    """displays number only if it is an unsigned int"""
    return("{} is a number".format(n))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
