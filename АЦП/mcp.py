import adc_plot
import time
from mcp3021_driver import MCP3021

mcp = MCP3021(dynamic_range = 3.3)

voltage_values = []
time_values = []
duration = 1.0

if __name__ == "__main__":
    try:
        start_time = time.time()
        while ((time.time() - start_time) < duration):
            voltage_values.append(mcp.get_voltage())
            time_values.append(time.time() - start_time)

        adc_plot.plot_voltage_vs_time(time = time_values, voltage = voltage_values, max_voltage = 12)
        adc_plot.plot_sampling_period_hist(time = time_values)

    finally:
        mcp.deinit()
