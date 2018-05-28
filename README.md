# Harvester

![Harvester Illustration](https://raw.githubusercontent.com/aquietlife/harvester/master/harvester.jpg)

## Parts

1x Harvester Board

3x 3.9k resistor

1x EEPROM chip (which one?)

10x buttons

1x header pin set

1x 5v regulator

1x 9v battery holder

1x switch

1x barrel wall power - very necessary



1x Raspberry Pi 3

1x Raspberry Pi 3 charger

1x 8gb micro SD with full-size SD card adapter and USB reader for computer



1x 12S Amp (for speaker)

2x 12S Microphone

1x Speaker



1x Enclosure (not made yet)



Instructions:



Download Raspian Image

Flash to SD cards (do this before the workshop)

https://desertbot.io/blog/headless-raspberry-pi-3-bplus-ssh-wifi-setup

https://styxit.com/2017/03/14/headless-raspberry-setup.html    

http://ivanx.com/raspberrypi/

Touch ssh file in boot directory

Connect RPi to Wifi with battery (can’t do right now)

Connecting w Ethernet and Raspi power works

Check:

Power w 9V and ethernet - works

Power w 9v and wifi - doesn’t work

Once RPi is setup and connected to Wifi, try these instructions:

https://www.hackster.io/shiva-siddharth/make-your-own-google-voice-hat-9f96ca

Added bcm2708.vc_i2c_override=1 to cmdline.txt

https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=87715

https://www.raspberrypi.org/forums/viewtopic.php?t=108134

Enabled i2c arm from raspi-config

Test Audio

https://www.raspberrypi-spy.co.uk/2013/06/raspberry-pi-command-line-audio/


https://www.raspberrypi.org/forums/viewtopic.php?t=12358

sudo arecord test.wav

sudo aplay test.wav

sudo aplay /usr/share/sounds/alsa/Front_Center.wav

https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/recording-audio


References:

https://caffinc.github.io/2016/12/raspberry-pi-3-headless/

Credits:

Voice sample: Miyu Hosoi
Circuit layout: Mark Kleeb
