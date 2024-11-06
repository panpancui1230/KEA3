import matplotlib.pyplot as plt
import pandas as pd
# read data
data_100 = pd.read_csv('./logs/combined_100_simulated_new.csv')
# data_500 = pd.read_csv('./logs/combined_500_simulated_new.csv')

# 绘制 NPQ vs idx
plt.figure(figsize=(10, 8))

# 100 光强下的 NPQ vs idx
plt.plot(data_100['idx'], data_100['Phi2'], label='Light Intensity 100', marker='o', linestyle='-')

# 500 光强下的 NPQ vs idx
# plt.plot(data_500['idx'], data_500['Phi2'], label='Light Intensity 500', marker='o', linestyle='-')

# plt.plot(data_100['idx'][:1000], data_100['Phi2'][:1000], label='Light Intensity 100', marker='o', linestyle='-')


# 图例、标题和标签
plt.xlabel('Index (idx)')
plt.ylabel('Phi2')
plt.title('Phi2')
plt.legend()
plt.grid(False)
plt.show()