"""
图 2.1.9-4：图像金字塔 — 高斯金字塔与拉普拉斯细节
输出：viz/images/2.1.9-4_image_pyramid.png
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

rng = np.random.default_rng(41)

# 模拟温度场：大尺度结构（整体渐变）+ 小尺度细节（热点 + 噪声）
y, x = np.mgrid[0:128, 0:128]
field = 25.0 + 3.0 * x / 128 + 8.0 * np.exp(-((x - 70) ** 2 + (y - 40) ** 2) / 300)
field += rng.normal(0, 0.5, field.shape)
field = np.clip(field, 20, 36)

img = (field - field.min()) / (field.max() - field.min()) * 255
img = img.astype(np.uint8)

# 高斯金字塔：连续降采样 3 层
levels = [img]
for _ in range(3):
    levels.append(cv2.pyrDown(levels[-1]))

# 拉普拉斯层 = 高斯层 - 上采样(下一高斯层)
laplacian = cv2.subtract(levels[0], cv2.pyrUp(levels[1]))

fig, axes = plt.subplots(1, 4, figsize=(14, 5))

sizes = [128, 64, 32, 16]
labels = ['原始温度场\n(128×128)', '高斯层 1\n(64×64)\n大尺度结构', '高斯层 2\n(32×32)', '高斯层 3\n(16×16)']
for ax, (level, size, label) in zip(axes, zip(levels, sizes, labels)):
    ax.imshow(level, cmap='hot', vmin=0, vmax=255)
    ax.set_title(label, fontsize=11)
    ax.set_xticks([]); ax.set_yticks([])

fig.suptitle('高斯金字塔 — 逐层降采样，分辨率减半，大尺度结构保留', fontsize=14, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.9-4_image_pyramid.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
