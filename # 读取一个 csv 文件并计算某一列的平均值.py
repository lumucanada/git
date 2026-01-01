# 使用 pandas 读取 data.csv
# 计算列名为 value 的平均值
import pandas as pd

df = pd.read_csv('data.csv')
average_value = df['value'].mean()
print(average_value)


print(f"Average value is {average_value}")

sss