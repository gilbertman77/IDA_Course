from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello world")



while(True):
    temperature = round(sense.get_temperature(), 2)
    pressure = round(sense.get_pressure(), 2) 
    humidity = round(sense.get_humidity(), 2) 

    
    sense.show_message(str(temperature), text_colour=(255,0,0), back_colour=(0,0,0),scroll_speed=0.1)
    sense.show_message(str(pressure), text_colour=(0,0,255), back_colour=(0,0,0),scroll_speed=0.1)
    sense.show_message(str(humidity), text_colour=(0,255,0), back_colour=(0,0,0),scroll_speed=0.1)
