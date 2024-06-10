import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
# 假设这是您的数据
data = np.random.randn(1000).cumsum()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(data)

# 设置刻度位置
ax.set_xticks([0, 250, 500, 750, 1000])

# 设置刻度标签，并可选择旋转角度和字体大小
ax.set_xticklabels(['开始', '第一阶段', '中间', '第二阶段', '结束'], rotation=30, fontsize='small')

plt.show()
