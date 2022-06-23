# Import Libraries 
from sense_hat import SenseHat
import pyrebase
import time

#  Create Sense Hat instance
sense = SenseHat()

# Define Colors
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#  Configure Firebase Connection
config = {
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE (OPTIONAL)
    "apiKey": "",
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE (OPTIONAL)
    "authDomain": "",
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the database URL from the Realtime DB screen in Firebase
    "databaseURL": "https://appdata-b53a0-default-rtdb.firebaseio.com/",
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE (OPTIONAL)
    # This is the node which you will be "looking into" to read/write data
    "storageBucket": ""
}
#  Set entry node
my_node = "shunt"

# Connect to Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Define variables
finding = 0           #  Set finding to 0

# Function to print message at terminal and Sense HAT
def print_message(my_message):
    sense.show_message(my_message, scroll_speed=0.05)
    print(my_message)

# Check database every 2 seconds, and calc/print items finding
# - This is very inefficient, why?
while True:
    time.sleep(2)          #  Print every 2 seconds
    finding = 0            #  Set finding to 0
    # Get data from "shunt" node
    my_data = db.child(my_node).get().val()
    # Check each item in our database
    for key in my_data:
    # If item status was no, but now "not no" we know its been found
        if my_data[key] == "no":
            finding = finding + 1 # If status "no" still finding
    print_message(str(finding))
    
