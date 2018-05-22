import csv

csv_2015_file=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/new_2017.csv','r')
csv_2015_read=csv.reader(csv_2015_file)
spring=[]
summar=[]
autumn=[]
winter=[]
for row in csv_2015_read:
    if row[0]!='date':
        month=float(row[0][4:6])
        if month==12 or month==1 or month==2:
            winter.append(row)
        if month==3 or month==4 or month==5:
            spring.append(row)
        if month==6 or month==7 or month==8:
             summar.append(row)
        if month==9 or month==10 or month==11:
             autumn.append(row)
csv_spring_file=open('spring.csv','ab')
csv_spring_write=csv.writer(csv_spring_file)
csv_spring_write.writerows(spring)
csv_spring_file.close()
csv_summar_file=open('summar.csv','ab')
csv_summar_write=csv.writer(csv_summar_file)
csv_summar_write.writerows(summar)
csv_summar_file.close()
csv_autumn_file=open('autumn.csv','ab')
csv_autumn_write=csv.writer(csv_autumn_file)
csv_autumn_write.writerows(autumn)
csv_autumn_file.close()
csv_winter_file=open('winter.csv','ab')
csv_winter_write=csv.writer(csv_winter_file)
csv_winter_write.writerows(winter)
csv_winter_file.close()
csv_2015_file.close()


