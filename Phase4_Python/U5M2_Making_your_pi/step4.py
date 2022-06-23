#  
#  Below is sample code that meets the objectives above.
#
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello world")

# 
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#  Define fast/slow scroll speeds
FAST = 0.05
SLOW = 0.1
 
color = WHITE
speed = SLOW
 
while(True):
    temperature = round(sense.get_temperature(), 2)
    pressure = round(sense.get_pressure(), 2)
    humidity = round(sense.get_humidity(), 2)
    xyz = sense.get_accelerometer()
 
 
    sense.show_message(str(temperature), text_colour=color, back_colour=(0,0,0),scroll_speed=speed)
    sense.show_message(str(pressure), text_colour=color, back_colour=(0,0,0),scroll_speed=speed)
    sense.show_message(str(humidity), text_colour=color, back_colour=(0,0,0),scroll_speed=speed)
    sense.show_message(str(xyz), text_colour=color, back_colour=(0,0,0),scroll_speed=speed)
    
 
    events = sense.stick.get_events()
    for event in events:
      # Skip releases
      if event.action != "released":
        if event.direction == "left":
          color = RED
        elif event.direction == "right":
          color = WHITE
        elif event.direction == "down":
          speed = SLOW
        elif event.direction == "up":
          speed = FAST  
