import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__ (self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.freq = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode (GPIO.BCM)
        GPIO.setup (self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM (self.gpio_pin, self.freq)
        self.pwm.start (0)

    def deinit (self):
        self.pwm.stop ()
        GPIO.output (self.gpio_pin, 0)
        GPIO.cleanup ()

    def set_voltage (self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print (f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print ("Устанавлниваем 0.0 В")
            duty_cycle = 0
            return 0

        else:
            duty_cycle = (voltage / self.dynamic_range * 100)

        self.pwm.ChangeDutyCycle (duty_cycle)
        if self.verbose:
            print (f"Коэффициент заполнения {duty_cycle:.2f}%")

if __name__ == "__main__":
    try:
        dac = PWM_DAC (12, 500, 3.29, True)

        while True:
            try:
                voltage = float (input ("Введите напряжение в Вольтах: "))
                dac.set_voltage (voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()
