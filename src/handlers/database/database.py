# File defining all database classes and functions for ease of use in other files, I tried MySQl but it was too complicated, so obviously, I went with my good friend MongoDB

# Importing the necessary modules
import sys
import os
from pymongo import MongoClient
import datetime

# Initializing the database
mongostring = ""
client = MongoClient(mongostring)

# Defining the database
db = client["dogshare"]
collection = db["users"]

# Class of all database functions

    # Function to add a new user to the database
class Database:
    def add_user(language, username, name, email, password, phone, address, zip):
        # Add user to MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]
        # Add user to the database
        try:
            # Check if the user already exists
            if collection.find_one({"username": username}):
                return "User already exists"
            else:
                collection.insert_one({
                "language": language,
                "username": username,
                "name": name,
                "email": email,
                "password": password,
                "phone": phone,
                "address": address,
                "zip": zip,
            })
                return "User added"

        except:
                return ("Exited with error code 1: User not added")

    # Function to find a user in the database
    def find_user(username):
        # Find user in MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Find user in the database
        try:
            user = collection.find_one({"username": username})
            return user
        except:
            return ("Exited with error code 2: User not found")

    # Function to delete a user from the database
    def delete_user(username):
        # Delete user from MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Delete user from the database
        try:
            collection.delete_one({"username": username})
            return ("User deleted")
        except:
            return ("Exited with error code 3: User not deleted")

    # Function to update a user in the database
    def update_user(username, language, name, email, password, phone, address, zip, dog_name, dog_breed, dog_age, dog_weight):
        # Update user in MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Update user in the database
        try:
            collection.update_one({"username": username}, {"$set": {username: username, "language": language, "name": name, "email": email, "password": password, "phone": phone, "address": address, "zip": zip}})
            return ("User updated")
        except:
            return ("Exited with error code 4: User not updated")

    # Function to add a new dog to the database
    def add_dog(usernameofowner, dog_name, dog_breed, dog_age, dog_weight):
        # Add dog to MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Add dog to the database
        try:
            collection.update_one({"username": usernameofowner}, {"$set": {"dog_name": dog_name, "dog_breed": dog_breed, "dog_age": dog_age, "dog_weight": dog_weight}})
            return ("Dog added")
        except:
            return ("Exited with error code 5: Dog not added")

    # Function to find a dog in the database
    def find_dog(usernameofowner):
        # Find dog in MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Find owner dog in the database
        try:
            dog = collection.find_one({"username": usernameofowner})
            # Sort the data of the user and delete all non-dog data
            dog.pop("language")
            dog.pop("username")
            dog.pop("name")
            dog.pop("email")
            dog.pop("password")
            dog.pop("phone")
            dog.pop("address")
            dog.pop("zip")
            return dog
        except:
            return ("Exited with error code 6: Dog not found")

    # Function to delete a dog from the database
    def delete_dog(usernameofowner):
        # Delete dog from MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Delete dog from the database
        try:
            collection.update_one({"username": usernameofowner}, {"$unset": {"dog_name": "", "dog_breed": "", "dog_age": "", "dog_weight": ""}})
            return ("Dog deleted")
        except:
            return ("Exited with error code 7: Dog not deleted")

    # Function to update a dog in the database
    def update_dog(usernameofowner, dog_name, dog_breed, dog_age, dog_weight):
        # Update dog in MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Update dog in the database
        try:
            collection.update_one({"username": usernameofowner}, {"$set": {"dog_name": dog_name, "dog_breed": dog_breed, "dog_age": dog_age, "dog_weight": dog_weight}})
            return ("Dog updated")
        except:
            return ("Exited with error code 8: Dog not updated")

    # Function to sort for dogs using the dog's weight, age, breed, or name
    def sort_dogs(sorttype):
        # Sort dogs in MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Sort dogs in the database
        if sorttype == "weight":
            try:
                dogs = collection.find().sort("dog_weight")
                return dogs
            except:
                return ("Exited with error code 9: Dogs not sorted")
        elif sorttype == "age":
            try:
                dogs = collection.find().sort("dog_age")
                return dogs
            except:
                return ("Exited with error code 9: Dogs not sorted")
        elif sorttype == "breed":
            try:
                dogs = collection.find().sort("dog_breed")
                return dogs
            except:
                return ("Exited with error code 9: Dogs not sorted")
        elif sorttype == "name":
            try:
                dogs = collection.find().sort("dog_name")
                return dogs
            except:
                return ("Exited with error code 9: Dogs not sorted")
    
    def find_dog_by_name(dog_name):
        # Find dog in MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Find owner dog in the database
        try:
            dog = collection.find_one({"dog_name": dog_name})
            # Sort the data of the user and delete all non-dog data
            dog.pop("language")
            dog.pop("username")
            dog.pop("name")
            dog.pop("email")
            dog.pop("password")
            dog.pop("phone")
            dog.pop("address")
            dog.pop("zip")
            return dog
        except:
            return ("Exited with error code 10: Dog not found")
    
    def loginUser(username, password):
        # Find user in MongoDB database
        # Connect to the database
        db = client["dogshare"]
        collection = db["users"]

        # Find user in the database
        try:
            if collection.find_one({"username": username, "password": password}):
                    return "True"
            else:
                return "Either the username or password is incorrect"
        except:
            return "Exited with error code 34: User not found"
            
    
    
    def testConnection():
        try:
            db = client["dogshare"]
            collection = db["users"]
            if collection.find_one({"username": "testConnection"}):
                return "Connection successful"     
            else:
                return "Unable to connect to database (error code 11)"
        except:
            return ("Unable to connect to database (error code 11.1)")
    # More functions to come
    
