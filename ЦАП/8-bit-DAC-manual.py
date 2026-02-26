import RPi.GPIO as GPIO

dynamic_range = 3.3

def voltage_to_number (voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print (f"Напряжение выходит за динамический диапозон ЦАП (0.0 - {dynamic_range:.2f} B)")
        print ("Устанавливаем 0.0 В")
        return 0

    return int (voltage / dynamic_range * (2**8 - 1)) 

def d_to_b (number):
    return [int (bit) for bit in bin (number)[2:].zfill(8)]
    
ports = [22, 27, 17, 26, 25, 21, 20, 16][::-1]
GPIO.setmode (GPIO.BCM)
GPIO.setup (ports, GPIO.OUT)

try:
    while True:
        try:
            voltage = float (input ("\nВведите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            a = d_to_b(number)

            GPIO.output (ports, a)
        except ValueError:
            print ("Вы ввели не число. Попробуйте ещё раз")

finally:
    GPIO.output (ports, 0)
    GPIO.cleanup ()