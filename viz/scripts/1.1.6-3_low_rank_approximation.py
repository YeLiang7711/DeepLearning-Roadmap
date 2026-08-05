"""
图 1.1.6-3：低秩近似示意 — 原始矩阵 vs k 秩近似
输出：viz/images/1.1.6-3_low_rank_approximation.png
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))

# 左：原始矩阵（满秩，全部元素）
ax = axes[0]
ax.imshow(np.ones((8, 10)), cmap='Greys', vmin=0, vmax=1, aspect='auto')
ax.set_title('原始矩阵 X（10000 维）\n全部信息', fontsize=13)
ax.set_xticks([])
ax.set_yticks([])
ax.text(0.5, -0.12, 'd = 10000', transform=ax.transAxes, ha='center', fontsize=11)
for spine in ax.spines.values():
    spine.set_edgecolor('#64748b')
    spine.set_linewidth(1.5)

# 箭头
axes[0].annotate('', xy=(0.55, 0.5), xycoords='axes fraction',
                 xytext=(0.45, 0.5), textcoords='axes fraction',
                 arrowprops=dict(arrowstyle='->', color='#111827', lw=2.5))

# 右：低秩近似（保留 k 列，丢弃部分）
ax = axes[1]
grid = np.zeros((8, 10))
grid[:, :6] = 0.85   # 保留的 k 个成分（主要结构）
grid[:, 6:] = 0.25   # 被丢弃的低方差成分
ax.imshow(grid, cmap='Greys', vmin=0, vmax=1, aspect='auto')
ax.set_title(r'低秩近似 $X_k$（k 维）' '\n保留主要结构，丢掉噪声', fontsize=13)
ax.set_xticks([])
ax.set_yticks([])
# 标注区域
ax.text(0.3, -0.12, 'k 个成分（保留）', transform=ax.transAxes, ha='center', fontsize=11)
ax.text(0.8, -0.12, '丢弃的\n低方差成分', transform=ax.transAxes, ha='center',
        fontsize=10, color='#64748b')
# 分界线
ax.axvline(5.5, color='#dc2626', linewidth=2, linestyle='--')
for spine in ax.spines.values():
    spine.set_edgecolor('#64748b')
    spine.set_linewidth(1.5)

fig.suptitle('低秩近似 — 用少量成分表示原始矩阵', fontsize=15, y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.93])
out = 'D:/LearnSpace/viz/images/1.1.6-3_low_rank_approximation.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
