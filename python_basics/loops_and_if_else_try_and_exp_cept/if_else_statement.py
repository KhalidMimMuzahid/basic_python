def check_number_even_or_odd(number):
    result=None
    if number%2 ==0 :
        result="even" 
    else:
        result="odd"
    return result
number = int(input("Enter the number: "))
print(str(number)+" is "+ check_number_even_or_odd(number))     