# app.py
import os
from flask import Flask
app = Flask(name)
@app.route("/")
def main():
return "Welcome!"
@app.route('/how are you')
def hello():
return 'I am good, how about
you?'
if name == "main":
app.run()
