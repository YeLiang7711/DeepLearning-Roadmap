"""
图 1.5.1-1：二元熵函数 H(p)
输出：viz/images/1.5.1-1_binary_entropy.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

p = np.linspace(0.001, 0.999, 400)
# 二元熵（以 2 为底，单位比特）
H = -p * np.log2(p) - (1 - p) * np.log2(1 - p)

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(p, H, color='#2563eb', linewidth=2.8)

# 最大点标注
ax.plot(0.5, 1.0, 'o', color='#dc2626', markersize=8, zorder=5)
ax.annotate('p = 0.5：熵最大 = 1 比特\n（完全不确定）',
            xy=(0.5, 1.0), xytext=(0.52, 0.85),
            fontsize=10.5, color='#dc2626',
            arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.4))

# 低不确定性端点标注
ax.annotate('p → 0：几乎确定是反面\n熵 → 0', xy=(0.08, 0.22), xytext=(0.1, 0.45),
            fontsize=10, color='#64748b',
            arrowprops=dict(arrowstyle='->', color='#64748b', lw=1.2))
ax.annotate('p → 1：几乎确定是正面\n熵 → 0', xy=(0.92, 0.22), xytext=(0.68, 0.45),
            fontsize=10, color='#64748b',
            arrowprops=dict(arrowstyle='->', color='#64748b', lw=1.2))

ax.set_xlabel('正面概率 p', fontsize=12)
ax.set_ylabel('熵 H(p)（比特）', fontsize=12)
ax.set_title('二元熵函数 — 不确定性随概率变化', fontsize=14, pad=12)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)
ax.grid(alpha=0.25)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.5.1-1_binary_entropy.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
