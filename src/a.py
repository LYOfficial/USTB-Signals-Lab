import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# 生成方波信号
def generate_square_wave(fs, duration, frequency):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    square_wave = 0.5 * (1 + np.sign(np.sin(2 * np.pi * frequency * t)))  # 生成方波
    return t, square_wave

# 高通滤波器设计
def butter_highpass(cutoff, fs, order=2):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

# 应用滤波器
def highpass_filter(data, cutoff, fs):
    b, a = butter_highpass(cutoff, fs)
    return lfilter(b, a, data)

# 设置参数
fs = 1000  # 采样率 1000 Hz
duration = 1.0  # 持续时间 1 秒
frequency = 5  # 方波频率 5 Hz
cutoff_frequency = 2  # 高通滤波器截止频率 2 Hz

# 生成方波信号
t, square_wave = generate_square_wave(fs, duration, frequency)

# 通过高通滤波器
filtered_signal = highpass_filter(square_wave, cutoff_frequency, fs)

# 绘制图形
plt.figure(figsize=(12, 6))

# 原始方波
plt.subplot(2, 1, 1)
plt.plot(t, square_wave, label='原始方波', color='blue')
plt.title('原始方波')
plt.xlabel('时间 (秒)')
plt.ylabel('幅值')
plt.grid()
plt.legend()

# 高通滤波后的信号
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, label='高通滤波后信号', color='orange')
plt.title('高通滤波后信号')
plt.xlabel('时间 (秒)')
plt.ylabel('幅值')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
