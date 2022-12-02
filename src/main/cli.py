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

sys.path.append('../src')


from src.handlers.database.database import Database

Database.testConnection()