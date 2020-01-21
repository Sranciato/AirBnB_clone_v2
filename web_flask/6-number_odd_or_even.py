#!/usr/bin/python3
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>')
def display_html(n):
    """display html page only if n is a number"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def display_odd_even(n):
    """display odd or even number in html"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
