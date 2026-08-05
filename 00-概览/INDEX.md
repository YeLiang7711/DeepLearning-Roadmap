# 🧠 LearnSpace 导航中枢

> 最后更新：2026-07-30 | 📄=有笔记 🔗=可跳转 ·=待编写

## 入口

- 📖 [[深度学习完整学习路线]] — 完整知识地图
- 🧭 [[使用指南]] — 学习原则、掌握程度

---

## 00-概览

- **0. 如何使用这份路线** — 推荐主线 / 三种掌握程度 / 学习原则 / 内容重心表

---

## 01-数学基础

### 1.1 线性代数
- 📂 [[../01-数学基础/1.1-线性代数/0-概述|概述]] — 全章速查表与推荐阅读顺序
- 📄 [[../01-数学基础/1.1-线性代数/1.1.1 向量、矩阵、张量与常用运算|1.1.1 向量、矩阵、张量]] — 标量/向量/矩阵/张量、矩阵乘法、转置、Hadamard 积
- 📄 [[../01-数学基础/1.1-线性代数/1.1.2 内积、范数、距离与相似度|1.1.2 内积、范数、距离]] — 点积、L1/L2/Frobenius 范数、欧氏/余弦/Mahalanobis 距离
- 📄 [[../01-数学基础/1.1-线性代数/1.1.3 线性相关、秩、基与子空间|1.1.3 线性相关、秩、基]] — 线性相关与无关、秩的定义与意义、基与子空间
- 📄 [[../01-数学基础/1.1-线性代数/1.1.4 特征值、特征向量、SVD|1.1.4 特征值、特征向量、SVD]] — 特征分解、奇异值分解、低秩近似
- 📄 [[../01-数学基础/1.1-线性代数/1.1.5 正定矩阵、协方差矩阵、求逆与伪逆|1.1.5 正定矩阵、协方差矩阵]] — 正定/半正定、协方差矩阵、矩阵求逆/伪逆/shrinkage
- 📄 [[../01-数学基础/1.1-线性代数/1.1.6 PCA及低秩近似|1.1.6 PCA 及低秩近似]] — PCA 降维/可视化/去噪/去相关/异常检测/压缩 六大应用

### 1.2 微积分
- 📂 [[../01-数学基础/1.2-微积分/0-概述|概述]] — 全章概览与阅读顺序
- 📄 [[../01-数学基础/1.2-微积分/1.2.1 导数、偏导数、方向导数与梯度|1.2.1 导数、偏导数、梯度]] — 变化率、偏导、梯度定义与梯度下降
- 📄 [[../01-数学基础/1.2-微积分/1.2.2 链式法则与反向传播|1.2.2 链式法则与反向传播]] — 复合函数求导、计算图、反向传播推导
- 📄 [[../01-数学基础/1.2-微积分/1.2.3 Jacobian、Hessian及其直觉|1.2.3 Jacobian 与 Hessian]] — 向量值函数导数、二阶导数矩阵、高维鞍点
- 📄 [[../01-数学基础/1.2-微积分/1.2.4 常见函数的导数|1.2.4 常见函数的导数]] — 激活函数/损失函数的导数速查表

### 1.3 概率统计
- 📂 [[../01-数学基础/1.3-概率统计/0-概述|概述]] — 全章概览与阅读顺序
- 📄 [[../01-数学基础/1.3-概率统计/1.3.1 随机变量、期望、方差、协方差|1.3.1 随机变量、期望、方差]] — 离散/连续随机变量、期望与方差性质
- 📄 [[../01-数学基础/1.3-概率统计/1.3.2 条件概率与贝叶斯公式|1.3.2 条件概率与贝叶斯]] — 条件概率、贝叶斯定理、先验/后验/似然
- 📄 [[../01-数学基础/1.3-概率统计/1.3.3 高斯分布与多元高斯分布|1.3.3 高斯与多元高斯]] — 一元/多元高斯、Σ 控制形状、68-95-99.7 规则
- 📄 [[../01-数学基础/1.3-概率统计/1.3.4 最大似然估计与最大后验估计|1.3.4 MLE 与 MAP]] — MLE→损失函数、MAP→L2 正则化
- 📄 [[../01-数学基础/1.3-概率统计/1.3.5 置信区间、分位数、假设检验|1.3.5 置信区间与假设检验]] — 分位数阈值、两类错误、AUROC 统计含义
- 📄 [[../01-数学基础/1.3-概率统计/1.3.6 稳健统计|1.3.6 稳健统计]] — Median/MAD、Huber 损失、Breakdown Point
- 📄 [[../01-数学基础/1.3-概率统计/1.3.7 Mahalanobis距离与协方差收缩|1.3.7 Mahalanobis 与收缩]] — 样本协方差的统计问题、Shrinkage、Ledoit-Wolf
- 📄 [[../01-数学基础/1.3-概率统计/1.3.8 偏差—方差权衡|1.3.8 偏差—方差权衡]] — 测试误差分解、过拟合/欠拟合诊断、双下降

### 1.4 优化
- 📂 [[../01-数学基础/1.4-优化/0-概述|概述]] — 全章概览与阅读顺序
- 📄 [[../01-数学基础/1.4-优化/1.4.1 梯度下降与随机梯度下降|1.4.1 梯度下降与 SGD]] — 下山比喻、GD/SGD/Mini-batch 变体、学习率直觉
- 📄 [[../01-数学基础/1.4-优化/1.4.2 Momentum、Adam、AdamW|1.4.2 Momentum 与 Adam]] — 惯性、自适应步长、解耦权重衰减
- 📄 [[../01-数学基础/1.4-优化/1.4.3 学习率、学习率调度与权重衰减|1.4.3 学习率与调度]] — Step/Cosine/Warmup、权重衰减=L2
- 📄 [[../01-数学基础/1.4-优化/1.4.4 凸优化与非凸优化|1.4.4 凸优化与非凸优化]] — 碗 vs 山脉、鞍点、局部极小
- 📄 [[../01-数学基础/1.4-优化/1.4.5 约束与正则化（L1与L2）|1.4.5 约束与正则化]] — L1/L2 约束几何、MAP 对应

### 1.5 信息论
- 📂 [[../01-数学基础/1.5-信息论/0-概述|概述]] — 全章概览与阅读顺序
- 📄 [[../01-数学基础/1.5-信息论/1.5.1 熵|1.5.1 熵]] — 信息量、二元熵函数、不确定性度量
- 📄 [[../01-数学基础/1.5-信息论/1.5.2 交叉熵|1.5.2 交叉熵]] — 分类损失、与熵/KL 的关系
- 📄 [[../01-数学基础/1.5-信息论/1.5.3 KL散度|1.5.3 KL 散度]] — 分布差距、不对称性、蒸馏/VAE 应用
- 📄 [[../01-数学基础/1.5-信息论/1.5.4 互信息|1.5.4 互信息]] — 共享信息、文氏图、表征学习目标
- 📄 [[../01-数学基础/1.5-信息论/1.5.5 信息瓶颈|1.5.5 信息瓶颈]] — 压缩+保留、漏斗结构、泛化解释

---

## 02-Python与PyTorch

### 2. Python、科学计算与数据工具
- Python 语法、函数、类、迭代器、上下文管理器
- 类型标注、异常处理、日志
- NumPy：数组、广播、索引、向量化
- SciPy：滤波、插值、统计与信号处理
- pandas：表格、元数据和实验结果整理
- Matplotlib / Seaborn：热图、曲线、分布和对比图
- scikit-learn：PCA、协方差、聚类、SVM、指标
- OpenCV / scikit-image：对齐、滤波、形态学、连通域
- 配置文件、命令行参数、随机种子和目录规范
- Git 基础、环境管理与依赖锁定

### 3. PyTorch 与深度学习训练闭环
- Tensor、dtype、shape、device 与自动微分
- Dataset、DataLoader、采样器与批处理
- nn.Module、参数、缓冲区、训练/评估模式
- 损失函数、优化器、学习率调度器
- 训练循环、梯度清零、反向传播与梯度裁剪
- checkpoint、断点续训和推理模式
- GPU、显存、混合精度、性能分析
- Hook 与中间特征提取
- 单元测试、shape 测试与数值稳定性

---

## 03-神经网络基础

### 4. 神经网络基础
- 感知机、MLP 与通用逼近
- 前向传播与反向传播
- 激活函数：ReLU、LeakyReLU、GELU、SiLU
- 损失函数：MSE、MAE、Smooth L1、交叉熵、Focal、Dice
- 初始化：Xavier、Kaiming
- 正则化：权重衰减、Dropout、数据增强、Early Stopping
- Normalization：BatchNorm、LayerNorm、GroupNorm、InstanceNorm
- 欠拟合、过拟合、数据泄漏与分布偏移
- 校准、不确定性与阈值

---

## 04-卷积神经网络

### 5. 卷积神经网络（CNN）
- 二维卷积、卷积核、通道、特征图
- Padding、Stride、Dilation、Pooling
- 感受野与有效感受野
- 深度可分离卷积、分组卷积、1×1 卷积
- 残差连接、跳跃连接与特征复用
- 多尺度特征与特征金字塔
- 上采样、反卷积与插值
- CNN 架构演化：LeNet / AlexNet / VGG → ResNet / DenseNet → Inception / EfficientNet → MobileNet / ShuffleNet → ConvNeXt
- 小目标与低分辨率条件下的下采样问题
- 📄 [[../04-卷积神经网络/CBAM|CBAM]] — 通道注意力 + 空间注意力（特征增强）

---

## 05-经典视觉与图像处理

### 6. 经典计算机视觉与图像处理
- 滤波：均值、高斯、中值、双边滤波
- 一阶/二阶导数：Sobel、Scharr、Laplacian
- 形态学：腐蚀、膨胀、开闭运算
- 阈值、连通域、轮廓和区域属性
- 模板匹配、互相关与图像配准
- 特征点与几何变换的基本概念
- 结构张量、方向性、纹理描述

---

## 06-分类检测分割

### 7. 分类、检测与分割
- 图像分类与多标签分类
- 目标检测：anchor、IoU、NMS；Faster R-CNN、YOLO、DETR
- 语义分割、实例分割与异常分割
- FCN、U-Net、DeepLab、FPN
- BCE、Focal、Dice、Tversky 损失
- 类别不平衡与小目标召回
- 数据增强、标注质量与标签噪声

---

## 07-迁移学习与度量学习

### 8. 迁移学习与深度特征
- 预训练、冻结、微调和线性探测
- 浅层纹理特征与深层语义特征
- 领域偏移与领域适配
- 特征归一化、降维、可视化（t-SNE / UMAP）
- Hook 提取多尺度特征
- ImageNet 预训练的优势与限制

### 9. 度量学习
- 欧氏距离、余弦距离、Mahalanobis 距离
- Siamese Network
- Contrastive Loss、Triplet Loss
- Hard / Semi-hard Negative Mining
- Prototypical Network
- Center Loss 与 ArcFace 思想
- kNN、原型与记忆库

---

## 08-对比学习与自监督

### 10. 对比学习
- 正样本、负样本与数据增强
- InfoNCE 与温度系数
- SimCLR、MoCo
- BYOL、SimSiam、Barlow Twins、VICReg
- 表征坍缩及避免方法
- 全局对比与 patch 级对比

### 11. 自监督学习
- 旋转、拼图、上下文预测等早期代理任务
- 去噪、遮挡恢复、inpainting
- Masked Image Modeling 与 MAE
- 自蒸馏：DINO 思想
- 多尺度预测、局部—全局一致性
- 预文本任务与目标任务一致性

---

## 09-自编码器体系

### 12. 自编码器体系
- 基础 AE、卷积 AE
- Denoising AE
- Sparse AE、Contractive AE
- U-Net 式重建与跳跃连接
- VAE、β-VAE、潜变量概率
- 重建误差、潜变量距离与多尺度误差
- 异常泛化、恒等映射与过强解码器
- 感知损失、梯度损失、SSIM 和频域损失

---

## 10-概率与生成模型

### 13. 概率密度估计与 Normalizing Flow
- 参数/非参数密度估计
- 高斯、GMM、KDE
- 变量变换公式、Jacobian 行列式
- 可逆网络与 Normalizing Flow
- RealNVP、Glow 的基本思想
- 特征空间 Flow：FastFlow、CFLOW-AD、CS-Flow
- 似然与语义异常不一致的问题

### 14. GAN 与生成式异常检测
- Generator、Discriminator、对抗损失
- 训练不稳定、模式崩溃
- DCGAN、WGAN、WGAN-GP
- AnoGAN、f-AnoGAN、GANomaly、Skip-GANomaly
- 生成质量与异常检测性能并不等价

### 15. Diffusion 与 Score-based Model
- 前向加噪与反向去噪
- DDPM、噪声调度、采样
- Score Matching 与 SDE 直觉
- 条件扩散、潜空间扩散
- 扩散重建异常检测
- 扩散中间特征与异常定位
- 采样速度、重建偏差与计算成本

---

## 11-异常检测基础

- 📄 [[../11-异常检测基础/距离度量在异常检测中的应用|距离度量在异常检测中的应用]] — 欧氏→PatchCore / Mahalanobis→PaDiM

### 16. 异常检测基础与评价
- 点异常、上下文异常、集合异常
- 样本级、区域级、像素级异常
- 无监督 / 半监督 / 单类 / 弱监督 / 全监督
- novelty detection 与 outlier detection
- AUROC、AUPR、F1、IoU、Dice、PRO
- 固定误报率下的召回率
- 阈值、校准、极值理论和置信区间
- 数据污染、分布漂移、开放集
- 图像级分数聚合：max、Top-k、连通区域

### 17. 经典统计与单类学习
- z-score、Median/MAD 与稳健阈值
- PCA、Kernel PCA、Robust PCA
- 低秩 + 稀疏分解
- One-Class SVM
- Isolation Forest、LOF
- Deep SVDD、Hypersphere Learning
- FCDD 与全卷积异常热图
- 特征坍缩与防止策略

---

## 12-工业异常检测

### 18. 特征记忆库与分布建模
- **SPADE** — 图像级最近邻与像素级特征匹配
- **PaDiM** — 多层 patch 特征 / 位置高斯分布 / Mahalanobis 分数 / 协方差问题
- **PatchCore** — Memory Bank / 最近邻 / Coreset Sampling / 图像级与像素级分数
- **CFA、SimpleNet** — 特征适配 / 人工异常特征与判别边界

### 19. 教师—学生蒸馏与工业方法
- 传统知识蒸馏：logit、soft target、温度系数
- 特征蒸馏、关系蒸馏
- 冻结教师、训练学生和特征归一化
- STFPM：多尺度特征金字塔匹配
- Reverse Distillation：从深层表示恢复多尺度教师特征
- EfficientAD：轻量 Teacher–Student / 局部异常分支 / AE 全局分支 / 分数融合
- DeSTSeg 等蒸馏 + 分割方法

### 20. 重建与伪异常工业方法
- DRAEM：伪异常、重建与判别分割
- RIAD：区域遮挡与重建
- CutPaste：自监督异常分类
- NSA、MemSeg、GLASS 等伪异常思路
- 合成分布、域差距和捷径学习
- 异常形状、幅度、边缘与扩散规律

### 21. 工业异常检测的统一与前沿方法
- UniAD、INP-Former 等统一建模
- DINO / DINOv2 特征
- Dinomaly、AnomalyDINO、AnomalyVFM
- WinCLIP、AnomalyCLIP、AdaCLIP
- 逻辑异常：GCAD、ComAD、MVTec LOCO AD
- 3D/多模态异常检测的基本方向
- MVTec AD、MVTec AD 2 等数据集及其局限

---

## 13-Attention与Transformer

### 22. Attention 与 Transformer
- Query、Key、Value 与 Scaled Dot-Product Attention
- Multi-Head Attention
- 位置编码、残差和 LayerNorm
- Encoder / Decoder 结构
- ViT：Patch Embedding 和分类 token
- Swin Transformer：窗口注意力与层级结构
- DeiT、PVT 等
- MAE、DINO 等自监督 Transformer
- CNN 与 Transformer 的归纳偏置差异

---

## 14-GNN与时序模型

### 23. 图神经网络（GNN）
- 图、节点、边、邻接矩阵与图拉普拉斯
- Message Passing
- GCN、GraphSAGE、GAT
- 图池化、图级/节点级任务
- 动态图、时空图
- 过平滑与可扩展性

### 24. 时序模型与视频/连续温度场
- 滑动窗口、滞后特征和时间切分
- RNN、LSTM、GRU
- Temporal CNN、TCN
- 3D CNN、ConvLSTM
- 时间序列 Transformer（Autoformer、PatchTST）
- Anomaly Transformer、TranAD 等异常方法
- 预测式、重建式和变化点检测

---

## 15-频域与物理信息

### 25. 频域、小波与多尺度信号方法
- 傅里叶变换、频谱、卷积定理
- 低通、高通、带通与频域滤波
- STFT（用于时序）
- 小波变换、离散小波、多尺度分解
- Laplacian Pyramid、Gaussian Pyramid
- 可学习滤波器、Wavelet CNN
- 频域损失与频域神经网络
- Fourier Neural Operator（FNO）基础

### 26. 物理信息神经网络与神经算子
- 常微分方程与偏微分方程基础
- 热传导方程、扩散方程和边界条件
- PINN：数据损失 + PDE 残差 + 边界损失
- 自动微分求空间/时间导数
- 逆问题与参数辨识
- DeepONet、FNO 等神经算子
- 模型误差、边界误差和物理假设失配

---

## 16-多模态与基础模型

### 27A. 自然语言处理（NLP）
- 文本清洗、分词、词表与 Tokenizer
- One-hot、Word2Vec、GloVe 与上下文表示
- RNN、LSTM、GRU 和 Seq2Seq
- Attention 与 Encoder–Decoder
- Transformer 语言模型
- BERT 式掩码语言模型与 GPT 式自回归模型
- 文本分类、序列标注、信息抽取、检索与生成
- 指令微调、Prompt、RAG 和工具调用
- 幻觉、评测、安全与结构化输出

### 27B. 语音、音频与一维信号
- 采样率、混叠、窗函数与频谱
- STFT、梅尔频谱和 MFCC
- 1D CNN、TCN、RNN 与音频 Transformer
- 语音识别、音频分类和声学事件检测
- 自监督语音表示的基本思想
- 振动、电流、压力等工业信号建模

### 27. 多模态学习
- 早期融合、中期融合和后期融合
- 特征对齐、Cross-Attention
- 缺失模态与模态可靠性
- CLIP 式图文对比学习
- 多传感器校准与时间同步
- 多模态异常分数融合

### 28. 基础模型与迁移能力
- Foundation Model 与 Scaling 基本概念
- DINOv2、SAM、CLIP 等视觉基础模型
- Prompt、Adapter、LoRA
- 线性探测、全量微调和参数高效微调
- Zero-shot、Few-shot 与开放词汇
- 域专用基础模型

---

## 17-模型压缩与部署

### 29. 模型压缩与高效网络
- 参数量、FLOPs、吞吐和端到端延迟
- 剪枝：结构化 / 非结构化
- 量化：PTQ、QAT、INT8
- 知识蒸馏用于模型压缩
- 低秩分解、权重共享
- MobileNet、EfficientNet、轻量 Attention
- 精度—速度—内存权衡

### 30. 模型导出与部署
- TorchScript 基础
- ONNX 导出、shape 与算子兼容
- ONNX Runtime
- TensorRT：精度模式、动态 shape、校准
- CPU / GPU / 边缘设备推理
- C++ / Python 接口与服务化
- 前处理和后处理一致性
- 版本管理、回滚和灰度验证

---

## 18-实验管理与MLOps

### 31. 实验管理、复现与软件工程
- 配置驱动实验
- Git 分支、commit 和代码审查
- 随机种子与确定性
- 数据版本、模型版本和指标版本
- TensorBoard、MLflow、Weights & Biases
- 单元测试、集成测试、数据测试
- 消融实验、超参数搜索
- 环境锁定、容器与 CI
- 论文阅读、复现记录和实验日志

### 32. 工业数据与系统工程
- 传感器原理、标定、发射率与表观温度
- 主动近红外反射与被动热红外的区别
- 坏点、非均匀性校正、漂移和噪声
- 数据采集、时间同步、触发和丢帧
- ROI 定位、对齐、有效区域 mask
- 工艺参数、批次与环境变量
- 阈值策略、滞回、连续帧确认
- 在线监控、数据漂移、告警和回退
- 人机复核、误报成本与漏报成本
- 模型更新、再验证和审计

### 33. MLOps、监控与持续改进
- 离线训练与在线推理流程
- 数据漂移、概念漂移与标签延迟
- 输入质量、分数分布和误报率监控
- 阈值版本与模型版本
- Champion–Challenger
- 灰度发布、A/B 测试和回滚
- 主动学习与难例回流
- 安全、权限、日志和审计

---

## 19-拓展知识

### 34. 因果、领域泛化与不确定性
- 相关与因果的区别
- 数据偏差与捷径学习
- Domain Adaptation、Domain Generalization
- 数据增强与不变性
- Deep Ensemble、MC Dropout
- OOD 检测与置信度校准

### 35. 强化学习、LLM 与 Agent（拓展）
- 强化学习：状态、动作、奖励、策略、价值
- DQN、Policy Gradient、Actor–Critic 的基本思想
- Transformer 语言模型、预训练与指令微调
- RAG、工具调用、Agent 工作流
- LoRA 等参数高效微调

---

## 20-项目实践

### 35A. 通用深度学习项目阶梯
- 项目 1：从零实现训练闭环（NumPy → PyTorch）
- 项目 2：图像分类（小型 CNN、ResNet、迁移学习）
- 项目 3：目标检测或语义分割（二选一深入）
- 项目 4：表征学习（AE/对比学习编码器 + 线性探测）
- 项目 5：Transformer（手写 Attention + 小型 ViT）
- 项目 6：生成模型（VAE + 小型 Diffusion）
- 项目 7：跨模态或序列项目（NLP/时序/音频/GNN 选一）
- 项目 8：部署与工程（ONNX 导出 + 实验追踪 + 回归测试）

### 36. 温度异常检测专项项目阶梯
- 项目 1：统计与数据基线（Median/MAD、PCA、Mahalanobis）
- 项目 2：多尺度结构 PCA（梯度/Laplacian/多尺度残差 + Patch PCA）
- 项目 3：小型去噪 AE（skip 结构对比 + 压力测试）
- 项目 4：伪异常分割（物理伪异常生成器 + 小型 U-Net）
- 项目 5：温度自监督编码器（遮挡恢复/VICReg/SimSiam → PCA/PaDiM/PatchCore）
- 项目 6：教师—学生与 EfficientAD（多教师来源对比）
- 项目 7：Transformer 或时序扩展（CNN-Attention / Swin / ConvLSTM）
- 项目 8：部署闭环（ONNX/TensorRT + 影子运行 + 监控）

### 37. 推荐实验矩阵
- B0 Median/MAD · B1 多尺度整图 PCA · B2 多尺度 Patch PCA
- D1 去噪 AE · D2 结构 AE · D3 伪异常 U-Net
- F1 PaDiM · F2 PatchCore
- T1 STFPM 式蒸馏 · T2 EfficientAD 改造
- A1 CNN-Attention · S1 ConvLSTM/TCN

---

## 21-学习计划与检查清单

### 38. 12～24 个月参考节奏
- 第 1～2 月：基础补齐（数学、Python、PyTorch）
- 第 3～4 月：CNN 与经典视觉
- 第 5～6 月：表征与重建
- 第 7～9 月：自监督与 Transformer
- 第 10～12 月：生成模型与序列
- 第 13～15 月：选择一个应用方向深入
- 第 16～18 月：扩展知识边界
- 第 19～24 月：部署与研究深化

### 39. 三条可选深度路线
- 路线 A：计算机视觉与工程落地
- 路线 B：生成式 AI 与多模态
- 路线 C：异常检测与物理场专项

### 40. 论文阅读方法 — 阅读时回答的 12 个问题
### 41. 复现开源项目的 8 个步骤

### 42. 基础能力检查清单
- PCA 重建 · 梯度下降/反向传播 · PyTorch 训练循环 · shape/dtype/device 调试 · 数据泄漏识别

### 43. 视觉与表征能力检查清单
- CNN 感受野计算 · 低分辨率 stride 选择 · 单通道/多通道设计 · 多尺度特征可视化 · 增强物理语义验证

### 44. 异常检测能力检查清单
- 样本/区域/像素级区分 · PatchCore/PaDiM 从零实现 · Teacher–Student vs AE · 伪异常差距评价 · 固定误报召回 · 阈值稳定性

### 45. 工程能力检查清单
- 版本管理 · 实验复现/报告 · ONNX 导出/验证 · P95/P99 延迟 · 上线监控/灰度/回滚

### 46. 温度异常检测专项执行顺序（10 步行动建议）
