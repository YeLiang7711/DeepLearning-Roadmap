"""
图 1.4.5-1：L1 vs L2 正则的约束几何
输出：viz/images/1.4.5-1_l1_l2_geometry.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

theta = np.linspace(0, 2 * np.pi, 400)

fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))

# 无约束最优解位置（对角线方向，w1 和 w2 都不为 0）
w_star = np.array([2.2, 0.9])

for ax, (norm_name, boundary) in zip(axes, [
    ('L2 约束（圆形）', np.stack([np.cos(theta), np.sin(theta)])),
    # L1 菱形：|w1| + |w2| = 1 的参数化（用 L1 范数归一化单位圆）
    ('L1 约束（菱形）', np.stack([
        np.cos(theta) / (np.abs(np.cos(theta)) + np.abs(np.sin(theta))),
        np.sin(theta) / (np.abs(np.cos(theta)) + np.abs(np.sin(theta))),
    ])),
]):
    # 约束区域
    ax.fill(boundary[0], boundary[1], color='#3b82f6', alpha=0.15)
    ax.plot(boundary[0], boundary[1], color='#2563eb', linewidth=2.2)

    # 无约束最优解
    ax.scatter(*w_star, color='#dc2626', s=80, zorder=5)
    ax.annotate('无约束最优解 w*', xy=w_star, xytext=(1.1, 2.35),
                fontsize=11, color='#dc2626', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#dc2626'))

    # 约束后最优解（L2：圆边上；L1：轴上的角）
    if 'L2' in norm_name:
        # 圆边上离 w* 最近的点 ≈ 方向归一化
        sol = w_star / np.linalg.norm(w_star)
        sol_label = '约束后解：\n在圆边上，两坐标都不为 0'
        xytext = (0.2, -1.9)
    else:
        # 菱形角：max(|w1|,|w2|) = C 的顶点在轴上
        sol = np.array([1.0, 0.0])
        sol_label = '约束后解：\n卡在菱形角上 → $w_2$ = 0'
        xytext = (0.35, -1.6)

    ax.scatter(*sol, color='#10b981', s=80, zorder=5, marker='s')
    ax.annotate(sol_label, xy=sol, xytext=xytext, fontsize=10,
                color='#047857', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#047857'))

    # 从 w* 到约束区域的最短路径示意
    ax.plot([w_star[0], sol[0]], [w_star[1], sol[1]], '--', color='#64748b',
            linewidth=1.2, alpha=0.7)

    ax.axhline(0, color='#94a3b8', linewidth=0.8)
    ax.axvline(0, color='#94a3b8', linewidth=0.8)
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_xlabel('$w_1$')
    ax.set_ylabel('$w_2$')
    ax.set_title(norm_name, fontsize=13)
    ax.set_aspect('equal')
    ax.grid(alpha=0.12)

fig.suptitle('正则化 = 把最优解限制在约束区域内（解 = 区域内离 w* 最近的点）',
             fontsize=13.5, y=1.02)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.4.5-1_l1_l2_geometry.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
