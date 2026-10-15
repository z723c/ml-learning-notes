"""通用训练 / 验证循环骨架。

写这一份的目的：以后每个项目都从这里复制，不再重写。
骨架里写死的是"容易忘记但必须有的东西"，注释解释了为什么。
"""
import torch


def train_one_epoch(model, loader, optimizer, criterion, device):
    model.train()                    # 必须：启用 Dropout / BN 的训练行为
    total_loss, correct, n = 0.0, 0, 0

    for x, y in loader:
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()        # 必须：否则梯度会累加
        logits = model(x)
        loss = criterion(logits, y)

        loss.backward()
        optimizer.step()

        total_loss += loss.item() * y.size(0)
        correct += (logits.argmax(dim=1) == y).sum().item()
        n += y.size(0)

    return total_loss / n, correct / n


@torch.no_grad()                     # 必须：否则验证会建计算图、显存爆炸
def evaluate(model, loader, criterion, device):
    model.eval()                     # 必须：否则 BN 用 batch 统计量、Dropout 还在丢
    total_loss, correct, n = 0.0, 0, 0

    for x, y in loader:
        x, y = x.to(device), y.to(device)
        logits = model(x)
        loss = criterion(logits, y)

        total_loss += loss.item() * y.size(0)
        correct += (logits.argmax(dim=1) == y).sum().item()
        n += y.size(0)

    return total_loss / n, correct / n


def fit(model, train_loader, val_loader, optimizer, criterion, device,
        epochs=10, ckpt_path="best.pt"):
    """训练主循环，按验证准确率保存最优权重。"""
    best_acc = 0.0
    history = []

    for epoch in range(1, epochs + 1):
        tr_loss, tr_acc = train_one_epoch(model, train_loader, optimizer, criterion, device)
        va_loss, va_acc = evaluate(model, val_loader, criterion, device)

        history.append(dict(epoch=epoch, tr_loss=tr_loss, tr_acc=tr_acc,
                            va_loss=va_loss, va_acc=va_acc))
        print(f"[{epoch:3d}/{epochs}] train loss {tr_loss:.4f} acc {tr_acc:.4f} | "
              f"val loss {va_loss:.4f} acc {va_acc:.4f}")

        if va_acc > best_acc:
            best_acc = va_acc
            torch.save(model.state_dict(), ckpt_path)

    print(f"best val acc: {best_acc:.4f}")
    return history, best_acc
