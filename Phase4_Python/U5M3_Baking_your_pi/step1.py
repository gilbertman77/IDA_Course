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
 
# Randomize Colors
# tc (text color)
# bc (background color)
tc = (randrange(255), randrange(255), randrange(255))
bc = (randrange(255), randrange(255), randrange(255))
 
# Print random RGB colors
print(tc, bc)
