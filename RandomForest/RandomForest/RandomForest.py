 # -*- coding: utf-8 -*-
import csv
import numpy
from array import array
from matplotlib import pyplot
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn import preprocessing
from sklearn import metrics
from sklearn import linear_model
from math import sqrt
from sklearn.model_selection import GridSearchCV
import pickle

#计算Pearson相关系数
def multipl(a,b):
    sumofab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab
 
def corrcoef(x,y):
    n=len(x)
    #求和
    sum1=sum(x)
    sum2=sum(y)
    #求乘积之和
    sumofxy=multipl(x,y)
    #求平方和
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #计算皮尔逊相关系数
    den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    return num/den

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
def uncenter_R2(a, b): #a是模拟值，b是真实值
    return (a**2).sum() / (b**2).sum()  

#数组标准化
#1.标准差归一化,除去均值，方差缩放
def standar_scale(a):
    standar_scaler = preprocessing.StandardScaler()#与a1的效果一样
    a_standarscale=standar_scaler.fit_transform(a)
    return a_standarscale
    
#2.线性归一化
def minmax_scale(a):
    minMax_scaler = preprocessing.MinMaxScaler()
    a_MinMax=minMax_scaler.fit_transform(a)
    return a_MinMax


#获得数据
aod1=[]
aod3=[]
aod5=[]
pm=[]
so2=[]
no2=[]
co=[]
o3=[]
date=[]
all_x=[]
csv_file_read=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/new_winter.csv')
csv_read=csv.reader(csv_file_read)

for row in csv_read:
    if row[0]!='date':
        aod1.append(row[4])
        aod3.append(row[5])
        aod5.append(row[6])
        pm.append(row[7])
        so2.append(row[8])
        no2.append(row[9])
        co.append(row[10])
        o3.append(row[11])
        date.append(row[0])
        all_x.append(row[4:17])
aod1=numpy.array(aod1)
aod1=aod1.astype(float)
print aod1.shape
aod3=numpy.array(aod3)
aod3=aod3.astype(float)
aod5=numpy.array(aod5)
aod5=aod5.astype(float)
pm=numpy.array(pm)
pm=pm.astype(float)
so2=numpy.array(so2)
so2=so2.astype(float)
no2=numpy.array(no2)
no2=no2.astype(float)
co=numpy.array(co)
co=co.astype(float)
o3=numpy.array(o3)
o3=o3.astype(float)
date=numpy.array(date)
date=date.astype(int)
all_x=numpy.array(all_x)
all_x=all_x.astype(float)
all_x = numpy.delete(all_x, 3, axis=1)
print all_x.shape
print all_x[0]


X=all_x[:,2:]
print X[0]
#X=standar_scale(X)
print X.mean(axis=0)#列
print X.std(axis=0)

y=pm
print y.shape

###########################################################
#parameter={'min_samples_split':[2,10,100,500],'min_samples_leaf':[2,10,20,50]}
#SVR拟合
model=RandomForestRegressor(n_estimators=500,min_samples_split=20)
#model=GridSearchCV(RF,parameter,scoring='r2')
model.fit(X,y)
#print model.best_params_

y_hat=model.predict(X)
#csv_file=open('result.csv','wb')
#csv_write=csv.writer(csv_file)
#csv_write.writerows(y_hat.reshape(-1,1))
#csv_file.close()


#评价指标
#R_2=R2((y_hat.reshape(-1,1)),(y.reshape(-1,1)))
r2=model.score(X,y)
R_square=metrics.r2_score((y.reshape(-1,1)), (y_hat.reshape(-1,1)))#计算r2,来表示y与拟合y_hat的接近程度
RMSE=sqrt(metrics.mean_squared_error(y.reshape(-1,1), y_hat.reshape(-1,1)))
print 'R2',R_square
print'RMSE',RMSE


#地面检测和预测值的线性拟合，注意是y与y_hat的拟合,评价模拟效果
model_line= linear_model.LinearRegression()
model_line.fit(y.reshape(-1,1), y_hat.reshape(-1,1))
a, b = model_line.coef_, model_line.intercept_#斜率，截距
y_predict_hat = model_line.predict(y.reshape(-1,1))

file = open("rfmodel.pickle", "wb")
pickle.dump(model, file)
file.close()

#绘图
pyplot.figure(figsize=(8,6))
pyplot.plot(y.reshape(-1,1), y_hat.reshape(-1,1),'b.',label='Matching Points')
pyplot.plot(y.reshape(-1,1),y_predict_hat.reshape(-1,1),'r-',label='Fitted curve',linewidth=0.6)
pyplot.plot((0,1100),(0,1100),'k--',label='1:1',linewidth=0.6)
pyplot.legend(loc=2) #指定legend的位置右下角
pyplot.annotate("$R^2$=%.3f"%R_square,(700,100))
pyplot.annotate("RMSE=%.3f$\mu{g/}{m}^{3}$"%RMSE,(700,50))

#设置坐标轴刻度
my_x_ticks = numpy.arange(0,1100,100)
my_y_ticks = numpy.arange(0,1100,100)
pyplot.xticks(my_x_ticks)
pyplot.yticks(my_y_ticks)
pyplot.xlim(0,1000)
pyplot.ylim(0,1000)

pyplot.xlabel('Observed PM2.5($\mu{g/}{m}^{3}$)')
pyplot.ylabel('Predicted PM2.5($\mu{g/}{m}^{3}$)')
pyplot.title('RandomForest')
pyplot.show()
print '********************************The next is validation***************************'

#ShuffleSplit交叉验证,分割次数也是10次
from sklearn.model_selection import ShuffleSplit
k_2=10
ss = ShuffleSplit(n_splits=k_2, test_size=0.25,random_state=0)
TotalRMSE_2=0
R2_SUM_2=0
#n_2=0
for train_2, test_2 in ss.split(X,y):
    #n_2+=1
    X_train_2, X_test_2, y_train_2, y_test_2 = standar_scale(X[train_2]), standar_scale(X[test_2]), y[train_2], y[test_2]
    model.fit(X_train_2,y_train_2)
    y_test_hat_2=model.predict(X_test_2)
    rmse_1=sqrt(metrics.mean_squared_error(y_test_2.reshape(-1,1),y_test_hat_2.reshape(-1,1)))
    print rmse_1
    TotalRMSE_2+=rmse_1
    r_1=metrics.r2_score(y_test_2.reshape(-1,1),y_test_hat_2.reshape(-1,1))
    print r_1
    R2_SUM_2+=r_1
    #print R2_SUM_2
print 'The second is Shufflesplit,splits=%d'%k_2  
print 'shufflesplit MSE:',TotalRMSE_2/k_2
print 'shufflesplit R2:',R2_SUM_2/k_2

#print '#############################################tiff read#####################################'
#from osgeo import gdal
#import numpy
#file = open("model.pickle", "rb")
#model = pickle.load(file)
#file.close()

##from numpy import newaxis
#new_img=[]
#dataset_read= gdal.Open("20141229AOD.tif")
#img_read_name=dataset_read.GetDescription()#文件名
#img_read_band=dataset_read.RasterCount#波段数
#img_read_width,img_read_height=dataset_read.RasterXSize,dataset_read.RasterYSize#X是宽（列数），Y是高（行数）
#img_read_geotrans=dataset_read.GetGeoTransform()#获得空间参考（仿射矩阵），六参数坐标转换模型，分别为左上角X坐标，像元X方向大小、旋转信息，左上角Y坐标，像元Y方向大小、旋转信息，Y方向像元大小为负数
#img_read_proj=dataset_read.GetProjection()#获取投影信息
#img_read_Metdata=dataset_read.GetMetadata()#参数结果：水平解析度，垂直解析度，第三个不知道，只有三个tag???

#img_read_data=dataset_read.ReadAsArray(0,0,img_read_width,img_read_height)#获得数据,参数说明xOffset,yOffset,cols,rows
#img_read_data=img_read_data*0.001
#img_read_dtype=img_read_data.dtype.name

#dataset_read2 = gdal.Open("20141229_so2.tif")
#img_read_data2=dataset_read2.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read3 = gdal.Open("20141229_no2.tif")
#img_read_data3=dataset_read3.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read4 = gdal.Open("20141229_co.tif")
#img_read_data4=dataset_read4.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read5 = gdal.Open("20141229_o3.tif")
#img_read_data5=dataset_read5.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read6 = gdal.Open("20141229_air.tif")
#img_read_data6=dataset_read6.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read7 = gdal.Open("20141229_rh.tif")
#img_read_data7=dataset_read7.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read8 = gdal.Open("20141229_speed.tif")
#img_read_data8=dataset_read8.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read9 = gdal.Open("20141229_pre.tif")
#img_read_data9=dataset_read9.ReadAsArray(0,0,img_read_width,img_read_height)

#dataset_read10 = gdal.Open("20141229_direction_new.tif")
#img_read_data10=dataset_read9.ReadAsArray(0,0,img_read_width,img_read_height)

#for i in range(0,img_read_height):
#    a=[]
#    a=numpy.dstack((img_read_data[i],img_read_data2[i],img_read_data3[i],img_read_data4[i],img_read_data5[i],img_read_data6[i],img_read_data7[i],img_read_data8[i],img_read_data9[i],img_read_data10[i]))
#    if i==0:
#        new_img=a
#    else:
#        new_img=numpy.vstack((new_img,a))
#print new_img.shape

#x_img = new_img.reshape(-1,10,order='C')#没问题
#y_img= model.predict(x_img)
#img_write_data=y_img.reshape(img_read_height,img_read_width)#注意顺序，重新整理成图像的维度

#img_write_dtype=gdal.GDT_Float64#待写入文件的类型
##创建文件
#driver=gdal.GetDriverByName("GTiff")
#dataset_write = driver.Create("MOD_PM_20141229_RF_all_new.tif",img_read_width,img_read_height,img_read_band,img_write_dtype)#只有最后的参数int->float
#dataset_write.SetGeoTransform(img_read_geotrans)#仿射变换参数
#dataset_write.SetProjection(img_read_proj)#投影信息
#dataset_write.GetRasterBand(1).WriteArray(img_write_data)#因为只有一个band所以是(1)
#del dataset_write