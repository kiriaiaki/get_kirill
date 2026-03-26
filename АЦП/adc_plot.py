import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)

    plt.title("Зависимость напряжения от времени", fontsize = 14)
    plt.xlabel("Время (с)", fontsize = 12)
    plt.ylabel("Напряжение (V)", fontsize = 12)
    plt.xlim(0, max(time) if time else 3.0)
    plt.ylim(0, max_voltage * 1.1)

    plt.grid(True)

    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []

    for i in range (1, len(time)):
        sampling_periods.append(time[i] - time[i-1])

    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)

    plt.title("Гистограмма периодов измерений", fontsize = 14)
    plt.xlabel("Период (с)", fontsize = 12)
    plt.xlim(0, 0.06)

    plt.grid(True)
    plt.show()
