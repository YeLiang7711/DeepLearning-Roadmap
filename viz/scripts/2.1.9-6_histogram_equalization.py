"""
图 2.1.9-6：直方图均衡化 — 对比度增强效果
输出：viz/images/2.1.9-6_histogram_equalization.png
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

rng = np.random.default_rng(29)

# 模拟低对比度温度图：整体 24~27°C，一个小热点
y, x = np.mgrid[0:100, 0:100]
base = 25.0 + 1.0 * np.exp(-((x - 50) ** 2 + (y - 50) ** 2) / 900)
base += rng.normal(0, 0.2, base.shape)
low_contrast = np.clip(base, 24, 27)
img = ((low_contrast - 24) / 3 * 255).astype(np.uint8)

equalized = cv2.equalizeHist(img)

# GridSpec：2 行 3 列（图像 | 直方图 | colorbar 专属列）
fig = plt.figure(figsize=(11, 8))
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1, 0.05],
                      wspace=0.25, hspace=0.3,
                      left=0.06, right=0.97, top=0.92, bottom=0.08)
ax_img = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0])]
ax_hist = [fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])]
cax = fig.add_subplot(gs[:, 2])

for ax, (title, data) in zip(ax_img, [
    ('原始温度图（低对比度）\n整体 24~27°C，热点几乎看不见', img),
    ('均衡化后\n对比度拉开，热点清晰可见', equalized),
]):
    im = ax.imshow(data, cmap='hot', vmin=0, vmax=255)
    ax.set_title(title, fontsize=11)
    ax.set_xticks([]); ax.set_yticks([])

for ax, (htitle, data) in zip(ax_hist, [
    ('原始直方图：像素挤在窄范围', img),
    ('均衡化直方图：分布被拉开', equalized),
]):
    hist = cv2.calcHist([data], [0], None, [256], [0, 256]).ravel()
    ax.bar(np.arange(256), hist, width=1, color='#f97316', alpha=0.8)
    ax.set_title(htitle, fontsize=11)
    ax.set_xlim(0, 255)
    ax.set_xlabel('灰度值'); ax.set_ylabel('像素数')
    ax.grid(alpha=0.2)

cbar = fig.colorbar(im, cax=cax)
cbar.set_label('灰度', fontsize=10)

fig.suptitle('直方图均衡化 — 把挤在一起的像素分布拉开', fontsize=14)
out = 'D:/LearnSpace/viz/images/2.1.9-6_histogram_equalization.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
