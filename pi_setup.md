# Raspberry Pi setup and configurations

## SSHFS
Mount the home directory on raspberry pi:
`sshfs pi@192.168.xx.yy:/home ~/pi`

See all mounted directories:
`mount`

Unmount a directory:
`umount ~/pi`

## Pololu Maestro USB Servo Controller Linux Software
A few packages are required to run this software. Install them with the command:
`sudo apt-get install libusb-1.0-0-dev mono-runtime libmono-winforms2.0-cil`

Follow the other instructions in the included README.txt

# LED Controller Software Requirements
Remember to enable SPI on the Raspberry Pi.
Install these packages:
```
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install spidev
```

# Other configurations

## WS2801 wire color codes
| Color | Pinout |
| --- | --- |
| Black | 5V |
| Green | CLK |
| Red | SI |
| Blue | GND |
