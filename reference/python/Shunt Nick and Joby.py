from sense_hat import SenseHat
import pyrebase

from random import randrange
import time

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 225, 0)
red = (255, 0, 0)

tc = ( randrange(225), randrange(225), randrange(225))
bc = ( randrange(225), randrange(225), randrange(225))

config = {
    "apiKey": "AIzaSyCjSm_3scO9I_efNaebJ3x3I-ULN8vJHj4",
    "databaseURL": "https://iot-project-2b3e0-default-rtdb.firebaseio.com",
    "authDomain": "iot-project-2b3e0.firebaseapp.com",
    "storageBucket": "iot",
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()

ScrollSpeed=0.1

while(True):
    
    my_t = round(sense.get_temperature(), 2)
    my_p = round(sense.get_pressure(), 2)
    my_h = round(sense.get_humidity(), 2)
    
    acceleration = sense.get_accelerometer_raw()
    my_x = round(acceleration['x'], 2)
    my_y = round(acceleration['y'], 2)
    my_z = round(acceleration['z'], 2)
    
    
    data = {
        "temp": my_t,
        "pressure": my_p,
        "humidity": my_h,
        "x": my_x,
        "y": my_y,
        "z": my_z
        }
    
    db.child("iot").update(data)
    msg = db.child("iot/message").get().val()
    msg_on = db.child("iot/message_on").get().val()
    msg_mode = db.child("iot/message_mode").get().val()
    msg_units = db.child("iot/message_unit").get().val()
    
    
    msg_units = "standard"
    
    if msg_on:
        if msg_mode == "env":
            if msg_units == "standard":
                my_t = round(my_t * 9/5 + 32, 2)
                my_p = round(my_p/ 1013, 2)
            msg = str(my_t) + " " + str(my_p) + " " + str(my_h)
        sense.show_message(msg, text_colour=tc, back_colour=bc, scroll_speed=ScrollSpeed)
        print(msg)
    else:
        sense.clear()
    time.sleep(1)
        
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == "up":
                msg_mode= "env"
             
            elif event.direction == "down":
                msg_mode= "msg"  
                print(msg_mode)
            
            elif event.direction == "right":
                tc = ( randrange(225), randrange(225), randrange(225))
                bc = ( randrange(225), randrange(225), randrange(225))
            
            elif event.direction == "left":
                t_red = my_t * 1.5
                t_red = max(0,t_red)
                t_red = min(255,t_red)
                t_blue = 255 - t_red
                t_red = int(t_red)
                t_blue = int(t_blue)
                
                tc = ( t_red, 0, t_blue)
                bc = ( randrange(225), randrange(225), randrange(225))
                
    print(tc)
            
        
    db.child("iot").update({"message_mode":msg_mode})
            
       