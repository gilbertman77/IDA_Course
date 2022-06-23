from sense_hat import SenseHat
import pyrebase
from random import randrange
import time
import threading
import asyncio

queue = asyncio.Queue()
loop = asyncio.get_event_loop()

#  Create Sense Hat instance
sense = SenseHat()

# Define Colors
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)

#  Configure Firebase Connection
config = {
    "apiKey": "",
    "authDomain": "",
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the database URL from the Realtime DB screen in Firebase
    "databaseURL": "https://appdata-b53a0-default-rtdb.firebaseio.com/",
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the node which you will be "looking into" to read/write data
    "storageBucket": ""
}
#  Define entry node
my_node = "shunt"

# Connect to Firebase
my_db = pyrebase.initialize_app(config)

# Initialize Global variables
old_data = None
finding = "Starting"
game_over = False

def print_msg(my_string, ss):
    sense.show_message(my_string, scroll_speed=ss)

# Listener funciton (runs when node is changed)
def stream_handler(message):
    fb_action()
    
def fb_action():
    global old_data, finding, game_over                     # Access global variables
    finding = 0                                             # Set items finding to 0
    new_data = my_db.database().child(my_node).get().val()  # Get updated data
    ### Loops through all DB elements
    for key in new_data:
        # If item with key is no, we add to increment finding
        if new_data[key] == "no":
            finding = finding + 1
        # If not first time running (old_data has data)
        if old_data:
            # If item status changed, we know its been found
            # since we can't unfind an item, print message
            if new_data[key] != old_data[key]:
                my_str = key + " found by " +  new_data[key]
                print(my_str)
                print_msg(my_str, 0.05)
                
#    if finding == 0:
#        sense.show_message("You win", scroll_speed = 0.05)
#        game_over = True
    # Set old data equal to new data
    old_data = new_data
    time.sleep(3)

# Configure new listener on "shunt" node

# @asyncio.coroutine
def print_finding():
    while True:
        sense.show_message(str(finding))
        time.sleep(2)
        
def main():
    x = threading.Thread(target=print_finding)
    x.start()
    

#threading.Thread(target=start_async_stuff).start()

'''
async def main():
    while True:
        sense.show_message(str(finding))
        time.sleep(2)
'''
if __name__ == '__main__':
    asyncio.run(main())
