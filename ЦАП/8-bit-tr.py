
import r2r_dac as r2r
import tr as tr
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
         
        while True:
            val = tr.get_wave_amplitude(signal_frequency, time.time())
            # print(val)
            dac.set_voltage(amplitude * val)
            tr.wait_for_sampling_period(sampling_frequency)

    finally:
         dac.deinit()