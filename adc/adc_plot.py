import matplotlib.pyplot as plt

def plot_voltage_vs_time (time, voltage, max_voltage, duration):
    plt.figure (figsize = (10,6))
    plt.plot (time, voltage)
    plt.title ("График зависимости напряжения на входе АЦП от времени")
    plt.xlim (0, duration)
    plt.ylim (0, max_voltage*1.1)
    plt.grid (True)
    plt.xlabel ("Время, с")
    plt.ylabel ("Напряжение, В")
    plt.show ()

def plot_sampling_period_hist (time):
    sampling_periods = []
    for i in range (1, len (time)):
        period = time[i] - time[i-1]
        sampling_periods.append (period)
    plt.figure (figsize = (10,6))
    plt.hist (sampling_periods, bins = 20)
    plt.grid (True)
    plt.show ()
