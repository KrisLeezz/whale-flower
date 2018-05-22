# -*- coding: utf-8 -*-
import numpy
import arcpy
import csv
#获得数据
wind_u=[]
wind_v=[]
wind_direction=[]
csv_file_read=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/new_2017.csv','r')
csv_read=csv.reader(csv_file_read)
csv_writefile=open('d.csv','wb')
csv_write=csv.writer(csv_writefile)
a=[]
for row in csv_read:
    if row[0]!='date':
        wind_u=float(row[-3])
        wind_v=float(row[-2])
        d=math.atan2( wind_u,wind_v)*180/3.1415926+180
        csv_write.writerow([d])


csv_file_read.close()
csv_writefile.close()
