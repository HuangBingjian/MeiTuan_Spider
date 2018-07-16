import csv
import os
import requests
import random
import time
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from mt_wordcloud import *
from mt_analyse import *

# 头信息,模仿手机端(小米/华为)
headers = [
    {
        'User-Agent': 'AiMeiTuan /Xiaomi-4.4.2-MI 6 -720x1280-240-5.5.4-254-863254010002128-qqcpd',
        'Host': 'api.meituan.com',
        'Connection': 'Keep-Alive'
    },
    {
        'User-Agent': 'AiMeiTuan /HUAWEI-4.4.2-HUAWEI MLA-AL10-720x1280-240-5.5.4-254-863254010002128-qqcpd',
        'Host': 'api.meituan.com',
        'Connection': 'Keep-Alive'
    }
]


class show_window(QWidget):
    def __init__(self):
        super(show_window, self).__init__()

        self.initUI()

        # 用于设置csv文件的存储路径和文件名,默认深圳
        self.save_path = './Resource'
        self.city_name = 'ShenZhen'
        self.file_path = os.path.join(self.save_path, self.city_name + '.' + 'csv')
        self.base_url = "http://api.meituan.com/group/v4/deal/select/city/{0}/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset={1}&limit=100"
        # 1为北京，10为上海，20为广州，30为深圳

    def initUI(self):
        self.setFixedSize(500,500)
        self.list_name = [ 'BeiJing', 'ShangHai', 'GuangZhou', 'ShenZhen', 'HangZhou', 'DongGuan', 'FoShan']
        self.list_city = [ '北京', '上海', '广州', '深圳', '杭州','东莞', '佛山']
        self.list_num = [ '1', '10', '20', '30', '50', '91', '92']

        self.nullLabel = QLabel(" ")
        self.titleLabel = QLabel("美团美食爬虫")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.authorLabel = QLabel("作者：黄炳坚 吴林源 廖凯文")
        self.authorLabel.setAlignment(Qt.AlignRight)

        self.wordLabel = QLabel("词云")
        self.widthLabel = QLabel("width")
        self.heightLabel = QLabel("height")
        self.maxLabel = QLabel("max_words")
        self.fontLabel = QLabel("max_font_size")
        self.randLabel = QLabel("random_state")
        self.scaleLabel = QLabel("scale")

        self.widthLine = QLineEdit("1400")
        self.heightLine = QLineEdit("700")
        self.maxLine = QLineEdit("200")
        self.fontLine =QLineEdit("200")
        self.randLine = QLineEdit("50")
        self.scaleLine = QLineEdit("2.0")

        self.widthLine.setFixedWidth(100)
        self.heightLine.setFixedWidth(100)
        self.maxLine.setFixedWidth(100)
        self.fontLine.setFixedWidth(100)
        self.randLine.setFixedWidth(100)
        self.scaleLine.setFixedWidth(100)

        self.areaLabel = QLabel("地区")
        self.areaCombo = QComboBox()
        self.areaCombo.addItems(self.list_city)

        self.showLabel = QLabel("显示前几")
        self.showSpin = QSpinBox()
        self.showSpin.setAlignment(Qt.AlignCenter)
        self.showSpin.setValue(10)
        self.showSpin.setRange(3,30)

        self.infoLabel = QLabel("输出")
        self.infoText = QTextEdit("美食搜索：")  # http://www.meituan.com/api/v1/divisions?mtt=1.help%2Fapi.0.0.jg5ary4h
        self.infoText.append('\n        点击按钮即刻开始')
        self.infoText.append('\n    温馨提示：\n\n    目前支持查询北京、上海、广州、深圳、杭州、东莞、佛山！\n\n    词云分析需要一些时间，请耐心等候！'
                             '\n\n    初次爬虫时需要耗时数分钟进行数据抓取！')
        self.infoText.append('\n----------------------------')
        self.infoText.append(' ')

        self.spiderButton = QPushButton("开始爬虫")
        self.spiderButton.setFixedSize(300,40)

        # 信号与槽
        self.spiderButton.clicked.connect(self.run)

        #　布局
        areaLayout = QVBoxLayout()              # 地区
        areaLayout.addWidget(self.areaLabel)
        areaLayout.addWidget(self.areaCombo)

        # 词云
        keyLayout = QVBoxLayout()
        keyLayout.addWidget(self.widthLabel)
        keyLayout.addWidget(self.heightLabel)
        keyLayout.addWidget(self.scaleLabel)
        keyLayout.addWidget(self.maxLabel)
        keyLayout.addWidget(self.randLabel)
        keyLayout.addWidget(self.fontLabel)

        valueLayout = QVBoxLayout()
        valueLayout.addWidget(self.widthLine)
        valueLayout.addWidget(self.heightLine)
        valueLayout.addWidget(self.scaleLine)
        valueLayout.addWidget(self.maxLine)
        valueLayout.addWidget(self.randLine)
        valueLayout.addWidget(self.fontLine)

        wordLayout = QHBoxLayout()
        wordLayout.addLayout(keyLayout)
        wordLayout.addLayout(valueLayout)

        wordcloudLayout = QVBoxLayout()
        wordcloudLayout.addWidget(self.wordLabel)
        wordcloudLayout.addLayout(wordLayout)

        showLayout = QVBoxLayout()
        showLayout.addWidget(self.showLabel)
        showLayout.addWidget(self.showSpin)

        infoLayout = QVBoxLayout()              # 输出信息
        infoLayout.addWidget(self.infoLabel)
        infoLayout.addWidget(self.infoText)

        Layout1 = QVBoxLayout()
        Layout1.addLayout(areaLayout)
        Layout1.addLayout(wordcloudLayout)
        Layout1.addLayout(showLayout)
        areaLayout.setAlignment(Qt.AlignTop)
        wordcloudLayout.setAlignment(Qt.AlignCenter)
        showLayout.setAlignment(Qt.AlignBottom)

        Layout2 = QHBoxLayout()
        Layout2.addLayout(Layout1)
        Layout2.addLayout(infoLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.titleLabel)
        mainLayout.addWidget(self.nullLabel)
        mainLayout.addWidget(self.authorLabel)
        mainLayout.addWidget(self.nullLabel)
        mainLayout.addLayout(Layout2)
        mainLayout.addWidget(self.nullLabel)
        mainLayout.addWidget(self.spiderButton, 0, Qt.AlignCenter)

        self.setLayout(mainLayout)
        self.setWindowTitle('美团美食爬虫')
        self.show()

    def run(self):
        index = self.areaCombo.currentIndex()
        self.city_name = self.list_name[index]
        self.file_path = os.path.join(self.save_path, self.city_name + '.' + 'csv')
        self.parse(index)

    def parse(self, index):
        self.open_file(self.file_path, index)                            # 打开CSV文件
        analyse_district(self.file_path, self.list_city[index])                          # 分析各行政区
        analyse_area(self.file_path, self.list_city[index], self.showSpin.value())       # 分析各地片区
        analyse_cate(self.file_path, self.list_city[index], self.showSpin.value())       # 分析美食类别
        # show_wordcloud(self.file_path, self.list_city[index], int(self.widthLine.text()), int(self.heightLine.text()), int(self.maxLine.text()),
        #                int(self.fontLine.text()), int(self.randLine.text()), float(self.scaleLine.text()))            # 显示词云图片

    def open_file(self, file_path, index):                               # 打开CSV文件,获取商家信息
        if not os.path.exists(file_path):                               # CSV不存在时才执行下面操作，存在则跳过
            if not os.path.exists(self.save_path):
                os.makedirs(self.save_path)

            file = open(file_path, 'w', encoding='utf_8_sig', newline='')
            csvwriter = csv.writer(file)
            csvwriter.writerow(
                    ['店铺名称', '类别', '评分', '所在区', '所属片区', '纬度', '经度', '详细地址', '优惠套餐情况', '营业时间', '联系电话', '累计售出份数', '餐厅简介', '特色菜'])
            # 获取商家信息
            i = 0
            while True:
                url = self.base_url.format(self.list_num[index], str(i * 100))
                itemlist = self.get_item(url)
                if not itemlist:
                    break
                for item in itemlist:
                    csvwriter.writerow(item.values())
                print('已获取%d个美团商家信息' % ((i + 1) * 100))
                i += 1
                time.sleep(random.randint(2, 5))    # 随机2~5秒爬取间隔
        #     self.infoText.append('一共成功获取了{0}地区{:d}条美食信息!'.format(self.list_city[index], i))
        #  self.infoText.append('\n{0}地区美食信息搜索解析完毕~'.format(self.list_city[index]))

    def get_item(self, url):                                 # 解析链接
        response = requests.get(url, headers=random.choice(headers))
        number = 0
        while True:
            try:
                info_dict = json.loads(response.text)
                info_list = info_dict['data']
                if info_list:
                    break
                else:
                    number += 1
                    if number >= 10:
                        return None
                    time.sleep(10)
                    response = requests.get(url, headers=random.choice(headers))
            except:
                number += 1
                if number >= 10:
                    return None
                time.sleep(10)
                response = requests.get(url, headers=random.choice(headers))

        itemlist = []
        for info in info_list:
            # 店铺名称
            name = info['poi']['name']
            # 所在区
            if info['poi']['addr'][2] == '区':
                distName = info['poi']['addr'][0:2]
            else:
                distName = ''
            # 所属片区
            areaName = info['poi']['areaName']
            # 详细地址
            addr = info['poi']['addr']
            # 纬度
            lat = info['poi']['lat']
            # 经度
            lng = info['poi']['lng']
            # 餐厅类别
            cateName = info['poi']['cateName']
            # 优惠套餐情况
            abstracts = ''
            for abstract in info['poi']['payAbstracts']:
                # abstracts.append(abstract['abstract'])
                abstracts = abstracts + abstract['abstract'] + ';'
            # 评分
            avgScore = info['poi']['avgScore']
            # 营业时间
            openInfo = info['poi']['openInfo'].replace('\n', ' ')
            # 联系电话
            phone = info['poi']['phone']
            # 累计售出份数
            historyCouponCount = info['poi']['historyCouponCount']
            # 餐厅简介
            introduction = info['poi']['introduction']
            # 特色菜
            featureMenus = info['poi']['featureMenus']
            item = {
                '店铺名称': name,
                '类别': cateName,
                '评分': avgScore,
                '所在区': distName,
                '所属片区': areaName,
                '纬度': lat,
                '经度': lng,
                '详细地址': addr,
                '优惠套餐情况': abstracts,
                '营业时间': openInfo,
                '联系电话': phone,
                '累计售出份数': historyCouponCount,
                '餐厅简介': introduction,
                '特色菜': featureMenus
            }

            itemlist.append(item)
        # 返回当前页面item列表
        return itemlist
