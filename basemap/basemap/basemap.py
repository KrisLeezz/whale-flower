# -*-coding=utf-8 -*-
from mpl_toolkits.basemap import Basemap  
import numpy as np  
import matplotlib.pyplot as plt 

#参考网址 http://matplotlib.org/basemap/users/cyl.html  
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon  是地图上下左右四个点经纬度值  
# resolution = 'c'，粗分辨率的海岸线
# projection='cyl'，等距圆柱投影  
m = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='c')  
#海岸线
m.drawcoastlines(color='black')
#填充颜色
#1.陆地和湖
m.fillcontinents(color='peru',lake_color='paleturquoise')
#2.剩余部分，也就是海？
m.drawmapboundary(fill_color='dodgerblue')  
# 画平行线和子午线，说白了就是格网 
m.drawparallels(np.arange(-90.,91.,30.))#平行线
m.drawmeridians(np.arange(-180.,181.,60.))#子午线
##国家
#m.drawcountries() 
##北美州
#m.drawstates()
##河流
#m.drawrivers()  
lon, lat = -104.237, 40.125  
xpt,ypt = m(lon,lat)#從lat,lon變換到plt中的坐標系  
lonpt, latpt = m(xpt,ypt,inverse=True)#從plt的坐標系變換到lat,lon  
m.plot(xpt,ypt,'bx')#bx是所畫的點的顏色形狀   
plt.title("Equidistant Cylindrical Projection")  
plt.show()  
#####################################################################################################
## setup Lambert Conformal basemap.兰伯特投影
## set resolution=None to skip processing of boundary datasets.没有数据集的处理
#m = Basemap(width=12000000,height=9000000,projection='lcc',
#            lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.,resolution=None)
## draw a land-sea mask for a map background.
## lakes=True means plot inland lakes with ocean color.
#m.drawlsmask(land_color='peru',ocean_color='aqua',lakes=True)
#plt.show()
#####################################################################################################
## setup Lambert Conformal basemap.
## set resolution=None to skip processing of boundary datasets.
#m = Basemap(width=12000000,height=9000000,projection='lcc',
#            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
#m.bluemarble()
#plt.show()