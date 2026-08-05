"""
图 1.4.3-1：不同学习率的训练损失曲线
输出：viz/images/1.4.3-1_learning_rates.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

rng = np.random.default_rng(5)

epochs = np.arange(1, 101)


def simulate_loss(lr, seed, floor=0.05):
    """简单模拟：收敛速度由 lr 决定，加噪声"""
    r = np.random.default_rng(seed)
    n_epochs = epochs.shape[0]
    # 收敛项 + 噪声；lr 越大收敛越快，但超过阈值会震荡
    if lr <= 0.2:
        decay = np.exp(-lr * 8 * epochs)
        noise = r.normal(0, 0.004, n_epochs)
        return decay + noise + floor
    else:
        # 过大学习率：发散震荡
        decay = np.exp(0.012 * epochs)
        osc = 0.15 * np.sin(0.6 * epochs)
        return decay + osc + 0.1


fig, ax = plt.subplots(figsize=(11, 5.8))

# η 过小
loss_small = simulate_loss(0.01, 1)
ax.plot(epochs, loss_small, color='#64748b', linewidth=2.2,
        label='η 过小（0.001）：下降极慢，训练时间不够到不了低损失')

# η 合适
loss_ok = simulate_loss(0.1, 2)
ax.plot(epochs, loss_ok, color='#2563eb', linewidth=2.6,
        label='η 合适（0.1）：平稳下降，快速收敛到低损失')

# η 过大
loss_big = simulate_loss(0.5, 3)
ax.plot(epochs, loss_big, color='#dc2626', linewidth=2.2,
        label='η 过大（0.5）：损失发散/震荡，不收敛')

ax.set_xlabel('训练轮数（epoch）', fontsize=12)
ax.set_ylabel('损失', fontsize=12)
ax.set_title('不同学习率的训练损失曲线', fontsize=14, pad=12)
ax.set_xlim(0, 100)
ax.set_ylim(0, 3.2)
ax.grid(alpha=0.25)
ax.legend(fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.4.3-1_learning_rates.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
