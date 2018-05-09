import csv
csv_file1=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/2017_all_air.csv','r')
csv_read=csv.reader(csv_file1)
csv_file2=open('spring2.csv','ab')
csv_write2=csv.writer(csv_file2)
csv_file3=open('summar2.csv','ab')
csv_write3=csv.writer(csv_file3)
csv_file4=open('autumn2.csv','ab')
csv_write4=csv.writer(csv_file4)
csv_file5=open('winter2.csv','ab')
csv_write5=csv.writer(csv_file5)
csv_file6=open('all2.csv','ab')
csv_write6=csv.writer(csv_file6)
for row in csv_read:
    #print row
    if row[0]!='date':
        csv_write6.writerow(row)
        if row[0][4:6]=='01'or row[0][4:6]=='02'or row[0][4:6]=='12':
            csv_write5.writerow(row)
        elif row[0][4:6]=='03'or row[0][4:6]=='04'or row[0][4:6]=='05':
            csv_write2.writerow(row)
        elif row[0][4:6]=='06'or row[0][4:6]=='07'or row[0][4:6]=='08':
            csv_write3.writerow(row)
        elif row[0][4:6]=='09'or row[0][4:6]=='10'or row[0][4:6]=='11':
            csv_write4.writerow(row)
csv_file2.close()     
csv_file1.close()
csv_file3.close()  
csv_file4.close()  
csv_file5.close()  
csv_file6.close()  
