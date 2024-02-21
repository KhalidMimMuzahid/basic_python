countries_file=open('/media/khalid/Coding/Practices/python/python_basics/files/countries.txt','r') # for reading
# open('/media/khalid/Coding/Practices/python/python_basics/files/countries.txt','w') #for writing
# open('/media/khalid/Coding/Practices/python/python_basics/files/countries.txt','a') #for appending
# open('/media/khalid/Coding/Practices/python/python_basics/files/countries.txt','r+') # for reading and writing

# print(countries_file.readline()) # it will print the first line from the file
# print(countries_file.readline()) # it will print the second line from the file
# print(countries_file.readline()) # it will print the third line from the file

# print(countries_file.readlines()[2]) #It will print the 3rd line , hence index starts from 0
for line in countries_file.readlines(): # It will print from index 0 line to last index index line
    print(line)

countries_file.close()