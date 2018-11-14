# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:17:42 2018

@author: fengzhizi32
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)
plt
.plot(a, np.cos(2*np.pi*a), 'r--')

p



lt.xlabel('横轴：时间', fontproperties='SimHei', fontstyle='italic' ,fontsize=20)
plt.ylabel('纵轴：振幅', fontproperties='STSong', fontstyle='normal', fontsize=20)
plt.title('正弦波实例 $y = cos(2\pi x)$', fontproperties='SimHei', fontstyle='italic' ,fontsize=20)
plt.text(2, 1, r'$\mu=100$', fontsize=15)

plt.axis([-1, 6, -2, 2])

plt.grid(True)

plt.savefig('test7', pli=600)

plt.show()