import pwm_dac as pd
import tr as tr
import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        pwm = pd.PWM_DAC(12, 500, 3.183, False)
         
        while True:
            val = tr.get_wave_amplitude(signal_frequency, time.time())
            # print(val)
            pwm.set_voltage(amplitude * val)
            tr.wait_for_sampling_period(sampling_frequency)

    finally:
         pwm.deinit()