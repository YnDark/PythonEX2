# 导包
import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决符号不显示问题
plt.rcParams['axes.unicode_minus'] = False

# 导入数据
df = pd.read_csv(r"D:\杨定鑫\Documents\py实验2\实验2\实验2\ETTh1.csv")
print(df)

# 计算每周油温的均值，绘制折线图和散点图。

# 计算每周油温的均值
## 使用isocalendar()获取周数
df['date'] = pd.to_datetime(df['date'])
df['year_week'] = df['date'].dt.strftime('%Y-%V')
df.to_csv("allData.csv")

## 计算每周油温的均值
OT_Mean = df.groupby(['year_week']).mean().reset_index()
print(OT_Mean)

# 绘制折线图
## 设置画布大小
fig = plt.figure(figsize=(10, 9))

plt.plot(OT_Mean['year_week'], OT_Mean['OT'])

## 设置刻度和x标签
plt.xticks(ticks=range(0, len(OT_Mean['year_week']), 5), labels=OT_Mean['year_week'][::5], rotation=90)

## 设置标题
plt.title('平均油温图', fontsize=20, loc='center', pad=1.5)

## 设置坐标轴标题
plt.xlabel("年份-第几周", fontsize=13, loc='center', labelpad=15)
plt.ylabel("平均油温", fontsize=13, loc='center', labelpad=15)

plt.show()

# 绘制散点图
## 设置画布大小
fig = plt.figure(figsize=(10, 9))

plt.plot(OT_Mean['year_week'], OT_Mean['OT'], 'ro', mfc='w')

## 设置刻度和x标签
plt.xticks(ticks=range(0, len(OT_Mean['year_week']), 5), labels=OT_Mean['year_week'][::5], rotation=90)

## 设置标题
plt.title('平均油温图', fontsize=20, loc='center', pad=1.5)

## 设置坐标轴标题
plt.xlabel("年份-第几周", fontsize=13, loc='center', labelpad=15)
plt.ylabel("平均油温", fontsize=13, loc='center', labelpad=15)

plt.show()

# 计算高有效负载、中间有效负载和低有效负载三列数据，按年份进行统计均值、最大值、最小值，使用多柱状图绘制展示。
df['year'] = df['date'].dt.strftime('%Y')
print(df)

# 按年统计均值、最大值、最小值
data = df.groupby(['year']).agg(
    {'HUFL': {'mean', 'max'}, 'MUFL': {'mean', 'max'}, 'LUFL': {'mean', 'max'}}).reset_index()

# 使用多柱状图展示
## 获取数据
year = data['year']
intYear = year.astype(int)
HUFL = data['HUFL']
MUFL = data['MUFL']
LUFL = data['LUFL']
print(year)
print(HUFL)

## 设置画布大小
fig = plt.figure(figsize=(12, 9))

## 平均值绘制柱状图
width = round(1.0 / (len(intYear) * 2), 1)
plt.bar(intYear + width, HUFL['mean'], width, label='HUFL')
plt.bar(intYear, MUFL['mean'], width, label='MUFL')
plt.bar(intYear - width, LUFL['mean'], width, label='LUFL')

## 设置x轴刻度
plt.xticks(ticks=range(intYear[0] + 0, intYear[0] + len(intYear)), labels=year+"年")

## 设置轴标签
plt.xlabel('年份', fontsize=13, loc='center', labelpad=15)
plt.ylabel('平均值', fontsize=13, loc='center', labelpad=15)

## 设置标题
plt.title('均值图像', fontsize=20, loc='center', pad=1.5)

## 设置图例
plt.legend(['HUFL', 'MUFL', 'LUFL'],loc='upper right')

## 设置柱状图标识
for a, b in zip(intYear + width, HUFL['mean']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear, MUFL['mean']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear - width, LUFL['mean']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

## 展示柱状图
plt.show()

## 设置画布大小
fig = plt.figure(figsize=(12, 9))

## 最大值绘制柱状图
plt.bar(intYear + width, HUFL['max'], width, label='HUFL')
plt.bar(intYear, MUFL['max'], width, label='MUFL')
plt.bar(intYear - width, LUFL['max'], width, label='LUFL')

## 设置x轴刻度
plt.xticks(ticks=range(intYear[0] + 0, intYear[0] + len(intYear)), labels=year+"年")

## 设置轴标签
plt.xlabel('年份', fontsize=13, loc='center', labelpad=15)
plt.ylabel('最大值', fontsize=13, loc='center', labelpad=15)

## 设置标题
plt.title('最大值图像', fontsize=20, loc='center', pad=1.5)

## 设置图例
plt.legend(['HUFL', 'MUFL', 'LUFL'], loc='upper right')

## 设置柱状图标识
for a, b in zip(intYear + width, HUFL['max']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear, MUFL['max']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear - width, LUFL['max']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

plt.show()

# 对油温数据，绘制直方图。自己按照最大、最小值划分区间。