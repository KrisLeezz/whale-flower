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
