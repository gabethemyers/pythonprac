import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math


def find_zstar(CL):
    """Returns a Zstar value calulated from Confidence Level"""
    return abs(stats.norm.ppf((1-CL)/2))

def find_CI(ph, zstar, n):
    """Returns a tuple of the confidence interval, and the standard error"""
    se = math.sqrt((ph * (1 - ph)/n))
    rc = ph + zstar * se
    lc = ph - zstar * se

    return (lc, rc), se

# Getting inputs for values
confidence_level = float(input('Enter confidence level as a decimal: '))
p_hat = float(input('enter p hat as a decimal: '))
n = float(input('enter n: '))

# using function to get confidence level and standard error from inputs
ci, se = find_CI(p_hat, find_zstar(confidence_level), n)

# Generating datasets for graph
x_values = np.linspace(p_hat - 3*se, p_hat + 3*se, 100)
y_values = stats.norm.pdf(x_values, p_hat, se)

# uses sentence structure for confidence interval
plt.text(p_hat - 3*se, 0, f'You can be {confidence_level*100}% confident that it will be between {round(ci[0], 3)} and {round(ci[1], 3)}')

# sets x axis ticks to correct values for normal model
plt.xticks([round(p_hat + x*se, 3) for x in range(-3,4)])

# plotting horizontal lines at the two confidence intervals
plt.axvline(ci[0])
plt.axvline(ci[1])

plt.plot(x_values, y_values)
plt.show()