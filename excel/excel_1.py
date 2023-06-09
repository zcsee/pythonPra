import pandas as pd

# # 创建一个Series，不指定索引
# S1 = pd.Series(["a", "b", "c", "d"])
# print(S1)
# print(S1.index)
# print(S1.values)
# #
# # 创建一个Series，指定索引
# S2 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
# print(S2)
# print(S2.index)
# print(S2.values)
#
# 创建一个Series，使用字典方式传入标签和数据
# S3 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4})
# print(S3)
# print(S3.index)
# print(S3.values)

"""
DataFrame部分
"""
#
# # 创建DataFrame对象
# df1 = pd.DataFrame(["a", "b", "c", "d"])
# print(df1)
#
# # 当传入一个嵌套列表时，会根据嵌套列表数显示成多列数据
# df2 = pd.DataFrame([('a', "A"), ('b', "B"), ('c', "C"), ('d', "D")])
# print(df2)
#
# # 给列表加标题
# df3 = pd.DataFrame([('a', "A"), ('b', "B"), ('c', "C"), ('d', "D")], columns=['小写', '大写'])
# print(df3)
# # 给列表加标题和序号
# df31 = pd.DataFrame([('a', "A"), ('b', "B"), ('c', "C"), ('d', "D")], columns=['小写', '大写'], index=['一', '二', '三', '四'])
# print(df31)
#
# # 通过传入字典实现
# data = {"小写": ["a", "b", "c", "d"], "大写": ["A", "B", "C", "D"]}
# df32 = pd.DataFrame(data, index=['一', '二', '三', '四'])
# print(df32)
#
# # 获取DataFrame的数据标签和数据
# print(df32.index)
# # 结果：Index(['一', '二', '三', '四'], dtype='object')
# print(df32.values)
# # 结果
# # [['a' 'A']
# #  ['b' 'B']
# #  ['c' 'C']
# #  ['d' 'D']]

# # 导入excel文件 df = pd.read_excel(r"D:/python/leetcode/files/cvm_yh.xlsx", sheet_name="Sheet1", usecols=[0,
# 1])
# df = pd.read_excel(r"D:/python/leetcode/files/cvm_yh.xlsx", sheet_name=0, usecols=[3, 4, 5, 8, 9])
# # 分别获取tz和tt的数据
# df_tz = df[df["可用区"] == "shanghai-tz"]
# df_tt = df[df["可用区"] == "shanghai-tt"]
#
# # 计算tz可用的内存和cpu总和
# tz_cpu_sum = df_tz["CPU"].sum()
# tz_mem_sum = df_tz["内存(MB)"].sum()
# print(tz_cpu_sum)
# print(tz_mem_sum)
#
# # 计算tt可用的内存和cpu总和
# tt_cpu_sum = df_tt["CPU"].sum()
# tt_mem_sum = df_tt["内存(MB)"].sum()
# print(tt_cpu_sum)
# print(tt_mem_sum)

# print(df_tz)
# print("-" * 100)
# print(df_tt)
# 使用下标序列导入sheet, # 使用index_col指定行索引 # 使用head指定列索引 print(df)

# df_csv = pd.read_csv(r"D:/python/leetcode/files/cvm_yh.csv", encoding='gbk', usecols=[0, 1], engine='python')
# print(df_csv)
