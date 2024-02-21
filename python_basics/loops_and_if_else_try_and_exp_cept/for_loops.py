for letter in "Hello, world": # loop over on string
    print(letter)
friends=["Khalid", "Shameem", "Maruf", "Habib"]

for friend in friends: # loop over on list
    print(friend)
    if(friend == "Maruf"): 
        break

countries=("Bangladesh", "Canada", "United States")
for country in countries: # loop over on touple
    print(country)

my_dict={
    "name":"Khalid", 
    "nationality": "Bangladeshi",
    "age": 26,
    "is_tall": True,
    "Qualification": "Bsc in CSE",
    "friends": ["Ashik", "Shameem", "Rakib"],
}
for each in my_dict: # loop over on dict
    print(each+ ": ", my_dict[each])

for x in range(10):
    if x == 5: continue # when x will comes to 5, then this loop will be skipped for this value and loop will start with the next value
    if x == 8: break # when x will come to 8, then this loop will be break / end
    print(x)

for x in range (3,10): # it will print from 3 to 9
    print(x)
else: 
    print("loop has finished")