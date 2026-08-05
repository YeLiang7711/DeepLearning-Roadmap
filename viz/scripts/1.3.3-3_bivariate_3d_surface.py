"""
图 1.3.3-3：二元高斯分布 3D 概率密度曲面（Plotly）
输出：viz/images/1.3.3-3_bivariate_3d_surface.png
"""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go


# ============================================================
# 输出配置
# ============================================================

OUTPUT_PNG = Path("D:/LearnSpace/viz/images/1.3.3-3_bivariate_3d_surface.png")

# 是否同时打开浏览器交互查看
SHOW_INTERACTIVE = True

# 输出分辨率
IMAGE_WIDTH = 2400
IMAGE_HEIGHT = 1600


# ============================================================
# 二元高斯分布参数
# ============================================================

mean = np.array(
    [0.0, 0.0],
    dtype=np.float64,
)

covariance = np.array(
    [
        [3.0, 1.5],
        [1.5, 1.0],
    ],
    dtype=np.float64,
)

determinant = np.linalg.det(covariance)

if determinant <= 0:
    raise ValueError("协方差矩阵必须为正定矩阵。")

covariance_inverse = np.linalg.inv(covariance)

correlation = covariance[0, 1] / np.sqrt(
    covariance[0, 0] * covariance[1, 1]
)

print(f"相关系数 ρ = {correlation:.6f}")


# ============================================================
# 建立坐标网格
#
# 使用约 ±3σ，而不是 ±4σ。
# 这样可以减少无意义的大面积空白底面。
# ============================================================

sigma_x1 = np.sqrt(covariance[0, 0])
sigma_x2 = np.sqrt(covariance[1, 1])

x1_values = np.linspace(
    -3.15 * sigma_x1,
    3.15 * sigma_x1,
    300,
)

x2_values = np.linspace(
    -3.15 * sigma_x2,
    3.15 * sigma_x2,
    240,
)

x1_grid, x2_grid = np.meshgrid(
    x1_values,
    x2_values,
    indexing="xy",
)


# ============================================================
# 计算二元高斯概率密度
# ============================================================

positions = np.stack(
    [x1_grid, x2_grid],
    axis=-1,
)

difference = positions - mean

mahalanobis_squared = np.einsum(
    "...i,ij,...j->...",
    difference,
    covariance_inverse,
    difference,
)

normalization = 1.0 / (
    2.0 * np.pi * np.sqrt(determinant)
)

density = normalization * np.exp(
    -0.5 * mahalanobis_squared
)

density_maximum = float(density.max())

print(f"最大概率密度 = {density_maximum:.6f}")


# ============================================================
# 裁剪极低密度区域
#
# 接近 0 的曲面不再覆盖整个底面，从而避免出现大片半透明薄膜。
# 底面投影仍然保留完整密度。
# ============================================================

surface_threshold = density_maximum * 0.012

surface_density = np.where(
    density >= surface_threshold,
    density,
    np.nan,
)


# ============================================================
# 暖色系颜色映射
#
# 低密度：近白色
# 中密度：浅琥珀
# 高密度：橙色
# ============================================================

warm_colorscale = [
    [0.00, "#FFFDF9"],
    [0.10, "#FFF5E8"],
    [0.25, "#FDE6BD"],
    [0.42, "#FBC56D"],
    [0.60, "#F5A623"],
    [0.78, "#EA810C"],
    [1.00, "#C95F08"],
]


# ============================================================
# 创建图形
# ============================================================

figure = go.Figure()


# ============================================================
# 1. 底面填充概率密度投影
# ============================================================

figure.add_trace(
    go.Surface(
        x=x1_grid,
        y=x2_grid,
        z=np.zeros_like(density),
        surfacecolor=density,

        cmin=0.0,
        cmax=density_maximum,
        colorscale=warm_colorscale,

        opacity=0.55,
        showscale=False,

        hoverinfo="skip",

        lighting=dict(
            ambient=1.0,
            diffuse=0.0,
            specular=0.0,
            roughness=1.0,
            fresnel=0.0,
        ),
    )
)


# ============================================================
# 2. 三维高斯概率密度曲面
# ============================================================

figure.add_trace(
    go.Surface(
        x=x1_grid,
        y=x2_grid,
        z=surface_density,
        surfacecolor=density,

        cmin=0.0,
        cmax=density_maximum,
        colorscale=warm_colorscale,

        opacity=0.87,
        showscale=False,

        hovertemplate=(
            "温度：%{x:.3f}<br>"
            "梯度：%{y:.3f}<br>"
            "概率密度：%{z:.5f}"
            "<extra></extra>"
        ),

        lighting=dict(
            ambient=0.72,
            diffuse=0.80,
            specular=0.10,
            roughness=0.92,
            fresnel=0.04,
        ),

        lightposition=dict(
            x=-120,
            y=-160,
            z=260,
        ),
    )
)


# ============================================================
# 3. 解析计算底面椭圆等高线
#
# 对二元高斯：
#
#   (x - μ)^T Σ⁻¹ (x - μ) = r²
#
# 构成协方差椭圆。
# ============================================================

eigenvalues, eigenvectors = np.linalg.eigh(covariance)

ellipse_transform = eigenvectors @ np.diag(
    np.sqrt(eigenvalues)
)

theta = np.linspace(
    0.0,
    2.0 * np.pi,
    500,
)

unit_circle = np.vstack(
    [
        np.cos(theta),
        np.sin(theta),
    ]
)

# 每个数值表示该等高线相对于峰值的密度比例
contour_fractions = [
    0.08,
    0.14,
    0.22,
    0.32,
    0.44,
    0.57,
    0.70,
    0.81,
    0.90,
]

for fraction in contour_fractions:
    radius_squared = -2.0 * np.log(fraction)
    radius = np.sqrt(radius_squared)

    ellipse = (
        mean[:, np.newaxis]
        + ellipse_transform
        @ (radius * unit_circle)
    )

    # 略高于 z=0，避免和底面发生深度冲突
    contour_z = np.full(
        theta.shape,
        density_maximum * 0.0015,
    )

    figure.add_trace(
        go.Scatter3d(
            x=ellipse[0],
            y=ellipse[1],
            z=contour_z,

            mode="lines",

            line=dict(
                color="rgba(157, 78, 14, 0.55)",
                width=3,
            ),

            hoverinfo="skip",
            showlegend=False,
        )
    )


# ============================================================
# 三维坐标轴样式
# ============================================================

common_axis_style = dict(
    showbackground=True,
    backgroundcolor="rgb(255, 255, 255)",

    showgrid=True,
    gridcolor="rgba(145, 145, 145, 0.25)",
    gridwidth=1,

    zeroline=True,
    zerolinecolor="rgba(100, 100, 100, 0.45)",
    zerolinewidth=1,

    showline=True,
    linecolor="rgba(80, 80, 80, 0.65)",
    linewidth=2,

    ticks="outside",
    tickcolor="rgba(60, 60, 60, 0.7)",
    tickfont=dict(
        size=16,
        color="#444444",
    ),

    showspikes=False,
)


# ============================================================
# 整体布局
# ============================================================

figure.update_layout(
    title=dict(
        text="二元高斯分布 — 正相关协方差结构",
        x=0.5,
        y=0.965,
        xanchor="center",
        yanchor="top",

        font=dict(
            family=(
                "Microsoft YaHei, "
                "Noto Sans CJK SC, "
                "SimHei, "
                "Arial Unicode MS, "
                "sans-serif"
            ),
            size=34,
            color="#202020",
        ),
    ),

    font=dict(
        family=(
            "Microsoft YaHei, "
            "Noto Sans CJK SC, "
            "SimHei, "
            "Arial Unicode MS, "
            "sans-serif"
        ),
        color="#303030",
    ),

    paper_bgcolor="white",
    plot_bgcolor="white",

    margin=dict(
        l=40,
        r=40,
        t=105,
        b=35,
    ),

    scene=dict(
        bgcolor="white",

        xaxis=dict(
            **common_axis_style,

            title=dict(
                text="温度",
                font=dict(
                    size=24,
                    color="#202020",
                ),
            ),

            range=[
                float(x1_values.min()),
                float(x1_values.max()),
            ],

            nticks=7,
            tickformat=".1f",
        ),

        yaxis=dict(
            **common_axis_style,

            title=dict(
                text="梯度",
                font=dict(
                    size=24,
                    color="#202020",
                ),
            ),

            range=[
                float(x2_values.min()),
                float(x2_values.max()),
            ],

            nticks=7,
            tickformat=".1f",
        ),

        zaxis=dict(
            **common_axis_style,

            title=dict(
                text="概率密度",
                font=dict(
                    size=24,
                    color="#202020",
                ),
            ),

            range=[
                0.0,
                density_maximum * 1.10,
            ],

            nticks=6,
            tickformat=".3f",
        ),

        # 正交投影可以消除过强的近大远小效果，
        # 更接近论文和教材中的科学绘图。
        camera=dict(
            eye=dict(
                x=1.55,
                y=-1.65,
                z=0.92,
            ),

            center=dict(
                x=0.0,
                y=0.0,
                z=-0.08,
            ),

            up=dict(
                x=0.0,
                y=0.0,
                z=1.0,
            ),

            projection=dict(
                type="orthographic",
            ),
        ),

        aspectmode="manual",

        aspectratio=dict(
            x=1.48,
            y=1.00,
            z=0.72,
        ),

        dragmode="orbit",
    ),
)


# ============================================================
# 输出 PNG
# ============================================================

OUTPUT_PNG.parent.mkdir(
    parents=True,
    exist_ok=True,
)

figure.write_image(
    str(OUTPUT_PNG),
    width=IMAGE_WIDTH,
    height=IMAGE_HEIGHT,
    scale=1,
)

print(f"PNG 已保存：{OUTPUT_PNG.resolve()}")
print(f"图片分辨率：{IMAGE_WIDTH} × {IMAGE_HEIGHT}")


# ============================================================
# 可选：浏览器交互查看
# ============================================================

if SHOW_INTERACTIVE:
    figure.show()
