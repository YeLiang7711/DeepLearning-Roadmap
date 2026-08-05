"""
图 2.1.8-3：KMeans vs DBSCAN 聚类对比（月牙数据 + 噪声点）
输出：viz/images/2.1.8-3_clustering_compare.png
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(17)

# 月牙形数据（上半月 + 倒扣下半月，两个不规则簇，KMeans 会切错）
n = 150
t = rng.uniform(0, np.pi, n)
moon1 = np.column_stack([np.cos(t), np.sin(t)]) * 2.2                    # 上半月
moon2 = np.column_stack([np.cos(t), -np.sin(t)]) * 2.2 + [1.8, -0.8]     # 倒扣下半月

# 噪声点（DBSCAN 会标为 -1）
noise = rng.uniform(-3.5, 3.5, size=(12, 2))

X = np.vstack([moon1, moon2, noise])

# KMeans（K=2，球形假设）
km = KMeans(n_clusters=2, n_init=10, random_state=42)
km_labels = km.fit_predict(X)

# DBSCAN（密度聚类，自动发现噪声）
db = DBSCAN(eps=0.45, min_samples=5)
db_labels = db.fit_predict(X)
n_clusters_db = len(set(db_labels)) - (1 if -1 in db_labels else 0)
n_noise = (db_labels == -1).sum()

cmap = {0: '#3b82f6', 1: '#f59e0b', -1: '#64748b'}

fig, axes = plt.subplots(1, 2, figsize=(13, 5.8))

# 左：KMeans
ax = axes[0]
for lab in set(km_labels):
    mask = km_labels == lab
    ax.scatter(X[mask, 0], X[mask, 1], s=20, color=cmap[lab],
               edgecolor='white', linewidth=0.4, label=f'簇 {lab+1}')
ax.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
           marker='*', s=220, color='#111827', zorder=5, label='簇中心')
ax.set_title('KMeans（K=2）：按距离划球形簇\n月牙被切成两半', fontsize=12)
ax.set_xlim(-4.5, 4.5); ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal'); ax.grid(alpha=0.2)
ax.legend(fontsize=9, loc='upper right')

# 右：DBSCAN
ax = axes[1]
for lab in set(db_labels):
    mask = db_labels == lab
    if lab == -1:
        ax.scatter(X[mask, 0], X[mask, 1], s=30, color=cmap[-1],
                   marker='x', linewidth=1.2,
                   label=f'噪声（{n_noise} 个）')
    else:
        ax.scatter(X[mask, 0], X[mask, 1], s=20, color=cmap[lab % 2],
                   edgecolor='white', linewidth=0.4, label=f'簇 {lab+1}')
ax.set_title(f'DBSCAN：按密度聚类\n自动发现 {n_clusters_db} 个簇 + 噪声点', fontsize=12)
ax.set_xlim(-4.5, 4.5); ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal'); ax.grid(alpha=0.2)
ax.legend(fontsize=9, loc='upper right')

fig.suptitle('KMeans vs DBSCAN — 不规则形状与噪声', fontsize=15, y=1.0)
plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.8-3_clustering_compare.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}   KMeans 簇数=2, DBSCAN 簇数={n_clusters_db}, 噪声={n_noise}')
