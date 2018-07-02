
@Copyright by SONG

一个爬取智联招聘的爬虫和易用分析工具

爬取智联招聘的爬虫以及简单分析
基于网络资料开发的一个Python3项目，可以对相关职位的月薪等信息进行可视化分析

功能
1.通过关键词爬取智联上的相关职位信息
2.输出信息为Excel表格
3.输出职位数排名前10的城市信息
4.输出职位全国的分布情况
5.分析关键词职位的月薪分布情况
6.分析职位要求并将数据通过词云图展示
7.数据可视化，数据库冗余信息清理小工具



数据库
使用MongoDB数据库，安装配置好MongoDB数据库
MongoDB.txt

使用方法
1. 根据需要配置config.py文件
可修改需要爬取的关键词和城市信息

2. 运行zhaopin_spider.py爬取数据
运行zhaopin_spider.py

PyMongo 是 MongoDB 的 Python 接口开发包
python -m pip install pymongo

requests是python的一个HTTP客户端库，跟urllib，urllib2类似，那为什么要用requests而不用urllib2呢？
官方文档中是这样说明的：
python的标准库urllib2提供了大部分需要的HTTP功能，但是API太逆天了，一个简单的功能就需要一大堆代码。
python -m pip install requests

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库，简单来说，它能将HTML的标签文件解析成树形结构，然后方便地获取到指定标签的对应属性。
python -m pip install beautifulsoup4

lxml包用于解析XML和html文件，可以使用xpath和css定位元素
python -m pip install lxml

3. 使用db_op.py清理数据
运行db_op.py，输入要清理的关键词，比如：演员、课程顾问之类的冗余信息

4. 使用zhaopin_analyzer.py分析数据
运行zhaopin_analyzer_test.py

Python Imaging Library (PIL)是python下的图像处理模块，支持多种格式，并提供强大的图形与图像处理功能。
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
downlod: Pillow-5.1.1-cp37-cp37m-win_amd64.whl
cmd: cd E:\Python\Python37\Scripts
     pip install E:\Python\Software\Pillow-5.1.1-cp37-cp37m-win_amd64.whl
     python
 >>> from PIL import Image
 >>>


Jieba是一个中文分词组件，可用于中文句子/词性分割、词性标注、未登录词识别，支持用户词典等功能。该组件的分词精度达到了97%以上。
python -m pip install jieba

NumPy(Numerical Python)提供了许多高级的数值编程工具，如：矩阵数据类型、矢量处理，以及精密的运算库。专为进行严格的数字处理而产生
numpy使用一种称为ndarray的类似Matlab的矩阵式数据结构管理数据，比python的列表和标准库的array类更为强大，处理数据更为方便。
pip install numpy

scipy是Python中科学计算程序的核心包，实现以下插值，积分，优化，图像处理等等，都是需要计算。
pip install scipy

先安装 visualcppbuildtools_full.exe

pandas 是基于 Numpy 构建的含有更高级数据结构和工具的数据分析包
pip install pandas

python里的matplotlib是一个很强大的绘图软件包。可以绘制类似matlab和R软件效果的图样。
pip install matplotlib

词云又叫文字云，是对网络文本中出现频率较高的"关键词"予以视觉上的突出,形成"关键词云层"或"关键词渲染",从而过滤掉大量的文本信息,使浏览网页者只要一眼扫过文本就可以领略文本的主旨。

wordcloud包生成的词云图
pip install WordCloud

openpyxl 是一个用来处理 excel 文件的 python 代码库。
pip install openpyxl

使用自己的词云图mask
将res目录下的mask改为自己的蒙版图片即可，推荐1600*1600像素以上

运行

from zhaopin_Analyzer import *
ana = Analysis('机器学习') # 第一个参数为需要分析的关键字，第二个参数默认为空，填写需要分析的城市名（已在config中配置的）
ana.easyRun()

5. 会在data和images文件夹生成信息
请参见data和images文件夹

方法
Analysis.top10City() # 获取职位数量排名前十的城市
Analysis.salaryAnalysis() # 对月薪进行分析
Analysis.saveBrief() # 存取职位简要信息用于生成词云图
Analysis.wordCloud() # 生成词云图
Analysis.easyRun() # 一次运行以上函数