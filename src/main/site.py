# Flask app for the same features as CLI.py

# Imports
import flask
from flask import request, jsonify, render_template, redirect, url_for, session
import sys

# Imports from other files
from src.handlers.database.database import Database

# Create the app

app = flask.Flask(__name__)

# Make sure the database is connected
print(Database.testConnection())

# Verify that the user is using Python 3.8 or higher
print("Python version: " + sys.version)

# Main page

@app.route('/', methods=['GET'])
def home():
    
    return render_template('login.html')

@app.route('/findsitter', methods=['GET', 'POST'])
def findsitter():
    # Get the data from the form
    day  = request.form['day']
    # Check if a data is available
    data = Database.findKeeper(day)
    if data == False:
        successmessage = "Sadly there are no keepers available on this day."
        status = "No keeper available"
    if data != False:
        successmessage = f"Hooray! There are keeper(s) available on the day {day}! Here is their information: {data}"
        status = "Keeper available"
    return render_template('sitterinfo.html', data=successmessage, status=status)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Get the data from the form
    username = request.form['username']
    password = request.form['password']
    # Check if a data is available
    data = Database.loginUser(username, password)
    if data == False:
        successmessage = "Wrong username or password."
        status = "Login failed"
    if data != False:
        successmessage = "Welcome back!"
        status = "Login success"
        return render_template('findsitter.html', data=successmessage, status=status)
    return render_template('login.html', data=successmessage, status=status)

app.run()