import numpy as np
import matplotlib.pyplot as plt

# 参数设置
fc = 7000  # 截止频率 7 kHz
n = 2  # 二阶滤波器
frequencies = np.linspace(10, 100000, 1000)  # 频率范围从10 Hz到100 kHz

# 计算理论幅频特性
H = 1 / np.sqrt(1 + (frequencies / fc)**(2 * n))

# 假设的更密集的实测数据
measured_frequencies = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                                  2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 
                                  10000, 15000, 20000, 30000, 40000, 50000, 
                                  60000, 70000, 80000, 90000, 100000])
measured_output = np.array([0.98, 0.99, 0.98, 0.97, 0.95, 0.93, 0.90, 0.85, 0.80, 0.75,
                            0.60, 0.40, 0.25, 0.15, 0.10, 0.05, 0.02, 0.01,
                            0.0, -0.5, -3.0, -10.0, -15.0, -20.0, -25.0, 
                            -30.0, -35.0, -40.0, -45.0])

# 绘制理论和实测曲线
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies, 20 * np.log10(H), label='Theoretical Response', color='blue')
plt.semilogx(measured_frequencies, 20 * np.log10(measured_output / 1.0), 'o-', label='Measured Response', color='orange')
plt.title('Theoretical vs Measured Frequency Response of 2nd Order Butterworth Low-pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(fc, color='red', linestyle='--', label='Cutoff Frequency (7 kHz)')
plt.legend()
plt.xlim(10, 100000)  # 将横轴范围设置为10 Hz到100 kHz
plt.ylim(-60, 5)
plt.show()
