import arcpy
import csv
import numpy
csv_file=open('G:/Arcgis/78+5.csv')
csv_read=csv.reader(csv_file)
#data=[row for row in csv_read]
id=[]
lon=[]
lat=[]
for row in csv_read:
    if row[0]!='id':
        id.append(row[0])
        lon.append(row[-2])
        lat.append(row[-1])
lon=numpy.array(lon)
lat=numpy.array(lat)
for i in range(0,len(lon)):
    LON=float(lon[i])
    LAT=float(lat[i])
    print 'lat=%f,lon=%f'%(LAT,LON)
    print 'site%s'%id[i]
    arcpy.MakeNetCDFTableView_md(\
        'G:/NCEP/airtemperature/air.2m.gauss.2015.nc','rhum','air_2m_gauss_2015_nc_%s'%id[i],"time","lat=%f,lon=%f"%(LAT,LON),"BY_VALUE")
    arcpy.CopyRows_management('air_2m_gauss_2015_nc_%s'%id[i], "G:/TABLE/TABLE.gdb/air_2m_gauss_2015_nc_%s"%id[i])