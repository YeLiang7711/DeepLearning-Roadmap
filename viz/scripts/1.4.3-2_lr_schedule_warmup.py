"""
图 1.4.3-2：Warmup + Cosine 学习率调度曲线
输出：viz/images/1.4.3-2_lr_schedule_warmup.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

total_steps = 100
warmup_steps = 10
peak_lr = 1.0

steps = np.arange(total_steps)

# Warmup：线性升到峰值
warmup = peak_lr * steps / warmup_steps

# Cosine 衰减：从峰值降到接近 0
cosine = peak_lr * 0.5 * (1 + np.cos(np.pi * (steps - warmup_steps) / (total_steps - warmup_steps)))

lr = np.where(steps < warmup_steps, warmup, cosine)

fig, ax = plt.subplots(figsize=(10.5, 5.5))

ax.plot(steps, lr, color='#2563eb', linewidth=2.6)

# Warmup 区域标注
ax.axvspan(0, warmup_steps, color='#f59e0b', alpha=0.10)
ax.annotate('Warmup\n（前几步小学习率，\n梯度稳定后再放开）',
            xy=(warmup_steps / 2, 0.32), fontsize=10.5, color='#b45309',
            ha='center')

# 峰值标注
ax.plot(warmup_steps, peak_lr, 'o', color='#dc2626', markersize=7, zorder=5)
ax.annotate('峰值学习率', xy=(warmup_steps, peak_lr),
            xytext=(warmup_steps + 3, peak_lr + 0.08),
            fontsize=10.5, color='#dc2626',
            arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.4))

# Cosine 区域标注
ax.axvspan(warmup_steps, total_steps, color='#3b82f6', alpha=0.06)
ax.text(total_steps - 1, 0.55, 'Cosine 衰减\n（平滑降到接近 0）',
        fontsize=10.5, color='#1d4ed8', ha='right')

ax.set_xlabel('训练步数', fontsize=12)
ax.set_ylabel('学习率', fontsize=12)
ax.set_title('Warmup + Cosine 学习率调度', fontsize=14, pad=12)
ax.set_xlim(0, total_steps)
ax.set_ylim(0, 1.15)
ax.grid(axis='y', alpha=0.25)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.4.3-2_lr_schedule_warmup.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
