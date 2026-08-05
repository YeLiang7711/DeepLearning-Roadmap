"""
图 1.3.3-1：一元高斯分布 68-95-99.7 规则
输出：viz/images/1.3.3-1_gaussian_68_95_99.png
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 指定中文字体
plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 13,
    'axes.titlesize': 15,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

fig, ax = plt.subplots(figsize=(12, 5))

x = np.linspace(-4.5, 4.5, 600)
y = norm.pdf(x, 0, 1)

colors = {'1σ': '#3b82f6', '2σ': '#6366f1', '3σ': '#8b5cf6'}

for sigma_mul in [3, 2, 1]:
    lo, hi = -sigma_mul, sigma_mul
    mask = (x >= lo) & (x <= hi)
    key = f'{sigma_mul}σ'
    ax.fill_between(x, y, alpha=0.22, color=colors[key], where=mask)
    ax.axvline(lo, color=colors[key], linestyle='--', linewidth=1.0, alpha=0.5)
    ax.axvline(hi, color=colors[key], linestyle='--', linewidth=1.0, alpha=0.5)

ax.plot(x, y, 'k-', linewidth=2.2)

annotations = [
    ('68.3%', 1.0, 0.16),
    ('95.4%', 2.0, 0.27),
    ('99.7%', 3.0, 0.38),
]
for pct_text, s, y_pos in annotations:
    ax.annotate(pct_text, xy=(s, norm.pdf(s)), xytext=(s + 0.6, y_pos),
                fontsize=15, fontweight='bold', ha='center', color=colors[f'{int(s)}σ'],
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#6b7280'))

for mult in [1, 2, 3]:
    ax.annotate(f'-{mult}σ', xy=(-mult, -0.015), ha='center', fontsize=11, color='#4b5563')
    ax.annotate(f'+{mult}σ', xy=(mult, -0.015), ha='center', fontsize=11, color='#4b5563')
ax.annotate('μ', xy=(0, -0.015), ha='center', fontsize=12, fontweight='bold', color='#1e293b')

from matplotlib.lines import Line2D
legend_elements = [
    plt.Rectangle((0,0),1,1, fc=colors['1σ'], alpha=0.22, label='μ ± 1σ  (68.3%)'),
    plt.Rectangle((0,0),1,1, fc=colors['2σ'], alpha=0.22, label='μ ± 2σ  (95.4%)'),
    plt.Rectangle((0,0),1,1, fc=colors['3σ'], alpha=0.22, label='μ ± 3σ  (99.7%)'),
]
ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9, fontsize=12)

ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-0.04, 0.46)
ax.set_xlabel('偏离均值的标准差倍数 (σ)')
ax.set_ylabel('概率密度')
ax.set_title('一元高斯分布 — 68–95–99.7 规则', pad=14)
ax.set_yticks([])
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

plt.tight_layout(pad=0.5)
out = 'D:/LearnSpace/viz/images/1.3.3-1_gaussian_68_95_99.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f'saved: {out}')
