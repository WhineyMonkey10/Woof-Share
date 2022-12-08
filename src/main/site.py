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
    
    return render_template('index.html')

@app.route('/findsitter', methods=['GET', 'POST'])
def findsitter():
    # Get the data from the form
    day  = request.form['day']
    # Check if a data is available
    data = Database.findKeeper(day)
    if data == False:
        successmessage = "Sadly there are no keeper available on this day."
    if data != False:
        successmessage = f"Hooray! There is a keeper available on the day {day}! Here is their information: {data}"
    return render_template('findsitter.html', data=successmessage)

app.run()