美团爬虫程序，可以爬取美团网站上的商铺及美食信息。

---
main.py ：主程序

mt_parse.py : 爬取信息，QT界面

mt_analyse.py : 对爬取的信息进行处理，图表化显示

mt_wordcloud.py : 云词功能


http://api.meituan.com/group/v4/deal/select/city/1/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset=100&limit=100

使用美团API接口获取商铺美食信息。1位置的数值可更改，1为北京，10为上海，20为广州，30为深圳，其它城市自行探索。

---

QT界面：

![image](https://github.com/HuangBingjian/MeiTuan_Spider/blob/master/Resource/result.jpg)

各行政区美食分布：

![image](https://github.com/HuangBingjian/MeiTuan_Spider/blob/master/Resource/北京各行政区美食分布.jpg)

各片区美食分布：

![image](https://github.com/HuangBingjian/MeiTuan_Spider/blob/master/Resource/杭州各片区美食分布.jpg)

美食的分布情况：

![image](https://github.com/HuangBingjian/MeiTuan_Spider/blob/master/Resource/北京美食的分类情况.jpg)

词云：

<img src="https://github.com/HuangBingjian/MeiTuan_Spider/blob/master/Resource/image.jpg" width="30%" height="30%" /><img src="https://github.com/HuangBingjian/MeiTuan_Spider/blob/master/Resource/词云_北京.jpg" width="30%" height="30%" />