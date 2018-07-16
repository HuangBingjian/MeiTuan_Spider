import csv
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

def show_wordcloud(file_path, city, width, height, max_words, max_font_size, random_state, scale):    # 显示词云图片
    file = open(file_path,'r',encoding='utf-8')
    rows = csv.reader(file)
    text = ''
    for row in rows:
        if row[-1] != '':
            text += row[-1] + '，'
    # print(text)
    text=text.replace("免费","").replace("到家","").replace("送货","").replace("店同城","").replace("生日蛋糕","")
    text=text.replace("上门","").replace("预定","").replace("预订","").replace("配送","").replace("英寸","").replace("代金券","")
    wordlist=jieba.cut_for_search(text)
    space_list=" ".join(wordlist)   # 连接词语
    backgroud=np.array(Image.open("./Resource/image.jpg")) # 背景图片
    # mt_wordcloud=WordCloud(width=width, height=700,background_color="white", # 背景颜色
    #                       margin=1,
    #                       mask=backgroud, # 写字用的背景图，从背景图取颜色
    #                       max_words=200,  # 最大词语数量
    #                       font_path="./Resource/zy.otf", # 字体
    #                       max_font_size=200, # 最大字体尺寸
    #                       random_state=50,# 随机角度
    #                       scale=2).generate(space_list) # 生成词云

    mt_wordcloud=WordCloud(width=width, height=height,background_color="white", # 背景颜色
                          margin=1,
                          mask=backgroud, # 写字用的背景图，从背景图取颜色
                          max_words=max_words,  # 最大词语数量
                          font_path="./Resource/zy.otf", # 字体
                          max_font_size=max_font_size, # 最大字体尺寸
                          random_state=random_state,# 随机角度
                          scale=scale).generate(space_list) # 生成词云

    image_color=ImageColorGenerator(backgroud) # 生成词云的颜色
    # plt.figure(4)
    # plt.imshow(mt_wordcloud.recolor(color_func=image_color), interpolation="bilinear") # 显示词云
    # plt.axis("off")
    # plt.figure(5)
    # plt.imshow(backgroud, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()
    # mt_wordcloud.to_file('./Resource/词云_{0}.jpg'.format(city))
