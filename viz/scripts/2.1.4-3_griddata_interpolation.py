"""
图 2.1.4-3：网格插值 — 离散传感器点 → 规则温度场
输出：viz/images/2.1.4-3_griddata_interpolation.png
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(23)

# 模拟真实温度场（用于生成"传感器读数"和验证）
gx, gy = np.mgrid[0:10:200j, 0:10:200j]
true_field = 25.0 + 5.0 * np.exp(-((gx - 3.5) ** 2 + (gy - 6) ** 2) / 6) \
                   + 3.0 * np.exp(-((gx - 7) ** 2 + (gy - 2.5) ** 2) / 4)

# 200 个离散传感器点（随机分布，工业场景）
pts = rng.uniform(0.5, 9.5, size=(200, 2))
values = true_field[np.clip((pts[:, 1] * 20).astype(int), 0, 199),
                    np.clip((pts[:, 0] * 20).astype(int), 0, 199)]
values += rng.normal(0, 0.15, size=200)      # 传感器噪声

# griddata 插值到规则网格
grid_x, grid_y = np.mgrid[0:10:150j, 0:10:150j]
interp_field = griddata(pts, values, (grid_x, grid_y), method='cubic')

# GridSpec：2 张图 + colorbar 专属列
fig = plt.figure(figsize=(13, 5.2))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 0.045],
                      wspace=0.15, left=0.04, right=0.97, top=0.85, bottom=0.10)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
cax = fig.add_subplot(gs[0, 2])

vmin, vmax = true_field.min(), true_field.max()

# 左：离散传感器点
sc = ax1.scatter(pts[:, 0], pts[:, 1], c=values, cmap='hot',
                 vmin=vmin, vmax=vmax, s=28, edgecolor='#111827', linewidth=0.4)
ax1.set_title('离散传感器点 (n=200)\n每个点有一个温度读数', fontsize=12)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(alpha=0.2)

# 右：插值后的连续场
im = ax2.imshow(interp_field.T, origin='lower', extent=[0, 10, 0, 10],
                cmap='hot', vmin=vmin, vmax=vmax)
ax2.contour(grid_x, grid_y, interp_field, levels=8, colors='#111827',
            linewidths=0.5, alpha=0.35)
ax2.set_title('griddata 插值后的规则温度场\n（cubic，150×150 网格）', fontsize=12)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect('equal')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

cbar = fig.colorbar(im, cax=cax)
cbar.set_label('温度 (°C)', fontsize=11)

fig.suptitle('网格插值 — 从离散传感器点到连续温度场', fontsize=15, y=0.98)
out = 'D:/LearnSpace/viz/images/2.1.4-3_griddata_interpolation.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
