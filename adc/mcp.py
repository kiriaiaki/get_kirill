import mcp3021_driver
import time
import adc_plot

voltage_values = []
time_values = []

try:
    mcp = mcp3021_driver.MCP3021 (5.5)
    duration = int (input ("Ведите время эксперимента: "))
    start_time = time.time()

    while (time.time () - start_time) < duration:
        voltage_values.append (mcp.get_voltage ())
        time_values.append (time.time () - start_time)
    adc_plot.plot_voltage_vs_time (time_values, voltage_values, 5.5, duration)
    adc_plot.plot_sampling_period_hist (time_values)

finally:
    mcp.deinit ()
