# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:02:34 2018

@author: fengzhizi32
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(10)
print(a)
print(type(a))
plt.subplot(311)
plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-')

plt.subplot(313)
plt.plot(a*1.5, a, a*2.5, a, a*3.5, a, a*4.5, a)
plt.savefig('test3', dpi=600)
plt.show()