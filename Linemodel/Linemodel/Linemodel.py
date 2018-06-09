# -*-coding: utf-8 -*-
import csv
import numpy
from array import array
from matplotlib import pyplot
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing
from math import sqrt

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
csv_file_read=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/new_2015_2017.csv')
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

#X=all_x
#X=numpy.delete(X, 0, axis=1)
#X=numpy.delete(X, 1, axis=1)
X=all_x[:,2:]
standar_scaler=preprocessing.MinMaxScaler()
X_standarscale= standar_scaler.fit_transform(X)
X=X_standarscale
#X=standar_scale(X)
print X.mean(axis=0)#列
print X.std(axis=0)
print X.shape

y=pm.reshape(-1,1)
print y.shape


###########################################################
#线性拟合
model= linear_model.LinearRegression()
model.fit(X, y)
a, b = model.coef_, model.intercept_#斜率，截距
y_hat = model.predict(X)

#基本评价指标
R_square=metrics.r2_score((y.reshape(-1,1)), (y_hat.reshape(-1,1)))#计算r2,来表示y与拟合y_hat的接近程度
RMSE=sqrt(metrics.mean_squared_error(y.reshape(-1,1), y_hat.reshape(-1,1)))
print 'R2',R_square#计算R2,来表示y与拟合y_hat的接近程度   
print'RMSE',RMSE

#地面检测和预测值的线性拟合，注意是y与y_hat的拟合,评价模拟效果
model_line= linear_model.LinearRegression()
model_line.fit(y.reshape(-1,1), y_hat.reshape(-1,1))
a, b = model_line.coef_, model_line.intercept_#斜率，截距
y_predict_hat = model_line.predict(y.reshape(-1,1))

#csv_file=open('y.csv','wb')
#csv_write=csv.writer(csv_file)
#csv_write.writerows(y_hat.reshape(-1,1))
#csv_file.close()
#绘图
pyplot.figure(figsize=(8,6))
pyplot.rc('font',family='Times New Roman') 
pyplot.scatter(y.reshape(-1,1), y_hat.reshape(-1,1),s=25,c='',marker='.',label='Matching Points',edgecolor='r',linewidths=0.5)
pyplot.plot(y.reshape(-1,1),y_predict_hat.reshape(-1,1),'b-',label='Fitted curve',linewidth=0.6)
pyplot.plot((0,1100),(0,1100),'k--',label='1:1',linewidth=0.5)
pyplot.legend(loc=2) #指定legend的位置右下角
pyplot.annotate("R$\mathrm{^2}$=%.2f"%R_square,(800,100))
pyplot.annotate("RMSE=%.2f"%RMSE,(800,50))

#设置坐标轴刻度
my_x_ticks = numpy.arange(0,1100,100)
my_y_ticks = numpy.arange(0,1100,100)
pyplot.xticks(my_x_ticks)
pyplot.yticks(my_y_ticks)
pyplot.xlim(0,1000)
pyplot.ylim(0,1000)

pyplot.xlabel('Observed PM2.5($\mathrm{\mu{g/}{m}^{3}}$)')
pyplot.ylabel('Predicted PM2.5($\mathrm{\mu{g/}{m}^{3}}$)')
pyplot.title('Linear')
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
    X_train_2, X_test_2, y_train_2, y_test_2 = X[train_2], X[test_2], y[train_2], y[test_2]
    model.fit(X_train_2,y_train_2.reshape(-1,1))
    y_test_hat_2=model.predict(X_test_2)
    TotalRMSE_2+=sqrt(metrics.mean_squared_error(y_test_2.reshape(-1,1),y_test_hat_2.reshape(-1,1)))
    R2_SUM_2+=metrics.r2_score(y_test_2.reshape(-1,1),y_test_hat_2.reshape(-1,1))
    #print R2_SUM_2
print 'The second is Shufflesplit,splits=%d'%k_2  
print 'shufflesplit MSE:',TotalRMSE_2/k_2
print 'shufflesplit R2:',R2_SUM_2/k_2
