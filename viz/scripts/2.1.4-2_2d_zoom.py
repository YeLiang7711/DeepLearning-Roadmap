"""
图 2.1.4-2：二维缩放 — 最近邻 vs 三次插值放大对比
输出：viz/images/2.1.4-2_2d_zoom.png
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(11)

# 模拟温度场：25°C 背景 + 两个高斯热点 + 随机噪声
y, x = np.mgrid[0:60, 0:60]
base = 25.0 + 6.0 * np.exp(-((x - 20) ** 2 + (y - 25) ** 2) / 120) \
            + 4.0 * np.exp(-((x - 45) ** 2 + (y - 15) ** 2) / 80)
temps = base + rng.normal(0, 0.3, base.shape)

# 降采样到 30×30（丢一半像素），再用不同插值放大回 60×60
small = temps[::2, ::2]
zoom_nearest = zoom(small, 2, order=0)     # 最近邻（0 阶）
zoom_cubic = zoom(small, 2, order=3)       # 三次样条（3 阶）

# GridSpec：3 张图 + 1 个专属 colorbar 列（物理上不可能压到图上）
fig = plt.figure(figsize=(15, 4.8))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 0.045],
                      wspace=0.12, left=0.03, right=0.97, top=0.85, bottom=0.10)
axes = [fig.add_subplot(gs[0, i]) for i in range(3)]
cax = fig.add_subplot(gs[0, 3])

vmin, vmax = temps.min(), temps.max()

imgs = [
    ('原始温度图 (60×60)', temps),
    ('降采样后最近邻放大\n（块状伪影，order=0）', zoom_nearest),
    ('降采样后三次插值放大\n（平滑，order=3）', zoom_cubic),
]

for ax, (title, data) in zip(axes, imgs):
    im = ax.imshow(data, cmap='hot', vmin=vmin, vmax=vmax)
    ax.set_title(title, fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])

cbar = fig.colorbar(im, cax=cax)
cbar.set_label('温度 (°C)', fontsize=11)

fig.suptitle('二维缩放 — 插值方式影响"看到的结构"', fontsize=15, y=0.98)
out = 'D:/LearnSpace/viz/images/2.1.4-2_2d_zoom.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
