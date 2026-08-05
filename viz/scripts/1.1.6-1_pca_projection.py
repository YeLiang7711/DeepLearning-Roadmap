"""
图 1.1.6-1：PCA 投影示意 — 2D 数据投影到方差最大的方向（PC1）
输出：viz/images/1.1.6-1_pca_projection.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(1)

# 生成椭圆分布数据（沿 30° 方向拉长）
n = 300
theta = np.radians(30)
rot = np.array([[np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]])
base = rng.normal(0, 1, size=(n, 2)) @ np.array([[3.0, 0], [0, 1.0]])
pts = base @ rot.T

# PC1 方向（数据方差最大的方向 ≈ 30°）
pc1 = rot[:, 0]

fig, ax = plt.subplots(figsize=(10, 7))

# 原始散点
ax.scatter(pts[:, 0], pts[:, 1], s=14, alpha=0.55, color='#3b82f6', zorder=2)

# 投影线（从每个点到 PC1 轴的垂线）
proj = (pts @ pc1)[:, None] * pc1
for p, q in zip(pts, proj):
    ax.plot([p[0], q[0]], [p[1], q[1]], color='#94a3b8', linewidth=0.4, alpha=0.35, zorder=1)

# PC1 方向箭头（过原点）
ax.arrow(0, 0, pc1[0] * 4.2, pc1[1] * 4.2, color='#dc2626', linewidth=3.2,
         head_width=0.18, head_length=0.25, zorder=4)
ax.annotate('PC1（方差最大方向）', xy=(pc1[0] * 3.0, pc1[1] * 3.0),
            xytext=(pc1[0] * 3.0 - 0.5, pc1[1] * 3.0 + 0.9),
            fontsize=12, color='#dc2626', fontweight='bold')

# PC2 方向（正交，示意）
pc2 = rot[:, 1]
ax.arrow(0, 0, pc2[0] * 1.6, pc2[1] * 1.6, color='#94a3b8', linewidth=2.0,
         head_width=0.12, head_length=0.16, zorder=4, linestyle='--')
ax.annotate('PC2（正交，方差次大）', xy=(pc2[0] * 1.3, pc2[1] * 1.3),
            xytext=(-4.0, pc2[1] * 1.3 + 0.6), fontsize=11, color='#64748b')

ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-4, 4)
ax.set_xlabel('特征 1', fontsize=12)
ax.set_ylabel('特征 2', fontsize=12)
ax.set_title('PCA 投影 — 找让数据最"散"的方向投影', fontsize=14, pad=12)
ax.grid(alpha=0.2)
ax.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#3b82f6',
               markersize=8, label='原始 2D 数据'),
    plt.Line2D([0], [0], color='#dc2626', linewidth=3, label='PC1 投影方向'),
    plt.Line2D([0], [0], color='#94a3b8', linewidth=2, linestyle='--', label='PC2（正交）'),
], loc='upper right', fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.1.6-1_pca_projection.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
