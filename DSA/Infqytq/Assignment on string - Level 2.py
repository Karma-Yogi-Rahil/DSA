#lex_auth_012693816331657216161

from types import prepare_class


def encode(message):
    Expected_output= ''
    count = 0
    i=0
    privious = message[0]
    #Remove pass and write your logic here
    while i < len(message):
        if privious == message[i]:
            count +=1
        else:
            Expected_output+=str(count)+privious
            count=1
            privious=message[i]
        

        if i==len(message)-1:
            Expected_output += str(count) + privious
        i+=1



    return Expected_output
            

#Provide different values for message and test your program
encoded_message=encode("A")
print(encoded_message)