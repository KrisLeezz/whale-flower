#PM2.5与AOD的匹配
#按照一年一年的处理
import shapefile
import csv
import glob

#获取shp的名字AOD
f1=glob.glob('G:/Arcgis/shape/MYD_2014/*win1.shp')#win1
shpe_win1_name=[]
for ff1 in f1:
    ff1_name=ff1.split('\\')[-1][:-4]
    shpe_win1_name.append(ff1_name)

f2=glob.glob('G:/Arcgis/shape/MYD_2014/*win3.shp')#win3
shpe_win3_name=[]
for ff2 in f2:
    ff2_name=ff2.split('\\')[-1][:-4]
    shpe_win3_name.append(ff2_name)

f3=glob.glob('G:/Arcgis/shape/MYD_2014/*win5.shp')#win5
shpe_win5_name=[]
for ff3 in f3:
    ff3_name=ff3.split('\\')[-1][:-4]
    shpe_win5_name.append(ff3_name)

shp_num=len(shpe_win1_name)
print 'total win number file is %d'%shp_num
#获取csv的名字PM
#f2=glob.glob('G:/Air Quality/process_data/site_20150101-20151231/*.csv')
#PM_name=[]
#for ff2 in f2:
#    ff2_name=ff2.split('\\')[-1]
#    PM_name.append(ff2_name)
#csv_num=len(PM_name)

#读取shp,里面是每一天的78个站的卫星AOD数据
for i in range(0,shp_num):#循环完365天的数据
    sf1= shapefile.Reader('G:/Arcgis/shape/MYD_2014/%s'%shpe_win1_name[i])
    sf3= shapefile.Reader('G:/Arcgis/shape/MYD_2014/%s'%shpe_win3_name[i])
    sf5= shapefile.Reader('G:/Arcgis/shape/MYD_2014/%s'%shpe_win5_name[i])
    if sf1!='NULL':
        #获取AOD的时间
        AOD_date=shpe_win1_name[i][13:21]
        #获取点的记录
        win1_points=sf1.records()
        win3_points=sf3.records()
        win5_points=sf5.records()
        points_num=len(win1_points)#以win1窗口为例
        #根据shp_date open 同一天的PM csv文件
        csv_date=AOD_date
        print 'the current processing is %s'%AOD_date
        #try的目的是防止文件打不开
        try:
            csv_file=open('G:/Air Quality/process_data/site_20140513-20141231/china_sites_%s.csv'%csv_date,"r")#!!!!
            csv_reader=csv.reader(csv_file)
            if csv_reader!='':
                #创建一个文件准备存储读好的信息
                csv_write_file1=open("G:/PM_vs_AOS_SO2_NO2_CO_O3/2014_PM_vs_AOD_%s.csv"%csv_date,"wb")
                csv_write1=csv.writer(csv_write_file1)
                title=['id','lon','lat','AOD_win1','AOD_win3','AOD_win5','PM2.5','so2','no2','co','o3']
                csv_write1.writerow(title)
                csv_write_file1.close()
                PM_data=[row for row in csv_reader]
                #print len(PM_data)
                #print PM_data[0]
                for ii in range(5,points_num):#循环读78个站点数据
                    #print points[ii] #当前站的整条AOD数据
                    #用于累加平均PM,so2,no2
                    pm_add=0
                    pm_add_n=0
                    so2_add=0
                    so2_add_n=0
                    no2_add=0
                    no2_add_n=0
                    co_add=0
                    co_add_n=0
                    o3_add=0
                    o3_add_n=0
                    #处理处理数据 得到当前的站点号 site_id,当前站点的AOD数据
                    site_id=win1_points[ii][0]
                    #site_aod=points[ii][-1]
                    #返回当前站在csv表中的位置
                    p=PM_data[0].index(site_id)
                    #取12，13，14的值准备进行平均
                    for row in PM_data:
                        if row[1]=='12':#12：00
                            if row[p]!='':
                                if row[2]=='PM2.5':
                                    pm_add+=float(row[p])
                                    pm_add_n+=1
                                elif row[2]=='SO2':
                                    so2_add+=float(row[p])
                                    so2_add_n+=1
                                elif row[2]=='NO2':
                                    no2_add+=float(row[p])
                                    no2_add_n+=1
                                elif row[2]=='CO':
                                    co_add+=float(row[p])
                                    co_add_n+=1
                                elif row[2]=='O3':
                                    o3_add+=float(row[p])
                                    o3_add_n+=1
                        if row[1]=='13':#13：00
                            if row[p]!='':
                                if row[2]=='PM2.5':
                                    pm_add+=float(row[p])
                                    pm_add_n+=1
                                elif row[2]=='SO2':
                                    so2_add+=float(row[p])
                                    so2_add_n+=1
                                elif row[2]=='NO2':
                                    no2_add+=float(row[p])
                                    no2_add_n+=1
                                elif row[2]=='CO':
                                    co_add+=float(row[p])
                                    co_add_n+=1
                                elif row[2]=='O3':
                                    o3_add+=float(row[p])
                                    o3_add_n+=1
                        if row[1]=='14':#14：00
                            if row[p]!='':
                                if row[2]=='PM2.5':
                                    pm_add+=float(row[p])
                                    pm_add_n+=1
                                elif row[2]=='SO2':
                                    so2_add+=float(row[p])
                                    so2_add_n+=1
                                elif row[2]=='NO2':
                                    no2_add+=float(row[p])
                                    no2_add_n+=1
                                elif row[2]=='CO':
                                    co_add+=float(row[p])
                                    co_add_n+=1
                                elif row[2]=='O3':
                                    o3_add+=float(row[p])
                                    o3_add_n+=1
                    if pm_add_n!=0:
                        pm=pm_add/pm_add_n
                    else:
                        pm=0
                    if so2_add_n!=0:
                        so2=so2_add/so2_add_n
                    else:
                        so2=0
                    if no2_add_n!=0:
                        no2=no2_add/no2_add_n
                    else:
                        no2=0
                    if co_add_n!=0:
                        co=co_add/co_add_n
                    else:
                        co=0
                    if o3_add_n!=0:
                        o3=o3_add/o3_add_n
                    else:
                        o3=0
                    a=[win1_points[ii][0],win1_points[ii][-3],win1_points[ii][-2],win1_points[ii][-1],win3_points[ii][-1],win5_points[ii][-1]]
                    a.append(pm)
                    a.append(so2)
                    a.append(no2)
                    a.append(co)
                    a.append(o3)
                    #print a
                    ##写入csv文件中wb
                    csv_write_file2=open("G:/PM_vs_AOS_SO2_NO2_CO_O3/2014_PM_vs_AOD_%s.csv"%csv_date,"ab")#追写，避免覆盖
                    csv_write2=csv.writer(csv_write_file2)
                    csv_write2.writerow(a)
                    csv_write_file2.close()
            else:print 'error'
            csv_file.close()
        except: print '*****************************china_sites_%s is error*******************************'%csv_date
    else:print'shp file error'
   