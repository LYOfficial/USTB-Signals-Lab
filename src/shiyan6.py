import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 之后的绘图代码...

# 频率范围
frequencies = np.array([0, 1, 3, 5, 10, 20]) * 1e3  # Hz
omega = 2 * np.pi * frequencies  # rad/s
wc = 2 * np.pi * 5000  # 截止频率

# 计算传递函数
H = 1 / (1 + (1/np.sqrt(2)) * (1j * omega / wc) + (1j * omega / wc)**2)

# 幅值（V）
output_voltage = np.abs(H)  # 假设输入为1V

# 增益 (dB)
gain_dB = 20 * np.log10(output_voltage)

# 绘图
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies, gain_dB, marker='o')
plt.title('低通滤波器幅频特性曲线')
plt.xlabel('频率 (Hz)')
plt.ylabel('增益 (dB)')
plt.grid(which='both', linestyle='--')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(5000, color='red', linestyle='--', label='截止频率 5 kHz')
plt.legend()
plt.xlim(10, 20000)
plt.ylim(-40, 10)

# 保存为 PNG 图片
plt.savefig('butterworth_filter_response.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()