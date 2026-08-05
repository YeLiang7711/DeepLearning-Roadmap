"""
图 1.3.3-2：二元高斯分布 — 三种协方差形状对比
输出：viz/images/1.3.3-2_bivariate_covariance_cases.png
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

mu = [0, 0]
cases = [
    (r'$\Sigma = I$    各向同性（正圆等高线）',
     np.array([[1.0, 0.0], [0.0, 1.0]])),
    (r'$\Sigma = \mathrm{diag}(3, 0.5)$    轴对齐椭圆（独立但方差不同）',
     np.array([[3.0, 0.0], [0.0, 0.5]])),
    (r'$\Sigma_{12} = \Sigma_{21} = 1.5$    倾斜椭圆（正相关 $\rho \approx 0.87$）',
     np.array([[3.0, 1.5], [1.5, 1.0]])),
]

for ax, (title, cov) in zip(axes, cases):
    # 采样
    samples = np.random.multivariate_normal(mu, cov, size=600)
    ax.scatter(samples[:, 0], samples[:, 1], s=6, alpha=0.35, color='#3b82f6')

    # 等高线
    x1, x2 = np.mgrid[-5:5:0.1, -4:4:0.1]
    pos = np.dstack((x1, x2))
    rv = multivariate_normal(mu, cov)
    ax.contour(x1, x2, rv.pdf(pos), levels=6, colors='#1e293b', linewidths=1.2, alpha=0.8)

    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4, 4)
    ax.set_xlabel('$x_1$（温度）')
    ax.set_ylabel('$x_2$（梯度）')
    ax.set_title(title, pad=12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)

fig.suptitle('二元高斯分布 — 协方差矩阵对分布形状的影响', fontsize=16, y=1.02)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.3.3-2_bivariate_covariance_cases.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
