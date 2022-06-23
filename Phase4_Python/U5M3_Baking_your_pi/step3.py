# Import Libraries
from sense_hat import SenseHat
from random import randrange
import time
 
#Create Sense Hat instance
sense = SenseHat()
 
# Define Colors
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Set message to display
msg_on= True
 
while(True):
  time.sleep(.5)
  
  # Randomize Colors
  # tc (text color)
  # bc (background color)
  tc = (randrange(255), randrange(255), randrange(255))
  bc = (randrange(255), randrange(255), randrange(255))
     
  # Print random RGB colors
  print(tc, bc)
 
  # Get data from SenseHat
  my_t = round(sense.get_temperature(), 2)
  my_p = round(sense.get_pressure(), 2)
  my_h = round(sense.get_humidity(), 2)
 
  acceleration = sense.get_accelerometer_raw()
  my_x = round(acceleration['x'], 2)
  my_y = round(acceleration['y'], 2)
  my_z = round(acceleration['z'], 2)
 
  # Create dictionary of values
  sense_data = {
    "temp": my_t,
    "pressure": my_p,
    "humidity": my_h,
    "x": my_x,
    "y": my_y,
    "z": my_z
      }
   
  # Print dictionary data
  print(sense_data)
