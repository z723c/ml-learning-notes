# 环境说明

**主力环境**：`conda activate medclip`

- Python 3.9.23 ｜ torch 2.5.1+cu124 ｜ CUDA 12.4
- GPU：RTX 3050 Laptop，4 GB
- 已装：transformers, monai, numpy, pandas, sklearn, jupyter, cv2, matplotlib
- 未装：open_clip（阶段 3 需要时再装）

**三个坑**：

1. PATH 里的 `python` 是 `C:\Python314\python.exe`（3.14，空的），**不要用**
2. 装包前必须 `conda activate medclip`
3. 装包用 `python -m pip`，不要用裸 `pip`