import csv
csv_file1=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/new_2017.csv','r')
csv_read1=csv.reader(csv_file1)

csv_file2=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/new_2015_2017.csv','ab')
csv_write=csv.writer(csv_file2)

for row in csv_read1:
    if row[0]!='date':
        csv_write.writerow(row)
csv_file1.close()
csv_file2.close()