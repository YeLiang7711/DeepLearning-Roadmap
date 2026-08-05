"""
图 2.1.8-2：核技巧 — 二维线性不可分 → 高维线性可分
输出：viz/images/2.1.8-2_kernel_trick.png
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(3)

# 同心圆数据（二维线性不可分）
theta = rng.uniform(0, 2 * np.pi, 120)
r_in = rng.uniform(0.6, 1.2, 120)
x_in = r_in * np.cos(theta)
y_in = r_in * np.sin(theta)

theta2 = rng.uniform(0, 2 * np.pi, 120)
r_out = rng.uniform(2.0, 3.0, 120)
x_out = r_out * np.cos(theta2)
y_out = r_out * np.sin(theta2)

X = np.vstack([np.column_stack([x_in, y_in]), np.column_stack([x_out, y_out])])
y = np.array([1] * 120 + [-1] * 120)

# RBF 核 SVM（隐式高维映射）
clf = SVC(kernel='rbf', gamma=1.0)
clf.fit(X, y)

# 决策区域
xx, yy = np.mgrid[-4:4:200j, -4:4:200j]
Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()])).reshape(xx.shape)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.6))

# 左：二维原始数据（线性不可分）
ax = axes[0]
ax.scatter(x_in, y_in, s=20, color='#3b82f6', edgecolor='white', linewidth=0.5)
ax.scatter(x_out, y_out, s=20, color='#f59e0b', edgecolor='white', linewidth=0.5)
ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.grid(alpha=0.2)
ax.set_title('二维：线性不可分\n（任何直线都切不开）', fontsize=12)

# 右：RBF 核的决策边界（在"高维空间"里切）
ax = axes[1]
ax.contourf(xx, yy, Z, levels=30, cmap='coolwarm', alpha=0.75)
ax.contour(xx, yy, Z, levels=[0], colors='#111827', linewidths=2.0)
ax.scatter(x_in, y_in, s=20, color='#3b82f6', edgecolor='white', linewidth=0.5)
ax.scatter(x_out, y_out, s=20, color='#f59e0b', edgecolor='white', linewidth=0.5)
ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.grid(alpha=0.2)
ax.set_title('RBF 核映射后：线性可分\n（决策边界=高维空间的一个平面）', fontsize=12)

fig.suptitle('核技巧 — 不用手动设计特征映射', fontsize=15, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.8-2_kernel_trick.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
