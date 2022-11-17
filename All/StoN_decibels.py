import math

signal_power = 100
noise_power = 8
ratio = signal_power/noise_power
decibels = 10 * math.log10(ratio)

print (decibels)