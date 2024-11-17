import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
frequencies_kHz = np.array([0, 3, 4, 5, 7, 9, 10, 12, 15, 17, 19, 20, 23, 25, 29, 33, 37, 44, 48, 50])  # kHz
amplitudes_mV = np.array([0, 42, 55, 75, 125, 153, 170, 190, 235, 250, 256, 268, 272, 278, 286, 294, 300, 304, 306, 306])  # mV

# 将幅值转换为 dB
input_amplitude_mV = 1000  # 1V = 1000 mV
gain_dB = 20 * np.log10(amplitudes_mV / input_amplitude_mV)

# 绘图
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies_kHz, gain_dB, marker='o')
plt.title('高通滤波器幅频特性曲线')
plt.xlabel('频率 (kHz)')
plt.ylabel('增益 (dB)')
plt.grid(which='both', linestyle='--')

# 调整横轴范围
plt.xlim(1, 60)  # 设置横轴范围为 1 kHz 到 60 kHz
plt.ylim(-50, 10)

# 显示图形
plt.show()
