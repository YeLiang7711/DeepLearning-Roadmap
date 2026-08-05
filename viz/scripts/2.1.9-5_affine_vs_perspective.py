"""
图 2.1.9-5：仿射变换 vs 透视变换 — 平行线保持 vs 汇聚
输出：viz/images/2.1.9-5_affine_vs_perspective.png
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

# 合成网格图（平行线最能看清"是否保持平行"）
img = np.full((200, 200), 220, np.uint8)
for i in range(0, 200, 25):
    img[i:i+1, :] = 120          # 横线
    img[:, i:i+1] = 120          # 竖线
cv2.rectangle(img, (60, 60), (140, 140), 60, -1)   # 中心方块

h, w = img.shape

# 仿射：旋转 + 缩放（平行线保持）
M_aff = cv2.getRotationMatrix2D((w/2, h/2), 20, 0.9)
affine = cv2.warpAffine(img, M_aff, (w, h))

# 透视：模拟斜拍（平行线汇聚）
src = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
dst = np.float32([[40, 20], [160, 0], [20, 180], [200, 200]])
M_per = cv2.getPerspectiveTransform(src, dst)
perspective = cv2.warpPerspective(img, M_per, (w, h))

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

for ax, (title, data) in zip(axes, [
    ('原始网格\n（横竖线都平行）', img),
    ('仿射变换\n（旋转+缩放：平行线仍平行）', affine),
    ('透视变换\n（模拟斜拍：平行线向消失点汇聚）', perspective),
]):
    ax.imshow(data, cmap='gray', vmin=0, vmax=255)
    ax.set_title(title, fontsize=12)
    ax.set_xticks([]); ax.set_yticks([])

# 在透视图上标出"汇聚"示意：延长两条竖线看消失点
ax = axes[2]
ax.annotate('消失点方向', xy=(205, 5), xytext=(150, 30),
            fontsize=10, color='#dc2626',
            arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.5))

fig.suptitle('仿射 vs 透视 — 平行线是否保持', fontsize=15, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.9-5_affine_vs_perspective.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
