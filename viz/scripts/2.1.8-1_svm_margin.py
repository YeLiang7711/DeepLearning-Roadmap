"""
图 2.1.8-1：SVM 间隔最大化与支持向量
输出：viz/images/2.1.8-1_svm_margin.png
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

rng = np.random.default_rng(8)

# 两类数据（可线性分离，留出间隔）
pos = rng.normal([2.5, 2.5], 0.9, size=(40, 2))
neg = rng.normal([-2.5, -2.5], 0.9, size=(40, 2))
X = np.vstack([pos, neg])
y = np.array([1] * 40 + [-1] * 40)

# 线性 SVM
clf = SVC(kernel='linear', C=1e6)
clf.fit(X, y)

# 决策边界与间隔线
w = clf.coef_[0]
b = clf.intercept_[0]
xx = np.linspace(-6, 6, 200)
yy = -(w[0] * xx + b) / w[1]
margin = 1 / np.linalg.norm(w)
yy_up = yy + margin / np.sqrt(w[0]**2 + w[1]**2) * np.sign(w[1])  # 上间隔
yy_down = yy - margin / np.sqrt(w[0]**2 + w[1]**2) * np.sign(w[1])

fig, ax = plt.subplots(figsize=(10, 7))

# 数据点（支持向量高亮）
sv = clf.support_vectors_
ax.scatter(pos[:, 0], pos[:, 1], s=45, color='#3b82f6', edgecolor='white', linewidth=0.8, label='类别 +1')
ax.scatter(neg[:, 0], neg[:, 1], s=45, color='#f59e0b', edgecolor='white', linewidth=0.8, label='类别 -1')
ax.scatter(sv[:, 0], sv[:, 1], s=160, facecolor='none',
           edgecolor='#dc2626', linewidth=2.5, label='支持向量')

# 决策边界与间隔
ax.plot(xx, yy, color='#111827', linewidth=2.2, label='决策边界')
ax.plot(xx, yy_up, color='#dc2626', linestyle='--', linewidth=1.6, label='间隔边界')
ax.plot(xx, yy_down, color='#dc2626', linestyle='--', linewidth=1.6)

# 间隔标注
mid_x, mid_y = 0, 0
ax.annotate('', xy=(0.9, 0.9), xytext=(-0.9, -0.9),
            arrowprops=dict(arrowstyle='<->', color='#10b981', lw=2.5))
ax.text(0.05, -1.4, '间隔（margin）\n越大 → 泛化越好', fontsize=11,
        color='#047857', fontweight='bold')

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_xlabel('特征 1')
ax.set_ylabel('特征 2')
ax.set_title('SVM — 间隔最大化的分界线', fontsize=14, pad=12)
ax.grid(alpha=0.2)
ax.legend(loc='upper right', fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.8-1_svm_margin.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}   支持向量数: {len(sv)}')
