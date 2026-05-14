import get_kirill.dac.mcp4725_driver as mc
import get_kirill.get_kirill.ЦАП.signal_generator_sin as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
voltage = []
times = []

if __name__ == "__main__":
    try:
        mcp = mc.MCP4725 (5)
        start_time = time.time ()

        while True:
            current_time = time.time () - start_time
            times.append (current_time)

            signal = amplitude*sg.get_sin_wave_amplitude (signal_frequency, current_time)
            voltage.append (signal)

            mcp.set_voltage (signal)

            sg.wait_for_sampling_period (sampling_frequency)

    finally:
         mcp.deinit ()
