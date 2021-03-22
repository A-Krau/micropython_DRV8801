# micropython_pololu
A basic library to control Pololu DRV8801 (and maybe others)

## Pololu DRV8801

## Class Reference

```python
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
 ```
Instantiate the class and pass the below arguments to run in __init__.

dir_pin: GPIO pin connected to DVR8801 "DIR".

speed_pin: GPIO pin connected to DVR8801 "PWM".

bk_pin: GPIO pin connected to DVR8801 "Brake". Set `None` if not used.

sleep_pin: GPIO pin connected to DVR8801 "Sleep". Default awake.  Set `None` if not used.

motor_sense:  Analog GPIO pin connected to potentiometer in motor used for testing.  Set `None` if not used.

current_sense: Analog GPIO pin connected to DVR8801 `CS` pin.  Set `None` if not used.

indicator: Enables GPIO 25 to be used as an indicator that mirrors dir_pin.

## Funtion Reference

### speed(freq, duty)

Sets the frequency and duty of the PWM signal sent to the DVR8801 PWM pin.

```python
def speed(self, freq, duty):
    self.pwm.freq(freq)
    self.pwm.duty_u16(duty)
```
### stop()

Sets the duty of the PWM pin to 0.

```python
def stop(self):
    self.pwm.duty_u16(0)
```

### extend()

Sets dir_pin low as well as GPIO 25.

```python
def extend(self):
    self.indicator_led.value(0)
    self.dir_pin.value(0)
```

### retract()

Sets dir_pin high as well as GPIO 25.

```python
def retract(self):
    self.indicator_led.value(1)
    self.dir_pin.value(1)
```

### brake()

Sets bk_pin high, enabling DVR8801 Brake mode.

```python
def brake(self):
    self.bk_pin.value(1)
```

### release()

Sets bk_pin low, disabling DVR8801 Brake mode.

```python
def brake(self):
    self.bk_pin.value(1)
```

### sleep()

Sets sleep_pin low, enabling DVR8801 sleep mode.

```python
def sleep(self):
    self.sleep_pin.value(0)
```

### wake()

Sets sleep_pin high, disabling DVR8801 sleep mode.

```python
def wake(self):
    self.sleep_pin.value(1)
```

### pot_read()

Returns poteniometer reading of current_sense.  As written code has unused `self.travel` that converts motor_sense potentiometer reading to linear distance of tested motors travel. (Ray Allen B6-7T).

Filtered pot is avereged over 16 readings to help reduce noise in analog signal.

```python
def pot_read(self):
    filtered_pot = 1
    for i in range(16):
        filtered_pot += self.motor_pot.read_u16()
    filtered_pot = filtered_pot / 16
    self.travel = ((self.motor_pot.read_u16())/93617)
    self.travel = round(self.travel, 3)
    return (filtered_pot)
```

### current_read()

Prints the current draw of motor attached to DVR8801.

```python
def current_read(self):
    voltage = self.current_sense.read_u16()
    voltage = voltage/19858
    current = round(voltage/.5, 2)
    print("Amps: " + str(current))
```
