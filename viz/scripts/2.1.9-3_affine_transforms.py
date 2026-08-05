"""
图 2.1.9-3：仿射变换 — 平移/旋转/缩放/剪切
输出：viz/images/2.1.9-3_affine_transforms.png
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

# 合成测试图：网格 + 方块（能看清变形）
img = np.full((120, 120), 200, np.uint8)
for i in range(0, 120, 20):
    img[i:i+1, :] = 120
    img[:, i:i+1] = 120
cv2.rectangle(img, (40, 40), (80, 80), 60, -1)

h, w = img.shape

transforms = []

# 1. 平移 (+15, +10)
M = np.float32([[1, 0, 15], [0, 1, 10]])
transforms.append(('平移 (+15, +10)', cv2.warpAffine(img, M, (w, h))))

# 2. 旋转 30°
M = cv2.getRotationMatrix2D((w/2, h/2), 30, 1.0)
transforms.append(('旋转 30°', cv2.warpAffine(img, M, (w, h))))

# 3. 缩放 1.3 倍
M = cv2.getRotationMatrix2D((w/2, h/2), 0, 1.3)
transforms.append(('缩放 1.3 倍', cv2.warpAffine(img, M, (w, h))))

# 4. 剪切（x 方向斜拉）
M = np.float32([[1, 0.4, 0], [0, 1, 0]])
transforms.append(('剪切 (x 方向 0.4)', cv2.warpAffine(img, M, (w, h))))

fig, axes = plt.subplots(1, 5, figsize=(16, 3.8))

axes[0].imshow(img, cmap='gray', vmin=0, vmax=255)
axes[0].set_title('原始图像\n（网格参考）', fontsize=12)
axes[0].set_xticks([]); axes[0].set_yticks([])

for ax, (title, warped) in zip(axes[1:], transforms):
    ax.imshow(warped, cmap='gray', vmin=0, vmax=255)
    ax.set_title(title, fontsize=12)
    ax.set_xticks([]); ax.set_yticks([])

fig.suptitle('仿射变换 — 都由一个 2×3 矩阵描述（warpAffine 一步完成）',
             fontsize=14, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.9-3_affine_transforms.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
