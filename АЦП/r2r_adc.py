import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(i) for i in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for number in range (256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio):
                return number

        return 255

    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()
        voltage = digital_value * self.dynamic_range / 256
        return voltage

    def successive_approximation_adc(self):
        low = 0
        high = 255
        cur_pos = 128

        for bit in range(8):
            self.number_to_dac(cur_pos)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio):
                high = cur_pos
                cur_pos = (high + low) // 2

            else:
                low = cur_pos + 1
                cur_pos = (high + low) // 2

        return low - 1
    def get_sar_voltage(self):
        digital_value = self.successive_approximation_adc()
        voltage = digital_value * self.dynamic_range / 256
        return voltage

if __name__ == "__main__":
    try:
        adc = R2R_ADC(dynamic_range = 3.3, compare_time=0.01, verbose=False)
        
        while True:
            try:
                # sc_voltage = adc.get_sc_voltage()
                # print(f"Voltage_SC: {sc_voltage:.3f}V")
                sar_voltage = adc.get_sar_voltage()
                print(f"Voltage_SAR: {sar_voltage:.3f}V")
                time.sleep(0.5)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        adc.deinit()    