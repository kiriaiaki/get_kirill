import time

def get_wave_amplitude(freq, time):
    v = freq * time
    v -= int(v)
    if 2 * v < 1:
        v *= 2
    else:
        v = 2 - v * 2
    return v


def wait_for_sampling_period(sampling_frequency):
    period = 1 / sampling_frequency
    time.sleep(period)