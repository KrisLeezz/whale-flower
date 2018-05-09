import arcpy
import datetime
from arcpy.sa import *

#arcpy.env.workspace = "G:/NCEP/work.gdb"

for i in range(91,365):
    dt_day=datetime.datetime.strptime("2017-1-1 12:00:00","%Y-%m-%d %H:%M:%S")#初始的天数
    dt_time_1=dt_day+datetime.timedelta(days=i)
    dt_time_2=dt_time_1+datetime.timedelta(hours=6)
    date1=dt_time_1.strftime("%Y-%m-%d %H:%M:%S")
    date2=dt_time_2.strftime("%Y-%m-%d %H:%M:%S")
    name1=date1.split()
    name1=name1[0].split('-')
    outfile1=name1[0]+'_'+name1[1]+'_'+name1[2]+'_12'
    name2=date2.split()
    name2=name2[0].split('-')
    outfile2=name2[0]+'_'+name2[1]+'_'+name2[2]+'_18'
    inNetCDFFile = 'G:/NCEP/pressure/pres.sfc.2017.nc'
    variable ='pres'
    XDimension = "lon"
    YDimension = "lat"
    outRasterLayer_1 = 'pres_%s'%outfile1
    outRasterLayer_2 = 'pres_%s'%outfile2
    bandDimmension = ''
    date_1=['time',date1]
    date_2=['time',date2]
    dimensionValues_1=[date_1]
    dimensionValues_2=[date_2]
    valueSelectionMethod = 'BY_VALUE'
    arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, variable,XDimension, YDimension,outRasterLayer_1, bandDimmension, dimensionValues_1,valueSelectionMethod)
    arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, variable,XDimension, YDimension,outRasterLayer_2, bandDimmension, dimensionValues_2,valueSelectionMethod)
    #提取点
    inPointFeatures = "78_BJ_TJ_HB_PM2.5.shp"
    inRaster_1= outRasterLayer_1
    inRaster_2= outRasterLayer_2
    outPointFeatures_1= "G:/NCEP/work_2017_pres.gdb/%s"%outRasterLayer_1
    outPointFeatures_2="G:/NCEP/work_2017_pres.gdb/%s"%outRasterLayer_2
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    # Execute ExtractValuesToPoints
    ExtractValuesToPoints(inPointFeatures, inRaster_1, outPointFeatures_1,"INTERPOLATE", "VALUE_ONLY")
    ExtractValuesToPoints(inPointFeatures, inRaster_2, outPointFeatures_2,"INTERPOLATE", "VALUE_ONLY")
    arcpy.Delete_management(outRasterLayer_1)
    arcpy.Delete_management(outRasterLayer_2)
    #arcpy.Delete_management(inNetCDFFile)
    arcpy.Delete_management(inRaster_1)
    arcpy.Delete_management(inRaster_2)
    #arcpy.Delete_management(inPointFeatures)


