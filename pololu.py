from machine import Pin
from machine import PWM
from machine import ADC
import time

class Motor_Driver:
    def __init__(self, dir_pin, speed_pin, bk_pin, freq, duty, motor_sense, current_sense):
        self.dir_pin = Pin(dir_pin, Pin.OUT)
        print(dir_pin)
        self.pwm = PWM(Pin(speed_pin))
        if bk_pin is not None:
            self.bk_pin = Pin(bk_pin. Pin.OUT)
        self.freq = freq
        self.duty = duty
        self.indicator_led = Pin(25, Pin.OUT)
        self.motor_sense = ADC(Pin(motor_sense))
        self.current_sense = ADC(Pin(current_sense))
        
    def speed(self):
        self.pwm.freq(self.freq)
        self.pwm.duty_u16(self.duty)
        
    def direction(self, x):
        self.indicator_led.value(x)
        self.dir_pin.value(x)
    
    def pot_read(self):
        travel = ((self.motor_sense.read_u16())/93617)
        travel = round(travel, 3)
        return (self.motor_sense.read_u16())
        
    def current_read(self):
        voltage = self.current_sense.read_u16()
        voltage = voltage/19858
        current = round(voltage/.5, 2)
        print("Amps: " + str(current))
        
