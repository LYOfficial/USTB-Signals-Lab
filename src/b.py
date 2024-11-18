import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

# 高通滤波器设计
def highpass_filter(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

# 设置参数
cutoff_frequency = 40000  # 高通滤波器截止频率 40 kHz
sampling_rate = 200000     # 采样率 200 kHz
frequency_range = np.linspace(1000, 60000, 1000)  # 频率范围 1-60 kHz

# 设计高通滤波器
b, a = highpass_filter(cutoff_frequency, sampling_rate)

# 计算幅频特性
w, h = freqz(b, a, worN=frequency_range, fs=sampling_rate)

# 绘制幅频特性曲线
plt.figure(figsize=(10, 6))
plt.plot(w, abs(h), 'b')  # 使用幅度值
plt.title('High-pass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.ylim(0, 1.1)  # 设置y轴范围
plt.xscale('log')  # 使用对数坐标
plt.grid(which='both', axis='both')
plt.axvline(cutoff_frequency, color='r', linestyle='--', label='Cutoff Frequency (40 kHz)')
plt.legend()
plt.show()
