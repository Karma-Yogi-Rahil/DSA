
s = '12:45:54PM'

hour = s[0:2].strip()
Mimutes = s[3:5]
secounds = s[6:8]
am_pm = s[8:]
print(hour,Mimutes,secounds,am_pm)

if am_pm == "PM":
    if hour =='12':
        hour_24 = hour
    else:   
        hour_24 = int(hour)+12

else:
    if hour == '12':
        hour_24 = '00'
    else:
        hour_24 = hour


print(str(hour_24).strip()+":"+str(Mimutes).strip()+":"+str(secounds).strip())

