def find_leap_years(given_year):
    list= []

    # Write your logic here
    count = 0

    while count <=15:
        if given_year %4==0 or given_year%100==0 and given_year%400:
                count+=1
                list.append(given_year)
                    

        given_year +=1

    

    return list[1:]

        
                    
                  

list_of_leap_years = find_leap_years(1000)
print(list_of_leap_years)