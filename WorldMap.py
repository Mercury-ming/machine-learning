# -*- coding:utf-8 -*-
# @Time    :'2020/5/9 11:54'
# @Author  : '一之明'
# @File    :WorldMap.py
# @Software:Win10, python3.7
# 导入请求发送模块,json转换模块,xlrd解析Excel表格
import requests, json, xlrd
from pyecharts import Map
import os 
os.chdir('D:\疫情分析')
# 请求海外各国疫情数据连接
baseUrl = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign&callback=jQuery34109782764069170033_1588994811575&_=1588994811576"
# 请求当前连接返回的数据
WorldData = requests.get(baseUrl).text.replace('"{', '{').replace('}"}', '}}').replace('\\', '')
# 处理数据
WorldData = WorldData[WorldData.index('{'): -1]
# 将当前的json字符串转换成python的字典
baseData = json.loads(WorldData)
excelData = xlrd.open_workbook('世界各国中英文对照表.xlsx')
# 通过索引顺序获取当前sheet表格
table = excelData.sheet_by_index(0)
# 获取行数
rows = table.nrows
# 创建国家中英文字典
countryDict = {}
# 循环获取中英文国家名称的键值对（字典）
for i in range(rows):
    countryDict[table.row_values(i)[1]] = table.row_values(i)[0]
# 保存英文国家名列表
englishCountryNameList = []
# 保存各个国家的确诊数据
countryConfirmDataList = []
# 获取每个国家的名称和当前确诊人数
for country in baseData['data']['foreignList']:
    if country['name'] in countryDict:
        englishCountryNameList.append(countryDict[country['name']])
        countryConfirmDataList.append(country['confirm'])
# 创建地图，添加世界地图相关参数
map = Map('世界疫情分布图', width=1280, height=600, title_color='red')
map.add('世界地图', englishCountryNameList, countryConfirmDataList, maptype='world',
        visual_range=[1, 10000], visual_text_color='#000', is_visualmap=True)
# 显示地图配置参数
map.show_config()
# 渲染地图
map.render(path='output/世界疫情分布图.html')
