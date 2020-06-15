# -*- coding:utf-8 -*-
# @Time    :'2020/5/9 14:54'
# @Author  : '一之明'
# @File    :WorldOther.py
# @Software:Win10, python3.7
import requests, json
from pyecharts import Line
import os
os.chdir('D:\疫情分析')
# 创建折线图
line = Line('海外各国疫情趋势图',width=960, height=600)

# 参与统计的国家列表
countryNameList = ['美国','法国','伊朗','意大利','韩国','西班牙','德国','日本本土','加拿大']
# 请求各个国家疫情数据连接
urlTemplate = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country={}&"
# 请求各个国家连接返回的数据
for country in countryNameList:
    url = urlTemplate.format(country)
    baseData = requests.get(url).text
    data = json.loads(baseData)
    # 保存日期列表
    dateList =[]
    # 保存每日累计确诊人数
    confirmList = []
    for item in data['data']:
        # 追加日期
        dateList.append(item['date'])
        # 追加确诊人数
        confirmList.append(item['confirm'])
    # 添加各国的折线数据
    line.add(country,dateList,confirmList,mark_point=['max'])
# 显示图像参数
line.show_config()
line.render(path='output/海外各国疫情趋势图.html')
