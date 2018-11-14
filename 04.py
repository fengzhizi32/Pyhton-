# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:31:59 2018

@author: fengzhizi32
"""
# 导入模块
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# 中文设置
# 设置字体为：黑体
matplotlib.rcParams['font.family'] = 'SimHei'
# 设置字体风格，正常 'normal' 或 斜体 'italic'
matplotlib.rcParams['font.style'] = 'italic'
# 设置字体大小，整数字号或者 'large' 或 'x-small'
matplotlib.rcParams['font.size'] = 20

# 设置所在区域范围
plt.subplot(311)
# 添加数据
plt.plot([3, 1, 4, 5, 2])

plt.subplot(313)
a = np.arange(10)
plt.plot(a, np.cos(2*np.pi*a), 'r--')

# 设置轴说明
plt.xlabel('横轴（时间）')
plt.ylabel('纵轴（振幅）')

# 保存图片png(名称， 像素)
plt.savefig('test4', dpi=600)
# 显示/查看
plt.show()