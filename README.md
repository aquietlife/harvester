# Harvester

![Harvester Illustration](https://raw.githubusercontent.com/aquietlife/harvester/master/harvester.jpg)
Illustration by [Seo Hye Lee](http://www.seohyelee.com/)

![Harvester Photo](http://aquiet.life/assets/objects/harvester/harvester_sean.jpg)

Harvester is a hand-held, portable live sampler that lets you make music with everyday sounds. With the instrument, you are able to capture sounds around you (your voice, another musical instrument, environmental noises etc.). The instrument provides an interface that lets you play back the sampled sound based around a musical, pentatonic scale. This allows for a wildly expressive sonic palette that can be used for musical performance and sound art installations.

[Video of Harvester](http://aquiet.life/assets/objects/harvester/harvester_snow.mov)

## Parts

A list of parts and costs can be found on this [Google Sheet](https://docs.google.com/spreadsheets/d/1hDYdzhToesEgNGzxmREglWhK1RFRyOljPsczHniATDo/edit?usp=sharing)

## Installation Instructions

### Solder up Harvester hat

* Full documentation TBD; The board itself has layouts for where compoenents should go!

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


### Set up Harvester Hat Hardware

** Part 1 **

* On your RPi, clone this repo

`git clone https://github.com/aquietlife/harvester`

At this point, it would probably be nice to install vim ;)

`sudo apt-get install vim`

Turn on i2s support in /boot/config.txt

`sudo vim /boot/config.txt`

Uncomment the following lines:

#dtparam=i2s=on 

#dtparam=i2c_arm=on 

#dtparam=spi=on 

#dtparam=audio=on 

Also add the following new entry:

`dtparam=i2c_vc=on`

Override bcm2708.vc_i2c_override in cmdline.txt

`sudo vim /boot/cmdline.txt`

Add the following line at the end of the line with a space after the word "consoles": 

`bcm2708.vc_i2c_override=1`

Finally enabled i2c arm from `raspi-config`

Then reboot your RPi

** Part 2 **

Start your Pi and move into the audio configuration scripts: 

`cd ~/harvester/software/custom-voice-hat/audio-config/scripts/`

Make the scripts executable: 

`sudo chmod +x ./custom-voice-hat.sh`

`sudo chmod +x ./install-i2s.sh`

Run the Executable scripts:

`sudo ./custom-voice-hat.sh`

`sudo ./install-i2s.sh` 

Run the custom-voice-hat.sh script again until you get .bak notification. 

`sudo ./custom-voice-hat.sh`

Reboot!




### Test Audio and Microphone

Test your audio:

* sudo aplay /usr/share/sounds/alsa/Front_Center.wav

Test your microphones:

* sudo arecord test.wav

* sudo aplay test.wav


### Install Python OSC server

* Install pyOSC

`pip install pyosc` 

You might also need to run it as:

`pip2 install pyosc`

### Install Pd

* Install Pd

`sudo apt-get install pd-comport`

`git clone git://github.com/umlaeute/pd-iemnet.git`

`cd pd-iemnet`

`make`

`sudo make install`

`cd ..`

* Install Pd libraries

`wget http://puredata.info/downloads/osc/releases/0.1/OSC-0.1.tar.gz`

`tar -xzvf OSC-0.1.tar.gz`

`cd OSC-0.1/`

`make`

`sudo make install`

`cd ..`

`wget http://puredata.info/downloads/osc/releases/0.2/osc-0.2.tar.gz`

`tar -xzvf OSC-0.2.tar.gz`

`cd osc-0.2/`

`make`

`sudo make install`

`cd ..`
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
