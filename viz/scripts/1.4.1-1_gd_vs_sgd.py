"""
图 1.4.1-1：全量 GD vs SGD 的优化路径对比
输出：viz/images/1.4.1-1_gd_vs_sgd.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})


def loss_fn(x, y):
    """碗形损失函数（中心在原点）"""
    return 0.5 * x ** 2 + 0.7 * y ** 2


def grad(x, y):
    return np.array([x, 1.4 * y])


def run_gd(x0, y0, lr, steps, noise=0.0):
    """GD：无噪声；SGD：每步加噪声（模拟小批量梯度的随机性）"""
    rng = np.random.default_rng(42)
    path = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        gx, gy = grad(x, y)
        if noise > 0:
            # 相对噪声：与梯度同量级，接近谷底时噪声自动变小
            gx += rng.normal(0, noise * max(0.1, abs(gx)))
            gy += rng.normal(0, noise * max(0.1, abs(gy)))
        x -= lr * gx
        y -= lr * gy
        path.append((x, y))
    return np.array(path)


fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))

x = np.linspace(-4.5, 4.5, 200)
y = np.linspace(-4.5, 4.5, 200)
X, Y = np.meshgrid(x, y)
Z = loss_fn(X, Y)

for ax, (title, path, color) in zip(axes, [
    ('全量 GD：平滑直达谷底', run_gd(4.0, 4.0, 0.15, 30, noise=0.0), '#2563eb'),
    ('SGD：锯齿形但每步便宜', run_gd(4.0, 4.0, 0.15, 40, noise=0.55), '#dc2626'),
]):
    ax.contourf(X, Y, Z, levels=16, cmap='GnBu', alpha=0.9)
    ax.plot(path[:, 0], path[:, 1], 'o-', color=color, markersize=3.5,
            linewidth=1.8, alpha=0.9)
    ax.plot(0, 0, '*', color='#111827', markersize=14, zorder=5)
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_xlabel('$w_1$')
    ax.set_ylabel('$w_2$')
    ax.set_title(title, fontsize=12.5)
    ax.grid(alpha=0.12)

fig.suptitle('全量 GD vs SGD 优化路径对比', fontsize=15, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.4.1-1_gd_vs_sgd.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
