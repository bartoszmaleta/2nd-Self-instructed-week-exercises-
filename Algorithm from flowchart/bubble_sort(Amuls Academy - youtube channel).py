# bubble sort in python :

# WORKING BUBBLE SORT WITH CONSTANT LIST:

# list = [10, 15, 4, 23, 0]
# print('Unsorted list: ', list) 

# for j in range(len(list) - 1):
#     for i in range(len(list) - 1 - j):
#         # if remove "-j", there will be all iterations
#         if list[i] > list[i + 1]: 
#             # descending order change the sign to '<'
#             list[i], list[i + 1] = list[i + 1], list[i]
#             print(list)
#         else:
#             print(list)
#     print()

# print('Sorted list: ', list)

# __________________________________
# __________________________________
# __________________________________
# __________________________________


# WORKING BUBBLE SORT WITH GIVEN/INSERTED LIST:

list = []
num = int(input('How many number you want to enter: '))
x = 0
print()
print('YOUR VALUES: ')
print()
for k in range(num):
    # for x in enumerate(list):
    #     f'{format(x + 1)}'
    list.append(int(input('Enter number: ')))

print('Unsorted list: ', list) 

for j in range(len(list) - 1):
    for i in range(len(list) - 1 - j):
        # if remove "-j", there will be all iterations
        if list[i] > list[i + 1]: 
            # descending order --> change the sign to '<'
            list[i], list[i + 1] = list[i + 1], list[i]
    #         print(list)  # 1st row
    #     else:            # 2nd row
    #         print(list)  # 3rd row
    # print()              # 4th row  
# comment 4 rows to get ONLY sorted and unsorted lists


print('Sorted list: ', list)
