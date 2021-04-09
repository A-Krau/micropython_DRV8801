from machine import Pin
from machine import PWM
from machine import ADC
import time

class Motor_Driver:
    def __init__(self, dir_pin, speed_pin, bk_pin, sleep_pin, motor_pot, current_sense, indicator):
        self.dir_pin = Pin(dir_pin, Pin.OUT)
        self.pwm = PWM(Pin(speed_pin))
        if bk_pin is not None:
            self.bk_pin = Pin(bk_pin, Pin.OUT)
        if sleep_pin is not None:
            self.sleep_pin = Pin(sleep_pin. Pin.OUT)
            self.sleep_pin.value(1)
        if indicator is True:
            self.indicator_led = Pin(25, Pin.OUT)
        if motor_pot is not None:
            self.motor_pot = ADC(Pin(motor_pot))
        if motor_pot is not None:
            self.current_sense = ADC(Pin(current_sense))
        
    def speed(self, freq, duty):
        self.pwm.freq(freq)
        self.pwm.duty_u16(duty)
        
    def stop(self):
        self.pwm.duty_u16(0)
        
    def extend(self):
        self.dir_pin.value(0)
        try:
            self.indicator_led.value(0)
        except AttributeError:
            pass
        
    def retract(self):
        self.dir_pin.value(1)
        try:
            self.indicator_led.value(1)
        except AttributeError:
            pass
    
    def brake(self):
        self.bk_pin.value(1)
        
    def release(self):
        self.bk_pin.value(0)
    
    def sleep(self):
        self.sleep_pin.value(0)
        
    def wake(self):
        self.sleep_pin.value(1)
        
    def pot_read(self):
        filtered_pot = 1
        for i in range(16):
            filtered_pot += self.motor_pot.read_u16()
        filtered_pot = filtered_pot / 16
        self.travel = ((self.motor_pot.read_u16())/93617)
        self.travel = round(self.travel, 3)
        return filtered_pot
    
    def current_read(self):
        voltage = self.current_sense.read_u16()
        voltage = voltage/19858
        current = round(voltage/.5, 2)
        print("Amps: " + str(current))

