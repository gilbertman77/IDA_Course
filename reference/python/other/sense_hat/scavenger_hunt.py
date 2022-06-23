from sense_hat import SenseHat
import pyrebase
from random import randrange
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
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the APIKey from the Project Settings screen in Firebase
    #"apiKey": "AIzaSyCuD2QQurLhyRq1dsLgWya0bUZld8qunyI",
    "apiKey": "",
    
    #"authDomain": "project-id.firebaseapp.com",
    "authDomain": "",
    
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the database URL from the Realtime DB screen in Firebase
    "databaseURL": "https://appdata-b53a0-default-rtdb.firebaseio.com/",
    
    # THIS MUST BE UPDATED PER YOUR FIREBASE DATABASE
    # This is the node which you will be "looking into to read/write data"
    "storageBucket": "shunt"
    #"storageBucket": "iot"
}
my_node = "shunt"

# Connect to Firebase
firebase = pyrebase.initialize_app(config)
#db = firebase.database()
dbRef1 = firebase.database().child(my_node)

while(True):

    #  Read Sense Hat Data
    my_t = round(sense.get_temperature(), 2)
    my_p = round(sense.get_pressure(), 2)
    my_h = round(sense.get_humidity(), 2)

    acceleration = sense.get_accelerometer_raw()
    my_x = round(acceleration['x'], 2)
    my_y = round(acceleration['y'], 2)
    my_z = round(acceleration['z'], 2)

    # Define data to be updated
    data = {
        "temp": my_t,
        "pressure": my_p,
        "humidity": my_h,
        "x_accel": my_x,
        "y_accel": my_y,
        "z_accel": my_z
      }
    
    # Update DB data
    dbRef1.update(data)

    # Read DB data
    msg = dbRef1.child("message").get().val()
    msg_on = dbRef1.child("display_on").get().val()
    msg_mode = dbRef1.child("display_mode").get().val()
    msg_units = dbRef1.child("display_units").get().val()

    # Randomize Colors
    tc = ( randrange(255), randrange(255), randrange(255))
    bc = ( randrange(255), randrange(255), randrange(255))
        
    mode = "env"
    #msg_on = True # Test variable
    if msg_on:
      if display_mode == "env":
        if display_units == "standard":
          my_t = round(my_t * 9/5 + 32, 2) # Convert to Fahernheit
          my_p = round(my_p / 1013, 2) # Convert millibars to atmospheres  
        env_msg = str(my_t) + " " + str(my_p) + " " + str(my_h)
        sense.show_message(env_msg, text_colour=tc, back_colour=bc, scroll_speed=0.1)
        print(env_msg)
      else:
        sense.show_message(msg, text_colour=tc, back_colour=bc, scroll_speed=0.1)
        print(msg)
    else:
        sense.clear()
    time.sleep(5)

# Update DB message_mode
# my_mode = "env"
# db.child("iot").update({"message_mode": my_mode})
# 
#
        
#  Challenges
#  Need to define challenges and walk students through part of the challenge.   Teacher guide get entire walkthrough
#
#  1 - Add random colors (DONE)
#  2 - Round incoming sense values (DONE)
#  3 - Turn message on/off with firebase db (DONE)
#  4 - Use Sense Hat joystick UP/DN to increase/decrease scroll speed (data is stored in DB)
#  5 - Use Sense Hat joystick L/R to manually change colors (left-text, right-back)
#  6 - Add mode to make display show temp/press/humidity
#  7 - Mode change with joystick button press
#  8 - Have text color change with temp (cold blue, progresses to red = hot)


