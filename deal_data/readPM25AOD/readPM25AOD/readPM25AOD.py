#功能：貌似是用于卫星AOD与地面站点数据匹配的，结果直接用于后面的程序建模
#建立站点名称list，注意顺序需要和卫星导出保持一致，这样后面不会乱
site_list=['huairou_1009','dingling_1002','changping_1010','shunyixincheng_1008','aotizhongxin_1011','wanliu_1007','nongzhanguan_1005','dongsi_1003','guanyuan_1006','gucheng_1012','tiantan_1004','wanshouxigong_1001']
#site_list=['dongsi_1003']
n1=len(site_list)
#print site_list
import csv
import glob
import datetime
#AOD
txt_list=glob.glob("2014*.txt")
#PM2.5
all_list=glob.glob("L_beijing_all_2014*.csv")
#print txt_list
n2=len(txt_list)
n3=len(all_list)
#print n

#for row in csv_reader:
#    print row[1]#时间
#    print row[0]#日期
for i in range(0,n1):#最外层站点循环
    site1=site_list[i]
    site=site1.split('_')
    print "the processing site is '%s'"%site[0]
    site_add='_'+site[1]+'A'+'_'+site[0]
    #只是提供时间记录
    csv_file2=open('PM2.5%s.csv'%site_add,'r')
    csv_reader=csv.reader(csv_file2)
    csv_rows=[row for row in csv_reader]
    line1=len(csv_rows)#获得行数，便于下面进行循环
    #待写入文件
    csv_file=open('MYD_2014_5_%sA.csv'%site_list[i],'wb')
    csv_write=csv.writer(csv_file)
    csv_write.writerow(['date','time','AOD','PM2.5'])
    #csv_file3=open('')
    #获得当前循环站点AOD
    for ii in range(0,n2):#当前站点循环AOD
        txt_filename=open(txt_list[ii],'r')
        txt_rows=txt_filename.readlines()#读取内容
        date=txt_list[ii][0:8]
        #print date
        a=txt_rows[i+1]#分割字符串
        aa=a.split(',')
        #print aa
        aaa=aa[-1]
        #print aaa
        if aaa!='\n':
            aod=float(aaa)
            #获得卫星过境的时间
            for iii in range(0,line1):#
                if csv_rows[iii][0]==date:
                    time=csv_rows[iii][1]
                    #time1=datetime.datetime.strptime(time,'%H:%M:%S')#用于后面时间加减
                    #print time[0]
                    if time!="":#时间可能缺失
                        #获得地面站点的PM2.5均值
                        try:
                            csv_file3=open('L_beijing_all_%s.csv'%date,'r')
                            csv_reader2=csv.reader(csv_file3)
                            csv_rows2=[row2 for row2 in csv_reader2]
                            n4=len(csv_rows2)
                        except:
                            break
                        ###################时间匹配#########################时间是从0开始的，代表的是过去一小时的PM2.5均值
                        ##时间的处理,获得上下界
                        #time_down=time1-datetime.timedelta(hours=1)
                        time_down=int(time[0])-1+8
                        #csv_rows2=[row for row in csv_reader2]
                        #print csv_rows
                        time_row=csv_rows2[0]#获得时间行
                        try:#异常处理：假如这个时间，在存储时间的文件中可能有缺失的
                            index1=time_row.index(str(time_down))
                            index2=time_row.index(str(time_down+1))
                            index3=time_row.index(str(time_down+2))
                            #print index1,index2,index3#获得当行的列索引
                        except:
                            continue#被来应该是pass，证明缺失这个时间的PM2.5数据，寻找下一天
                            #提取对应时间的地面站点PM2.5取平均值，利用了上面的索引
                        for iiii in range(0,n4):#改成行数
                            if csv_rows2[iiii][0]==site[0]:#取文件中的该站点的行的位置
                                if csv_rows2[iiii][index1]!=''and csv_rows2[iiii][index2]!=''and csv_rows2[iiii][index3]!='':#三个值缺一，则卫星过境时没有对应的地面PM2.5数据
                                    PM_avr=(float(csv_rows2[iiii][index1])+float(csv_rows2[iiii][index2])+float(csv_rows2[iiii][index3]))/3
                                    print PM_avr
                                    csv_write.writerow([date,time,aod,PM_avr])
                                    break
                        #csv_write.writerow([date,time,aod,PM_avr])
                        break
                    else:
                        break
                else:
                    continue
        else:
            aod=''
            continue
