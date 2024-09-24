import matplotlib.pyplot as plt
import numpy as np

# 假设 tideO 是一个包含海浪高度数据的数组
# 这里我们用随机数据来模拟 tideO
tideO= np.random.rand(20)  # 生成20个随机数作为示例数据

# x -> 24小时，y -> 海浪高度
x = np.arange(20)
y = tideO

# 用 matplotlib 绘制图表
fig, ax = plt.subplots()
ax.plot(x, y)

# 进行一下美化，比如添加标题
ax.set_title("Tide Height in Oct 1st")
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Tide Height (meters)")

# 显示图表
plt.show()