"""
图 1.3.6-1：Huber 损失 vs MSE vs MAE（含连接关系标注）
输出：viz/images/1.3.6-1_huber_loss.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

delta = 1.345   # 切换点（N(0,1) 下 95% 效率）

r = np.linspace(-4, 4, 800)
mse = 0.5 * r**2
mae = np.abs(r)

huber = np.where(
    np.abs(r) <= delta,
    0.5 * r**2,
    delta * (np.abs(r) - 0.5 * delta),
)

fig, ax = plt.subplots(figsize=(11, 6))

# ---- 背景带：Huber 与 MSE 的重合区（|r| ≤ δ）----
ax.axvspan(-delta, delta, color='#f59e0b', alpha=0.08, zorder=0)
ax.text(0, 5.6, 'Huber = MSE 重合区（二次）',
        ha='center', fontsize=10, color='#b45309')

# ---- 背景带：Huber 与 MAE 平行区（|r| > δ）----
ax.axvspan(delta, 4, color='#3b82f6', alpha=0.06, zorder=0)
ax.axvspan(-4, -delta, color='#3b82f6', alpha=0.06, zorder=0)
ax.text(2.55, 5.6, 'Huber ∥ MAE 平行区（线性）',
        ha='center', fontsize=10, color='#1d4ed8')

# 三曲线：先画参考线，Huber 主曲线最后画
ax.plot(r, mse, color='#94a3b8', linestyle='--', linewidth=2.0, label='MSE：处处二次（异常值主导）')
ax.plot(r, mae, color='#3b82f6', linestyle='--', linewidth=2.0, label='MAE：处处线性（小误差不精细）')
ax.plot(r, huber, color='#dc2626', linewidth=3.0, label=f'Huber（δ={delta}）')

# 切换点标记
ax.axvline(delta, color='#dc2626', linestyle=':', linewidth=1.2, alpha=0.6)
ax.axvline(-delta, color='#dc2626', linestyle=':', linewidth=1.2, alpha=0.6)
ax.annotate(f'δ={delta}', xy=(delta, 4.6), fontsize=10, color='#dc2626', ha='center')
ax.annotate(f'−δ={-delta}', xy=(-delta, 4.6), fontsize=10, color='#dc2626', ha='center')

# 连接标注：Huber 与 MSE 重合（左侧）→ 分离点
ax.annotate('Huber 与 MSE 在此处重合\n（|r| ≤ δ 时完全相等）',
            xy=(0.6, 0.18), xytext=(0.04, 2.7),
            fontsize=9.5, color='#b45309',
            arrowprops=dict(arrowstyle='->', color='#b45309', lw=1.3))

# 连接标注：Huber 与 MAE 平行（右侧）
ax.annotate('Huber 在此处与 MAE 平行\n（|r| > δ 时同为线性，斜率相同）',
            xy=(2.6, 1.1), xytext=(1.9, 3.6),
            fontsize=9.5, color='#1d4ed8',
            arrowprops=dict(arrowstyle='->', color='#1d4ed8', lw=1.3))

ax.set_xlabel('残差 r = ŷ − y', fontsize=12)
ax.set_ylabel('损失值', fontsize=12)
ax.set_title('Huber 损失 — MSE 与 MAE 的平滑过渡及连接关系', fontsize=14, pad=12)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 8.5)
ax.grid(alpha=0.25)
ax.legend(loc='upper center', fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.3.6-1_huber_loss.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
