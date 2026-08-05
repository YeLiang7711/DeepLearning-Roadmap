"""
图 1.1.6-2：高维特征 PCA 降维后的可视化 — PC1-PC2 散点图（三类样本）
输出：viz/images/1.1.6-2_pca_visualization.png
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(3)

# 模拟高维特征的三类样本：2 个信号维（决定类别）+ 18 个噪声维
n_per_class = 200
centers = {
    '正常样本': np.array([0.0, 0.0]),
    '异常A类': np.array([4.0, 2.0]),
    '异常B类': np.array([-3.5, 4.0]),
}
colors = {'正常样本': '#3b82f6', '异常A类': '#f59e0b', '异常B类': '#10b981'}

X, y = [], []
for label, c in centers.items():
    # 20 维：前 2 维决定类别位置（信号），其余 18 维是噪声（PCA 正好抓到前 2 维）
    noise = rng.normal(0, 1.0, size=(n_per_class, 18))
    base = np.column_stack([
        rng.normal(c[0], 0.8, n_per_class),
        rng.normal(c[1], 0.8, n_per_class),
        noise,
    ])
    X.append(base)
    y.extend([label] * n_per_class)

X = np.vstack(X)
y = np.array(y)

# PCA 降到 2 维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

fig, ax = plt.subplots(figsize=(9, 7))

for label in centers:
    mask = y == label
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1], s=14, alpha=0.6,
               color=colors[label], label=f'{label} (n={mask.sum()})')

ax.set_xlabel(f'PC1（解释方差 {pca.explained_variance_ratio_[0]*100:.1f}%）', fontsize=12)
ax.set_ylabel(f'PC2（解释方差 {pca.explained_variance_ratio_[1]*100:.1f}%）', fontsize=12)
ax.set_title('20 维特征 PCA 降至 2 维 — 三类样本清晰可分', fontsize=14, pad=12)
ax.grid(alpha=0.2)
ax.legend(fontsize=10.5, framealpha=0.92, loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.1.6-2_pca_visualization.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}   explained={pca.explained_variance_ratio_.sum()*100:.1f}%')
