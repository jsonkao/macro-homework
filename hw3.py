import math

n = 0.02
g = 0.015
delta = 0.1
sigma = 0.25

def y_star():
    return sigma / ((1 + n)*(1 + g) - 1 + delta)

def time_to_double(rate):
    return math.log(2, rate)

print(f'Steady state output: {y_star():.04f}')
print(f'Output time to double: {time_to_double((1 + n) * (1 + g)):.02f}')
print(f'Output per capita time to double: {time_to_double((1 + n)):.02f}')
