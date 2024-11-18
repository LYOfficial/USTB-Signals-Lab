import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 使负号正常显示

# 生成信号和噪声
def generate_signal_and_noise(fs, duration):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    signal = 1 * np.sin(2 * np.pi * 5000 * t)  # 5 kHz信号，幅值1 V
    noise = 0.5 * np.random.normal(0, 1, signal.shape)  # 15 kHz噪声，幅值0.5 V
    return t, signal + noise, signal, noise

# 巴特沃斯低通滤波器设计
def butter_lowpass(cutoff, fs, order=2):
    nyq = 0.5 * fs  # 计算奈奎斯特频率
    normal_cutoff = cutoff / nyq  # 归一化截止频率
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# 应用滤波器
def lowpass_filter(data, cutoff, fs):
    b, a = butter_lowpass(cutoff, fs)
    return lfilter(b, a, data)

# 设置参数
fs = 100000  # 采样率 100 kHz
duration = 1.0  # 持续时间 1秒
cutoff_frequencies = [6000, 10000, 12000]  # 截止频率

# 生成信号和噪声
t, noisy_signal, signal, noise = generate_signal_and_noise(fs, duration)

# 绘制时域和频域图表
plt.figure(figsize=(15, 10))

for i, cutoff in enumerate(cutoff_frequencies):
    # 滤波
    filtered_signal = lowpass_filter(noisy_signal, cutoff, fs)

    # 时域图
    plt.subplot(3, 2, i * 2 + 1)
    plt.plot(t, noisy_signal, label='带噪信号', alpha=0.5)
    plt.plot(t, filtered_signal, label='滤波后信号', color='orange')
    plt.title(f'截止频率: {cutoff} Hz')
    plt.xlabel('时间 (秒)')
    plt.ylabel('幅值 (V)')
    plt.legend()
    plt.grid()

    # 计算频率响应
    b, a = butter_lowpass(cutoff, fs)  # 获取滤波器系数
    w, h = freqz(b, a, worN=8000)

    # 频域图
    plt.subplot(3, 2, i * 2 + 2)
    plt.plot(0.5 * fs * w / np.pi, abs(h), 'b')
    plt.title(f'截止频率: {cutoff} Hz 的频率响应')
    plt.xlabel('频率 (Hz)')
    plt.ylabel('幅度')
    plt.grid()

plt.tight_layout()
plt.show()
