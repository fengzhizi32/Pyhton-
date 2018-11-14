# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:26:04 2018

@author: fengzhizi32
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 产生时间序列   从配置文档中读取时间相关数据
rate_h, hstrain = wavfile.read(r'H1_Strain.wav', 'rb')
rate_l, lstrain = wavfile.read(r'L1_Strain.wav', 'rb')
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose

# 读取应变数据
htime_interval = 1/rate_h
ltime_interval = 1/rate_l

htime_len = hstrain.shape[0]/rate_h
htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
ltime_len = lstrain.shape[0]/rate_l
ltime = np.arange(-ltime_len/2, htime_len/2, ltime_interval)

# 绘制H1 Strain   使用来自‘H1‘探测器的数据作图
# 创建一个绘图空间
fig = plt.figure(figsize=(12, 6))
plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
# 画出以时间为x轴，应变数据为y轴的图像，并设置标题和坐标轴的标签
plth.set_xlabel('Time (seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

# 显示并保存图像
# 自动调整图像外部边缘
fig.tight_layout()

plt.savefig('wf_template.png')
plt.show()
plt.close(fig)