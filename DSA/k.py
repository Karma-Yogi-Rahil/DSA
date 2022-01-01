st = "9:00am-10:00am"
def CountingMinutes(str):
    from datetime import datetime, time

    a = st.split("-")
    print(a)

    new_a = []

    for i in a :
        time_12 = datetime.strptime(i,"%I:%M%p")
        print(time_12)
        time_24 = datetime.strptime(time_12,"%H:%M")
        a.append(time_24)


    a = new_a
    for i in range(len(a)) :
        for j in range(1,len(a)) :
            if a[i] > a[j]:
                minutes  = a[i]-a[j]

            else:
                minutes = a[j]-a[i] 


    return minutes 


