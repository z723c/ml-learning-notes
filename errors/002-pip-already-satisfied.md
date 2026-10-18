# pip 说 already satisfied，但其实没装

> 2026-10-18 ｜ `pip` `torch` `cuda` `force-reinstall`

**现象**：换 CUDA 版 torch 时 pip 回 `Requirement already satisfied: torch==2.5.1`，但 `torch.cuda.is_available()` 仍是 `False`。

**原因**：CPU 版和 CUDA 版的 wheel **版本号相同**（都是 `2.5.1`）。pip 只比对版本号，不比对构建；`--index-url` 不会强制重装。下面解法里 `--force-reinstall` 负责忽略"已满足"，`--no-deps` 只换这三个包、不动 numpy 等依赖。

**解法**：

```powershell
python -m pip install --index-url https://download.pytorch.org/whl/cu124 --force-reinstall --no-deps torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1
```

**判据**：

| 检查 | CPU 版 | CUDA 版 |
|---|---|---|
| `pip show torch` | `2.5.1` | `2.5.1+cu124` |
| `torch.version.cuda` | `None` | `12.4` |
| `pip list` 里的 `nvidia-*` | 无 | 有 |

**教训**：换构建 / 换 wheel 来源时，"版本满足" ≠ "装对了"，一律加 `--force-reinstall`。

**附**：第一次 GPU 运算含 cuBLAS 初始化，测速必须先预热，否则会测出"GPU 比 CPU 慢"。
