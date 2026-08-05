"""
图 1.3.8-2：双下降现象（Double Descent）
输出：viz/images/1.3.8-2_double_descent.png
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

# 关键点：x = 参数数量 / 样本数量，y = 测试误差
# 经典 U 型 → 插值阈值（参数=样本数，峰值）→ 过参数化区域再次下降
key_points = np.array([
    [0.15, 0.85],   # 模型太小，高偏差
    [0.35, 0.42],   # 经典最优点附近
    [0.65, 0.30],   # U 型谷底
    [0.95, 0.38],   # 向插值阈值爬升
    [1.00, 0.48],   # 插值阈值（峰）
    [1.35, 0.40],   # 过参数化开始下降
    [2.0, 0.30],
    [3.5, 0.22],
])

x_dense = np.linspace(0.15, 3.5, 400)
y_dense = PchipInterpolator(key_points[:, 0], key_points[:, 1])(x_dense)

fig, ax = plt.subplots(figsize=(11, 6))

# 区域背景
ax.axvspan(0.15, 1.0, color='#f59e0b', alpha=0.06)
ax.axvspan(1.0, 3.5, color='#3b82f6', alpha=0.06)
ax.text(0.045, 0.94, '经典 U 型区域', transform=ax.transAxes,
        fontsize=10.5, color='#b45309')
ax.text(0.62, 0.94, '过参数化区域（误差再次下降）',
        transform=ax.transAxes, fontsize=10.5, color='#1d4ed8')

# 曲线
ax.plot(x_dense, y_dense, color='#111827', linewidth=3.0)

# 插值阈值标记
ax.axvline(1.0, color='#dc2626', linestyle='--', linewidth=1.8)
ax.annotate('插值阈值\n（参数数 = 样本数）',
            xy=(1.0, 0.48), xytext=(1.0, 0.88),
            fontsize=10.5, color='#dc2626', fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.4))

# 经典 U 型最低点
ax.plot(0.65, 0.30, 'o', color='#b45309', markersize=8, zorder=5)
ax.annotate('经典最优点', xy=(0.65, 0.30), xytext=(0.42, 0.18),
            fontsize=10, color='#b45309',
            arrowprops=dict(arrowstyle='->', color='#b45309', lw=1.3))

ax.set_xlabel('参数数量（相对样本数）', fontsize=12)
ax.set_ylabel('测试误差', fontsize=12)
ax.set_title('双下降现象（Double Descent）', fontsize=14, pad=12)
ax.set_xlim(0.15, 3.5)
ax.set_ylim(0.15, 1.0)
ax.grid(alpha=0.25)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.3.8-2_double_descent.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
