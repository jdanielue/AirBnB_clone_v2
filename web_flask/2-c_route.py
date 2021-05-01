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
    """ return value 2 """
    return "Hello HBNB!"

@app.route( "/c/<text>")
def r2(text):
    """ return value 3"""
    new_text = text.replace("_"," ")
    return ("C {}" .format(new_text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
