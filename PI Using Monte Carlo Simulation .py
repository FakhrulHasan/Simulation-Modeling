# -*- coding: utf-8 -*-
"""011171168_Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e5yoxmWDapalmDtdL5d5fI3J0xahFA14
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import random
trial_no = int(input())
r= 8.5

x_hits=[]
y_hits=[]
x_nhits=[]
y_nhits=[]



def monte_carlo(trial_no):
  hits = 0
  for i in range(trial_no):
    X_r = random.uniform(0, r)
    Y_r = random.uniform(0, r)

    d = math.sqrt(X_r**2 + Y_r**2)

    if d <= r:
      hits+=1
      x_hits.append(X_r)
      y_hits.append(Y_r)
    elif d>r:
      x_nhits.append(X_r)
      y_nhits.append(Y_r)
  pi = ((hits/trial_no)*(8.5*8.5)*4) / (r**2)
  return pi   


pi_value = monte_carlo(trial_no)


print(pi_value)

plt.figure()
xlist = np.linspace(-8.5, 8.5, 100) 
ylist = np.linspace(0, 8.5, 100)
X,Y = np.meshgrid(xlist, ylist)


F = X**2 + Y**2 - 8.5**2  
plt.contour(X, Y, F, [0], colors = 'b', linestyles = 'solid')
plt.axes().set_aspect('equal')

plt.plot(x_hits,y_hits, 'gs') 
plt.plot(x_nhits,y_nhits, 'rs')      
plt.show()