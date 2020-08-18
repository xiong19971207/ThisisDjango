import pandas as pd
import json

csv_data = pd.read_csv(r'test.csv', )  # 读取训练数据

# 获取数据总量
print(csv_data.shape)  # (383，37)

N = 5
csv_batch_data = csv_data.tail(N)  # 取后5条数据
print(csv_batch_data.shape)  # (5, 37)

# 返回最后五行全部数据
last_data = csv_data.tail(5)
print(last_data)

# 返回全部字段
data_columns = csv_data.columns
print(data_columns)

# 输出一到二行的数据
hear_data = csv_data.loc[:2]
print(hear_data)

# 输出选中行的任意列
detail_columns = csv_data.loc[:2, 'sku']
print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
print(detail_columns)

# 输出任意一列字段
print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
any_column = csv_data['sku']
print(any_column)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++')

# 查看数据维度
print(csv_data.shape)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
# 数据表基本信息(维度，列名称，数据格式，所占空间)
print(csv_data.info)
# 输出每一列的类型
print(csv_data.dtypes)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
# 输出指定字段的类型
print(csv_data['sku'].dtype)

print('===================================================')
# 查看空值的，暂时不会用
print(csv_data.isnull)

# 查看某一字段的唯一值
print(csv_data['snapshot-date'].unique())

# 将每一行的数据都打包成一个列表，然后套在一个列表中
print(csv_data.values)

# dropna函数。删除空行或者空列
# axis表示维度(1代表纵向，0代表横向) how表示空值数量(all表示全是空值时，any表示有空值)
# thresh:一行或一列中至少出现了thresh个才删除。
# inplace表示是在原数据中修改，还是在副本中修改
csv_data.dropna(axis=1, how='all', inplace=True)

# 删除一个字段
a = pd.read_csv('test.csv')
a.drop('snapshot-date', axis=1, inplace=True)
a.to_csv('11.csv')

# 填充空值
a = pd.read_csv('bear.csv')
a.fillna(value='bear', inplace=True)
a.to_csv('xx.csv')

# 填充不同的空值
b = pd.read_csv('bear.csv')
values = {'snapshot-date': 1, 'condition': 2}
b.fillna(value=values, inplace=True)
b.to_csv('bb.csv')

# 清除字符空白,没吊用
c = pd.read_csv('bear.csv')
print(c['Recommended action'].dtype)
# newname = c['Recommended action'].map(str.strip(' '))
# c['Recommended action'] = newname
print('oooooooooooooooooooooooooooooooooooooo')
c.to_csv('cc.csv')
print(c['Recommended action'])

# 大小写转换
print(c['product-name'].str.upper())

# 更改数据格式
print('+_+_+_+++_+_++_+++++_+_++_+++_+_+_+_+_+')
c['Healthy Inventory Level'] = c['Healthy Inventory Level'].astype('object')
print(c['Healthy Inventory Level'].dtype)

# 更改字段名称
c.rename(columns={'product-name': 'bear-name'}).to_csv('dd.csv')

# 替换字段名称
# inplace=True表示直接在副本中保存，否则没啥用
d = pd.read_csv('bear.csv')
d['asin'].replace('B07FLRB3X5', 'bear', inplace=True)
d.to_csv('dd.csv')
