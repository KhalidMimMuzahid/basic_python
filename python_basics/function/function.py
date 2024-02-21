def greetings_function(name="Khalid", age=18):  #we can set the  default value
    print("Welcome "+ str(name)+ ". Your are "+str(age)+ " years old.") # for every single indentation, it takes 4 separate spaces
greetings_function("Khabib", 27)

def show_my_friends(*friends): # using *friends, it will be a tuple with all of the values that will be passed
    print("your friends are ",friends)
show_my_friends("Shameem", "Habib", "Ashik")