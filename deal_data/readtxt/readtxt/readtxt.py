#功能：忘了- -，貌似是有用的
#打开待存储AOD的csv文件
import csv
csv_filename=open("AERONET_4_MODIS_MOD_AOD.csv","r")
csv_read=csv.reader(csv_filename)
csv_rows=[row for row in csv_read]
#print rows3
n=0
for row in csv_rows:
    n+=1
print "There are %d days that need to deal with"%(n-1)
csv_filename.close()
print "********************get the time**************************"


#获取文件夹中的txt
import glob
txt_list=glob.glob("2014*.txt")#txt_list存储的是txt文件的名字
month=txt_list[0][4:6]#获得月份信息,month是str
n1=len (txt_list)#获得当月的处理天数
print "%s month, %d files need to be processed" %(month,n1)
print "********************get the files' names**************************"
#创建待写入文件，字典的形式
filename=["data","beijing","beijing_radi","beijing_CAMS","bxianghe"]
csv_filename2=open("L_AERONET_4_MODIS_MOD_AOD.csv",'wb')
csv_write=csv.writer(csv_filename2)
csv_write.writerow(filename)
#print csv_rows[1][0]
#print txt_list[0][0:8]
for row in csv_rows:#从csv的表格开始
    datalist=[row[0],"","","",""]#临时存储每一行的数据
    for i in range(0,n1):#第一个csv的日期在txt名字的表里搜寻一样的       
        if row[0]==txt_list[i][0:8]:#rows3[i][0]后面的0是固定的，变化的是i,范围是1~367，就是n2-1////#txt_list[i][0:8],i与n1有关
            #找到文件后打开
            #csv_write.writerow({'data':row[0]})
            txt_filename=open(txt_list[i],'r')
            txt_rows=txt_filename.readlines()#读取内容
            #读取后四条记录           
            for ii in range(-4,0):
                #print txt_rows[ii]#获取的是一整条记录
                aaa=txt_rows[ii]
                print [aaa]
                aaa=aaa.strip()
                #print [aaa]
                #txt_rows[ii].replace('\n','')
                txt_rowssplit=aaa.split(",")
                #print txt_rowssplit[-1]#获取待写入的AODtxt
                datalist[ii+5]=txt_rowssplit[-1]
            #csv_write.writerow(datalist)
            txt_filename.close()
    if row[0]!='data':
        csv_write.writerow(datalist)
print "********************get the MODIS AOD**************************"
csv_filename2.close()

