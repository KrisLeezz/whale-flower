#获得数据,作用是生成一个包含所有数据的csv文档
f=glob.glob('G:/PM_vs_AOS_SO2_NO2_CO_O3/all/*.csv')
print 'total win number file is %d'%len(f)
file_name=[]#1319
file_path=[]#1319
for ff in f:
    ff_name=ff.split('\\')[-1][:-4]
    file_name.append(ff_name)
    file_path.append(ff)

data=[]#1319
for i in range(0,len(f)):
    csv_file=open(file_path[i])
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        if row[3]!='AOD_win1':
            if row[3]!='0'and row[6]!='0'and row[7]!='0'and row[8]!='0'and row[9]!='0'and row[10]!='0':
                #data1=numpy.array(row)
                #print file_name[i][-8:]
                row.append(file_name[i][-8:])
                #print row
                csv_file_all=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/all_2.csv','ab')
                csv_write_all=csv.writer(csv_file_all)
                csv_write_all.writerow(row)
                csv_file_all.close()
                data.append(row)
            else:continue
        else:continue
    #data1=[row for row in csv_reader]
    #data1=numpy.array(data1)
    ##print data1.shape
    #data.append(data1[1:])
data=numpy.array(data)
print data.shape
#三个index:文件1319，站点80，项目11
aod1=data[::,::,3:4]
aod_1=aod1.reshape(-1,1)
AOD_win1=aod_1.astype(float)#
aod3=data[::,::,4:5]
aod_3=aod3.reshape(-1,1)
AOD_win3=aod_3.astype(float)#
aod5=data[::,::,5:6]
aod_5=aod5.reshape(-1,1)
AOD_win5=aod_5.astype(float)#
pm=data[::,::,6:7]
pm=pm.reshape(-1,1)
PM=pm.astype(float)#y
so2=data[::,::,7:8]
so2=so2.reshape(-1,1)
SO2=so2.astype(float)#
no2=data[::,::,8:9]
no2=no2.reshape(-1,1)
NO2=no2.astype(float)#
co=data[::,::,9:10]
co=co.reshape(-1,1)
CO=co.astype(float)#
o3=data[::,::,10:11]
o3=o3.reshape(-1,1)
O3=o3.astype(float)#

