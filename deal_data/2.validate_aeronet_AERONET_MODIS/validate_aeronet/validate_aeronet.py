#功能：用于AOD验证，涉及到时间匹配，但是程序的容错性不好，而且不是完全自动的，需要在进行改进
#四个站点是分开的
import time
import csv
import datetime
usetime1=time.time()
csv_filename1=open("MYD2014windows3.csv",'r')
csv_reader1=csv.reader(csv_filename1)

csv_filename2=open("L_Beijing_RADI.csv",'r')
csv_reader2=csv.reader(csv_filename2)
csv_readeAeronet=[row for row in csv_reader2]
#print csv_readeAeronet
count=0#有效记录计数
n=0
for row in csv_readeAeronet:
    n=n+1
#print n
csv_filename3=open("MYD_windows3_aeronet_beijing_RADI.csv","wb")#不同的站改名字
csv_writer1=csv.writer(csv_filename3)
csv_writer1.writerow(["Date","Time","3_beijing_RADI","beijing_RADI"])#不同的站改名字

for row1 in csv_reader1:
    if row1[0]!="data" and row1[2]!="":#beijing站是2
        #避免写入标题行,row[1]若为空的话意味着没有数据也要调到下一条，但是要输出：有数据的话循环到下变的
        date1=row1[0][0:4]+"-"+row1[0][4:6]+"-"+row1[0][6:8]
        year1=date1[0:4]#获得当前年、月、日
        month1=date1[5:7]
        #month1=str(int(month1))
        day1=date1[8:10]
        #day1=str(int(day1))
        time1=row1[1]+":00"
        #print date1+","+time1
        dt_time1=datetime.datetime.strptime(date1+","+time1,"%Y-%m-%d,%H:%M:%S")#用于后面时间加减
        print "the current processing time is %s"%dt_time1
        #时间的处理,获得上下界
        dt_up=dt_time1-datetime.timedelta(minutes=15)
        #print dt_up
        dt_down=dt_time1+datetime.timedelta(minutes=15)
        #print dt_down
        i=0#平均计数的
        ii=0
        a1=0#平均累加的
        #确定了当前数据，开始循环AERONET站的数据
        for nn in range(0,n):
            if csv_readeAeronet[nn][0]!="Date(dd-mm-yy)":#这里可以加一个对a1！=0的if,因为这里的数据是按照时间排序的，有值就证明已经匹配上了
                #print csv_readeAeronet[nn][0]
                time2=csv_readeAeronet[nn][3]#先获取时间，因为这个文件时间存储格式的问题，比较麻烦
                date2=csv_readeAeronet[nn][2]+"-"+csv_readeAeronet[nn][1]+"-"+csv_readeAeronet[nn][0]
                #这里时间有错误，当变成几十的天数时会有问题
                dt_time2=datetime.datetime.strptime(date2+","+time2,"%Y-%m-%d,%H:%M:%S")
                #print dt_time2
                str_dt_time2=str(dt_time2)
                year2=str_dt_time2[0:4]
                month2=str_dt_time2[5:7]
                day2=str_dt_time2[8:10]                               
                #time2=row2[3]                  
                if year1==year2:
                        #print "year is same"
                    if month1==month2:
                            #print "month is same"
                        if day1==day2:#
                            ii=ii+1
                                #print"day is same"
                            #dt_time2=datetime.datetime.strptime(date2+","+time2,"%Y-%m-%d,%H:%M:%S")
                            print "    ","-->the date is same, loop time is %s"%dt_time2
                            if dt_up<=dt_time2<=dt_down:
                                #a1+=float(csv_readeAeronet[nn][8])
                                a1+=float(csv_readeAeronet[nn][8])*1000#乘以MODIS比例系数，减小误差
                                i+=1
                            else:
                                print "        ","the time %s don't match"%dt_time2
                        else:
                            #print "the day don't match"
                            continue
                    else:
                        #print "the month don't match"
                        continue
                else:
                    continue
        if row1[2]!="":
            if a1!=0:
                print a1
                aa1=float(a1)/(i)
                #print aa1
                row1.insert(3,aa1)
                #print row1
                print row1[0:4]
                csv_writer1.writerow(row1[0:4])
                count=count+1
            else:
                aa1=""#代表没值
                row1.insert(3,aa1)
                print row1[0:4]
                csv_writer1.writerow(row1[0:4])
        else:
            row1.insert(3,"")
            csv_writer1.writerow(row1[0:4])
    elif row1[0]!="data":#这行的作用是写入初标题行外的空行，缺当前站点的MODIS数据   
        row1.insert(3,"")#插入空值
        print row1[0:4]
        csv_writer1.writerow(row1[0:4])#如果该行为标题或者空行，将当前行写入新的文件中
print "the total valided record is %d"%count
print "********************Finish**********************"
csv_filename1.close()
csv_filename2.close()
csv_filename3.close()
usetime2=time.time()
print "the time used is %f"%((usetime2-usetime1)/60)



