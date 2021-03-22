import json
from machine import Pin
from machine import PWM
from time import sleep
from pololu import Motor_Driver

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

cycle = 0
duty = 65000
freq = 1000

motor = Motor_Driver(16,17,18,None,26,27, True)
            #(self, dir_pin, speed_pin, bk_pin, sleep_pin, motor_sense, current_sense):
motor.speed(freq, duty)

while True:
    if button.value() == True:
        led.off()
    else:
        led.on()       
    if motor.pot_read() <= 400:
        motor.speed(freq, duty)
        motor.extend()
        cycle += 1
        print(cycle)
    if motor.pot_read() >= 20000:
        motor.speed(freq, duty)
        motor.retract()     
    print(motor.pot_read())
    motor.current_read()
    if cycle >= 2:
        motor.brake()
        motor.stop()
        if button.value() == False:
            cycle = 0
            motor.release()
            motor.speed(freq, duty)
    sleep(.1)
    
    
