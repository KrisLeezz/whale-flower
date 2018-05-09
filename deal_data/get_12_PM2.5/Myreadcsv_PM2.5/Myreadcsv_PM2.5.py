#功能：从地面监测文件中提取出需要的 站点的大致时间的结果
#改成批量处理的话只需要改动文件的名字就行了

# -*- coding: utf-8 -*-
#read csv
import csv
#读取当下文件夹中的csv文件到一个list里
import glob
csv_list=glob.glob("beijing_all_*.csv")
for i in range(97,359):#这里根据文件需要进行修改
    print csv_list[i]
    csv_file1=open(csv_list[i],"r")
    print csv_file1
    csv_read1=csv.reader(csv_file1)
    rows1=[row for row in csv_read1]
    #print rows
    #按照时间提取了需要的大行
    choose_row_head=rows1[0]
    choose_row1=rows1[46] 
    choose_row2=rows1[51] 
    choose_row3=rows1[56] 
    choose_row4=rows1[61] 
    choose_row5=rows1[66] 
    choose_row6=rows1[71]
    choose_row7=rows1[76]
    csv_file1.close()
    print "---------------------------------------------get data is okay!---------------------------------------------------------"
    #write csv
    #csv_list_writename_M[i]="M_%str"%csv_list[i]
    #print csv_list_writename_M[i]
    print "M_%s"%csv_list[i]
    csv_file2=open("M_%s"%csv_list[i],"wb")
    csv_write2=csv.writer(csv_file2)
    csv_write2.writerow(choose_row_head) 
    for ii in range(1,8):
        csv_write2.writerow(rows1[41+ii*5])
    print "---------------------------------------------write in a middle csv file!------------------------------------------------"
    csv_file2.close()
    #借着上一步的中间文件，按字典读取
    csv_file3=open("M_%s"%csv_list[i],"r")
    csv_read3=csv.DictReader(csv_file3)
    fieldnames=csv_read3.fieldnames
    print fieldnames
    print "----------------------------------------------dictory reads okay-------------------------------------------------------"
    colums=[row for row in csv_read3]
    #按照字典查询
    choose_colum0=[row["hour"] for row in colums]
    choose_colum1=[row["东四"] for row in colums]
    choose_colum2=[row["天坛"] for row in colums]
    choose_colum3=[row["官园"] for row in colums]
    choose_colum4=[row["万寿西宫"] for row in colums]
    choose_colum5=[row["奥体中心"]for row in colums]
    choose_colum6=[row["农展馆"] for row in colums]
    choose_colum7=[row["万柳"] for row in colums]
    choose_colum8=[row["古城"] for row in colums]
    choose_colum9=[row["顺义"] for row in colums]
    choose_colum10=[row["昌平"] for row in colums]
    choose_colum11=[row["怀柔"] for row in colums]
    choose_colum12=[row["定陵"] for row in colums]
    #insert()函数插入到指定位置，后面的元素后移
    choose_colum0.insert(0,"hour".decode("utf8").encode("gbk"))
    choose_colum1.insert(0,"dongsi".decode("utf8").encode("gbk"))
    choose_colum2.insert(0,"tiantan".decode("utf8").encode("gbk"))
    choose_colum3.insert(0,"guanyuan".decode("utf8").encode("gbk"))
    choose_colum4.insert(0,"wanshouxigong".decode("utf8").encode("gbk"))
    choose_colum5.insert(0,"aotizhongxin".decode("utf8").encode("gbk"))
    choose_colum6.insert(0,"nongzhanguan".decode("utf8").encode("gbk"))
    choose_colum7.insert(0,"wanliu".decode("utf8").encode("gbk"))
    choose_colum8.insert(0,"gucheng".decode("utf8").encode("gbk"))
    choose_colum9.insert(0,"shunyixincheng".decode("utf8").encode("gbk"))
    choose_colum10.insert(0,"changping".decode("utf8").encode("gbk"))
    choose_colum11.insert(0,"huairou".decode("utf8").encode("gbk"))
    choose_colum12.insert(0,"dingling".decode("utf8").encode("gbk"))
    #查询结果写入文件
    #csv_file_writename_L[i]="L_%str"%csv_list[i]
    csv_file4=open("L_%s"%csv_list[i],"wb")
    csv_write4=csv.writer(csv_file4)#这个时候csv_write4是空的
    csv_write4.writerow(choose_colum0)
    csv_write4.writerow(choose_colum1)
    csv_write4.writerow(choose_colum2)
    csv_write4.writerow(choose_colum3)
    csv_write4.writerow(choose_colum4)
    csv_write4.writerow(choose_colum5)
    csv_write4.writerow(choose_colum6)
    csv_write4.writerow(choose_colum7)
    csv_write4.writerow(choose_colum8)
    csv_write4.writerow(choose_colum9)
    csv_write4.writerow(choose_colum10)
    csv_write4.writerow(choose_colum11)
    csv_write4.writerow(choose_colum12)

    print"*******************************Finish it successfully!***************************************"
    csv_file4.close()
    csv_file3.close()
