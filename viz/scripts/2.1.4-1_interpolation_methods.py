"""
图 2.1.4-1：一维插值方法对比 — nearest / linear / cubic / PCHIP
输出：viz/images/2.1.4-1_interpolation_methods.png
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline, PchipInterpolator

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

# 温度场景：升温到 27°C 后进入平台（平台处三次插值会过冲）
t = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
temp = np.array([25.0, 26.0, 27.0, 27.0, 27.0, 27.0])

t_dense = np.linspace(0, 5, 500)

nearest = interp1d(t, temp, kind='nearest')(t_dense)
linear = interp1d(t, temp, kind='linear')(t_dense)
cubic = CubicSpline(t, temp)(t_dense)
pchip = PchipInterpolator(t, temp)(t_dense)

fig, ax = plt.subplots(figsize=(11, 6))

# 已知点（黑点）
ax.scatter(t, temp, color='#111827', s=55, zorder=6, label='已知数据点')

# 四种插值
ax.plot(t_dense, nearest, color='#64748b', linewidth=2.0, label='最近邻（阶梯状）')
ax.plot(t_dense, linear, color='#2563eb', linewidth=2.0, label='线性（折角连线）')
ax.plot(t_dense, cubic, color='#dc2626', linewidth=2.4, label='三次样条（光滑，但过冲）')
ax.plot(t_dense, pchip, color='#10b981', linewidth=2.6, label='PCHIP（保形，不过冲）')

# 过冲区域标注（cubic 超过 27 的部分）
overshoot_mask = cubic > 27.02
if overshoot_mask.any():
    idx = np.where(overshoot_mask)[0]
    x_lo, x_hi = t_dense[idx[0]], t_dense[idx[-1]]
    # 箭头精确指向过冲峰值点（x 和 y 都取峰值位置，保证落在曲线上）
    peak_pos = idx[np.argmax(cubic[overshoot_mask])]
    x_peak = float(t_dense[peak_pos])
    y_peak = float(cubic[peak_pos])
    ax.axvspan(x_lo, x_hi, color='#dc2626', alpha=0.08)
    ax.annotate(f'三次插值过冲：\n温度超过 27°C（物理上不存在）',
                xy=(x_peak, y_peak),
                xytext=(2.0, 28.3),
                fontsize=10.5, color='#dc2626',
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.4))

# 平台参考线
ax.axhline(27.0, color='#94a3b8', linestyle=':', linewidth=1.0, alpha=0.7)
ax.text(5.05, 27.02, '27°C 平台', fontsize=9.5, color='#64748b', va='bottom')

ax.set_xlabel('时间', fontsize=12)
ax.set_ylabel('温度 (°C)', fontsize=12)
ax.set_title('一维插值方法对比 — 升温后进入平台', fontsize=14, pad=12)
ax.set_xlim(0, 5.5)
ax.set_ylim(24.5, 29)
ax.grid(alpha=0.2)
ax.legend(loc='upper left', fontsize=10, framealpha=0.92)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/2.1.4-1_interpolation_methods.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}   三次插值最大过冲: {cubic.max():.3f}°C')
