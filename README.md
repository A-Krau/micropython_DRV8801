# micropython_pololu
A basic library to control Pololu DRV8801 (and maybe others)

## Pololu DVR8801

## Class Reference

```python
def __init__(self, dir_pin, speed_pin, bk_pin, sleep_pin, motor_sense, current_sense):
        self.dir_pin = Pin(dir_pin, Pin.OUT)
        self.pwm = PWM(Pin(speed_pin))
        if bk_pin is not None:
            self.bk_pin = Pin(bk_pin, Pin.OUT)
        if sleep_pin is not None:
            self.sleep_pin = Pin(sleep_pin. Pin.OUT)
            self.sleep_pin.value(1)
        self.indicator_led = Pin(25, Pin.OUT)
        self.motor_sense = ADC(Pin(motor_sense))
        self.current_sense = ADC(Pin(current_sense))
        ```

## Funtion Reference

### 
