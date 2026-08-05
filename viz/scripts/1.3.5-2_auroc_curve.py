"""
图 1.3.5-2：ROC 曲线与 AUROC 面积
输出：viz/images/1.3.5-2_auroc_curve.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(7)

# 模拟：正常样本分数低，异常样本分数高（有一定重叠）
normal_scores = rng.normal(0.0, 1.0, size=5000)
anomaly_scores = rng.normal(2.0, 1.0, size=500)

# 遍历阈值，计算 TPR（召回率）和 FPR（误报率）
# 阈值从小到大时，TPR/FPR 从 1 降到 0 → 反转得到 (0,0)→(1,1) 的标准顺序
thresholds = np.sort(np.concatenate([normal_scores, anomaly_scores]))
fpr = np.empty_like(thresholds)
tpr = np.empty_like(thresholds)
for i, t in enumerate(thresholds):
    tpr[i] = (anomaly_scores > t).mean()
    fpr[i] = (normal_scores > t).mean()
fpr = fpr[::-1]
tpr = tpr[::-1]
# 补上 (0,0) 和 (1,1) 端点
fpr = np.concatenate([[0.0], fpr, [1.0]])
tpr = np.concatenate([[0.0], tpr, [1.0]])

# 梯形法算 AUROC
auc = np.trapezoid(tpr, fpr)

fig, ax = plt.subplots(figsize=(8.5, 8))

# 曲线下的面积（AUC）
ax.fill_between(fpr, tpr, 0, color='#3b82f6', alpha=0.18)
# ROC 曲线
ax.plot(fpr, tpr, color='#1d4ed8', linewidth=2.6, label='ROC 曲线')
# 随机猜测对角线
ax.plot([0, 1], [0, 1], color='#94a3b8', linestyle='--', linewidth=1.8,
        label='随机猜测 (AUC=0.5)')

# 阈值方向标注
ax.annotate('阈值低\n什么都报：召回高，误报也高',
            xy=(0.88, 0.93), fontsize=10, color='#1e40af', ha='center')
ax.annotate('阈值高\n很少报：误报低，召回也低',
            xy=(0.10, 0.16), fontsize=10, color='#1e40af', ha='center')

# AUC 数值标注
ax.text(0.55, 0.32, f'AUROC = {auc:.2f}', fontsize=16, fontweight='bold',
        color='#1d4ed8')

ax.set_xlabel('误报率 FPR（1 - 特异性）', fontsize=12)
ax.set_ylabel('召回率 TPR（灵敏度）', fontsize=12)
ax.set_title('ROC 曲线 — 不同阈值下误报与召回的权衡', fontsize=14, pad=12)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)
ax.grid(alpha=0.25)
ax.legend(loc='lower right', fontsize=10.5, framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.3.5-2_auroc_curve.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}   AUC={auc:.4f}')
