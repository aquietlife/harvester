# External module imports
import RPi.GPIO as GPIO
import time
import board
import adafruit_bno055
from pythonosc import udp_client

# Setup board
i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

#client setup
c = udp_client.SimpleUDPClient('127.0.0.1', 9001)

# Pin Definitons:
button1 = 6
button2 = 24
button3 = 12
button4 = 13
button5 = 22
button6 = 17
button7 = 16
button8 = 4
buttonRecord = 23
buttonLoop = 5

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(buttonRecord, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(buttonLoop, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

print("Here we go! Press CTRL+C to exit")
try:
	while True:
            #print("gyroscope (rad/sec: {}".format(sensor.gyro))
            #time.sleep(1)
            if GPIO.input(button1) == False:
                c.send_message("/1", "button1")
                print('Button 1 Pressed')
                time.sleep(0.2)
            elif GPIO.input(button2) == False:
                c.send_message("/2", "button2")
                print('Button 2 Pressed')
                time.sleep(0.2)
            elif GPIO.input(button3) == False:
                c.send_message("/3", "button3")
                print('Button 3 Pressed')
                time.sleep(0.2)
            elif GPIO.input(button4) == False:
                c.send_message("/4", "button4")
                print('Button 4 Pressed')
                time.sleep(0.2)
            elif GPIO.input(button5) == False:
                c.send_message("/5", "button5")
                print('Button 5 Pressed')
                time.sleep(0.2)
            elif GPIO.input(button6) == False:
                c.send_message("/6", "button6")
                print('Button 6 Pressed')
                time.sleep(0.2)
            elif GPIO.input(button7) == False:
                c.send_message("/7", "button7")
                print('Button 7 Pressed')
                time.sleep(0.2)
            elif GPIO.input(button8) == False:
                c.send_message("/8", "button8")
                print('Button 8 Pressed')
                time.sleep(0.2)
            elif GPIO.input(buttonRecord) == False:
                c.send_message("/record", "record")
                print('Button Record Pressed')
                time.sleep(0.2)
            elif GPIO.input(buttonLoop) == False:
                c.send_message("/loop", "loop")
                print('Button Loop Pressed')
                time.sleep(0.2)


except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
