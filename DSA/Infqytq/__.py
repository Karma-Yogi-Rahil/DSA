def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    ticket_numbers = 100 
    for i in range(1,no_of_passengers+1):
        print(ticket_numbers)
        print(i)
        ticket_numbers = ticket_numbers+1

        
        #a = airline+":"+ source[:3]+":"+destination[:3]+":"+ str(ticket_numbers)
        ticket_number_list.append(airline+":"+ source[:3]+":"+destination[:3]+":"+ str(ticket_numbers))

            

    #Use the below return statement wherever applicable
    if no_of_passengers >5:
        return ticket_number_list[-5:]
    else:
        return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))