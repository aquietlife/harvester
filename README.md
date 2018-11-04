# Harvester

![Harvester Illustration](https://raw.githubusercontent.com/aquietlife/harvester/master/harvester.jpg)
Illustration by [Seo Hye Lee](http://www.seohyelee.com/)

## Parts

A list of parts and costs can be found on this [Google Sheet](https://docs.google.com/spreadsheets/d/1l5mX_4e5-Yf7ezj4Uyb-OJHwEcOEgB5TfozrZ1NfUMg/edit?usp=sharing)

## Installation Instructions

### Solder up Harvester hat

* Instructions TBD, look at parts list

### Install Raspian for Raspberry Pi

* Download the latest version of Raspian here: https://www.raspberrypi.org/downloads/raspbian/

* Install Raspian to your SD card. On OSX, you can use these instrucitons: https://www.raspberrypi.org/documentation/installation/installing-images/mac.md

* Whle the SD card is still connected, create a file called "ssh" in the boot directory of the card to enable SSH, e.g.:

`touch /Volumes/boot/ssh`

* Also, create a file called wpa_supplicant.conf in the boot directory

`vim /Volumes/boot/wpa_supplicant.conf `

* And add the following lines, replacing MySSID and MyPassword with you WiFi's network name and password:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={ 
ssid="MySSID" 
psk="MyPassword" 
}
```

* Afterwards, plug your SD card into your RPI, power it on, and try to SSH into it:

`ssh pi@raspberrypi.local`

The password is `raspberry`

Then run the following command to set up your RPI to keep SSH on:

`sudo raspi-config`

Most importantly, go to Interfacing Options > SSH and enable SSH!

Select finish, then your RPi will reboot. Try connecting again and if everything is working, move on to the next section :D


### Set up EEPROM chip for amp and microphone

* https://www.hackster.io/shiva-siddharth/make-your-own-google-voice-hat-9f96ca

* Added bcm2708.vc_i2c_override=1 to cmdline.txt

* https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=87715

* https://www.raspberrypi.org/forums/viewtopic.php?t=108134

* Enabled i2c arm from raspi-config

### Test Audio and Microphone

* https://www.raspberrypi-spy.co.uk/2013/06/raspberry-pi-command-line-audio/

* https://www.raspberrypi.org/forums/viewtopic.php?t=12358

* sudo arecord test.wav

* sudo aplay test.wav

* sudo aplay /usr/share/sounds/alsa/Front_Center.wav

* https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/recording-audio

### Install Python OSC server

* install pyOSC

### Install Pd

* Install Pd

`sudo apt-get install pd-comport`

`git clone git://github.com/umlaeute/pd-iemnet.git`

`cd pd-iemnet`

`make`

`sudo make install`

* Install Pd libraries

`wget http://puredata.info/downloads/osc/releases/0.1/OSC-0.1.tar.gz`

`tar -xzvf OSC-0.1.tar.gz`

`cd OSC-0.1/`

`make`

`sudo make install`

### Install Harvester Software

![Harvester Pd Software](https://raw.githubusercontent.com/aquietlife/harvester/master/software/raspberrypi/harvester-pd.png)

* Install this repo

* Test scripts manually

`python harvester/software/raspberrypi/gpio-osc.py &`

`pd -stderr -nogui -verbose -audiodev 4 harvester/software/raspberrypi/harvester.pd &`


* Celebrate!

### Autostart software

Add the following lines to the bottom of /home/pi/.bashrc

`vim /home/pi/.bashrc`

```
if pgrep -x "python" > /dev/null
then
    echo "Python is already runnning"
else
    echo "Python is not running, attempting to run Python"
	python harvester/software/raspberrypi/gpio-osc.py >/dev/null 2>&1 &
fi

if pgrep -x "pd" > /dev/null
then
    echo "Pd is already running"
else
    echo "Pd is not running, attempting to run Pd"
	pd -stderr -nogui -verbose -audiodev 4 harvester/software/raspberrypi/harvester.pd >/dev/null 2>&1 &
fi
```

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
