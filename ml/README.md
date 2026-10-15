# 机器学习与深度学习

每个主题一个子目录，命名 `编号-主题`，例如：

```
ml/
├── 01-ml-basics/        # 监督/无监督、偏差方差、过拟合
├── 02-linreg-logreg/    # 线性回归、逻辑回归、梯度下降
├── 03-mlp/              # 多层感知机、激活函数、正则化
├── 04-cnn/              # 卷积、池化、LeNet / VGG / ResNet
├── 05-training-tricks/  # 初始化、BN、Dropout、学习率调度、微调
├── 06-optimizers/       # SGD / Momentum / Adam
└── 07-transformer/      # 注意力、多头、位置编码
```

每个子目录放两个文件：

- `notes.md` —— 从 [`templates/notes.md`](../templates/notes.md) 复制
- `*.py` —— **不看教程重写一遍**的实现代码（这是分辨"真懂"和"跟着敲"的唯一标准）
