# CBAM — Convolutional Block Attention Module

> 状态：待展开
> 论文：Woo et al., "CBAM: Convolutional Block Attention Module", ECCV 2018

## 一句话

在 CNN 特征图后面插入一个轻量模块，自动学习"哪些通道重要"（通道注意力）和"哪些空间位置重要"（空间注意力），让特征图更有判别力。

## 两大组件

```
输入特征图 F
    │
    ├─→ 通道注意力 Mc ─→ F' = Mc(F) ⊗ F      "第几个通道有用？"
    │
    ├─→ 空间注意力 Ms ─→ F'' = Ms(F') ⊗ F'   "通道里哪个位置有用？"
    │
    └─→ 精炼特征图 F''
```

## 定位

- 属于：CNN 特征增强模块
- 前置：SE-Net（只做通道注意力）
- 后继思想：Self-Attention / Transformer

## 待补充

- [ ] 通道注意力的具体计算（AvgPool + MaxPool → MLP → Sigmoid）
- [ ] 空间注意力的具体计算（通道压缩 → 卷积 → Sigmoid）
- [ ] 插入位置（插在卷积 Block 的什么位置效果最好）
- [ ] 与 SE-Net 的对比
- [ ] 在异常检测中的可能用法
