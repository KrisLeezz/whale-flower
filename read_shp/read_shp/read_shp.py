#AERONET与AOD匹配
import shapefile
import glob
import datetime
import csv
#读取AOD的信息
f1=glob.glob('G:/Arcgis/shape/MYD_2017/*win5.shp')#根据窗口数进行更改!!!!!
print 'total win number file is %d'%len(f1)
shpe_name=[]
for ff1 in f1:
    ff1_name=ff1.split('\\')[-1][:-4]
    shpe_name.append(ff1_name)

#读取AERONET
f2=glob.glob('G:/AERONET/V3_AERONET/deal/Interpolation_550/Interpation_550/*.csv')
AERONET_name=[]
for ff2 in f2:
    ff2_name=ff2.split('\\')[-1]
    AERONET_name.append(ff2_name)

for i in range(len(shpe_name)):#365个文件
     
        sf = shapefile.Reader('G:/Arcgis/shape/MYD_2017/%s'%shpe_name[i])#必须要带着shx,shp,dbf等等一系列文件,这三个是必须的
        if sf!='NULL':
            #获取AOD的时间
            AOD_date_year=int(shpe_name[i][13:21][0:4])
            AOD_date_month=int(shpe_name[i][13:21][4:6])
            AOD_date_day=int(shpe_name[i][13:21][6:9])
            AOD_date_hour=5
            AOD_date_minute=30
            AOD_date_second=00
            AOD_date=str(AOD_date_year)+'-'+str(AOD_date_month)+'-'+str(AOD_date_day)+','+str(AOD_date_hour)+':'+str(AOD_date_minute)+':'+str(AOD_date_second)
            AOD_dt_time=datetime.datetime.strptime(AOD_date,"%Y-%m-%d,%H:%M:%S")
            #时间选取的上下界
            dt_up=AOD_dt_time-datetime.timedelta(minutes=30)
            dt_down=AOD_dt_time+datetime.timedelta(minutes=30)
            #print sf.fields#其实相当于属性表的表头ID,LON,LAT,VALUES...
            points=sf.records()#12+4=16条记录
            #point_num=len(points)
            #print "total %d point"%point_num
       
            #获取站点的AOD值
            #for point in points:
            #    print point
            #print points[0:5]#AERONET站点顺序分别是：A01香河，A02北京_RADI,A03北京，A04北京_CAMS，A05北京_PKU
            #站点的时间都是一样的
            #print points[0]
            #print points[1]#!!!!
            #print points[2]
            #print points[3]
            print points[4]
            if points[4][-1]!='' and points[4][-1]!=0:#确认当天有卫星AOD后!!!!!!!!!!!!!
                sum_aod=0#累加计数
                n_aod=0
                csv_filename=open('G:/AERONET/V3_AERONET/deal/Interpolation_550/Interpation_550/%s'%AERONET_name[4],'r')#根据站改序号!!!!!!!!!!
                csv_reader=csv.reader(csv_filename)
                Aeronet=[row for row in csv_reader]
                for row in Aeronet:
                    if row[0]==str(AOD_date_year)+'/'+str(AOD_date_month)+'/'+str(AOD_date_day):
                        AERONET_dt_time=datetime.datetime.strptime(row[0]+','+row[1],"%Y/%m/%d,%H:%M:%S")
                        if dt_up<=AERONET_dt_time<=dt_down:
                            if row[6]!='-999':
                                sum_aod=sum_aod+float(row[6])
                                n_aod=n_aod+1
                            elif row[6]=='-999':
                                sum_aod=sum_aod
                                n_aod=n_aod
                if n_aod!=0:
                    aod=sum_aod/n_aod
                    a=[str(AOD_date_year)+'/'+str(AOD_date_month)+'/'+str(AOD_date_day),points[4][-1],aod]#!!!!
                    print a
                    csv_write_file=open("AERONET_vs_AOD_WIN5_Beijing_PKU.csv","ab")#!!!!
                    csv_write=csv.writer(csv_write_file)
                    csv_write.writerow(a)
                    csv_write_file.close()
                else:continue
                    #a=[str(AOD_date_year)+'/'+str(AOD_date_month)+'/'+str(AOD_date_day),'','']
                    #print a
                    #csv_write_file=open("AERONET_vs_AOD_WIN1_Beijing_PKU.csv","ab")#!!!!
                    #csv_write=csv.writer(csv_write_file)
                    #csv_write.writerow(a)
                    #csv_write_file.close()
            else:continue
                #a=[str(AOD_date_year)+'/'+str(AOD_date_month)+'/'+str(AOD_date_day),'','']
                #print a
                #csv_write_file=open("AERONET_vs_AOD_WIN1_Beijing_PKU.csv","ab")#!!!!
                #csv_write=csv.writer(csv_write_file)
                #csv_write.writerow(a)
                #csv_write_file.close()

        else:
            print"read failed"
            continue
   
