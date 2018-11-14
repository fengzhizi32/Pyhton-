# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:58:40 2018

@author: fengzhizi32
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置中文样式
matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.style']='italic'
matplotlib.rcParams['font.size']=20

# 生成数据
a = np.arange(0.0, 5.0, 0.02)

# 设置轴说明
plt.xlabel('横轴：时间')
plt.ylabel('纵轴：振幅')

# 构建数据图表
plt.plot(a, np.cos(2*np.pi*a), 'r--')

# 保存文件
plt.savefig('test5', dpi=600)

# 展示数据图表
plt.show()