"""
图 1.3.5-1：异常分数直方图 — μ+3σ 阈值 vs 95% 分位数阈值对比
输出：viz/images/1.3.5-1_threshold_comparison.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(42)

# 右偏的异常分数分布（大量低分 + 少量高分长尾）
scores = np.concatenate([
    rng.gamma(shape=2.2, scale=0.65, size=900),   # 大多数正常样本
    rng.gamma(shape=5.0, scale=0.55, size=80),     # 少量偏高样本
    rng.uniform(5.0, 8.0, size=30),                # 极端高分（可能是异常）
])
scores = np.clip(scores, 0, 8)

mu = scores.mean()
sigma = scores.std()
thr_3sigma = mu + 3 * sigma
thr_q95 = np.quantile(scores, 0.95)

fig, ax = plt.subplots(figsize=(11, 5.2))

# 直方图
counts, bins, _ = ax.hist(scores, bins=60, range=(0, 8), color='#3b82f6',
                          alpha=0.85, edgecolor='white', linewidth=0.6)
ymax = counts.max()

# 标注位置（相对高度）
h_line = 0.9 * ymax   # 阈值线箭头指向的高度

# μ+3σ 阈值线（红，虚线）
ax.axvline(thr_3sigma, color='#dc2626', linestyle='--', linewidth=2.2)
ax.annotate(f'μ+3σ = {thr_3sigma:.2f}\n（被高分拉宽 → 阈值过高）',
            xy=(thr_3sigma, h_line),
            xytext=(0.28, 0.86), textcoords='axes fraction',
            fontsize=11, color='#dc2626', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.6))

# 95% 分位数阈值线（青，实线）
ax.axvline(thr_q95, color='#0d9488', linestyle='-', linewidth=2.4)
ax.annotate(f'95% 分位数 = {thr_q95:.2f}\n（只看排名，不看形状）',
            xy=(thr_q95, h_line),
            xytext=(0.62, 0.55), textcoords='axes fraction',
            fontsize=11, color='#0d9488', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#0d9488', lw=1.6))

# 尾部极端高分区域浅色高亮
ax.axvspan(thr_q95, 8, color='#0d9488', alpha=0.06)
ax.text(0.965, 0.94, '极端高分区\n（可能是异常）',
        transform=ax.transAxes, fontsize=9.5, color='#0d9488',
        ha='right', va='top')

ax.set_xlabel('异常分数', fontsize=12)
ax.set_ylabel('样本数', fontsize=12)
ax.set_title('异常分数分布 — μ+3σ 与 95% 分位数阈值对比', fontsize=14, pad=12)
ax.set_xlim(0, 8)
ax.set_ylim(0, ymax * 1.18)   # 顶部留出标注空间
ax.grid(axis='y', alpha=0.25)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.3.5-1_threshold_comparison.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
print(f'mean={mu:.3f} std={sigma:.3f} mu+3σ={thr_3sigma:.3f} q95={thr_q95:.3f}')
