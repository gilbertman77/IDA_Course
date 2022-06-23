from sense_hat import SenseHat
import pyrebase
from random import randrange
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
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the APIKey from the Project Settings screen in Firebase
    "apiKey": "AIzaSyCuD2QQurLhyRq1dsLgWya0bUZld8qunyI",
    
    "authDomain": "project-id.firebaseapp.com",

    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the database URL from the Realtime DB screen in Firebase
    "databaseURL": "https://appdata-b53a0-default-rtdb.firebaseio.com/",
    
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the node which you will be "looking into" to read/write data
    "storageBucket": "iot"
}

# Connect to Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()


while(True):

    #  Read sense hat data and round them
    my_t = round(sense.get_temperature(), 2)
    my_p = round(sense.get_pressure(), 2)
    my_h = round(sense.get_humidity(), 2)
    acceleration = sense.get_accelerometer_raw()
    my_x = round(acceleration['x'], 2)
    my_y = round(acceleration['y'], 2)
    my_z = round(acceleration['z'], 2)

    # Create dictionary list of items to update in Firebase
    data = {
        "temp": my_t,
        "pressure": my_p,
        "humidity": my_h,
        "x": my_x,
        "y": my_y,
        "z": my_z
      }
    
    # Update DB with "data" dictionary
    db.child("iot").update(data)

    # Read Firebase data
    msg = db.child("iot/message").get().val()              # message text
    msg_on = db.child("iot/message_on").get().val()        # "true" or "false
    msg_mode = db.child("iot/message_mode").get().val()    # "env" or "msg"
    msg_units = db.child("iot/message_units").get().val()  # "metric" or "standard"

    # Randomize Colors
    tc = ( randrange(255), randrange(255), randrange(255))
    bc = ( randrange(255), randrange(255), randrange(255))
        
    # Determine what to display
    if msg_on:  # if message_on is false we clear the display
      if msg_mode == "env":   # if displaying enviromental info we check units
        if msg_units == "standard":  # if units standard do conversion
          my_t = round(my_t * 9/5 + 32, 2) # Convert to Fahrenheit
          my_p = round(my_p / 1013, 2)     # Convert mbars to atmospheres
        msg = str(my_t) + " " + str(my_p) + " " + str(my_h)
      sense.show_message(msg, text_colour=tc, back_colour=bc, scroll_speed=0.1)
      print(msg)
    else:
      sense.clear()
    time.sleep(5)

## Update DB message_mode
# my_mode = "env"  # can be "env" or "msg"
# db.child("iot").update({"message_mode": my_mode})

## Update DB msg_units
# my_units = "metric"  # can be "metric" or "standard"
# db.child("iot").update({"msg_units": my_units})

## Update DB msg_units
# my_on = True  # can be True or False
# db.child("iot").update({"msg_on": my_on})

#  Challenges
#  Students through part of the challenges.   Teachers get entire walkthrough
#
#  1 - Add random colors (DONE)
#  2 - Round incoming sense values (DONE)
#  3 - Turn message on/off with firebase db (DONE)
#  4 - Use Sense Hat joystick UP/DN to increase/decrease scroll speed
#  5 - Use Sense Hat joystick L/R to manually change colors (left-random text/bg, right-normal)
#  6 - Add mode to make display show temp/press/humidity
#  7 - Mode change with joystick button press
#  8 - Have text color change with temp (cold blue, progresses to red = hot)
