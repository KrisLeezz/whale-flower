#-*-coding=utf-8 -*-
import netCDF4
import datetime
from netCDF4 import Dataset
from netCDF4 import num2date
from matplotlib import pyplot
import numpy 
from mpl_toolkits.basemap import Basemap
import csv
ncdata=Dataset('G:\downscaling\GCMs\pr_day_bcc-csm1-1_historical_r1i1p1_18500101-20121230.nc','r')
print ncdata.variables.keys
time=ncdata.variables['time'][:]#366天
lons=ncdata.variables['lon'][:]
lats=ncdata.variables['lat'][:]
rhum=ncdata.variables['pr'][0:10000]
rhum_units=ncdata.variables['pr'].units

#转化nc文件时间的算法
dates=num2date(ncdata.variables['time'][:],ncdata.variables['time'].units)

#print dates[1]
#print dates[1].hour
#time_idx=237#2012年随便的一天
##python和reanalysis时间的统计上是有差异的
#offset = datetime.timedelta(hours=6)#timedelta代表的是一个时间间隔的函数 
#dt_time=[datetime.date(1,1,1)+datetime.timedelta(hours=t)-offset for t in time]
##date 是datetime中的一个对象，表示一个时间.其形式为date(year,month,day),所有的参数都是必须的
#cur_time=dt_time[time_idx]

#中心坐标点
lon_0 = lons.mean()
lat_0 = lats.mean()

m = Basemap(lat_0=lat_0, lon_0=lon_0)
lon, lat =numpy.meshgrid(lons, lats)#meshgrid()格网化
xi, yi = m(lon, lat)


#取得每天6：00全球rhum
for i in range (0,10000):
    if i%4==1:
        rhum_0 = rhum[999,::, ::]#对应的变量是时间，纬度，经度的函数
        print dates[i]
        
print rhum.shape
#并没有对数值做插值处理
cs = m.pcolor(xi, yi, numpy.squeeze(rhum_0))#这里rhum_0表示的是最后一天6：00的rhum数据///pcolor()根据传入的data，绘制伪彩色图像//squeeze去除维度为1的维

# Add Grid Lines
# 绘制经纬线
m.drawparallels(numpy.arange(-90., 91., 20.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(numpy.arange(-180., 181., 40.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(rhum_units)

# Add Title
date=str(dates[i])
pyplot.title('%s Surface humidity'%date)
#HR_LON,HR_LAT=116.644,40.3937
#DL_LON,DL_LAT=116.17,40.2865
#CP_LON,CP_LAT=116.23,40.1952
#SY_LON,SY_LAT=116.72,40.1438
#AT_LON,AT_LAT=116.407,40.0031
#HD_LON,HD_LAT=116.315,39.9934
#NZ_LON,NZ_LAT=116.473,39.9716
#DS_LON,DS_LAT=116.434,39.9522
#GY_LON,GY_LAT=116.361,39.9425
#GC_LON,GC_LAT=116.225,39.9279
#TT_LON,TT_LAT=116.434,39.8745
#WSXG_LON,WSXG_LAT=116.366,39.8673
csv_file=open('G:\downscaling\china_america_meterology\data_daily_summary\usa_5_station\position_5.csv','r')
csv_read=csv.reader(csv_file)

date=[row for row in csv_read]
#LONS=[116.644,116.17,116.23,116.72,116.407,116.315,116.473,116.434,116.361,116.225,116.434,116.366]
#LATS=[40.3937,40.2865,40.1952,40.1438,40.0031,39.9934,39.9716,39.9522,39.9425,39.9279,39.8745,39.8673]
LONS=[]
LATS=[]
site=[]
for row in date:
    if row[0]!='Station':
        LONS.append(row[2])
        LATS.append(row[1])
        site.append(row[0])
LONS=numpy.array(LONS)
LATS=numpy.array(LATS)
LONS=LONS.astype('float')+360
LATS=LATS.astype('float')
#LON,LAT=numpy.meshgrid(LONS,LATS)

X_SITE,Y_SITE=m(LONS,LATS)
m.plot(X_SITE,Y_SITE,'b+')
pyplot.show()
ncdata.close()