from RPi import GPIO
import time

sense_pin = 22
supply_pin= 18

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sense_pin, GPIO.IN)
    GPIO.setup(supply_pin, GPIO.OUT)
    GPIO.output(supply_pin, GPIO.HIGH)

def check_state():
    if GPIO.input(sense_pin):
        print "HIGH"
    else:
        print "LOW"

if __name__ == "__main__":
    init()
    while 1:
        check_state()
        time.sleep(2)
