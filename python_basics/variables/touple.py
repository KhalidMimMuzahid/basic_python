# 1:16:30
# https://www.youtube.com/watch?v=jBzwzrDvZ18
#  tuples are immutable in Python. Once a tuple is created, we cannot change its values
three_number=(1,2,3)
three_number_2=tuple((1,2,3))#tuple using tuple constructor
print(type(three_number_2)) #<class 'tuple'>
# three_number[2]=45 #Error:TypeError: 'tuple' object does not support item assignment

strings=("Bangladesh", "Canada", "United States")
numbers=(1,2,3,4,5)
bools=(True, False, False, True)
mixtures= ("Bangladesh",1,True) ## Tuple allow to store different types of data
print(three_number[2])
print(strings)
print(numbers)
print(mixtures)
print(type(mixtures)) #<class 'tuple'>