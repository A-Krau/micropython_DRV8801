from machine import Pin, PWM
from time import sleep
from pololu import Motor_Driver

duty =65000
freq = 1000

motor = Motor_Driver(16,17,None,freq,duty,26,27)
            #(self, dir_pin, speed_pin, bk_pin, freq, duty, motor_sense, current_sense)

while True:
    motor.speed()
    if motor.pot_read() <= 400:
        motor.direction(1)
    if motor.pot_read() >= 65000:
        motor.direction(0)
    print(motor.pot_read())
    motor.current_read()
    sleep(.1)
    
    