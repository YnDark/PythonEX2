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

# 颜色设置
color1 = [142 / 255, 207 / 255, 201 / 255]
color2 = [255 / 255, 190 / 255, 122 / 255]
color3 = [250 / 255, 127 / 255, 111 / 255]

# 计算每周油温的均值，绘制折线图和散点图。
## 计算每周油温的均值
df['date'] = pd.to_datetime(df['date'])
df['year_week'] = df['date'].dt.strftime('%Y-%V')
OT_Mean = df.groupby(['year_week']).mean().reset_index()
print(OT_Mean[['year_week', 'OT']])

# 绘制折线图

## 设置画布大小
fig = plt.figure(figsize=(11, 9))
plt.plot(OT_Mean['year_week'], OT_Mean['OT'], color='black', alpha=0.5)

## 设置网格
plt.grid(True, axis='y', linestyle='--')

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
plt.bar(intYear + width, HUFL['mean'], width, label='HUFL', color=color1)
plt.bar(intYear, MUFL['mean'], width, label='MUFL', color=color2)
plt.bar(intYear - width, LUFL['mean'], width, label='LUFL', color=color3)

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
plt.bar(intYear + width, HUFL['max'], width, label='HUFL', color=color1)
plt.bar(intYear, MUFL['max'], width, label='MUFL', color=color2)
plt.bar(intYear - width, LUFL['max'], width, label='LUFL', color=color3)

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
plt.bar(intYear + width, HUFL['min'], width, label='HUFL', color=color1)
plt.bar(intYear, MUFL['min'], width, label='MUFL', color=color2)
plt.bar(intYear - width, LUFL['min'], width, label='LUFL', color=color3)

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
oil_temps = df['OT']
extra_data = df['HUFL']  # 额外的一列数据

# 计算分组边界
min_temp = oil_temps.min()
max_temp = oil_temps.max()
bins = [min_temp + (max_temp - min_temp) / 10 * i for i in range(11)]

# 为每个区间设置标签
labels = [f'{int(bins[i])}°C - {int(bins[i + 1])}°C' for i in range(len(bins) - 1)]

# 对数据进行分组并添加标签
oil_temps = pd.cut(oil_temps, bins=bins, labels=labels)
extra_data = pd.cut(extra_data, bins=bins, labels=False)

# 统计每个温度区间的频率
temp_counts = oil_temps.value_counts()
extra_counts = extra_data.value_counts()

# 准备分裂参数
explode_values = [0.1 if label in [labels[0], labels[-1]] else 0 for label in labels]


# 自定义autopct，只显示大于0%的百分比
def custom_autopct(pct):
    return ('%.1f%%' % pct) if pct > 0 else ''


# 绘制饼图
plt.figure(figsize=(12, 10))
size = 0.3

# 设置颜色
colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#CCCCCC",
          "#FF6666", "#3399FF", "#66FF66", "#FF9933", "#C0C0C0"]

wedges1, texts1, autotexts1 = plt.pie(temp_counts, labels=temp_counts.index, radius=1,
                                      autopct=custom_autopct, explode=explode_values, shadow=True, colors=colors,
                                      pctdistance=0.85)
# 添加图例
plt.legend(wedges1, labels, title="油温区间", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

# 添加标题
plt.title('油温数据扇形图')

plt.show()

# 绘制双环扇形图
plt.figure(figsize=(12, 10))
size = 0.3

# 设置颜色
colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#CCCCCC",
          "#FF6666", "#3399FF", "#66FF66", "#FF9933", "#C0C0C0"]

# 绘制外环
plt.pie(extra_counts, radius=1 - size, wedgeprops=dict(width=size, edgecolor='w'),
        autopct=custom_autopct, shadow=True, colors=colors, pctdistance=0.75)

# 绘制内环
wedges1, texts1, autotexts1 = plt.pie(temp_counts, labels=temp_counts.index, radius=1,
                                      wedgeprops=dict(width=size, edgecolor='w'),
                                      autopct=custom_autopct, explode=explode_values, shadow=True, colors=colors,
                                      pctdistance=0.85)

# 添加图例
plt.legend(wedges1, labels, title="油温区间", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

# 添加标题
plt.title('油温数据双环扇形图')

# 显示图表
plt.show()

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
## 获取'2017-1-1':'2017-1-7'七天的数据
dayData = df[['date', 'HUFL']].set_index('date')
HUFL = dayData['2017-1-1':'2017-1-7'].reset_index()
print(HUFL)

fig = plt.figure(figsize=(10, 4))

## 绘制热力图
plt.imshow([HUFL['HUFL']], aspect=8, )

## 显示颜色条
plt.colorbar(orientation='horizontal', pad=0.3, shrink=0.75, location='top')

## 设置两轴刻度
plt.xticks(range(0, len(HUFL['date']), 24), HUFL['date'][0::24].dt.strftime('%Y/%m/%d'), rotation=90)
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

fig = plt.figure(figsize=(20, 11))
plt.title("HUFL折线图-MUFL直方图-LUFL散点图",fontsize=20)
plt.axis("off")

plt.subplot(2, 2, 1)
plt.plot(date, HUFL, color=color3)

plt.xlabel("月份-日期 时间", fontsize=13)
plt.ylabel("HUFL", fontsize=13)

plt.subplot(2, 2, 2)
plt.hist(MUFL, bins=20, color=color2)
plt.xlabel("MUFL", fontsize=13)
plt.ylabel("出现次数", fontsize=13)

plt.subplot(2, 1, 2)
plt.plot(date, LUFL, 'ro')
plt.xlabel("月份-日期 时间", fontsize=13)
plt.ylabel("LUFL", fontsize=13)

plt.show()
