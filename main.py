from machine import Pin
from machine import PWM
from time import sleep
from pololu import Motor_Driver

duty = 15000
freq = 1000

motor = Motor_Driver(16,17,None,None,26,27)
            #(self, dir_pin, speed_pin, bk_pin, sleep_pin, motor_sense, current_sense):

while True:
    motor.speed(freq, duty)
    if motor.pot_read() <= 400:
        motor.extend()
    if motor.pot_read() >= 65000:
        motor.retract()
    print(motor.pot_read())
    motor.current_read()
    sleep(.1)
    
    
