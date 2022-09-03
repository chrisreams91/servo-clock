# 3d printed servo-clock

Prusa i3 MK3S+ 3D Printer

Prusament PETG Urban Grey For the All of the parts

TBD for the segment covers

Used https://www.thingiverse.com/thing:3266949 for the design and list of materials

# Hardware

1x Raspberry Pi 3b+

2x Adafruit PCA9685 boards https://www.adafruit.com/product/815

1x https://www.amazon.com/Belker-Universal-Adapter-Supply-Speaker/dp/B07N18XN84

28x servo motors https://www.amazon.com/gp/product/B072V529YD/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1

Originaly tried these boards but they did not work on arrival https://www.amazon.com/Onyehn-Channel-PCA9685-Arduino-Raspberry/dp/B07GJCPWW2

# Setting up the Pi from factory reset

1. Basic pi config

   ```sudo apt update

   sudo apt-get install i2c-tools

   sudo apt install git

   sudo apt-get git

   sudo i2cdetect -y 1

   sudo raspi-config #enable i2c and spa / configure timezone

   ```

2. Circuit python lib installation

   https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

   ```sudo apt-get update

   sudo apt-get upgrade

   sudo apt-get install python3-pip

   sudo pip3 install --upgrade setuptools

   cd ~

   sudo pip3 install --upgrade adafruit-python-shell

   wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py

   sudo python3 raspi-blinka.py

   ```

3. Validating setup was done correctly

   create and run the python script below to validate

   ```
   import board
   import digitalio
   import busio

   print("Hello blinka!")

   pin = digitalio.DigitalInOut(board.D4)
   print("Digital IO ok!")

   i2c = busio.I2C(board.SCL, board.SDA)
   print("I2C ok!")

   spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
   print("SPI ok!")

   print("done!")
   ```

4. install and set to run on boot

   ```
   git clone https://github.com/chrisreams91/servo-clock.git

   sudo nano /etc/rc.local

   ```

   and add

   ```
   python /yourPathToDir/servo-clock/main.py
   ```
