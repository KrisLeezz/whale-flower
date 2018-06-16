#import csv

#csv_2015_file=open('G:/PM_vs_AOS_SO2_NO2_CO_O3/new_2017.csv','r')
#csv_2015_read=csv.reader(csv_2015_file)
#jan=[]
#feb=[]
#mar=[]
#apr=[]
#may=[]
#jun=[]
#jul=[]
#aug=[]
#sep=[]
#oct=[]
#nov=[]
#dec=[]
#for row in csv_2015_read:
#    if row[0]!='date':
#        month=float(row[0][4:6])
#        if month==1:
#             jan.append(row)
#        if month==2 :
#             feb.append(row)
#        if month==3 :
#             mar.append(row)
#        if month==4 :
#             apr.append(row)
#        if month==5 :
#            may.append(row)
#        if month==6 :
#            jun.append(row)
#        if month==7 :
#            jul.append(row)
#        if month==8 :
#            aug.append(row)
#        if month==9 :
#            sep.append(row)
#        if month==10 :
#            oct.append(row)
#        if month==11 :
#            nov.append(row)
#        if month==12 :
#            dec.append(row)

#csv_jan_file=open('jan.csv','ab')
#csv_jan_write=csv.writer(csv_jan_file)
#csv_jan_write.writerows(jan)
#csv_jan_file.close()
#csv_feb_file=open('feb.csv','ab')
#csv_feb_write=csv.writer(csv_feb_file)
#csv_feb_write.writerows(feb)
#csv_feb_file.close()
#csv_mar_file=open('mar.csv','ab')
#csv_mar_write=csv.writer(csv_mar_file)
#csv_mar_write.writerows(mar)
#csv_mar_file.close()
#csv_apr_file=open('apr.csv','ab')
#csv_apr_write=csv.writer(csv_apr_file)
#csv_apr_write.writerows(apr)
#csv_apr_file.close()
#csv_may_file=open('may.csv','ab')
#csv_may_write=csv.writer(csv_may_file)
#csv_may_write.writerows(may)
#csv_may_file.close()
#csv_jun_file=open('jun.csv','ab')
#csv_jun_write=csv.writer(csv_jun_file)
#csv_jun_write.writerows(jun)
#csv_jun_file.close()
#csv_jul_file=open('jul.csv','ab')
#csv_jul_write=csv.writer(csv_jul_file)
#csv_jul_write.writerows(jul)
#csv_jul_file.close()
#csv_aug_file=open('aug.csv','ab')
#csv_aug_write=csv.writer(csv_aug_file)
#csv_aug_write.writerows(aug)
#csv_aug_file.close()
#csv_sep_file=open('sep.csv','ab')
#csv_sep_write=csv.writer(csv_sep_file)
#csv_sep_write.writerows(sep)
#csv_sep_file.close()
#csv_oct_file=open('oct.csv','ab')
#csv_oct_write=csv.writer(csv_oct_file)
#csv_oct_write.writerows(oct)
#csv_oct_file.close()
#csv_nov_file=open('nov.csv','ab')
#csv_nov_write=csv.writer(csv_nov_file)
#csv_nov_write.writerows(nov)
#csv_nov_file.close()
#csv_dec_file=open('dec.csv','ab')
#csv_dec_write=csv.writer(csv_dec_file)
#csv_dec_write.writerows(dec)
#csv_dec_file.close()
#csv_2015_file.close()

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
