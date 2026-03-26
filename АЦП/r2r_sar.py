import r2r_adc as r2r
import adc_plot
import time

adc = r2r.R2R_ADC(dynamic_range = 3.3, compare_time = 0.0001, verbose = False)

voltage_values = []
time_values = []
duration = 3.0

if __name__ == "__main__":
    try:
        start_time = time.time()
        while ((time.time() - start_time) < duration):
            voltage_values.append(adc.get_sar_voltage())
            time_values.append(time.time() - start_time)

        adc_plot.plot_voltage_vs_time(time = time_values, voltage = voltage_values, max_voltage = 3.3)
        adc_plot.plot_sampling_period_hist(time = time_values)

    finally:
        adc.deinit()