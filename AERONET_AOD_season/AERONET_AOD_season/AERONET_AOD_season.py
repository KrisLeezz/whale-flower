import csv
csv_file1=open("G:/AERONET/2017_aeronet_vs_AOD/AERONET_vs_AOD_WIN1_Beijing_RADI.csv","r")
csv_date1=csv.reader(csv_file1)
csv_file2=open("G:/AERONET/2017_aeronet_vs_AOD/AERONET_vs_AOD_WIN3_Beijing_RADI.csv","r")
csv_date2=csv.reader(csv_file2)
csv_file3=open("G:/AERONET/2017_aeronet_vs_AOD/AERONET_vs_AOD_WIN5_Beijing_RADI.csv","r")
csv_date3=csv.reader(csv_file3)
csv_file4=open("AERONET_vs_AOD_winter.csv","ab")
csv_write=csv.writer(csv_file4)
for row1 in csv_date1:
    row1_=row1[0].split('/')
    month=row1_[1]
    if month=='12'or month=='1'or month=='2':
        for row2 in csv_date2:
            if row1[0]==row2[0]:
                row1.append(row2[1])
                for row3 in csv_date3:
                    if row1[0]==row3[0]:
                        row1.append(row3[1])
                        csv_write.writerow(row1)
                        break
                break
csv_file4.close()
csv_file3.close()
csv_file2.close()
csv_file1.close()
