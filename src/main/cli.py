# A program that allows  the user to add themselves to the database or find someone to keep their dog
# Started simple, but I'm trying to add more features, also will add very nice GUI soon. Then ofc, make it a web app.


# Imports
import sys
import os

# Cache

sessionUser = None
loginstatus = False

# Lists, dictionaries, etc.

validDays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

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


# Functions

def main():# Main menu
        print("Welcome to DogShare!")
        type = input("Please login or register to continue: ")
        if type == "login":
                try:
                        print("Please enter your username and password")
                        username = input("Username: ")
                        password = input("Password: ")
                        if Database.loginUser(username, password) == True:
                                print("Login successful")
                                global sessionUser
                                sessionUser = username
                                loginstatus = True
                        else:
                                print("Login failed")
                                sys.exit(1)

                        

                except:
                        print("Login failed (error code 12)")
                        sys.exit(1)
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
                        attempt = Database.add_user(language, username, name, email, password, phone, address, zip)
                        if attempt:
                                print("Attempting to login")
                                try:
                                        Database.loginUser(username, password)
                                        sessionUser = username
                                        loginstatus = True
                                except:
                                        raise Exception("Login failed, although the user was registered")
                        else:
                                print("Registration failed, user already exists")
                                sys.exit(1)

                
                except:
                        print("Registration failed (error code 13)")
                        sys.exit(1)
        
        if loginstatus:
                option = input("Welcome to DogShare! Please select an option \n 1. Find someone to keep your dog (f) \n 2. Keep someone's dog (k)\n 3. Settings (s)\n 4. Exit (x)\n")
                try:
                        if option == "f":
                                day = input("When do you want someone to keep your dog? \n").lower()
                                print(Database.findKeeper(day))
                                
                        elif option == "k":
                                day = input("Please enter the following information: \n What day of this week do you want to keep the dog? \n").lower()
                                print(day)
                                if day in validDays:
                                        print("Adding you to the database")
                                        username = sessionUser
                                        Database.addKeeper(username, day)
                                else:
                                        print("Invalid day")
                                        sys.exit(1)
                        elif option == "s":
                                print("Settings")
                                input("Please choose a setting: \n 1. Change password \n 2. Change email \n 3. Change phone \n 4. Change address \n 5. Change zip \n 6. Change language \n 7. Delete account \n 8. Exit")
                                if input == 1:
                                        print("Change password")
                                        password = input("Please enter your new password: ")
                                        username = sessionUser
                                        Database.change_password(password, username)
                                elif input == 2:
                                        print("Change email")
                                        email = input("Please enter your new email: ")
                                        username = sessionUser
                                        Database.change_email(email, username)
                                elif input == 3:
                                        print("Change phone")
                                        username = sessionUser
                                        Database.change_phone(username)
                                elif input == 4:
                                        address = input("Please enter your new address: ")
                                        username = sessionUser
                                        Database.change_address(address, username)
                                elif input == 5:
                                        zip = input("Please enter your new zip: ")
                                        username = sessionUser
                                        Database.change_zip(zip, username)
                                elif input == 6:
                                        language = input("Please enter your new language: ")
                                        username = sessionUser
                                        Database.change_language(language, username)
                                elif input == 7:
                                        username = sessionUser
                                        Database.delete_account(username)
                        elif option == "x":
                                print("Exiting")
                                os._exit(1)
                except:
                        raise Exception("An error occured (error code 14)")