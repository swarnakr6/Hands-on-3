#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

# Time the function for various values of n
n_values = np.arange(1, 1001, 50)
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    times.append(elapsed_time)

# Plot time vs n
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'bo', label='Actual Time')

# Fit a polynomial curve to the data
def poly_func(n, a, b, c):
    return a * np.power(n, 2) + b * n + c

popt, _ = curve_fit(poly_func, n_values, times)
a, b, c = popt
plt.plot(n_values, poly_func(n_values, a, b, c), 'r-', label='Fitted Curve: {:.2f}n^2 + {:.2f}n + {:.2f}'.format(a, b, c))

plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time Complexity Analysis')
plt.legend()
plt.grid(True)
plt.show()




# In[2]:


# Plot time vs n with approximate n_0
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'bo', label='Actual Time')
plt.plot(n_values, poly_func(n_values, a, b, c), 'r-', label='Fitted Curve: {:.2f}n^2 + {:.2f}n + {:.2f}'.format(a, b, c))

# Indicate approximate n_0
plt.axvline(x=300, color='g', linestyle='--', label='Approximate n_0')

plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time Complexity Analysis')
plt.legend()
plt.grid(True)
plt.show()



# In[ ]:




