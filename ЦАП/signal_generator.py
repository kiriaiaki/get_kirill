import time
import numpy

def get_sin_wave_amplitude(freq, time):
    v = numpy.sin(2 * numpy.pi * freq * time)
    v = (v + 1) / 2
    return v


def wait_for_sampling_period(sampling_frequency):
    period = 1 / sampling_frequency
    time.sleep(period)