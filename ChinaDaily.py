# -*- coding:utf-8 -*-
# @Time    :'2020/5/9 15:30'
# @Author  : '一之明'
# @File    :ChinaDaily.py
# @Software:Win10, python3.7
import requests, json
from pyecharts import Line
import os

os.chdir('D:\疫情分析')
# 请求海外各国疫情数据连接
baseUrl = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=jQuery34107864327291719062_1588994556210&_=1588994556211"
# 请求当前连接返回的数据
chinaData = requests.get(baseUrl).text.replace('"{', '{').replace('}"}', '}}').replace('\\', '')
# 处理数据
chinaData = chinaData[chinaData.index('{'): -1]
# 将当前的json字符串转换成python的字典
baseData = json.loads(chinaData)
# 保存疫情属性列表
attrList = ['累计确诊', '现有疑似', '现有确诊', '现有重症', '境外输入']

# 日期列表
dateList = []
# 累计确诊列表
confirmList = []
# 现有疑似列表
suspectList = []
# 现有确诊列表
nowConfirmList = []
# 现有重症列表
nowSevereList = []
# 境外输入列表
importedCaseList = []
# 解析数据
for item in baseData['data']['chinaDayList']:
    # 追加数据
    dateList.append(item['date'])
    confirmList.append(item['confirm'])
    suspectList.append(item['suspect'])
    nowConfirmList.append(item['nowConfirm'])
    nowSevereList.append(item['nowSevere'])
    importedCaseList.append(item['importedCase'])
# 创建折线图
line = Line('全国疫情发展趋势图', width=960, height=600)
# 添加折线数据
line.add('累计确诊', dateList, confirmList, mark_point=['max'])
line.add('现有疑似', dateList, suspectList, mark_point=['max'])
line.add('现有确诊', dateList, nowConfirmList, mark_point=['max'])
line.add('现有重症', dateList, nowSevereList, mark_point=['max'])
line.add('境外输入', dateList, importedCaseList, mark_point=['max'])
# 显示图像参数
line.show_config()
line.render(path='output/全国疫情发展趋势图.html')
