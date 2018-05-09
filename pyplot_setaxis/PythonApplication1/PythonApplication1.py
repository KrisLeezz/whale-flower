#
import numpy
from array import array
from pyearth import Earth
from matplotlib import pyplot
import csv
csv_file1=open('data1.csv','r')
csv_reader1=csv.DictReader(csv_file1)
X=[row['AOD'] for row in csv_reader1]

X=numpy.array(X)
#print X
csv_file1.close()
csv_file2=open('data1.csv','r')
csv_reader2=csv.DictReader(csv_file2)
y=[row1['PM']for row1 in csv_reader2]

y=numpy.array(y)
#print y
csv_file2.close()

from pylab import *
from matplotlib.ticker import  MultipleLocator
from matplotlib.ticker import  FormatStrFormatter

#将x主刻度标签设置为20的倍数(也即以 20为主刻度单位其余可类推)
xmajorLocator = MultipleLocator(0.5);
#设置x轴标签文本的格式
xmajorFormatter = FormatStrFormatter('%3.1f') 
#将x轴次刻度标签设置为5的倍数
xminorLocator = MultipleLocator(0.1) 
#设定y 轴的主刻度间隔及相应的刻度间隔显示格式
#将y轴主刻度标签设置为1.0的倍数
ymajorLocator = MultipleLocator(50) 
 #设置y轴标签文本的格式
ymajorFormatter = FormatStrFormatter('%1.1f')
#将此y轴次刻度标签设置为0.2的倍数
yminorLocator = MultipleLocator(5) 

ax = subplot(111)
plot(X,y,'r')
#设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)
#显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度
show()
#
