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
## 计算每周油温的均值
df['date'] = pd.to_datetime(df['date'])
df['year_week'] = df['date'].dt.strftime('%Y-%V')
OT_Mean = df.groupby(['year_week']).mean().reset_index()
print(OT_Mean[['year_week', 'OT']])

# 绘制折线图
## 设置画布大小
fig = plt.figure(figsize=(11, 9))
plt.plot(OT_Mean['year_week'], OT_Mean['OT'], color='black')

## 设置图例
plt.legend(("平均油温",))

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
fig = plt.figure(figsize=(11, 9))

plt.plot(OT_Mean['year_week'], OT_Mean['OT'], 'ro', mfc='w')

## 设置刻度和x标签
plt.xticks(ticks=range(0, len(OT_Mean['year_week']), 5), labels=OT_Mean['year_week'][::5], rotation=90)

## 设置图例
plt.legend(("平均油温",), loc='best')

## 设置标题
plt.title('平均油温图', fontsize=20, loc='center')

## 设置坐标轴标题
plt.xlabel("年份-第几周", fontsize=13, loc='center', labelpad=15)
plt.ylabel("平均油温", fontsize=13, loc='center', labelpad=15)

plt.show()

# 计算高有效负载、中间有效负载和低有效负载三列数据，按年份进行统计均值、最大值、最小值，使用多柱状图绘制展示。
df['year'] = df['date'].dt.strftime('%Y')
print(df)

## 按年统计均值、最大值、最小值
data = df.groupby(['year']).agg(
    {'HUFL': {'mean', 'min', 'max'}, 'MUFL': {'mean', 'min', 'max'}, 'LUFL': {'mean', 'min', 'max'}}).reset_index()
print(data)

## 使用多柱状图展示
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
plt.bar(intYear + width, HUFL['mean'], width, label='HUFL', color='orange')
plt.bar(intYear, MUFL['mean'], width, label='MUFL', color='blue')
plt.bar(intYear - width, LUFL['mean'], width, label='LUFL', color='green')

## 设置x轴刻度
plt.xticks(ticks=range(intYear[0] + 0, intYear[0] + len(intYear)), labels=year + "年")

## 设置轴标签
plt.xlabel('年份', fontsize=13, loc='center', labelpad=15)
plt.ylabel('平均值', fontsize=13, loc='center', labelpad=15)

## 设置标题
plt.title('均值图像', fontsize=20, loc='center', pad=1.5)

## 设置图例
plt.legend(['HUFL', 'MUFL', 'LUFL'], loc='best')

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
plt.bar(intYear + width, HUFL['max'], width, label='HUFL', color='orange')
plt.bar(intYear, MUFL['max'], width, label='MUFL', color='blue')
plt.bar(intYear - width, LUFL['max'], width, label='LUFL', color='green')

## 设置x轴刻度
plt.xticks(ticks=range(intYear[0] + 0, intYear[0] + len(intYear)), labels=year + "年")

## 设置轴标签
plt.xlabel('年份', fontsize=13, loc='center', labelpad=15)
plt.ylabel('最大值', fontsize=13, loc='center', labelpad=15)

## 设置标题
plt.title('最大值图像', fontsize=20, loc='center', pad=1.5)

## 设置图例
plt.legend(['HUFL', 'MUFL', 'LUFL'], loc='best')

## 设置柱状图标识
for a, b in zip(intYear + width, HUFL['max']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear, MUFL['max']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear - width, LUFL['max']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

plt.show()

## 设置画布大小
fig = plt.figure(figsize=(12, 9))

## 最小值绘制柱状图
plt.bar(intYear + width, HUFL['min'], width, label='HUFL', color='orange')
plt.bar(intYear, MUFL['min'], width, label='MUFL', color='blue')
plt.bar(intYear - width, LUFL['min'], width, label='LUFL', color='green')

## 设置x轴刻度
plt.xticks(ticks=range(intYear[0] + 0, intYear[0] + len(intYear)), labels=year + "年")

## 设置轴标签
plt.xlabel('年份', fontsize=13, loc='center', labelpad=15)
plt.ylabel('最小值', fontsize=13, loc='center', labelpad=15)

## 设置标题
plt.title('最小值图像', fontsize=20, loc='center', pad=1.5)

## 设置图例
plt.legend(['HUFL', 'MUFL', 'LUFL'], loc='best')

## 设置柱状图标识
for a, b in zip(intYear + width, HUFL['min']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear, MUFL['min']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

for a, b in zip(intYear - width, LUFL['min']):
    plt.text(a, b, format(round(b, 1), ','), ha='center', va='bottom', fontsize=11)

plt.show()

# 对油温数据，绘制直方图。自己按照最大、最小值划分区间。
## 计算区间个数
OT_max = df['OT'].max()
OT_min = df['OT'].min()
bins = int(OT_max - OT_min)
print(OT_max)
print(OT_min)

## 设置画布大小
fig = plt.figure(figsize=(12, 9))

## 绘图
plt.hist(df['OT'], bins=bins, color='gray')

## 设置标题
plt.title("油温直方图")

## 设置图例
plt.legend(("油温出现次数",))

## 设置标签
plt.xlabel('油温')
plt.ylabel('出现次数')

plt.show()

# 对油温数据进行统计，绘制饼图。分为10个，将最大、最小区域分裂，并添加阴影效果。再加一列数据，绘制双环型图。
#plt.pie(df['OT'])
#plt.show()


# 对高无效负载、中间无效负载和低无效负载三列数据，绘制箱型图
HULL = df['HULL']
MUFL = df['MUFL']
LULL = df['LULL']

plt.boxplot([HULL, MUFL, LULL],
            whis=1.5,
            labels=['HULL', 'MUFL', 'LULL'],
            showmeans=True
            , flierprops={'markerfacecolor': 'red', 'markeredgecolor': 'red', 'markersize': 3}
            , meanprops={'markerfacecolor': 'black', 'markeredgecolor': 'black', 'markersize': 8, 'marker': 'h'}
            , medianprops={'linestyle': '--', 'color': 'orange'})

## 设置标题
plt.title("高无效负载、中间无效负载、低无效负载箱型图")

## 设置图例
plt.legend(["上下限", "平均值", "上下限"])

## 设置坐标轴标签
plt.xlabel("数据类型")
plt.ylabel("对应数据大小")

plt.show()
# 计算上四分位数和下四分位数
Q1_HULL = HULL.quantile(0.25)
Q2_HULL = HULL.quantile(0.75)

Q1_MUFL = MUFL.quantile(0.25)
Q2_MUFL = MUFL.quantile(0.75)

Q1_LULL = LULL.quantile(0.25)
Q2_LULL = LULL.quantile(0.75)

# 基于1.5倍四分位差计算上下限对应值
low_limit_HULL = Q1_HULL - 1.5 * (Q2_HULL - Q1_HULL)
high_limit_HULL = Q2_HULL + 1.5 * (Q2_HULL - Q1_HULL)

low_limit_MUFL = Q1_MUFL - 1.5 * (Q2_MUFL - Q1_MUFL)
high_limit_MUFL = Q2_MUFL + 1.5 * (Q2_MUFL - Q1_MUFL)

low_limit_LULL = Q1_LULL - 1.5 * (Q2_LULL - Q1_LULL)
high_limit_LULL = Q2_LULL + 1.5 * (Q2_LULL - Q1_LULL)

# 寻找异常值
val_HULL = df['HULL'][(df['HULL'] > high_limit_HULL) | (df['HULL'] < low_limit_HULL)]
val_MUFL = df['MUFL'][(df['MUFL'] > high_limit_MUFL) | (df['MUFL'] < low_limit_MUFL)]
val_LULL = df['LULL'][(df['LULL'] > high_limit_LULL) | (df['LULL'] < low_limit_LULL)]

print("异常值如下")
print("val_HULL-----------------------------")
print(val_HULL)

print("val_MUFL-----------------------------")
print(val_MUFL)

print("val_LULL-----------------------------")
print(val_LULL)

# 从高有效负载数据这列中，选择任意连续7天的数据，绘制热力图。
df[['date', 'HUFL']].map( )

## 绘制热力图
plt.imshow([HUFL])

## 显示颜色条
plt.colorbar()

## 设置两轴刻度
plt.xticks(range(6), df['date'][1000:1006], rotation=90)
plt.yticks([0], ["HUFL"])

## 设置标题
plt.title("HUFL其中连续七天数据热力图")

## 设置两轴标签
plt.xlabel("时间")

plt.show()

# 选取高无效负载、中间无效负载和低无效负载三列数据，绘制2行2列的多子图
HUFL = df['HUFL'][0:100]
MUFL = df['MUFL'][0:100]
LUFL = df['LUFL'][0:100]
date = df['date'][0:100]

print(df)
print(date)
print(HUFL)

fig = plt.figure(figsize=(20, 11))
plt.subplot(2, 2, 1)
plt.plot(date, HUFL)
#plt.xticks(rotation=90)
plt.xlabel("月份-日期 时间", fontsize=13)
plt.ylabel("HUFL", fontsize=13)

plt.subplot(2, 2, 2)
plt.hist(MUFL, bins=20)
plt.xlabel("MUFL", fontsize=13)
plt.ylabel("出现次数", fontsize=13)

plt.subplot(2, 1, 2)
plt.plot(date, LUFL, 'ro')
plt.xlabel("月份-日期 时间", fontsize=13)
plt.ylabel("LUFL", fontsize=13)

plt.show()
