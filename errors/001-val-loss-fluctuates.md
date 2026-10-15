# 验证集指标每次跑都不一样

> 日期：2026-__-__ ｜ 卡了 40 分钟 ｜ 关键词：`model.eval` `BatchNorm` `Dropout` `复现`

## 环境

- Python 3.11 / PyTorch 2.x / 单卡
- 运行方式：固定了随机种子后仍不稳定

## 报错原文

没有报错，是**结果不对**——同一个模型权重，验证准确率在 0.87 到 0.91 之间跳。这类问题比报错更难查。

## 原因

验证阶段没有调用 `model.eval()`。后果有两个：

1. **Dropout 还在随机丢弃神经元**，每次前向的输出都不同。
2. **BatchNorm 还在用当前 batch 的均值/方差**，而不是训练时累积的全局统计量。验证 batch 越小，波动越大。

固定 `torch.manual_seed` 不足以解决，因为 DataLoader 多进程、cuDNN 非确定性算法都会引入随机性。

## 解法

```python
@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()          # ← 关键的一行
    ...
```

排查顺序（以后照这个顺序走）：

1. 验证前有没有 `model.eval()`，训练前有没有 `model.train()`。
2. 验证有没有包在 `torch.no_grad()` 里。
3. DataLoader 的 `shuffle` 在验证集上是不是 `False`。
4. 需要完全确定时再打开 `cudnn.deterministic = True`。

## 一句话教训

**`model.train()` / `model.eval()` 不是可选项，是训练循环的固定组成部分。** 写训练脚本时先把这两个调用写上，再写别的。
