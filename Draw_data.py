# -*- coding: utf-8 -*
import time

import matplotlib.pyplot as plt
import matplotlib as mpl

# import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 图中文字体设置为黑体
mpl.rcParams['font.serif'] = ['KaiTi']
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

if __name__ == "__main__":
    # 对比算法
    x = []
    y = []
    z = []

    plt.plot(x, y, label="Negative spread value", color="red", linewidth=1)

    plt.xlabel("正种子选取算法")

    plt.xticks(x)

    plt.title("影响力扩展度随种子集合变化(1000次实验平均值)")

    plt.legend()
    plt.grid()
    # 设置每个点上的数值
    for i in range(6):
        plt.text(x[i], y[i], y[i], fontsize=8, color="red", style="italic", weight="light",
                 verticalalignment='center', horizontalalignment='center', rotation=45)

    plt.savefig(f"./result/对比算法result {time.strftime('%Y-%m-%d %H_%M_%S')}.png")
    plt.show()
