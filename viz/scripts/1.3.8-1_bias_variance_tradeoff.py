"""
图 1.3.8-1：偏差—方差权衡曲线
输出：viz/images/1.3.8-1_bias_variance_tradeoff.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

c = np.linspace(0, 10, 300)

# 偏差² 随复杂度单调下降，方差单调上升，总误差 = 二者之和（+不可约误差）
bias2 = 3.0 * np.exp(-0.42 * c) + 0.15
variance = 0.055 * c ** 2.2
total = bias2 + variance

# 最优点（总误差最小）
best_idx = np.argmin(total)
c_best, total_best = c[best_idx], total[best_idx]

fig, ax = plt.subplots(figsize=(11, 6))

# 区域背景：欠拟合（左）/ 过拟合（右）
ax.axvspan(0, c_best, color='#ef4444', alpha=0.05)
ax.axvspan(c_best, 10, color='#3b82f6', alpha=0.05)
ax.text(0.06, 0.94, '← 欠拟合区域（高偏差）',
        transform=ax.transAxes, fontsize=10.5, color='#b91c1c')
ax.text(0.55, 0.94, '过拟合区域（高方差）→',
        transform=ax.transAxes, fontsize=10.5, color='#1d4ed8')

# 三条曲线
ax.plot(c, bias2, color='#dc2626', linewidth=2.4, label='偏差²（随复杂度单调下降）')
ax.plot(c, variance, color='#2563eb', linewidth=2.4, label='方差（随复杂度单调上升）')
ax.plot(c, total, color='#111827', linewidth=3.0, label='总误差 = 偏差² + 方差')

# 最优点标注
ax.axvline(c_best, color='#111827', linestyle=':', linewidth=1.4, alpha=0.7)
ax.plot(c_best, total_best, 'o', color='#111827', markersize=9, zorder=5)
ax.annotate(f'最优点（总误差最小）\n复杂度 ≈ {c_best:.1f}',
            xy=(c_best, total_best),
            xytext=(c_best + 0.8, total_best + 0.6),
            fontsize=10.5, color='#111827', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#111827', lw=1.5))

ax.set_xlabel('模型复杂度', fontsize=12)
ax.set_ylabel('误差', fontsize=12)
ax.set_title('偏差—方差权衡', fontsize=14, pad=12)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.grid(alpha=0.25)
ax.legend(loc='upper center', fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.3.8-1_bias_variance_tradeoff.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
