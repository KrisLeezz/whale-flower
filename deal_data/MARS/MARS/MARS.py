import numpy
from array import array
from pyearth import Earth
from matplotlib import pyplot
import csv
from sklearn import preprocessing 


#数组的统计属性
from numpy import mean, median
from numpy import mean, ptp, var, std
def statistics(a):
    print 'the statistics information is:'
    print 'mean is :',mean(a)
    print 'media is :',median(a)
    print 'min is :',float(min(a))
    print 'max is :',float(max(a))
    #极差
    print 'span is:',ptp(a)
    #方差
    print 'variance is:',var(a)
    #标准差
    print 'standard deviation is:',std(a)
    #变异系数,无量纲的离散程度的表示
    print 'coefficient of variation is:',mean(a) / std(a)

#绘制数据分布直方图
def drawHist(a,x_title,y_title,title):
     #创建直方图
     #第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
     #第二个参数为划分的区间个数
     pyplot.hist(a, 30)
     pyplot.xlabel(x_title)
     pyplot.ylabel(y_title)
     pyplot.title(title)
     pyplot.show()

#创建累积曲线
def drawCumulativeHist(a,x_title,y_title,title):
     #第一个参数为待绘制的定量数据
     #第二个参数为划分的区间个数
     #normed参数为是否无量纲化
     #histtype参数为'step'，绘制阶梯状的曲线
     #cumulative参数为是否累积
     pyplot.hist(a, 20, normed=True, histtype='step', cumulative=True)
     pyplot.xlabel(x_title)
     pyplot.ylabel(y_title)
     pyplot.title(title)
     pyplot.show()

#绘制箱型图
def drawBox(a,lab,title):
    #第一个参数为待绘制的定量数据
    #第二个参数为数据的文字说明
    pyplot.boxplot([a], labels=[lab])
    pyplot.title(title)
    pyplot.show()



#数组标准化
#1.标准差归一化,除去均值，方差缩放
def scale(a):
    # calculate mean  
    a_mean = a.mean(axis=0)  
    # calculate variance   
    a_std = a.std(axis=0)  
    # standardize X  
    a1 = (a-a_mean)/a_std  
    return a1
    # use function preprocessing.scale to standardize X  
    a_scale = preprocessing.scale(a)#与a1的效果一样
    #print a_scale
    
#2.线性归一化
def minmax_scale(a):
    #a_std=(a-a.min(axis=0))/(a.max(axis=0)-a.min(axis=0)) 
    #a_minmax=a_std/(a.max(axis=0)-a.min(axis=0))+a.min(axis=0)) 
    min_max_scaler = preprocessing.MinMaxScaler()  
    a_minMax = min_max_scaler.fit_transform(a)
    return a_minMax

################################################################################
#打开csv获得X
csv_file1=open('MOD_2014_year.csv','r')
csv_reader1=csv.DictReader(csv_file1)
X1=[row['AOD'] for row in csv_reader1]
X2=numpy.array(X1)
X=X2.astype('float64')#不可以直接更改dtype，需要通过X.astype（）函数

print 'the original data X used to model :',X
#获得X的统计信息
statistics(X)
##频率分布图
#drawHist(X,'AOD','Frequency','the Frequency of AOD')
##频率累计图
#drawCumulativeHist(X,'AOD','Frequency','Curve cumulative of AOD')
##箱图
#drawBox(X,'AOD','BOX of AOD')


#重新对X进行shape塑造，方便后面的计算，从这里开始X是reshape之后的X
X=X.reshape(-1,1)#不影响原来的shape的结果


#对X进行归一化处理，这里用到了两种方法，第一种是方差标准化，第二种是线性归一化
#print 'choose the  normalization method,input 1 if you choose scale,inout 2 if you choose MinMax '
c=0
if c==1:#方差标准化
    X_scale=scale(X)
    
elif c==2:#线性归一化
    X_scale=minmax_scale(X)
    
elif c==0:#不进行归一化
    X_scale=X
    
elif c==3:#鲁棒性归一化
    from sklearn.preprocessing import RobustScaler
    X_scale=RobustScaler().fit_transform(X)

print 'the standar result of X is:',X_scale
##测试X_scale,正常情况下均值为0，方差为1
#1.
print 'mean=',X_scale.mean()
print 'std=',X_scale.std()
#2.
print 'min=',X_scale.min()
print 'max=',X_scale.max()
csv_file1.close()

##为了理解方便、表示方法简单
X=X_scale

##归一化之后的统计信息
##获得X的统计信息
statistics(X)
##频率分布图
#drawHist(X,'AOD','Frequency','the Frequency of standar AOD')
##频率累计图
#drawCumulativeHist(X,'AOD','Frequency','Curve cumulative of standar AOD')
##箱图
#drawBox(X.reshape(264,),'AOD','BOX of standar AOD')
#**************************************************************************
#打开csv获得y
csv_file1.close()
csv_file2=open('MOD_2014_year.csv','r')
csv_reader2=csv.DictReader(csv_file2)
y1=[row1['PM2.5']for row1 in csv_reader2]
y2=numpy.array(y1)
y=y2.astype('float64')
print 'the original data used to model :',y
##获得y的统计信息
statistics(y)
##频率分布图
#drawHist(y,'PM2.5','Frequency','the Frequency of PM2.5')
##频率累计图
#drawCumulativeHist(y,'PM2.5','Frequency','Curve cumulative of PM2.5')
##箱图
#drawBox(y,'PM2.5','BOX of PM2.5')
##print y.shape
##重新对y进行shape塑造，方便后面的计算，从这里开始y是reshape之后的y
y=y.reshape(-1,1)#不影响结果

#拟合
#1)Fit an Earth model
model = Earth()
model.fit(X,y) #这里用的是标准化之后的数据
#2)Print the model模型结果
print(model.trace())
print(model.summary())
#3)预测的y
y_hat = model.predict(X)
#print y_hat
#print'RMSE',numpy.sqrt(metrics.mean_squared_error(y, y_hat))
#print'MSE',metrics.mean_squared_error(y, y_hat)

#绘图显示
pyplot.figure(figsize=(12,6)) 
pyplot.plot(X,y,'m+',label='original values')
pyplot.plot(X,y_hat,'b.',label='polyfit values')
pyplot.legend(loc=4) #指定legend的位置右下角

#设置坐标轴刻度
my_x_ticks = numpy.arange(0,3.5,0.5)
my_y_ticks = numpy.arange(0,600,50)
pyplot.xticks(my_x_ticks)
pyplot.yticks(my_y_ticks)

pyplot.xlabel('AOD')
pyplot.ylabel('PM2.5(ug/m3)')
pyplot.title('the relationship between PM2.5 and AOD')
pyplot.show()

print '********************************The next is validation***************************'
#基本的评价指标
#计算MSE的函数
def MSE(a,b):#a是模拟值，b是真实值or#b是模拟值，a是真实值,因为有平方不影响
    sum_error=0
    for i in range(len(a)):
        sum_error+=(a[i]-b[i])**2
    mse_error=sum_error/len(a)
    return mse_error

#计算拟合R2

def R2(a, b): #a是模拟值，b是真实值
    return 1 - ((a - b)**2).sum() / ((b - b.mean())**2).sum()  
    
#第一种10折交叉验证实现方法
from sklearn.model_selection import KFold
#print 'Please choose the value of K'
#k_1=input()
k_1=10
kf = KFold(n_splits=k_1)
TotalMSE_1=0
R2_SUM_1=0
#n_1=0
for train_1, test_1 in kf.split(X,y):
    #n_1+=1
    X_train_1, X_test_1, y_train_1, y_test_1 = X[train_1], X[test_1], y[train_1], y[test_1]
    model.fit(X_train_1,y_train_1)
    y_test_hat_1=model.predict(X_test_1)
    y_test_hat_1=y_test_hat_1.reshape(-1,1)#重新shape，避免后面计算产生误差
    TotalMSE_1+=MSE(y_test_hat_1,y_test_1)  
    R2_SUM_1+=R2(y_test_hat_1,y_test_1)
print 'The frist is K-Fold,K=%d'%k_1
print 'k-fold MSE:',TotalMSE_1/k_1
print 'k-fold R2:',R2_SUM_1/k_1

#from sklearn import cross_validation
#accuracy= cross_validation.cross_val_score(model,X,y,scoring='accuracy',cv=10)
#print accuracy

###第二种10折交叉验证实现方法，同上面的结果是一样的，更改scoring参数就行
#from sklearn.model_selection import cross_val_predict
#from sklearn.model_selection import cross_val_score
#from sklearn import metrics
##交叉验证的预测
#predicted_y= cross_val_predict(model, X, y, cv=10)
##print predicted_y
##评价指标
#scores=cross_val_score(model, X, y, cv=10,scoring='neg_mean_squared_error')#scoring指定score类型是MSE
#print -scores#scores输出的是一个负数

#ShuffleSplit交叉验证,分割次数也是10次
from sklearn.model_selection import ShuffleSplit
#print 'Please choose the number of split'
#k_2=input()
k_2=10
ss = ShuffleSplit(n_splits=k_2, test_size=0.25,random_state=0)
TotalMSE_2=0
R2_SUM_2=0
#n_2=0
for train_2, test_2 in ss.split(X,y):
    #n_2+=1
    X_train_2, X_test_2, y_train_2, y_test_2 = X[train_2], X[test_2], y[train_2], y[test_2]
    model.fit(X_train_2,y_train_2)
    y_test_hat_2=model.predict(X_test_2)
    y_test_hat_2=y_test_hat_2.reshape(-1,1)#重新shape，避免后面计算产生误差
    TotalMSE_2+=MSE(y_test_hat_2,y_test_2)
    R2_SUM_2+=R2(y_test_hat_2,y_test_2)
print 'The second is Shufflesplit,splits=%d'%k_2  
print 'shufflesplit MSE:',TotalMSE_2/k_2
print 'shufflesplit R2:',R2_SUM_2/k_2


print '#############################################tiff read#####################################'
#from libtiff import TIFF
#tif = TIFF.open('test_null_MYD.tif', mode='r')
#img = tif.read_image()
#print img
#print tif.info()
#img = img.reshape(-1,1)*0.001
##print img
##print img.dtype 
##print img.shape
##print img.min()
##print img.max()
#y_img= model.predict(img)
#drawCumulativeHist(y_img,'AOD','Frequency','Curve cumulative of standar AOD')

#img =img.reshape(33,56)
#y_img=y_img.reshape(33,56)

#out_tiff = TIFF.open('test_null_MYD_PM2.5.tif', mode = 'w')
#out_tiff.write_image(y_img)  
#out_tiff.close()  

from osgeo import gdal
dataset_read = gdal.Open("MOD_20140126.tif")
img_read_name=dataset_read.GetDescription()#文件名
img_read_band=dataset_read.RasterCount#波段数
img_read_width,img_read_height=dataset_read.RasterXSize,dataset_read.RasterYSize#X是宽（列数），Y是高（行数）
img_read_geotrans=dataset_read.GetGeoTransform()#获得空间参考（仿射矩阵），六参数坐标转换模型，分别为左上角X坐标，像元X方向大小、旋转信息，左上角Y坐标，像元Y方向大小、旋转信息，Y方向像元大小为负数
img_read_proj=dataset_read.GetProjection()#获取投影信息
img_read_Metdata=dataset_read.GetMetadata()#参数结果：水平解析度，垂直解析度，第三个不知道，只有三个tag???
img_read_data=dataset_read.ReadAsArray(0,0,img_read_width,img_read_height)#获得数据,参数说明xOffset,yOffset,cols,rows
img_read_dtype=img_read_data.dtype.name#int 16
x_img = img_read_data.reshape(-1,1)*0.001#重新进行shape，方便带入模型中进行计算
y_img= model.predict(x_img)
#n=img_read_width*img_read_height
#for ii in range(0,n):
#    if y_img[ii]>=0:
#        y_img[ii]= y_img[ii]
#    else:
#        y_img[ii]=-9999
#print y_img
#img_write_band=img_read_band
#img_write_height=img_read_height
#img_write_width=img_write_width

img_write_data=y_img.reshape(img_read_height,img_read_width)#注意顺序，重新整理成图像的维度
#print img_write_data.shape
#img_write_dtype=y_img.dtype.name#float 64
img_write_dtype=gdal.GDT_Float64#待写入文件的类型
#创建文件
driver=gdal.GetDriverByName("GTiff")
dataset_write = driver.Create("MOD_PM_20140126.tif",img_read_width,img_read_height,img_read_band,img_write_dtype)#只有最后的参数int->float
dataset_write.SetGeoTransform(img_read_geotrans)#仿射变换参数
dataset_write.SetProjection(img_read_proj)#投影信息
#for i in range(img_read_band):
dataset_write.GetRasterBand(1).WriteArray(img_write_data)#因为只有一个band所以是(1)
del dataset_write

