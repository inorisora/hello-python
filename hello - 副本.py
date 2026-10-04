# 第一跳：环境验收小脚本
# 目标：确认 py312 工作间完整可用（解释器 / numpy / matplotlib 出图）
import sys

import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0, 2 * np.pi, 200)
plt.plot(x, np.sin(x))
plt.title("First step!")
plt.savefig("first_plot.png", dpi=120)
print("Saved first_plot.png - environment is ready!")
