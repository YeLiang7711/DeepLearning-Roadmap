"""
图 1.4.4-1：凸 vs 非凸损失曲面
输出：viz/images/1.4.4-1_convex_vs_nonconvex.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

# 左：凸（碗形）
x = np.linspace(-3, 3, 200)
ax = axes[0]
ax.plot(x, x ** 2, color='#2563eb', linewidth=3.0)
ax.fill_between(x, x ** 2, color='#2563eb', alpha=0.12)
ax.scatter([0], [0], color='#dc2626', s=60, zorder=5)
ax.annotate('全局最小值\n（唯一谷底）', xy=(0, 0), xytext=(0.6, 4.2),
            fontsize=11, color='#dc2626', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#dc2626'))
ax.annotate('任意起点 → 都收敛到同一个谷底',
            xy=(-1.2, 4.5), fontsize=10, color='#1e40af')
ax.set_title('凸函数（碗形）', fontsize=13)
ax.set_xlabel('参数 w')
ax.set_ylabel('损失 L(w)')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)
ax.grid(alpha=0.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 右：非凸（山脉）
x2 = np.linspace(-3, 3, 400)
nonconvex = (x2 - 1.6) ** 2 * (x2 + 1.6) ** 2 * 0.6 + 0.15 * np.sin(4 * x2) + 0.8
ax = axes[1]
ax.plot(x2, nonconvex, color='#b45309', linewidth=3.0)
ax.fill_between(x2, nonconvex, color='#f59e0b', alpha=0.15)
# 局部极小和全局极小
local_min = -1.1
global_min = 1.6
ax.scatter([local_min], [nonconvex[np.argmin(abs(x2 - local_min))]], color='#94a3b8', s=60, zorder=5)
ax.scatter([global_min], [nonconvex[np.argmin(abs(x2 - global_min))]], color='#dc2626', s=60, zorder=5)
ax.annotate('局部极小\n（卡住这里就惨了）', xy=(local_min, 3.0),
            xytext=(-2.9, 4.6), fontsize=10, color='#64748b',
            arrowprops=dict(arrowstyle='->', color='#64748b'))
ax.annotate('全局最小值', xy=(global_min, 1.0),
            xytext=(1.9, 4.6), fontsize=11, color='#dc2626', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#dc2626'))
ax.set_title('非凸函数（山脉形）', fontsize=13)
ax.set_xlabel('参数 w')
ax.set_ylabel('损失 L(w)')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)
ax.grid(alpha=0.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.suptitle('凸 vs 非凸 — 优化难度的根源', fontsize=15, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.4.4-1_convex_vs_nonconvex.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
