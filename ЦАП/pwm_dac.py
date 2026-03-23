import RPi.GPIO as GPIO

dynamic_range = 3.3

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin, pwm_frequency)
        self.pwm.start(0)
        
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        duty = int(100 * voltage / self.dynamic_range)
        if self.verbose:
            print(f"duty is {duty}")
        self.pwm.ChangeDutyCycle(duty)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()