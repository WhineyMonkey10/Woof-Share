# A program that allows  the user to add themselves to the database or find someone to keep their dog
# Started simple, but I'm trying to add more features, also will add very nice GUI soon. Then ofc, make it a web app.


# Imports
import sys


# Big print to make a dog logo

print(""" __      __              _____    _________.__                          
/  \    /  \____   _____/ ____\  /   _____/|  |__ _____ _______   ____  
\   \/\/   /  _ \ /  _ \   __\   \_____  \ |  |  \\__  \\_  __ \_/ __ \ 
 \        (  <_> |  <_> )  |     /        \|   Y  \/ __ \|  | \/\  ___/ 
  \__/\  / \____/ \____/|__|    /_______  /|___|  (____  /__|    \___  >
       \/                               \/      \/     \/            \/ """)

print(""" .____                     .___.__                
|    |    _________     __| _/|__| ____    ____  
|    |   /  _ \__  \   / __ | |  |/    \  / ___\ 
|    |__(  <_> ) __ \_/ /_/ | |  |   |  \/ /_/  >
|_______ \____(____  /\____ | |__|___|  /\___  / 
        \/         \/      \/         \//_____/  """)

# Make sure the database is connected
from src.handlers.database.database import Database
print(Database.testConnection())

# Verify that the user is using Python 3.8 or higher
print("Python version: " + sys.version)

# Main menu
print("Welcome to DogShare!")
type = input("Please login or register to continue: ")
if type == "login":
        try:
                print("Please enter your username and password")
                username = input("Username: ")
                password = input("Password: ")
                if Database.loginUser(username, password) == "True":
                        print("Login successful")
                else:
                        print("Login failed")
                
        except:
                print("Login failed (error code 12)")
elif type == "register":
        try:
                print("Please enter your information")
                language = input("Language: ")
                username = input("Username: ")
                name = input("Name: ")
                email = input("Email: ")
                password = input("Password: ")
                phone = input("Phone: ")
                address = input("Address: ")
                zip = input("Zip: ")
                print(Database.add_user(language, username, name, email, password, phone, address, zip))
                
        except:
                print("Registration failed (error code 13)")