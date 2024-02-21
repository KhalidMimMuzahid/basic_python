try:
    x= int(input('input an integer: '))
    print(x)
    y= 10/x
    print(y)
except ValueError: # only when , this error is a ValueError
    print("ValueError, please try again.")
except ZeroDivisionError:  # only when , this error is a ZeroDivisionError
    print("ZeroDivisionError, please try again.")
except: # if this error is not match any of above errors, then this block will be executed
    print("Something went wrong, please try again.")
else: # only when , there have not any error, then this block will be execute
    print("nothing went wrong.")
finally: # this block always will be executed after finishing this try-except
    print("try except finished")