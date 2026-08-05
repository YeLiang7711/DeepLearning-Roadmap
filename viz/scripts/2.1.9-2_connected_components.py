"""
图 2.1.9-2：连通域分析 — 掩膜 → 缺陷区域清单
输出：viz/images/2.1.9-2_connected_components.png
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(31)

# 模拟阈值后的缺陷掩膜：三个大小不一的区域
mask = np.zeros((90, 90), np.uint8)
cv2.rectangle(mask, (10, 15), (30, 40), 255, -1)     # 大缺陷
cv2.circle(mask, (55, 55), 12, 255, -1)              # 中缺陷
cv2.circle(mask, (70, 20), 4, 255, -1)               # 小缺陷（可能是噪声）

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)

fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))

# 左：原始掩膜
ax = axes[0]
ax.imshow(mask, cmap='gray', vmin=0, vmax=255)
ax.set_title('阈值后的掩膜\n（白色 = 疑似缺陷）', fontsize=12)
ax.set_xticks([]); ax.set_yticks([])

# 右：连通域标记
ax = axes[1]
colored = np.zeros((*mask.shape, 3), np.uint8)
colors = [(59, 130, 246), (245, 158, 11), (16, 185, 129)]
for i in range(1, num_labels):
    colored[labels == i] = colors[(i - 1) % 3]
ax.imshow(colored)
for i in range(1, num_labels):
    x, y, w, h, area = stats[i]
    cx, cy = centroids[i]
    ax.add_patch(plt.Rectangle((x - 0.5, y - 0.5), w, h, fill=False,
                               edgecolor='#dc2626', linewidth=2))
    ax.plot(cx, cy, 'o', color='#dc2626', markersize=6)
    ax.text(x + w + 2, y + h / 2, f'#{i}\n面积={area}',
            fontsize=9, color='#111827', va='center')
ax.set_xlim(-5, 100); ax.set_ylim(95, -5)
ax.set_title('连通域分析\n（编号 + 包围盒 + 质心 + 面积）', fontsize=12)
ax.set_xticks([]); ax.set_yticks([])

fig.suptitle('连通域 — 把掩膜变成缺陷清单', fontsize=15, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.9-2_connected_components.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}   区域数: {num_labels - 1}')
