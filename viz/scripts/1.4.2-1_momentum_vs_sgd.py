"""
图 1.4.2-1：SGD vs Momentum 在峡谷地形中的路径
输出：viz/images/1.4.2-1_momentum_vs_sgd.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})


def valley(x, y):
    """峡谷地形：y 方向很陡（系数 10），x 方向平缓"""
    return x ** 2 + 10 * y ** 2


def grad(x, y):
    return np.array([2 * x, 20 * y])


def run_sgd(x0, y0, lr, steps, momentum=0.0):
    path = [(x0, y0)]
    x, y = x0, y0
    vx, vy = 0.0, 0.0
    for _ in range(steps):
        gx, gy = grad(x, y)
        vx = momentum * vx + (1 - momentum) * gx
        vy = momentum * vy + (1 - momentum) * gy
        x -= lr * vx
        y -= lr * vy
        path.append((x, y))
    return np.array(path)


fig, ax = plt.subplots(figsize=(10, 7))

x = np.linspace(-1.6, 1.6, 200)
y = np.linspace(-1.6, 1.6, 200)
X, Y = np.meshgrid(x, y)
Z = valley(X, Y)
ax.contourf(X, Y, Z, levels=18, cmap='Blues', alpha=0.75)
ax.contour(X, Y, Z, levels=10, colors='#1e3a8a', linewidths=0.5, alpha=0.35)

start = (-1.4, 0.9)

# SGD：震荡
path_sgd = run_sgd(*start, lr=0.08, steps=60, momentum=0.0)
ax.plot(path_sgd[:, 0], path_sgd[:, 1], 'o-', color='#94a3b8',
        markersize=2.5, linewidth=1.2, alpha=0.8, label='SGD：垂直方向来回震荡')

# Momentum：平滑
path_mom = run_sgd(*start, lr=0.12, steps=45, momentum=0.9)
ax.plot(path_mom[:, 0], path_mom[:, 1], 'o-', color='#2563eb',
        markersize=3.5, linewidth=2.2, label='Momentum (β=0.9)：沿谷底平滑前进')

ax.plot(0, 0, '*', color='#111827', markersize=16, zorder=5)
ax.annotate('谷底 (0,0)', xy=(0, 0), xytext=(0.25, -0.45),
            fontsize=11, color='#111827', fontweight='bold')

ax.set_xlabel('$w_1$（平缓方向）', fontsize=12)
ax.set_ylabel('$w_2$（陡峭方向）', fontsize=12)
ax.set_title('峡谷地形中的优化路径 — SGD vs Momentum', fontsize=14, pad=12)
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.grid(alpha=0.12)
ax.legend(loc='upper right', fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.4.2-1_momentum_vs_sgd.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
