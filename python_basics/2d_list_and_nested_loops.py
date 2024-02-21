# my_list=[1,2,3,4]
# print(my_list)
my_2d_list=[ #<class 'list'>
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(my_2d_list)
# print(type(my_2d_list)) #<class 'list'>
# print(my_2d_list[1][1])
for row in my_2d_list:
    print("row:",row)
    for element in row:
        print("     element:",element)