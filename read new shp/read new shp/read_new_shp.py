#整合气象变量
import csv
import shapefile

csv_file=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/2015_all.csv','r')
csv_read=csv.reader(csv_file)
csv_file2=open('test.csv','ab')
csv_write=csv.writer(csv_file2)
for row in csv_read:
    if row[0]!='id':
        print row[-1]
        csv_site_id=row[0]
        csv_year=row[-1][0:4]
        csv_month=row[-1][4:6]
        csv_day=row[-1][6:8]
        shp_date=str(csv_year)+'_'+str(csv_month)+'_'+str(csv_day)
        air_sf = shapefile.Reader('G:/NCEP_V2.0/2015pres/pres_%s_6'%shp_date) 
        air_points=air_sf.records()
        for air_point in air_points:
            air_site_id=air_point[1]#获取站点ID
            airtemperature=air_point[-1]#获得变量信息
            if csv_site_id==air_site_id:
                row.append(airtemperature)              
                csv_write.writerow(row)
                break
csv_file.close()
csv_file2.close()