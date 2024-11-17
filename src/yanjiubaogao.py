import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import matplotlib


# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生成信号和噪声
fs = 100000  # 采样率
t = np.arange(0, 1.0, 1.0/fs)
signal_freq = 5000  # 信号频率
noise_freq = 15000  # 噪声频率

signal = np.sin(2 * np.pi * signal_freq * t)
noise = 0.5 * np.sin(2 * np.pi * noise_freq * t)
input_signal = signal + noise

# 巴特沃斯滤波器设计
def butter_lowpass(cutoff, fs, order=2):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=2):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# 设置不同的截止频率
cutoff_frequencies = [6000, 10000, 12000]
results = {}

# 绘制时域和频域图
plt.figure(figsize=(14, 8))

for i, cutoff in enumerate(cutoff_frequencies):
    filtered_signal = butter_lowpass_filter(input_signal, cutoff, fs)
    
    # 计算信噪比
    signal_power = np.mean(signal**2)
    noise_power = np.mean((filtered_signal - signal)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    results[cutoff] = snr
    
    # 绘制时域图
    plt.subplot(2, len(cutoff_frequencies), i+1)
    plt.plot(t, filtered_signal, label=f'Cutoff: {cutoff} Hz')
    plt.title(f'Time Domain (Cutoff: {cutoff} Hz)')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()
    
    # 绘制频域图
    plt.subplot(2, len(cutoff_frequencies), i+1+len(cutoff_frequencies))
    freqs, response = freqz(butter_lowpass(cutoff, fs)[0], butter_lowpass(cutoff, fs)[1], worN=8000)
    plt.plot(0.5*fs*freqs/np.pi, np.abs(response), label=f'Cutoff: {cutoff} Hz')
    plt.title('Frequency Response')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Gain')
    plt.grid()

plt.tight_layout()
plt.show()

# 输出信噪比表格
print("Cutoff Frequency (Hz) | SNR (dB)")
for cutoff, snr in results.items():
    print(f"{cutoff:20} | {snr:.2f}")
