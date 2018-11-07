# External module imports
import RPi.GPIO as GPIO
import time
import OSC

#client setup
c = OSC.OSCClient()

#local host: port 9001
c.connect(('127.0.0.1', 9001))

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
            if GPIO.input(button1) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/1")
                msg.append("button1")
                c.send(msg)
        	print('Button 1 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button2) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/2")
                msg.append("button2")
                c.send(msg)
        	print('Button 2 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button3) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/3")
                msg.append("button3")
                c.send(msg)
        	print('Button 3 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button4) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/4")
                msg.append("button4")
                c.send(msg)
        	print('Button 4 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button5) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/5")
                msg.append("button5")
                c.send(msg)
        	print('Button 5 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button6) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/6")
                msg.append("button6")
                c.send(msg)
        	print('Button 6 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button7) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/7")
                msg.append("button7")
                c.send(msg)
        	print('Button 7 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button8) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/8")
                msg.append("button8")
                c.send(msg)
        	print('Button 8 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(buttonRecord) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/record")
                msg.append("record")
                c.send(msg)
        	print('Button Record Pressed')
        	time.sleep(0.2)
            elif GPIO.input(buttonLoop) == False:
                msg = OSC.OSCMessage()
                msg.setAddress("/loop")
                msg.append("loop")
                c.send(msg)
        	print('Button Loop Pressed')
        	time.sleep(0.2)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
