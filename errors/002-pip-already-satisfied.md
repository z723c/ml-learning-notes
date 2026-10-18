# pip 说 already satisfied，但其实没装

> 2026-10-18 ｜ `pip` `torch` `cuda` `force-reinstall`

**现象**：换 CUDA 版 torch 时 pip 回 `Requirement already satisfied: torch==2.5.1`，但 `torch.cuda.is_available()` 仍是 `False`。

**原因**：CPU 版和 CUDA 版的 wheel **版本号相同**（都是 `2.5.1`）。pip 只比对版本号，不比对构建；`--index-url` 不会强制重装。

**解法**：

```powershell
python -m pip install --index-url https://download.pytorch.org/whl/cu124 --force-reinstall --no-deps torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1

--force-reinstall 忽略"已满足"；--no-deps 只换这三个包，不动 numpy 等依赖。
换构建 / 换 wheel 来源时，"版本满足" ≠ "装对了"，一律加 --force-reinstall