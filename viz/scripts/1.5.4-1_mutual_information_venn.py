"""
图 1.5.4-1：熵、条件熵、互信息的关系（文氏图）
输出：viz/images/1.5.4-1_mutual_information_venn.png
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.facecolor': 'white',
})

fig, ax = plt.subplots(figsize=(8, 6.5))

# 两个圆（重叠区域 = 互信息）
c1 = Circle((0.28, 0.5), 0.32, fill=True, color='#3b82f6', alpha=0.35)
c2 = Circle((0.72, 0.5), 0.32, fill=True, color='#10b981', alpha=0.35)
ax.add_patch(c1)
ax.add_patch(c2)
ax.add_patch(Circle((0.28, 0.5), 0.32, fill=False, edgecolor='#1d4ed8', linewidth=2.5))
ax.add_patch(Circle((0.72, 0.5), 0.32, fill=False, edgecolor='#047857', linewidth=2.5))

# 标注
ax.text(0.16, 0.62, 'H(X)', fontsize=13, fontweight='bold', color='#1d4ed8')
ax.text(0.84, 0.62, 'H(Y)', fontsize=13, fontweight='bold', color='#047857')

ax.text(0.42, 0.66, 'I(X;Y)\n共享信息', fontsize=11.5, fontweight='bold',
        color='#7c2d12', ha='center',
        bbox=dict(boxstyle='round,pad=0.35', fc='#fef3c7', ec='#f59e0b', alpha=0.95))

ax.text(0.09, 0.40, 'H(X|Y)\n仅 X 独有\n（Y 给不了的）',
        fontsize=10, color='#1e40af', ha='center')
ax.text(0.91, 0.40, 'H(Y|X)\n仅 Y 独有',
        fontsize=10, color='#065f46', ha='center')

ax.text(0.5, 0.10, '联合不确定性 H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)',
        fontsize=10.5, ha='center', color='#475569',
        bbox=dict(boxstyle='round,pad=0.4', fc='#f8fafc', ec='#cbd5e1'))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('熵、条件熵、互信息的关系', fontsize=14, pad=15)

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/1.5.4-1_mutual_information_venn.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
