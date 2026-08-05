# 图片规则详解与代码模板

## 目录与命名

```
viz/
├── scripts/        ← 脚本
│   └── X.X.N-N_描述.py
└── images/         ← 图片（与脚本同名）
    └── X.X.N-N_描述.png
```

**编号规则**：`章节号-章节内序号`。例：
- `1.3.3-1` = 1.3.3 节第 1 张图
- `1.3.3-2` = 1.3.3 节第 2 张图
- 换章节后序号重新从 1 开始

---

## 标准脚本骨架

```python
"""
图 X.X.N-N：描述
输出：viz/images/X.X.N-N_desc.png
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Microsoft YaHei',   # 中文字体（Windows）
    'font.size': 11,
    'axes.unicode_minus': False,        # 负号正常显示
    'figure.facecolor': 'white',
})

# ... 绘图代码 ...

plt.tight_layout()
out = 'D:/LearnSpace/viz/images/X.X.N-N_desc.png'
plt.savefig(out, dpi=160, bbox_inches='tight', facecolor='white')
plt.close()
print(f'saved: {out}')
```

运行：`cd D:/LearnSpace && python viz/scripts/X.X.N-N_desc.py`

---

## md 引用格式

```markdown
![图X.X.N-N：描述标题](../../viz/images/X.X.N-N_desc.png)

*图 X.X.N-N：图注——逐元素解释图中内容（数据、线条、区域、标注各是什么）。*
```

图注必须解释图中**每个有意义的元素**。范例：

> *图 1.3.5-2：正常分数 ~N(0,1)、异常分数 ~N(2,1) 的模拟 ROC 曲线。蓝色曲线下的面积即 AUROC（=0.92）；灰色虚线为随机猜测基线（AUC=0.5）。阈值低时曲线走向右上（什么都报），阈值高时走向左下（很少报）。*

---

## 图要讲故事：数值必须验证

图片不能只"形状对"，数值必须合理。生成后**打印关键数值**核对：

```python
print(f'saved: {out}   AUC={auc:.4f}')   # ROC 图：对照理论值 Φ(1.414)≈0.9214
print(f'mean={mu:.3f} std={sigma:.3f} mu+3σ={thr_3sigma:.3f} q95={thr_q95:.3f}')  # 阈值对比图
```

已验证的数值对照：
- 正常 N(0,1) vs 异常 N(2,1) 的 ROC → AUC ≈ 0.92（理论 Φ(1.414)）
- 高斯 68-95-99.7 → 面积 68.3%/95.4%/99.7%（scipy 直接算）

---

## 踩过的坑（禁止重犯）

| 坑 | 症状 | 修复 |
|---|---|---|
| 直方图 `set_ylim(0, 1.0)` 手写死 | 柱子被裁剪成底部细条 | `counts, bins, _ = ax.hist(...)`，`ymax = counts.max()`，`set_ylim(0, ymax * 1.18)` |
| 标注用写死的数据坐标 | 文字飘在图上/互相重叠 | `xytext` 用 `textcoords='axes fraction'`，`(0.28, 0.86)` 形式 |
| ROC 曲线遍历顺序反了 | AUC < 0.5（如 0.078） | 阈值从小到大 TPR/FPR 从 1 降到 0，需 `[::-1]` 反转 |
| matplotlib 3D 曲面 | 重叠、模糊、深度错误 | 用 plotly（`go.Surface` + `fig.write_image`）或 pyvista |
| 中文 Glyph 警告 | 文字变方块 | `font.family = 'Microsoft YaHei'` + `axes.unicode_minus = False` |
| 下标字符缺字体（ₖ 等） | Glyph 警告 | 用 LaTeX `$X_k$` 代替 Unicode 下标 |
| 表格内 `|Σ|` | 公式断掉 | 用 `\det(\mathbf{\Sigma})` |

---

## 3D 图规范

matplotlib 的 mplot3d 效果差（软件光栅化、深度排序错误）。用户对 3D 图有明确要求，**默认用 plotly**：

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Surface(
    x=X, y=Y, z=Z,
    colorscale='Oranges',          # 暖色系贴合温度主题
    opacity=0.85,
    contours_z=dict(show=True, usecolormap=True, project_z=True),
))

fig.write_image(out, scale=2, width=2000, height=1400)
```

需要 `pip install plotly kaleido`。生成后必须**实际查看图片**确认没有重叠（3D 图容易出布局问题）。

---

## 配色习惯

- 顺序色（数量/密度）：单一色相渐变，如 `Oranges`、`YlOrBr`、`Blues`
- 类别色（分类）：蓝 `#3b82f6`、橙 `#f59e0b`、绿 `#10b981`、红 `#dc2626`——固定顺序，不循环
- 对比图中的关键对象用红色（主曲线/阈值线），参考对象用灰/蓝虚线
- 背景区域标注（欠拟合/过拟合等）：`axvspan` 低透明度 + 文字标注
