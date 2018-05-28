# Harvester

![Harvester Illustration](https://raw.githubusercontent.com/aquietlife/harvester/master/harvester.jpg)

## Parts

A list of parts and costs can be found on this [Google Sheet](https://docs.google.com/spreadsheets/d/1l5mX_4e5-Yf7ezj4Uyb-OJHwEcOEgB5TfozrZ1NfUMg/edit?usp=sharing)

# Installation Instructions

* Download Raspian Image

* Flash to SD cards (do this before the workshop)

* Touch ssh file in boot directory to enable SSH

* Connect RPi to Wifi with battery (can’t do right now)

* Connecting w Ethernet and Raspi power works

* Check:

* Power w 9V and ethernet - works

* Power w 9v and wifi - doesn’t work

* Once RPi is setup and connected to Wifi, try these instructions:

* https://www.hackster.io/shiva-siddharth/make-your-own-google-voice-hat-9f96ca

* Added bcm2708.vc_i2c_override=1 to cmdline.txt

* https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=87715

* https://www.raspberrypi.org/forums/viewtopic.php?t=108134

* Enabled i2c arm from raspi-config

* Test Audio

* https://www.raspberrypi-spy.co.uk/2013/06/raspberry-pi-command-line-audio/

* https://www.raspberrypi.org/forums/viewtopic.php?t=12358

* sudo arecord test.wav

* sudo aplay test.wav

* sudo aplay /usr/share/sounds/alsa/Front_Center.wav

* https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/recording-audio


## References

### Setting up Raspberry Pi

* https://desertbot.io/blog/headless-raspberry-pi-3-bplus-ssh-wifi-setup

* https://styxit.com/2017/03/14/headless-raspberry-setup.html    

* http://ivanx.com/raspberrypi/

### Misc

* https://caffinc.github.io/2016/12/raspberry-pi-3-headless/

## Credits

Voice sample: Miyu Hosoi

Circuit layout: Mark Kleeb
