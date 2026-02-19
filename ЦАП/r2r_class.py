import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__ (self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose    
    
        GPIO.setmode (GPIO.BCM)
        GPIO.setup (gpio_bits, GPIO.OUT)


    def deinit (self):
        GPIO.output (gpio_bits, 0)
        GPIO.cleanup ()


    def set_number (self, number):
        a = [int (bit) for bit in bin (number)[2:].zfill(8)]
        GPIO.output (gpio_bits, a)
    

    def set_voltage (self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print ("Напряжение выходит за динамический диапозон ЦАП (0.0 - {dynamic_range:.2f} B)")
            print ("Устанавливаем 0.0 В")
            number = 0 

        else:
            number = int (voltage / dynamic_range * (2**8 - 1)) 
            
        self.set_number (number)
    

if __name__ == "__main__":
    try:
        dac = R2R_DAC ([22, 27, 17, 26, 25, 21, 20, 16], 3.183, True)

        while True:
            try:
                voltage = float (input ("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")
            
    finally:
        dac.deinit ()