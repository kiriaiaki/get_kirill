import pwm_dac as pd
import signal_generator as sg
import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        pwm = pd.PWM_DAC(12, 500, 3.183, False)
         
        while True:
            val = sg.get_sin_wave_amplitude(signal_frequency, time.time())
            # print(val)
            pwm.set_voltage(amplitude * val)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
         pwm.deinit()