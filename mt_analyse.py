import pandas
from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False


# 分析各区
def analyse_district(file_path, city):
    pyplot.figure(1)
    df = pandas.read_csv(file_path)
    district = pandas.DataFrame(df["所在区"].value_counts())
    index_list = []
    for i in list(district.index):
        if i == "":
            i = "不明"
        index_list.append(i)
    district.index = index_list

    for i in range(len(["所在区"])):
        feature = ["所在区"][i]
        x_labels = list(district.index)
        x = range(len(x_labels))
        pyplot.xticks(x, x_labels)
        y = district[feature]
        x = [j + 0.2 * i for j in x]
        pyplot.bar(x, y, width=0.5, label="{0}行政区".format(city))

    for a, b in zip(range(len(index_list)), district.values):
        pyplot.text(a, b + 1, '%d' % b, ha='center', va='bottom', fontsize=10)

    pyplot.legend()
    pyplot.title('{0}各行政区美食分布'.format(city))
    pyplot.savefig('./Resource/{0}各行政区美食分布.jpg'.format(city))
    pyplot.show()

# 分析区域
def analyse_area(file_path, city, count):
    pyplot.figure(2)
    df = pandas.read_csv(file_path)
    area = pandas.DataFrame(df["所属片区"].value_counts()[:count])
    index_list = []
    for i in list(area.index):
        if i == "":
            i = "未知"
        index_list.append(i)
    area.index = index_list

    for i in range(len(["所属片区"])):
        feature = ["所属片区"][i]
        x_labels = list(area.index)
        x = range(len(x_labels))
        pyplot.xticks(x, x_labels)
        y = area[feature]
        x = [j + 0.2 * i for j in x]
        pyplot.bar(x, y, width=0.5, label="{0}各片区".format(city))

    for a, b in zip(range(count), area.values):
        pyplot.text(a, b + 1, '%d' % b, ha='center', va='bottom', fontsize=10)

    pyplot.legend()
    pyplot.title('{0}各片区美食分布'.format(city))
    pyplot.savefig('./Resource/{0}各片区美食分布.jpg'.format(city))
    pyplot.show()


# 分析类别
def analyse_cate(file_path, city, count):
    pyplot.figure(3)
    df = pandas.read_csv(file_path)
    cate = pandas.DataFrame(df["类别"].value_counts()[:count])
    index_list = []
    for i in list(cate.index):
        if i == "":
            i = "未知"
        index_list.append(i)
    cate.index = index_list

    for i in range(len(["类别"])):
        feature = ["类别"][i]
        x_labels = list(cate.index)
        x = range(len(x_labels))
        pyplot.xticks(x, x_labels)
        y = cate[feature]
        x = [j + 0.2 * i for j in x]
        pyplot.bar(x, y, width=0.5, label="{0}美食分类".format(city))

    for a, b in zip(range(count), cate.values):
        pyplot.text(a, b + 1, '%d' % b, ha='center', va='bottom', fontsize=10)

    pyplot.legend()
    pyplot.title('{0}美食的分类情况'.format(city))
    pyplot.savefig('./Resource/{0}美食的分类情况.jpg'.format(city))
    pyplot.show()