print '#############################################tiff read#####################################'

from osgeo import gdal
import numpy
#from numpy import newaxis
new_img=[]
dataset_read= gdal.Open("r20161215.tif")
img_read_name=dataset_read.GetDescription()#文件名
img_read_band=dataset_read.RasterCount#波段数
img_read_width,img_read_height=dataset_read.RasterXSize,dataset_read.RasterYSize#X是宽（列数），Y是高（行数）
img_read_geotrans=dataset_read.GetGeoTransform()#获得空间参考（仿射矩阵），六参数坐标转换模型，分别为左上角X坐标，像元X方向大小、旋转信息，左上角Y坐标，像元Y方向大小、旋转信息，Y方向像元大小为负数
img_read_proj=dataset_read.GetProjection()#获取投影信息
img_read_Metdata=dataset_read.GetMetadata()#参数结果：水平解析度，垂直解析度，第三个不知道，只有三个tag???

img_read_data=dataset_read.ReadAsArray(0,0,img_read_width,img_read_height)#获得数据,参数说明xOffset,yOffset,cols,rows
img_read_dtype=img_read_data.dtype.name
print img_read_data[40][2]

dataset_read2 = gdal.Open("r20161215so2.tif")
img_read_data2=dataset_read2.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data2[40][2]

dataset_read3 = gdal.Open("r20161215no2.tif")
img_read_data3=dataset_read3.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data3[40][2]

dataset_read4 = gdal.Open("r20161215co.tif")
img_read_data4=dataset_read4.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data4[40][2]

dataset_read5 = gdal.Open("r20161215o3.tif")
img_read_data5=dataset_read5.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data5[40][2]

dataset_read6 = gdal.Open("r20161215air.tif")
img_read_data6=dataset_read6.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data6[40][2]

dataset_read7 = gdal.Open("r20161215rh.tif")
img_read_data7=dataset_read7.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data7[40][2]

dataset_read8 = gdal.Open("r20161215wind.tif")
img_read_data8=dataset_read8.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data8[40][2]

dataset_read9 = gdal.Open("r20161215pres.tif")
img_read_data9=dataset_read9.ReadAsArray(0,0,img_read_width,img_read_height)
print img_read_data9[40][2]
for i in range(0,66):
    a=[]
    a=numpy.dstack((img_read_data[i],img_read_data2[i],img_read_data3[i],img_read_data4[i],img_read_data5[i],img_read_data6[i],img_read_data7[i],img_read_data8[i],img_read_data9[i]))
    if i==0:
        new_img=a
    else:
        new_img=numpy.vstack((new_img,a))

print new_img.shape
x_img = new_img.reshape(-1,9,order='C')#没问题
y_img= model.predict(x_img)
img_write_data=y_img.reshape(img_read_height,img_read_width,1)#注意顺序，重新整理成图像的维度

img_write_dtype=gdal.GDT_Float64#待写入文件的类型
#创建文件
driver=gdal.GetDriverByName("GTiff")
dataset_write = driver.Create("MOD_PM_20140126.tif",img_read_width,img_read_height,img_read_band,img_write_dtype)#只有最后的参数int->float
dataset_write.SetGeoTransform(img_read_geotrans)#仿射变换参数
dataset_write.SetProjection(img_read_proj)#投影信息
dataset_write.GetRasterBand(1).WriteArray(img_write_data)#因为只有一个band所以是(1)
del dataset_write

