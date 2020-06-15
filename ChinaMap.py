# -*- coding:utf-8 -*-
# @Time    :'2020/5/9 13:55'
# @Author  : '一之明'
# @File    :ChinaMap.py
# @Software:Win10, python3.7
import requests, json
from pyecharts import Map
import os

os.chdir('D:\疫情分析')
# 请求全国疫情数据连接
baseUrl = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery3410673155463671044_1588993976533&_=1588993976534"
# 请求当前连接返回的数据
chinaData = requests.get(baseUrl).text.replace('"{', '{').replace('}"}', '}}').replace('\\', '')
# 处理数据
chinaData = chinaData[chinaData.index('{'): -1]
# 将当前的json字符串转换成python的字典
baseData = json.loads(chinaData)
# 保存省份名称
provinceNameList = []
# 保存各省份确诊人数
provinceConfirmList = []
provinceList = baseData['data']['areaTree'][0]['children']
for province in provinceList:
    provinceNameList.append(province['name'])
    provinceConfirmList.append(province['total']['confirm'])
# 创建地图，添加全国地图相关参数
map = Map('全国疫情分布图', width=1280, height=600, title_color='red')
map.add('中国地图', provinceNameList, provinceConfirmList, maptype='china',
        visual_range=[1, 1000], visual_text_color='#000', is_visualmap=True)
# 显示地图配置参数
map.show_config()
# 渲染地图
map.render(path='output/全国疫情分布图.html')
