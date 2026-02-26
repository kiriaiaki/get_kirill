import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__ (self, gpio_bits, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.freq = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose    
    
        GPIO.setmode (GPIO.BCM)
        GPIO.setup (gpio_bits, GPIO.OUT)
        self.pwm = GPIO.PWM (self.gpio_bits, self.freq)
        self.pwm.start (0)


    def deinit (self):
        GPIO.output (self.gpio_bits, 0)
        GPIO.cleanup ()

    
    def set_voltage (self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print (f"Напряжение выходит за динамический диапозон ЦАП (0.0 - {self.dynamic_range:.2f} B)")
            print ("Устанавливаем 0.0 В")
            number = 0 

        else:
            number = int (voltage * 100/ self.dynamic_range)
            
        self.pwm.ChangeDutyCycle (number)
    

if __name__ == "__main__":
    try:
        dac = PWM_DAC (12, 500, 3.290, True)

        while True:
            try:
                voltage = float (input ("\nВведите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз")
            
    finally:
        dac.deinit ()