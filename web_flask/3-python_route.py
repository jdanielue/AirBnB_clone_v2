#!/usr/bin/python3
""" script to create a web app """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.route( "/hbnb")
def r():
    """ return value """
    return "HBNB!"

@app.route( "/")
def r1():
    """ return value 1"""
    return "Hello HBNB!"

@app.route( "/c/<text>")
def r2(text):
    """ return value 2"""
    new_text = text.replace("_"," ")
    return ("C {}".format(new_text))

@app.route( "/python")
def r3():
    """ return value 3"""
    return "Python is cool"

@app.route( "/python/<text>")
def r3a(text):
    """ return value 4"""
    if text is None:
        return "Python is cool"
    new_text = text.replace("_"," ")
    return "Python {}".format(new_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
