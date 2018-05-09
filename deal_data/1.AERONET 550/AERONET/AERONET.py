#功能：AOD插值
import math
import csv
from csv import DictReader
#读取当下文件夹中的csv文件到一个list里
import glob
csv_list=glob.glob("G:\AERONET\V3_AERONET\deal\Interpolation_550\Interpation_550\*.csv")
for n in range(0,len(csv_list)):#这个代表文件的个数
    filename=csv_list[n].split('\\')[-1]
    filename=filename[:-4]
    csv_file1=open(csv_list[n],"r")
    csv_reader=csv.DictReader(csv_file1)

    colums=[row for row in csv_reader]
    nn=n+1
    print "process the %d csv,get the data in the csv"%nn
    csv_file1.close()
    #计算行数
    i=0
    for row in colums:
        i+=1
    #print i
    #按照字典查询获取需要的参数
    date=[row["Date(dd:mm:yyyy)"]for row in colums]
    time=[row["Time(hh:mm:ss)"]for row in colums]
    y1=[row["AOD_440nm"]for row in colums]
    y2=[row["AOD_675nm"]for row in colums]
    aa=[row["440-675_Angstrom_Exponent"]for row in colums]
    print "get 3 parameters"
    #写入表头文件
    tablename=["Date(dd:mm:yyyy)","Time(hh:mm:ss)","AOT_440nm","AOT_675nm","angstrom","calute angstrom","AOT_550nm_angstrom","AOT_550nm_caluteangstrom"]
    csv_file2=open("G:\AERONET\V3_AERONET\deal\Interpolation_550\Interpation_550/Interpolation_%s.csv"%filename,"wb")
    csv_write=csv.writer(csv_file2)
    csv_write.writerow(tablename)
    csv_file2.close()
    #写入数据，防止覆盖重追加模式重新打开
    csv_file3=open("G:\AERONET\V3_AERONET\deal\Interpolation_550\Interpation_550/Interpolation_%s.csv"%filename,"ab")
    csv_write1=csv.writer(csv_file3)
    invalid_num=0
    for ii in range(0,i):
        if y1[ii]=='-999' or y2[ii]=='-999':
            #print y1[ii],y2[ii]
            csv_write1.writerow([date[ii],time[ii],y1[ii],y2[ii],aa[ii],-999,-999,-999])
            invalid_num+=1
        else:
            a=-math.log(float(y1[ii])/float(y2[ii]))/math.log(440.0/675.0)#埃指数的计算
            y3=float(y2[ii])*math.pow(550.0/675.0,-float(aa[ii]))#根据站点给出的埃指数计算
            y4=float(y2[ii])*math.pow(550.0/675.0,-float(a))#根据自己计算的a来计算
            csv_write1.writerow([date[ii],time[ii],y1[ii],y2[ii],aa[ii],a,y3,y4])#原来我在这里墨迹了好久，总是按照行输出，原来我去加一个中括号就行了，就变成了列输出
    
    print 'the %s file is processed,total %d points,%d invalue datas' %(filename,i,invalid_num)
    csv_file3.close()
total_file_num=n+1
print "************************you have finished it successfully,total %d files******************************"%total_file_num


