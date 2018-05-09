#仅仅为了测试
import os
import sys
from datetime import datetime
path='G:/MODIS/NEW_MODIS/2017c6.1/ALL-AOD'
f=os.listdir(path)
file_num=0
for i in f:
    if i.endswith('Deep_Blue_Aerosol_Optical_Depth_550_Land_Best_Estimate.tif'):
        file_num=file_num+1#计数
        oldname=i
        oldname_split=i.split('.')
        sensor_type=oldname_split[0]
        AOD_date=oldname_split[1][1:8]
        AOD_collection=oldname_split[3]
        oldname_split_split=oldname_split[6].split('-')
        #AOD_name=oldname_split_split[0]
        AOD_name='DB_Best_Estimate_550_AOD'
        file_type='.'+oldname_split[-1]

        #转换日期
        YEAR=int(AOD_date[0:4])
        DAY=int(AOD_date[4:7])
        if YEAR%4 ==0:
            k=1
        else:
            k=0

        if 0<DAY<=31:
            month =1
            day =DAY
        elif 31<DAY<=59+k:
            month =2
            day =DAY-31
        elif 59+k<DAY<=90+k:
            month =3
            day =DAY-59-k
        elif 90+k<DAY<=120+k:
            month =4
            day =DAY-90-k
        elif 120+k<DAY<=151+k:
            month =5
            day =DAY-120-k
        elif 151+k<DAY<=181+k:
            month =6
            day =DAY-151-k
        elif 181+k<DAY<=212+k:
            month =7
            day =DAY-181-k
        elif 212+k<DAY<=243+k:
            month =8
            day =DAY-212-k
        elif 243+k<DAY<=273+k:
            month =9
            day =DAY-243-k
        elif 273+k<DAY<=304+k:
            month =10
            day =DAY-273-k
        elif 304+k<DAY<=334+k:
            month =11
            day =DAY-304-k
        elif 334+k<DAY<=365+k:
            month =12
            day =DAY-334-k
        elif DAY<0 or DAY>365+k:
            print 'DAY error'
        dt = datetime(YEAR, month, day)
        print str(DAY)+'-->'+str(dt)

        AOD_year=str(YEAR)
        if month<10:
            AOD_month='0'+str(month)
        else:
            AOD_month=str(month)
        if day<10:
            AOD_day='0'+str(day)
        else:
            AOD_day=str(day)
        newname=sensor_type+'_'+AOD_collection+'_'+AOD_year+AOD_month+AOD_day+'_'+str(DAY)+'_'+AOD_name+file_type
        os.chdir(path)
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
    else: continue
print "the number of day is",file_num


