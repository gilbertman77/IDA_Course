from sense_hat import SenseHat
import pyrebase
from random import randrange
import time

#  Create Sense Hat instance
sense = SenseHat()
sense.set_rotation(180) # Make text flip 180 for easier display

# Define Colors
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)

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
    # This is the node which you will be "looking into to read/write data"
    "storageBucket": "iot"
}

# Connect to Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()


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
    db.child("iot").update(data)

    # Read DB data
    msg = db.child("iot/message").get().val()
    display_on = db.child("iot/display_on").get().val()
    display_message = db.child("iot/display_message").get().val()
    display_metric = db.child("iot/display_metric").get().val()

    # Randomize Colors
    tc = ( randrange(255), randrange(255), randrange(255))
    bc = ( randrange(255), randrange(255), randrange(255))
        
    # Determine what is displayed on sense hat
    if display_on:
      if not display_message:
        if not display_metric:
          my_t = round(my_t * 9/5 + 32, 2) # Convert to Fahernheit
          my_p = round(my_p / 1013, 2) # Convert millibars to atmospheres
        msg = str(my_t) + " " + str(my_p) + " " + str(my_h)
      sense.show_message(msg, text_colour=tc, back_colour=bc, scroll_speed=0.1)
      print(msg)
    else:
      sense.clear()
    # Wait five seconds
    time.sleep(5)
        
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