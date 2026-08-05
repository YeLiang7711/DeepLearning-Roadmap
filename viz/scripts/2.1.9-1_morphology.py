"""
图 2.1.9-1：形态学运算 — 腐蚀/膨胀/开/闭
输出：viz/images/2.1.9-1_morphology.png
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

rng = np.random.default_rng(19)

# 模拟缺陷掩膜：一个大的缺陷区域 + 小噪点 + 一个洞
mask = np.zeros((80, 80), np.uint8)
cv2.rectangle(mask, (25, 25), (55, 50), 255, -1)          # 主缺陷块
cv2.circle(mask, (60, 60), 2, 255, -1)                    # 噪点
cv2.circle(mask, (60, 10), 2, 255, -1)                    # 噪点
cv2.circle(mask, (38, 37), 5, 0, -1)                      # 洞

kernel = np.ones((3, 3), np.uint8)
eroded = cv2.erode(mask, kernel, iterations=1)
dilated = cv2.dilate(mask, kernel, iterations=1)
opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

fig, axes = plt.subplots(1, 5, figsize=(16, 4))

titles = ['原始掩膜\n（主缺陷+噪点+洞）', '腐蚀\n（区域缩小）', '膨胀\n（区域扩大）',
          '开运算\n（去噪点）', '闭运算\n（填洞）']
for ax, (title, data) in zip(axes, zip(titles, [mask, eroded, dilated, opened, closed])):
    ax.imshow(data, cmap='gray', vmin=0, vmax=255)
    ax.set_title(title, fontsize=12)
    ax.set_xticks([]); ax.set_yticks([])

fig.suptitle('形态学运算 — 二值掩膜的形状精修', fontsize=15, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.9-1_morphology.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
