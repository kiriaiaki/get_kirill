import get_kirill.dac.r2r_dac as r2r
import get_kirill.get_kirill.ЦАП.signal_generator_sin as sg
import time

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000
voltage = []
times = []

try:
    dac = r2r.R2R_DAC ([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    start_time = time.time ()
    while True:
        current_time = time.time () - start_time
        times.append (current_time)

        signal = amplitude*sg.get_sin_wave_amplitude (signal_frequency, current_time)
        voltage.append (signal)

        dac.set_voltage (signal)

        sg.wait_for_sampling_period (sampling_frequency)

finally:
    dac.deinit ()
