#-*- coding=utf-8 -*-
import arcpy
import csv
import numpy
csv_file=open('G:\downscaling\china_america_meterology\data_daily_summary\usa_5_station\position_5.csv','r')
csv_read=csv.reader(csv_file)
#data=[row for row in csv_read]
id=[]
lon=[]
lat=[]
for row in csv_read:
    if row[0]!='id':
        id.append(row[0])
        lat.append(row[-2])
        lon.append(row[-1])
lon=numpy.array(lon)
lat=numpy.array(lat)
for i in range(0,len(lon)):
    LON=float(lon[i])+360
    LAT=float(lat[i])
    print 'lat=%f,lon=%f'%(LAT,LON)
    print 'site%s'%id[i]
	#这种方式取点按照先谁取谁的原则
    arcpy.MakeNetCDFTableView_md(\
        'G:\downscaling\GCMs\pr_day_bcc-csm1-1_historical_r1i1p1_18500101-20121230.nc','pr','bbc_pr_%s'%id[i],"time","lon %f;lat %f"%(LON,LAT),"BY_VALUE")
    arcpy.CopyRows_management('bbc_pr_%s'%id[i], "G:\downscaling\GCMs\pr\\bbc_pr_%s.csv"%id[i])