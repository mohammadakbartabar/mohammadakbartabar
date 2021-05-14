# mind that this program thinks that you where born at 00:00:00 
# this app is based on the Gregorian calender
print("salam ")
name= input("esm khod ra benevisid"":")
print("khosh amadi",name)
sal_tavalod= int(input("sal tavalod khod ra vared konid"))
mah_tavalod= int(input('mah tavalod khod ra vared konid'))
roz_tavalod= int(input("roz tavalod khod ra vared konid "))
import datetime
date_and_time = datetime.datetime.now()
year = (date_and_time.year)
month = (date_and_time.month)
day = (date_and_time.day)
hour = (date_and_time.hour)
minute = (date_and_time.minute)
second = (date_and_time.second)
if mah_tavalod <= month:
    age_year = year - sal_tavalod
    age_month = month - mah_tavalod
else :
    age_year = (year - sal_tavalod) - 1
    age_month = 12 + (month - mah_tavalod)
    if roz_tavalod <=day :
      age_day = day - roz_tavalod
    else:
        age_day =  30 + (day - roz_tavalod)
        age_month = age_month - 1
age_hour = hour 
age_minute = minute 
age_second = second
print (age_year ,'years' ,age_month ,'months' ,age_day ,'days' ,
                age_hour ,'hours' ,age_minute ,'minutes' ,age_second ,'seconds')
