# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
plt.ylabel('Grade')
plt.axis([-1, 10, 0, 6])
plt.savefig('test1', dpi=600)
plt.show()