from sklearn.decomposition import PCA
import csv
import numpy
from sklearn import preprocessing
def standar_scale(a):
    standar_scaler = preprocessing.StandardScaler()#与a1的效果一样
    a_standarscale=standar_scaler.fit_transform(a)
    return a_standarscale

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
csv_file_read=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/2015_all_air.csv')
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
        all_x.append(row[4:16])
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
all_x = numpy.delete(all_x, 3, axis=1)#去掉PM
print all_x.shape

X=all_x[:,2:]
X=standar_scale(X)
print 'shpe=',X.shape
print 'Mean=',X.mean(axis=0)#列
print 'Std=',X.std(axis=0)

pca = PCA(n_components='mle')
pca.fit(X)#用数据来训练PCA模型
new_X=pca.fit_transform(X)
print pca.explained_variance_ratio_
print new_X.shape
print X.shape

