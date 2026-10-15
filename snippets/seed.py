"""固定随机种子，保证实验可复现。

用法：
    from seed import set_seed
    set_seed(42)
"""
import os
import random

import numpy as np


def set_seed(seed: int = 42) -> None:
    """固定 Python / numpy / torch 的随机源。

    注意：cudnn.deterministic=True 会牺牲一部分速度换取可复现性。
    只有在"结果对不上、需要排查"时才打开，日常训练可以注释掉这两行。
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

    try:
        import torch
    except ImportError:
        return

    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    # torch.backends.cudnn.deterministic = True
    # torch.backends.cudnn.benchmark = False
