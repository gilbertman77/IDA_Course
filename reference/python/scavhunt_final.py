from sense_hat import SenseHat
import pyrebase
import time

#  Create Sense Hat instance
sense = SenseHat()

# Define Colors
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)

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

# Initialize Global variables
old_data = None         # Initializes old_data to compare to new_data
finding = "Starting"    # Initializes num of items finding to "Starting"
sh_message = "Starting" # Initializes sh_message to "Starting"
new_item = False        # Initializes new_item found to False

# Listener triggers when change in database is detected
# Calculate items still finding, print item found, block main program
def stream_handler(message):
    global old_data, finding, sh_message, new_item
    finding = 0;           #  Reset finding to 0
    new_data = db.child(my_node).get().val()
    # Check each item in our database
    for key in new_data:
        # If item with key is no, we add to increment finding
        if new_data[key] == "no":
            finding = finding + 1 # If status "no" still finding
        # If item status was no, but now "not no" we know its been found
        if new_data[key] != "no" and old_data[key] == "no":
            # set message to item and finder
            sh_message = key + " found by " +  new_data[key]
            new_item = True #  Set new item flag to true
    old_data = new_data         #  Set old data to new data


def print_message(my_message):
    sense.show_message(my_message, scroll_speed=0.04)

old_data = db.child(my_node).get().val()
my_stream = db.child(my_node).stream(stream_handler)

# Main loop prints number of items left
while True:
    time.sleep(2)          #  Print every 2 seconds
    # If not new item set message to number items
    if not new_item: 
        sh_message = str(finding)
    # If no more items set message to game over
    elif finding == 0:
        sh_message = "Game Over"
    print_message(sh_message)
    new_item = False  # Reset flag
