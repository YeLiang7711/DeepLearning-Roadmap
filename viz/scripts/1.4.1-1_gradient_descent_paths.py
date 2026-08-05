"""
图 1.4.1-1：梯度下降路径 — 三种学习率对比
输出：viz/images/1.4.1-1_gradient_descent_paths.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})


def rosenbrock_2d(x, y):
    """简单碗形（二次曲面），最低点在 (1,1)"""
    return (x - 1) ** 2 + 2 * (y - 1) ** 2


def grad(x, y):
    return np.array([2 * (x - 1), 4 * (y - 1)])


def run_gd(x0, y0, lr, steps):
    path = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        g = grad(x, y)
        x -= lr * g[0]
        y -= lr * g[1]
        path.append((x, y))
    return np.array(path)


fig, ax = plt.subplots(figsize=(10, 7))

# 等高线背景
x = np.linspace(-0.5, 2.0, 200)
y = np.linspace(-0.5, 2.0, 200)
X, Y = np.meshgrid(x, y)
Z = rosenbrock_2d(X, Y)
cf = ax.contourf(X, Y, Z, levels=16, cmap='YlOrBr', alpha=0.85)
ax.contour(X, Y, Z, levels=10, colors='#8a5a2b', linewidths=0.5, alpha=0.4)

start = (0.0, 0.0)

# η 过小：龟速
path_small = run_gd(*start, lr=0.03, steps=60)
ax.plot(path_small[:, 0], path_small[:, 1], 'o-', color='#64748b',
        markersize=3, linewidth=1.6, alpha=0.85, label='η 过小（0.03）：龟速前进')

# η 合适：平滑收敛
path_ok = run_gd(*start, lr=0.18, steps=25)
ax.plot(path_ok[:, 0], path_ok[:, 1], 'o-', color='#2563eb',
        markersize=4, linewidth=2.2, label='η 合适（0.18）：平滑收敛')

# η 过大：震荡
path_big = run_gd(*start, lr=0.75, steps=40)
ax.plot(path_big[:, 0], path_big[:, 1], 'o-', color='#dc2626',
        markersize=3.5, linewidth=1.8, alpha=0.9, label='η 过大（0.75）：来回震荡')

# 最低点
ax.plot(1, 1, '*', color='#111827', markersize=16, zorder=5)
ax.annotate('最低点 (1,1)', xy=(1, 1), xytext=(1.32, 1.22),
            fontsize=11, color='#111827', fontweight='bold')

ax.set_xlabel('$w_1$', fontsize=12)
ax.set_ylabel('$w_2$', fontsize=12)
ax.set_title('梯度下降路径 — 学习率的影响', fontsize=14, pad=12)
ax.set_xlim(-0.5, 2.0)
ax.set_ylim(-0.5, 2.0)
ax.grid(alpha=0.15)
ax.legend(loc='upper right', fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.4.1-1_gradient_descent_paths.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
