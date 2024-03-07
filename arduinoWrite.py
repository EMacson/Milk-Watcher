import time
from serial import Serial

mySerial = Serial(port='COM5', baudrate=9600)

switchOn = "1"
switchOff = "0"

while True:
    mySerial.write(bytes(switchOn,'UTF-8'))
    time.sleep(1)
    mySerial.write(bytes(switchOff,'UTF-8'))
    time.sleep(2)
    