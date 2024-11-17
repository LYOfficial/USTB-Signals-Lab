import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz
import matplotlib


# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 方波参数
frequency = 30e3  # 30 kHz
amplitude = 1.0   # 1 V
sampling_rate = 1e6  # 1 MHz
duration = 1e-3   # 1 ms

# 时间轴
t = np.arange(0, duration, 1/sampling_rate)

# 生成方波
square_wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))

cutoff_freq = 10e3  # 10 kHz
order = 2
b, a = butter(order, cutoff_freq / (0.5 * sampling_rate), btype='high')

# 计算滤波器频率响应
w, h = freqz(b, a, worN=8000, fs=sampling_rate)

# 绘制时域波形
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, square_wave, label='输入方波')
plt.title('理论时域')
plt.xlabel('时间 [秒]')
plt.ylabel('幅度 [伏特]')
plt.legend()
plt.grid()

# 绘制频率响应
plt.subplot(2, 1, 2)
plt.plot(w, 20 * np.log10(abs(h)), label='高通滤波器响应')
plt.title('理论频谱')
plt.xlabel('频率 [赫兹]')
plt.ylabel('幅度 [分贝]')
plt.xlim(0, 100e3)  # 只显示0到100 kHz范围
plt.ylim(-60, 5)
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('theoretical_waveform_and_spectrum.png')
plt.show()