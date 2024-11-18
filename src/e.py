import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# 设计二阶巴特沃斯低通滤波器
def butter_lowpass(cutoff, fs, order=2):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=2):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# 参数设置
fs = 100000  # 采样频率 100 kHz
cutoff = 5000  # 截止频率 5 kHz
t = np.linspace(0, 0.01, fs // 10)  # 10 ms时间

# 不同频率的方波信号
frequencies = [1000, 5000, 10000]  # 1 kHz, 5 kHz, 10 kHz
signals = [0.5 * (1 + np.sign(np.sin(2 * np.pi * f * t))) for f in frequencies]

# 绘制输入和输出波形
plt.figure(figsize=(15, 10))

for i, (f, signal) in enumerate(zip(frequencies, signals)):
    output = lowpass_filter(signal, cutoff, fs)
    
    # 输入信号
    plt.subplot(len(frequencies), 2, 2*i + 1)
    plt.plot(t, signal, label='Input Signal ({} Hz)'.format(f))
    plt.title('Input Signal ({} Hz)'.format(f))
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()
    
    # 输出信号
    plt.subplot(len(frequencies), 2, 2*i + 2)
    plt.plot(t, output, label='Output Signal', color='orange')
    plt.title('Output Signal (Filtered)')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()

plt.tight_layout()
plt.show()
