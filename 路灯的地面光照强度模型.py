import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 数据点
r_data = np.array([3, 4.5, 6, 7.5, 8.4, 5])
E_data = np.array([18, 14, 9, 6, 5, 13])

# 模型函数
def improved_model(r, C, n, A):
    return C / (r**n + A)

# 设置拟合参数范围，确保单调递减
bounds = ([0, 0, 0], [np.inf, 5, np.inf])  # C > 0, n > 0, A >= 0

# 使用 curve_fit 进行拟合
popt, pcov = curve_fit(improved_model, r_data, E_data, bounds=bounds)

# 提取拟合参数
C, n, A = popt
print(f"拟合得到的参数: C = {C:.2f}, n = {n:.2f}, A = {A:.2f}")

# 生成拟合曲线数据
r_fit = np.linspace(1, 20, 100)  # 确保拟合范围是 [1, 20]
E_fit = improved_model(r_fit, C, n, A)

# 验证单调性
is_monotonic = np.all(np.diff(E_fit) < 0)
print(f"拟合模型在 [1, 20] 范围内是否单调递减: {is_monotonic}")

# 绘制原始数据和拟合曲线
plt.scatter(r_data, E_data, label='数据点')
plt.plot(r_fit, E_fit, 'r-', label='拟合曲线')
plt.xlabel('距离 r (m)')
plt.ylabel('光照强度 E (lux)')
plt.legend()
plt.title('模型拟合结果')
plt.show()
