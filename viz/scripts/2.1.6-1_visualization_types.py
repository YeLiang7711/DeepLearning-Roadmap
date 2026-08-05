"""
图 2.1.6-1：可视化的四种基本类型（四宫格）
输出：viz/images/2.1.6-1_visualization_types.png
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 10,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(5)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. 折线图：训练/验证损失
epochs = np.arange(1, 51)
train_loss = 2.0 * np.exp(-0.08 * epochs) + 0.05 + rng.normal(0, 0.01, 50)
val_loss = 2.0 * np.exp(-0.07 * epochs) + 0.12 + rng.normal(0, 0.015, 50)
val_loss[40:] += 0.08 * np.arange(1, 11)      # 后期验证损失回升（过拟合）
ax = axes[0, 0]
ax.plot(epochs, train_loss, label='训练损失', color='#2563eb')
ax.plot(epochs, val_loss, label='验证损失', color='#dc2626')
ax.set_xlabel('epoch'); ax.set_ylabel('损失')
ax.legend(fontsize=9); ax.grid(alpha=0.2)
ax.set_title('① 折线图 — 训练损失曲线', fontsize=12)

# 2. 热图：温度场
y, x = np.mgrid[0:60, 0:60]
field = 25 + 5 * np.exp(-((x - 30) ** 2 + (y - 30) ** 2) / 200)
field += rng.normal(0, 0.2, field.shape)
ax = axes[0, 1]
im = ax.imshow(field, cmap='hot', vmin=field.min(), vmax=field.max())
ax.set_xticks([]); ax.set_yticks([])
fig.colorbar(im, ax=ax, shrink=0.85, label='°C')
ax.set_title('② 热图 — 温度场', fontsize=12)

# 3. 直方图：正常 vs 异常分数
normal = rng.normal(2.0, 0.8, 800)
anomaly = rng.normal(4.5, 1.0, 200)
ax = axes[1, 0]
sns.histplot(normal, bins=40, kde=True, color='#3b82f6', label='正常', ax=ax)
sns.histplot(anomaly, bins=40, kde=True, color='#f59e0b', label='异常', ax=ax)
ax.axvline(3.5, color='#dc2626', linestyle='--')
ax.set_xlabel('异常分数'); ax.legend(fontsize=9); ax.grid(alpha=0.2)
ax.set_title('③ 直方图 — 分数分布对比', fontsize=12)

# 4. 箱线图：多模型对比
models = ['PCA', 'AE', 'PaDiM', 'PatchCore']
data = [rng.normal(0.82, 0.04, 10), rng.normal(0.85, 0.05, 10),
        rng.normal(0.90, 0.03, 10), rng.normal(0.92, 0.02, 10)]
ax = axes[1, 1]
bp = ax.boxplot(data, tick_labels=models, patch_artist=True,
                medianprops=dict(color='#111827'))
colors = ['#94a3b8', '#3b82f6', '#f59e0b', '#10b981']
for patch, c in zip(bp['boxes'], colors):
    patch.set_facecolor(c); patch.set_alpha(0.7)
ax.set_ylabel('AUROC'); ax.grid(axis='y', alpha=0.2)
ax.set_title('④ 箱线图 — 多模型对比', fontsize=12)

fig.suptitle('可视化的四种基本类型', fontsize=15, y=0.99)
plt.tight_layout(rect=[0, 0, 1, 0.96])
out = 'D:/LearnSpace/viz/images/2.1.6-1_visualization_types.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
