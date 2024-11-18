import numpy as np
import matplotlib.pyplot as plt

# 定义参数
fc = 5000  # 截止频率 5 kHz
n = 2  # 二阶
frequencies = np.logspace(1, 5, 20)  # 频率范围 10 Hz 到 100 kHz，共20个点

# 计算理论幅频特性
H = 1 / np.sqrt(1 + (frequencies / fc) ** (2 * n))

# 绘制理论曲线
plt.figure(figsize=(10, 6))
plt.plot(frequencies, H, label='理论幅频特性', color='blue')

# 添加实测曲线（假设实测数据）
measured_frequencies = np.array([10, 100, 200, 500, 800, 1000, 1500, 2000, 3000, 4000,
                                  5000, 6000, 8000, 10000, 12000, 15000, 20000, 30000, 50000, 100000])
measured_amplitudes = np.array([1.0, 0.98, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70,
                                 0.60, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.02])

plt.plot(measured_frequencies, measured_amplitudes, 'o-', label='实测幅频特性', color='red')

# 图形设置
plt.title('二阶巴特沃斯低通滤波器的幅频特性')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅值')
plt.grid(which='both', linestyle='--')
plt.legend()
plt.xscale('log')
plt.xlim(10, 100000)
plt.ylim(0, 1.1)
plt.tight_layout()
plt.show()
