
# 1 - Sum row value 
# row: 1
# result: 22
def sum_row(array2D,row):
    sum = 0
    for num in array2D[row]:
        sum += num
    return sum
array2D = [
  [2, 4, 6, 8],
  [5, 7, 9, 1],
  [3, 5, 8, 3],
  [4, 1, 7, 9]
]
number = sum_row(array2D,1)
print(number)
#2 - Sum column value
# col: 2
# result: 30

def sum_column(array2D, column):
    sum = 0
    for col in array2D:
        sum += col[column]
    return sum
array2D = [
  [2, 4, 6, 8],
  [5, 7, 9, 1],
  [3, 5, 8, 3],
  [4, 1, 7, 9]
]
number_column = sum_column(array2D,2)
print(number_column)
#3 - Check number on row and column is odd or even number
# col: 2
# row: 3
# result: 7 is odd number

def odd_num(arr2D,row_index,col_index):
    num=arr2D[row_index][col_index]
    if num %2 == 1:
        return arr2D[row_index][col_index]
arr2D = [
    [2, 4, 6, 8],
    [5, 7, 9, 1],
    [3, 5, 8, 3],
    [4, 1, 7, 9]
]
result = odd_num(arr2D,3,2) 
print(result) 


#4 - Count all odd number
def odd_number(array2D):
    count = 0
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] % 2 ==1:
                count += 1
    return count
array2D = [
  [2, 4, 6, 8],
  [5, 7, 9, 1],
  [3, 5, 8, 3],
  [4, 1, 7, 9]
]
print(odd_number(array2D))



#5 - Replace value to star
# Result:
# [
#   [2, 4, 6, '*'], 
#   [5, 7, '*', 1], 
#   [3, '*', 8, 3], 
#   ['*', 1, 7, 9]
# ]
def replace(arr2D):
    for i in range(len(arr2D)):
        arr2D[i][len(arr2D[i])-1 -i]="*"
    return arr2D
arr2D = [
    [2, 4, 6, 8],
    [5, 7, 9, 1],
    [3, 5, 8, 3],
    [4, 1, 7, 9]
]
print(replace(arr2D))

#6 - Sum  column in line (like star)
# Result: 26

def replace(arr2D):
    sum=0
    for i in range(len(arr2D)):
        sum+=arr2D[i][len(arr2D[i])-1 -i]
    return sum
arr2D = [
    [2, 4, 6, 8],
    [5, 7, 9, 1],
    [3, 5, 8, 3],
    [4, 1, 7, 9]
]
print(replace(arr2D))

#7 - Replace by star like result below:
# [
# ['*', 4, 6, 8], 
# [5, '*', 9, 1],
#  [3, 5, '*', 3],
#  [4, 1, 7, '*']
# ]

def replace(arr2D):
    for i in range(len(arr2D)):
        arr2D[i][i]="*"
    return arr2D
arr2D = [
    [2, 4, 6, 8],
    [5, 7, 9, 1],
    [3, 5, 8, 3],
    [4, 1, 7, 9]
]
print(replace(arr2D))


# def greatest_sum(array1, array2):
#     sum1 = sum(array1)
#     sum2 = sum (array2)
#     if sum1 > sum2:
#         result = array1
#     elif sum2 > sum1:
#         result = array2
#     else:
#         result = "Equal"
#     return result
# array1 = [3,2,3]
# array2 = [5,8,2]
# print(greatest_sum(array1, array2))



# def replaced(array2D):
#     isChange = False
#     for value in array2D:
#         for i in range(len(value)):
#             if value[i] == 7:
#                 value[i] = 8
#                 isChange = True
#     if isChange:
#         return array2D
#     else:
#         return "Nothing to replace"
# array2D = [[2,4,],[4,6],[7,8]]
# print(replaced(array2D))



# def replaced_number(array):
#     for num in array:
#         for i in range(len(num)):
#             if num[i] == 7:
#                 num[i] = 8
#     return array
# array = [[1,2,3],[7,7,7]]
# print(replaced_number(array))



def first_number_seven(array2D):
    for num in array2D:
        for i in range(len(num)):
            if num[i] == 7:
                num = 8
    return num
arrays =[[1,4,3,5],[2,,4,7]]
print(first_number_seven(arrays))


def convert_number(array):
    for number in array:
        for i in range(len(number)):
            if number[i] == 7:
                number[i] = 8
    return number
numbers =[[1,7,3],[7,5,7]]
print(convert_number(numbers))




# def instead_numbers(array):
#     for number in array:
#         for i in range(len(number)):
#             if number[i] == 7:
#                 number[i] = 8
#     return array
# arrays = [[1,2,5,6,7],[1,5,9,12,7]]
# print(instead_numbers(arrays))





def count_number(array):
    count = 0
    for number in array:
        for i in range(len(number)):
            if number[i] == 7:
                count = 8
    return count
array2D = [[1,4,7,6,7,7,7],[3,4,7,6,5,7]]
print(count_number(array2D))



def checkRoomAvailable(array2D, row, column):
    roomFree = False
    for i in range(len(array2D)) :
        for j in range(len(array2D[i])):
            if i == row and j == column and array2D[i][j] != 1:
                roomFree = True
    return roomFree

def countRoomLive(array2D):
    countRoom = 0
    for i in range(len(array2D)) :
        for j in range(len(array2D[i])):
            if array2D[i][j] == 1:
                countRoom += 1
    return countRoom

array2D = [
            [0, 0, 1],
            [1, 0, 0],
            [0, 0, 1]
        ]
row = 0
column = 0
message = "CANNOT ADD"
if checkRoomAvailable(array2D, row, column) and countRoomLive(array2D) < 3:
    message = "CAN ADD"
print(message)


def compare(array2D1,array2D):
    sum1=0
    for arr in array2D1:
        for num in arr:
            sum1+=num
    sum2=0
    for arr in array2D:
        for num in arr:
            sum2+=num
    if sum1==sum2:
        if len(array2D1)==len(array2D):
            return "equal"
    else:
            return "not equal"
array2D1=[[0,0,0],[0,0,0]]
array2D=[[0,0,0],[1,0,0]]
print(compare(array2D1,array2D))



# def countNumber(array,number):
#     count = 0
#     for num in array:
#         if num == number:
#             count += 1
#     return count
# def already_exist(array,number):
#     already_exist = False
#     for num in array:
#         if number == num:
#             already_exist =True
#     return already_exist
# array =[9,9,9,5,6,8,9,5,54,4,4]
# new_array = []
# for num in array:
#     if countNumber(array,num) > 1 and not already_exist(new_array,num):
#         new_array.append(num)
# print(new_array)




def countNumber(array,number):
    count = 0
    for num in array:
        if num == number:
            count += 1
    return count
def already_exist(array,number):
    already_exist = False
    for num in array:
        if number == num:
            already_exist = True
    return already_exist
def find_number_more_than_one(array):
    new_array = []
    for num in array:
        if countNumber(array,num) > 1 and not already_exist(new_array,num):
            new_array.append(num)
    return new_array
array2D = [[9, 9, 8, 8, 8, 1, 3,3],[1,1,3]] 
for i in range(len(array2D)):
    array2D[i] = find_number_more_than_one(array2D[i])
print(array2D)


# def array(array2D):
#     result = []
#     for array in array2D:
#         sum_array_word = ""
#         for i in range(len(array)):
#             sum_array_word += array[i]
#         result.append(sum_array_word.lower())
#     return result
# array2D = [
# ['B', 'A', 'N', 'A', 'N', 'A'],
# ['C', 'O', 'C', 'O', 'N', 'U', 'T']
# ]
# print(array(array2D))





# def array(array2D):
#     resut = []
#     for array in array2D:
#         array_text = ""
#         for i in range(len(array)):
#             array_text += array[i]
#         resut.append(array_text.lower())
#     return resut
# array2D = [
# ['B', 'A', 'N', 'A', 'N', 'A'],
# ]
# print(array(array2D))


# array2D = [
# ["A", "B"],
# ["D", "F"],
# ["A", "A"],
# ["V", "B"],
# ]
# for row in array2D:
#     row[2] = '*'
# print(array2D)




def array(array2D,index):
    result = []
    for array in array2D:
        if index < len(array):
            array[index] = " * "  
            result.append(array)
        else:
            result = ("column error") 
    
    return result

array2D = [
    ["A", "B", "C"],
    ["D", "F", "C"],
    ["A", "A", "F"],
    ["V", "B", "C"],
]
print(array(array2D, 2))


def room_avalable(array2D, row , column):
    room = False
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if i == row and j == column and array2D[i][j] != 1:
                room = True


def count_room(array2D):
    count = 0
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] == 1:
                count += 1
    return count 
array2D = [
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 1]
           ]
print(count_room(array2D))



# def replace(array2D , number , sign):
#     for i in range(len(array2D)):
#         if array2D[i] == number:
#             array2D[i] = sign
#     return array2D
# array2D =[
#     [1,2,7,4,7],
#     [4,5,7,7,1],
#     [3,4,7,1,1]
# ]
# for arr in array2D:
#     replace(arr, 4 , "Hi")
# print(array2D)




# def replace(array2D, number , sign):
#     for i in range(len(array2D)):
#         if array2D[i] == number:
#             array2D[i] = sign
#     return array2D
# array2D =[
#     [1,2,7,4,7],
#     [4,5,7,7,1],
#     [3,4,7,1,1]
# ]
# changSign = 0
# for arr in array2D:
#     replace(arr, 3, "#")
# print(array2D)


def replace(array , number, sign):
    for i in range(len(array)):
        if array[i] == number:
            array[i]  = sign
    return array
array2D =[
    [1,2,7,4,7],
    [4,5,7,7,1],
    [3,4,7,1,1]
]
signNumber = 0
for arr in array2D:
    replace(arr, 7,"$")
print(array2D)


# def count_seven(array):
#     count = 0 
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] == 7:
#                 count += 1
#     return count
# array =  [
#   [2, 7, 4, 5],
#   [3, 4, 5, 7],
#   [7, 4, 7, 9]
# ]
# print(count_seven(array))




# def sount(array,number):
#     count = 0
#     for num in array:
#         if num == number:
#             count += 1
#     return count

# array = [
#   [2, 7, 4, 5],
#   [3, 4, 5, 7],
#   [7, 4, 7, 9]
# ]

# count_seven = 0
# for arr in array:
#     count_seven += sount(arr,7)
# print(count_seven)


# def count_number(list, number):
#     count = 0
#     for num in list:
#         if num == number:
#             count += 1
#     return count
# array =[
#     [2,7,4,5],
#     [3,4,5,7],
#     [7,4,7,9]
# ]
# count_seven_number = 0
# for arr in array:
#     count_seven_number += count_number(arr,2)
# print(count_seven_number)


def replaced_seven(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 7:
                array[i][j] = "*"
    return array
array = [
  [2, 7, 4, 5],
  [3, 4, 5, 7],
  [7, 4, 7, 9]
]
print(replaced_seven(array))


def replaced(list,number):
    for i in range(len(list)):
        if list[i] == number:
            list[i] ="*"
    return list
array2D =[
    [1,2,7,4,7],
    [4,5,7,7,1],
    [3,4,7,1,1]
]
for arr in array2D:
    replaced(arr,2)
print(array2D)


def replace(array2D,number , sign):
    for i in range(len(array2D)):
        if array2D[i] == number:
            array2D[i] = sign
    return array2D
array2D =[
    [1,2,7,4,7],
    [4,5,7,7,1],
    [3,4,7,1,1]
]
replaceNumber = 0
for arr in array2D:
    replace(arr,7,"*")
# q1. Replace all number 7 to "*"
# q2. Replace all number 1 to "*"
# q3. Replace all number 4 to "*"
# q4. Replace all number 7 to "$"
# q5. Replace all number 1 to "$"
# q6. Replace all number 4 to "$"
# q7. Replace all number 7 to "#"
# q8. Replace all number 1 to "#"
# q9. Replace all number 4 to "#"


text = input("Please enter text: ")
result = ""
for i in range(len(text)):
    if text[i] !=" ":
        print(text[i])



text = input("Please enter text: ")
result =""
for i in range(len(text)):
    if text[i] =="a" or text[i] =="A":
        if len(text)-1:
             result = result + str(i)+"-"
        else:
            result = result + str(i)
print(result)   


text = input("Please enter text: ")
result = ""
for i in range(len(text)):
    if text[i] .isupper():
        result=("Yes")
    else:
        result=("No")
print(result)


text ="3 4 5 6"
result = ""
for i in range(len(text)):
    if text[i] != " ":
        result += text[i]
print(result)


text ="3 4 5 6"
sum = 0
for i in range(len(text)):
    if text[i] != " ":
        sum +=int(text[i])
print(sum)


text = "454639"
for i in range(len(text)):
    print(text[len(text)-1-i])


text = "454639"
even_number = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        even_number += int(text[i])
print(even_number)


text = "454639"
sum = 0
for i in range(len(text)):
    sum += int(text[i])
print(sum)


text = "454639"
count_even = 0
count_odd = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(count_even, count_odd)



number = input("Enter number:")
result = 0
for i in range(len(number)):
    if int(number[i]) % 2 == 0:
        result =("Even number")
    else:
        result =("Odd number")
print(result)


number = input("Enter number: ")
if number >= str(10) and number <= str(20):
    print("Continue")
elif number <= str(10) and number >= str(20):
    print("Out of range")

text = "9394884039"
count = 0
for i in range(len(text)):
    if text[i] == "8":
        count += 1
print(count)


text = "9394884039"
isFound = False
for i in range(len(text)):
    if text[i] =="8" and not isFound == True:
        print(i)
        isFound = True


text = "3 4 5 6"
result = ""
for i in range(len(text)):
    if text[i] != " ":
        result += text[i]
print(result)


text = "3 4 5 6"
result = 0
number = ""
for i in range(len(text)):
    if text[i] !=" ":
        result = int(text[i])*2
        number += str(result)+ (" ")
print(number)


def odd_numbers(number):
    odd = []
    for i in range(len(number)):
        if number[i] % 2 ==1:
            odd.append(number[i])
    return odd
print(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


i = int(input("Choose a number: "))
if i < 0 :
	print("Your number is negative")
elif i > 5  and i < 10:
	print("Your number is greater than 5")
elif i > 10 :
	print("Your number is greater than 10")
else :
	print("Your number is between 0 and 5")


def positive_numbers(number):
    positive = []
    for i in range(len(number)):
        if number[i] > 0:
            positive.append(number[i])
    return positive
print(positive_numbers([-3, -2, -1, 0, 1, 2, 3] ))

def number_odd(number):
    odd = []
    for i in range(len(number)):
        if number[i] % 2 == 1:
            odd.append(number[i])
    return odd
print(number_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def check_room_available(array2D , row , column):
    roomFree = False
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if row == i and column == j and array2D[i][j] != 1:
                roomFree = True
    return roomFree
def room_live(array2D):
    count_room = 0
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] == 1:
                count_room += 1
    return count_room
array2D = [
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 1]
          ]
row = 0
column = 0
message = "CANNOT ADD"
if check_room_available(array2D, row, column) and room_live(array2D) < 3:
    message = "CAN ADD"
print(message)


def move_right(array2D):
    is_stoped = False
    for i in range(len(array2D)):
        for j in range(len(array2D[i])-1):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i][j+1] = '*'
                    is_stoped = True
    return array2D


def move_left(array2D):
    is_stoped = False
    for i in range(len(array2D)):
        for j in range(1, len(array2D[i])):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i][j-1] = '*'
                    is_stoped = True
    return array2D

def move_up(array2D):
    is_stoped = False
    for i in range(1,len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i-1][j] = '*'
                    is_stoped = True
    return array2D

def move_down(array2D):
    is_stoped = False
    for i in range(len(array2D)-1):
        for j in range(len(array2D[i])):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i+1][j] = '*'
                    is_stoped = True
    return array2D

def move(array2D,direction):
    if direction == "L":
        array2D = move_left(array2D)
    elif direction == "R":
        array2D = move_right(array2D)
    elif direction == "U":
        array2D = move_up(array2D)
    elif direction == "D":
        array2D = move_down(array2D)
    else:
        array2D = array2D
    
    return array2D

array2D = [
    ['0', '0', '0', '0', '0'],
    ['0', '0', '*', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]
# L,R,U,D
print(move(array2D,"U"))


# def move_star(array):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] == "*":
#                 array[i][j] = "0"
#                 array[i][j+1] = "*"
#                 break
#     return array
# array2D = [
#     ['0', '0', '0', '0', '0'],
#     ['0', '0', '0', '*', '0'],
#     ['0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0'],
# ]
# print(move_star(array2D))




# create function move star "*" to next right
# Result:

# array2D = [
#     ['0', '0', '0', '0', '0'],
#     ['0', '0', '0', '*', '0'],
#     ['0', '0', '0', '0', '0'],
#     ['0', '0', '0', '0', '0'],
# ]       

# this star move left

# def move_left(array):
#     isStar  = False
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] =="*":
#                 if isStar == False:
#                     array[i][j] = "0"
#                     array[0][j-1] = "*"
#                     isStar = True
#     return array
# array2D = [
#         ['0', '0', '0', '0', '0'],
#         ['0', '0', '*', '0', '0'],
#         ['0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0']
# ]
# print(move_left(array2D))


# this star move up

# def move_up(array):
#     isStar  = False
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] =="*":
#                 if isStar == False:
#                     array[i][j] = "0"
#                     array[i-1][j] = "*"
#                     isStar = True
#     return array
# array2D = [
#         ['0', '0', '0', '0', '0'],
#         ['0', '0', '*', '0', '0'],
#         ['0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0']
# ]
# print(move_up(array2D))


# move down

def move_down(array):
    isStar  = False
    for i in range(len(array)-1):
        for j in range(len(array[i])):
            if array[i][j] =="*":
                if isStar == False:
                    array[i][j] = "0"
                    array[i+1][j] = "*"
                    isStar = True
    return array
array2D = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '*', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
]
print(move_down(array2D))




def count_numeber(array , number):
    count = 0
    for i in range(len(array)):
        if array[i]  == number:
            count += 1
    return count
array2D = [
  [2, 7, 4, 5],
  [3, 4, 10, 7],
  [7, 4, 7, 9]
] 
number = 0
for arr in array2D:
    number += count_numeber(arr , 4)
print(number)


#5 - count number 3

def count_numeber(array , number):
    count = 0
    for i in range(len(array)):
        if array[i]  == number:
            count += 1
    return count
array2D = [
  [2, 7, 4, 5],
  [3, 4, 10, 7],
  [7, 4, 7, 9]
] 
number = 0
for arr in array2D:
    number += count_numeber(arr , 3)
print(number)


#4 - count number 7

def count_numeber(array , number):
    count = 0
    for i in range(len(array)):
        if array[i]  == number:
            count += 1
    return count
array2D = [
  [2, 7, 4, 5],
  [3, 4, 10, 7],
  [7, 4, 7, 9]
] 
number = 0
for arr in array2D:
    number += count_numeber(arr , 7)
print(number)


#3 - count number 9

def count_numeber(array , number):
    count = 0
    for i in range(len(array)):
        if array[i]  == number:
            count += 1
    return count
array2D = [
  [2, 7, 4, 5],
  [3, 4, 10, 7],
  [7, 4, 7, 9]
] 
number = 0
for arr in array2D:
    number += count_numeber(arr , 9)
print(number)


#2 - count number 2

def count_number(array , number):
    count = 0 
    for i in range(len(array)):
        if array[i] == number:
            count += 1
    return count
array2D = [
  [2, 7, 4, 5],
  [3, 4, 10, 7],
  [7, 4, 7, 9]
] 
number = 0
for arr in array2D:
    number +=count_number(arr,2)
print(number)



#1 - count number 5
def countNumber(array,number):
    count=0
    for i in range(len(array)):
        if array[i]==number:
            count+=1
    return count

array2D = [
  [2, 7, 4, 5],
  [3, 4, 10, 7],
  [7, 4, 7, 9]
] 
total=0
for arr in array2D:
    total+=countNumber(arr,5)
print(total)



# def counntEven(array):
#     count = 0
#     for i in array:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(counntEven([3,5,1,9,7,2,0]))

# def countEven(array):
#     count = 0
#     for i in range(len(array)):
#         if int(array[i]) % 2 == 0:
#             count += 1
#     return count
# print(countEven([3,5,1,9,7,2,0]))


# def countOdd(array):
#     count  = 0
#     for i in range(len(array)):
#         if int(array[i]) % 2 == 1:
#             count += 1
#     return count
# print(countOdd([3,5,1,9,7,2,0]))



def countNumbers(array):
    countEven = 0
    countOdd = 0
    for i in range(len(array)):
        if int(array[i]) % 2 == 0:
            countEven += 1
        else:
            countOdd += 1
    return str(countEven)+"\n"+str(countOdd)
print(countNumbers([3,5,1,9,7,2,0]))


# def countEven(array):
#     count = 0
#     for i in range(len(array)):
#         if int(array[i]) % 2 == 0:
#             count += 1
#     return count
# print(countEven([5,7,1,11]))




def countOdd(array):
    count = 0
    for i in range(len(array)):
        if int(array[i]) % 2 == 1:
            count += 1
    return count
print(countOdd([5,7,1,11]))



# def counntEven(array):
#     count = 0
#     for i in array:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(counntEven([3,5,1,9,7,2,0]))

# def countEven(array):
#     count = 0
#     for i in range(len(array)):
#         if int(array[i]) % 2 == 0:
#             count += 1
#     return count
# print(countEven([3,5,1,9,7,2,0]))


# def countOdd(array):
#     count  = 0
#     for i in range(len(array)):
#         if int(array[i]) % 2 == 1:
#             count += 1
#     return count
# print(countOdd([3,5,1,9,7,2,0]))



def countNumbers(array):
    countEven = 0
    countOdd = 0
    for i in range(len(array)):
        if int(array[i]) % 2 == 0:
            countEven += 1
        else:
            countOdd += 1
    return str(countEven)+"\n"+str(countOdd)
print(countNumbers([3,5,1,9,7,2,0]))


# fruits = ["apple","banana","cherry"]
# fruits.append("orange")
# print(fruits)


# fruits = ['apple','banana','cherry']
# fruits.insert(3,"orange")
# print(fruits)


# fruits = ['apple','banana','cherry']
# fruits.pop(0)
# print(fruits)



# append in array

# student = []
# student.append("name")



# [1,-1,7,-20,8]
# display positve number [1,7,8]
def positive(number):
    count = 0
    for i in range(len(number)):
        if number[i] >= 0:
            count += 1
    return count
print(positive([1,-1,7,-20,8]))



# display negative number[-1,-20]
# def negative(number):
#     count = 0
#     for i in range(len(number)):
#         if number[i] < 0:
#             count += 1
#     return count
# print(negative([1,-1,7,-20,8]))


# display odd number[1,-1,7]

# def odd(numebr):
#     odd = 0
#     for i in range(len(numebr)):
#         if int(numebr[i]) % 2 == 1:
#             odd += 1
#     return odd
# print(odd([1,-1,7,-20,8]))


# def maximum(number):
#     max = number[0]
#     for i in range(len(number)):
#         if int(number[i]) > int(max):
#             max = number[i]
#     return max
# num =["1270","3218","193"]
# for i in range(len(num)):
#     print(maximum(num[i]))




# def find_odd(array):
#     odd = 0
#     for i in range(len(array)):
#         if int(array[i]) % 2 == 1:
#             odd += int(array[i])
#     return odd
# user_input = input("Enter number: ")
# print(find_odd(user_input))


# def find_name(name):
#     print(name +"how can I know")
# find_name('Manen')



def maximum(number):
    max = number[0]
    for i in range(len(number)):
        if int(number[i]) > int(max):
            max = number[i]
    return int(max)
num = ["1270","32018","193"]
# for i in range(len(num)):
#     print(maximum(num[i]))
result = []
for number in num:
    result.append(int(max(number)))
print(result)


# Exercise 4:
#   Find first 7 in array 2D
# example1:
#   input : [[7,7,7],[0,9,7],[0,0,0]]
#   output : This is first seven locating at row 0 col 0.
# example2:
#   input : [[0,0,0],[0,9,7],[7,7,7]]
#   output : This is first seven locating at row 1 col 2
# example3:
#   input : [[0,0,0],[1,2,3]]
#   output : There is no seven found!








# def first_seven_number(number):




# def transform_array(arr):
#     result = []
#     for num in arr:
#         result.append(' '.join([str(num)] * num))
#     return '\n'.join(result)

# input_array = [2, 1, 4]
# print(transform_array(input_array))



# def count(array):
#     count = []
#     for number in array:
#         count.append(number)
#     return "\n"+ count
# print(count([2,3,4]))




# def sum(numbers):
#     sum = 0
#     for num in numbers:
#         sum += num
#     return sum
# def sum_array2D(array2D):
#     total = 0
#     for array in array2D:
#         total +=sum(array)
#     return total
# array2D = [[1,2,3],[4,5,6]]
# print(sum_array2D(array2D))


# num_array2D = [
#     [1,2,3],
#     [4,3,5],
#     [1,0,7],
#     [2,2,2]
# ]








number = "12336"
sum = 0
result = " "
for i in range(len(number)):
    if int(number[i])> 0:
        sum += int(number[i])
        result="Monday"
if sum > 0:  
    result = "Tuesday"
print(sum)






# def upper_str(string):
#     array_str = []
#     for char in string:
#         array_str.append(char.upper())
#         return array_str
# array2D = ["Banana","Mango","Apple"]
# new_array2D = []
# for i in range(len(array2D)):
#     array2D[i] =upper_str(array2D[i])
# print(array2D)



def move_right(array2D):
    is_stoped = False
    for i in range(len(array2D)):
        for j in range(len(array2D[i])-1):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i][j+1] = '*'
                    is_stoped = True
    return array2D


def move_left(array2D):
    is_stoped = False
    for i in range(len(array2D)):
        for j in range(1, len(array2D[i])):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i][j-1] = '*'
                    is_stoped = True
    return array2D

def move_up(array2D):
    is_stoped = False
    for i in range(1,len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i-1][j] = '*'
                    is_stoped = True
    return array2D

def move_down(array2D):
    is_stoped = False
    for i in range(len(array2D)-1):
        for j in range(len(array2D[i])):
            if array2D[i][j] == "*":
                if is_stoped == False:
                    array2D[i][j] = '0'
                    array2D[i+1][j] = '*'
                    is_stoped = True
    return array2D

def move(array2D,direction):
    if direction == "L":
        array2D = move_left(array2D)
    elif direction == "R":
        array2D = move_right(array2D)
    elif direction == "U":
        array2D = move_up(array2D)
    elif direction == "D":
        array2D = move_down(array2D)
    else:
        array2D = array2D
    
    return array2D

array2D = [
    ['0', '0', '0', '0', '0'],
    ['0', '0', '*', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]
# L,R,U,D
print(move(array2D,"L"))


def sumNumber(numbers):
    lastNumber = numbers
    while len(lastNumber) > 1:
        sumNumber = 0 
        for i in range(len(lastNumber)):
            sumNumber += int(lastNumber[i])
        lastNumber = str(sumNumber)
    return lastNumber
def dayByNumber(number):
    result = ""
    if number == 1:
        result = "Monday"
    elif number == 2:
        result = "Tuseday"
    elif number == 3:
        result = "Wednesday"
    elif number == 4:
        result ="Thursday"
    elif number == 5:
        result ="Friday"
    elif number == 6:
        result = "Saturday"
    elif number == 7:
        result ="Sunday"
    else:
        result = "No Day"
    return result
userInput = int(input("Enter Numbers: "))
numbers = str(userInput)
dayNumber = int(sumNumber(numbers))
print(dayByNumber(dayNumber))



def move_right(array2D):
    is_star = False
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if array2D[i][j] == "*":
                if is_star == False:
                    array2D[i][j] = "0"
                    array2D[i][j+1] = "*"
                    is_star = True
    return array2D
def move_left(array2D):
    isStar = False
    for i in range(len(array2D)):
        for j in range(1,len(array2D[i])):
            if array2D[i][j] =="*":
                if isStar == False:
                    array2D[i][j] = "0"
                    array2D[i][j-1] ="*"
                    isStar = True
    return array2D
def move_up(array2D):
    isStar = False
    for i in range(len(array2D)):
        for j in range(1,len(array2D[i])):
            if array2D[i][j] == "*":
                if isStar == False:
                    array2D[i][j] = "0"
                    array2D[i-1][j] = "*"
    return array2D
array2D = [
    ["0","0","0","0","0"],
    ["0","0","*","0","0"],
    ["0","0","0","0","0"]
]
print(move_up(array2D))


# Ex5.create function to count letter "B" or "b" in string "abcdbeB"

def count(string):
    count = ""
    for i in range(len(string)):
        if string[i] =="b" or string[i] =="B":
            count += str(string[i])
    return count
enter = input("Enter: ")
print(count(enter))


# Ex1.create function to sum number in string "1 2 3 4 5 6"

def sum(string):
    sum = 0
    for i in range(len(string)):
        if string[i] != " ":
            sum += int(string[i])
    return sum
me_input = input("enter number: ")
print(sum(me_input))



# Ex2.create function to sum odd number in string "1 2 3 4 5 6"

def sum(string):
    sum = 0
    for i in range(len(string)):
        if string[i] !=" " and int(string[i])% 2==1:
            sum += int(string[i])
    return sum
me_input = input("enter number: ")
print(sum(me_input))



# Ex3.create function to find min number in string "1 2 6 3 4 0 5"
def min(string):
  min_me = int(string[0])
  for i in range(len(string)):
    if string[i] !=" ":
        if int(string[i]) < min_me:
            min_me = int(string[i])
  return min_me
me_input = input("enter number: ")
print(min(me_input))



# def find_min_in_string(s):
#     # Step 1: Split the string by spaces
#     numbers = s.split()
    
#     # Step 2: Convert each split component to an integer
#     integers = [int(num) for num in numbers]
    
#     # Step 3: Find and return the minimum value
#     return min(integers)

# # Example usage
# s = "1 2 6 3 4 0 5"
# min_number = find_min_in_string(s)
# print(min_number)  # Output: 0


# EX4.create function to reverse string "abc" =>cda


# def reverse(string):
#     result = ""
#     for i in range(len(string)):
#         result += str(len(string)-1-i)
#     return reverse
# user_input =input("enter text: ")
# print(reverse(user_input))



def letter(string):
    result = ""
    last = len(string)-1
    for i in range(len(string)):
        result += string[last - i]
    return result
me = input("enter word: ")
print(letter(me)) 


for i in range(5):
    print("soory")



# def numbers(num1,num2):
#     total = 0   
#     if num1 == num2:
#         total = int(number1) * int(num2)
#     elif num1 != num2:
#         total = int(num1) + int(num2)
#     return total
# number1 = input("enter number: ")
# number2 = input("enter number: ")
# print(numbers(number1,number2))



def sum(num1,num2):
    sum = 0
    if num1 + num2 == 0:
        sum ="Even"
    else:
        sum = "Odd"
    return sum
num1 = input("enter number: ")
num2 = input("enter number: ")
print(sum(num1,num2))



def count_vowel(vowel):
    count_vowel = 0
    for i in range(len(vowel)):
        if vowel[i] =="A" or vowel[i] =="a":
            count_vowel += 1
        if vowel[i] =="E" or vowel[i] =="e":
            count_vowel += 1
        elif vowel[i] =="i" or vowel[i] =="i":
            count_vowel += 1
        elif vowel[i] =="O" or vowel[i] =="o":
            count_vowel += 1        
        elif vowel[i] =="U" or vowel[i] =="u":
            count_vowel += 1
    return count_vowel
vowel = input("Enter text: ")
print(count_vowel(vowel))


text = "Good moring"
for i in range(len(text)):
    print(text[len(text)-i-1])



#  3. Create function to find a middle letter.




def find_middle_letter(s):
    """
    This function returns the middle letter(s) of the given string `s`.
    If the string length is odd, it returns the single middle letter.
    If the string length is even, it returns the two middle letters.
    """
    length = len(s)
    
    if length == 0:
        return "The string is empty."
    
    middle_index = length // 2
    
    if length % 2 == 1:
        # Length is odd: return the middle letter
        return s[middle_index]
    else:
        # Length is even: return the two middle letters
        return s[middle_index - 1:middle_index + 1]

# Example usage:
text = "Cat"
print("Middle letter:", find_middle_letter(text))  # Output: 't'


def sum_nummbers(number):
    sum = 0
    for i in range(len(number)):
        if int(number[i]) > 0:
            sum += int(number[i])
    return sum
number = "12345"
print(sum_nummbers(number))




# a = "4"
# if a == 4:
#     print("a")
# elif a != 4:
#     print("Not a")

# a = 23
# b = bool(a)
# print(b)
# print(type(b))

# Ex1:
#   Enter text and count the letter only not include space
# Ex2 :
#   Enter 3 text and count letter "A" in  each text 
#   result display example: 1 | 0 |3
# Ex3:
#   Enter text and sum all number of letter "B" text
#   result display example: B10



# text = input("enter text ")
# count = 0
# for i in range(len(text)):
#     if text[i] != " ":
#         count += 1
# print(count) 

# result = ""
# for i in range(3):
#     text = input("Enter text: ")
#     countA = 0
#     for j in range(len(text)):
#         if text[j] == "A" or text[j] == "a":
#          countA +=1
#     if i == 2:
#         result += str(countA)
#     else:
#         result += str(countA) + "|"
# print(result)

# text = input("Enter text: ")
# countB = 0
# for i in range(len(text)):
#     if text[i] == "b" or text[i] == "B":
#         countB +=1
# print("B", countB)


# def my_function(x):
#     print(x)
# my_function(100)


# number = input("Please enter number: ")
# number = 0
# for i in range(int(number)):
#     if number % 2 == 0:
#         print(number,"is odd number")
#     else:
#         print((number),"is even number")

mesage =""
while mesage != "Try again!":
    user_input = input("enter text: ")
    if user_input == A:
         mesage = "Found A"
else:
         mesage = "Try again!"
print(mesage)



number = int(input("Enter number: "))
for i in range(3):
    number = int[i]
    for j in range(len(int(number))):
        if number <= 20:
            print("take")
    else:
        if number >= 20:
            print("Not")


for i in range(3):
    result = ""
    user_input = int(input("Enter code: "))
    if 11>= user_input <=20:
        result = "Good"
    elif 11 < user_input <=10:
        result = "It not good code"
print(result)



isFound = False
result = ""
for i in range(2):
    name = input("enter name: ")
    if name[i] <= "3" and not isFound == False:
        result ="Okay"
    else:
        result ="Why"
        isFound = True
print(result)




won = False
for i in range(5):
    user_input = int(input("Enter your guess: "))
    if 10 <= user_input <= 30:
        won = True
if won:
    print("WIN")
else:
    print("LOST")



number = input("enter number: ")
for i in range(len(number)):
    print(number[i])



text = input("Enter text: ")
count = 0
for i in range(len(text)):
    if text[i] =="a" and text[i+1] =="b":
        count += 1
print(count)


number = input("Enter number: ")
sum = 0
is_7 = False
for i in range(len(number)-1):
    if number[i] !="7" and is_7 == False:
        sum += int(number[i])
    else:
        is_7 = True
print(sum)



text = input("enter text: ")
result = ""
comment=""
for i in range(len(text)):
    if text[i] =="a" and text[i+1] =="b":
        result += text[i]
if result:
    comment="Yes"
else:
    comment="No"
print(comment)



text = input("Enter text: ")
index = -1
for i in range(len(text)):
    if text[i] == "k" or text[i] =="K":
        index =i
print(index)


number = input("Enter number: ")
comment = "SORTED"
for i in range(len(number)-1):
    if int(number[i]) > int(number[i+1]):
        comment="NOT SORTED"
print(comment)




result = ""
for i in range(5):
    num = int(input("Enter num: "))
    sum = 0
    for j in range(num):
        if num % 2 == 1:
            result =" ME"
            sum +=1
        else:
            result ="YOU"
            sum +=2
print(result)



numbers = input("Enter number: ")
sum = 0
result = ""
for i in range(len(numbers)):
    if numbers[i] !=" ":
        sum += int(numbers[i])
    elif (numbers[i]) <= '20':
        result = "WIN"
    elif (numbers[i]) > '20':
        result = "LOST"
print(result)



# mesage ="Won"
# isLost = False
# for i in range(5):
#     numbers = int(input("Enter number: "))
#     if numbers < 10 or numbers > 30:
#         isLost = True
# if isLost:
#     mesage = "Lost"
# print(mesage)


mesage = ""
isLost = False
for i in range(5):
    num = int(input())
    if num >= 10 and num <=30 and isLost == False:
        mesage = "Won"
    else:
        mesage ="Lost"
        isLost = True
print(mesage)


count = int(input("Enter your number: "))
sum = 0
for i in range(count):
    number = int(input())
    sum = sum + number
print("The sum all of number is :", sum)



text = input("Please enter your text: ")
is_storng_password = False
for i in range(len(text)):
    if text[i] == '@':
        is_storng_password = True
if is_storng_password:
    print("Strong password")
else:
    print("Weak password")


# text = input("Please enter your password: ")
# mesage = " "
# is_strong_password = True
# for i in range(len(text)):
#     if text[i] == text[i].upper() and text[i] =="@":
#         is_strong_password = True
# if is_strong_password:
#     print("Strong password")
# else:
#     print("Weak Password")



line = int(input("Enter number of line:"))
text = int(input("Enter number of texts per line:"))
Enter_letter=input("Enter letter:")
for i in range(line):
    result = ''
    for j in range(text):
        result += Enter_letter
    print(result)


# Ex8:Enter text and display the last index of letter "A"

text = input("Please enter your text now: ")
position = 0
for i in range(len(text)):
    if text[i] == "A" or text[i] == "a":
        position = i
print(position)


# Ex7:Enter text and display the first index of letter "A"

text = input("Please enter your text now: ")
posiion = 0
isFound = False
for i in range(len(text)):
    if (text[i] == "a" or text[i] == "A") and not isFound:
        posiion = i
        isFound = True
print(posiion)


# Ex6 Enter text and display counter of lowercase letter "B" and uppercase letter "B"

text = input("Please enter your text: ")
counterB = 0
for i in range(len(text)):
    if text[i] == "b" or text[i] == "B":
        counterB += 1
print(counterB)




# Ex5 Enter text and display only letter "A" index

# text = input("Please your text ")
# indexA=0
# for i in range(len(text)):
#     if text[i]=="A":
#         indexA=i
# print("Index A:", indexA)

text = input("Please enter your text now: ")
for i in range(len(text)):
    if text[i] == "A" or text[i] == "a":
        print(i)


# Ex4: Enter text and display reverse text

# text = input("Please enter your text:a ")
# for i in range(len(text)):
#     print(text[len(text)-1-i])

text = input("Please enter yuor text: ")
reversed = len(text) -1
result = ""
for i in range(len(text)):
    result += str([reversed-i])
print(result)



# Ex3: Enter text and display only letter in odd index

text = input("Please enter your text: ")
countOdd = 0
for i in range(len(text)):
    if i % 2 == 1: 
        print(text[i])



# Ex2: Enter text and display only uppercase letter

text = input("Please enter your text: ")
uppercase_letter = ""
for i in range(len(text)):
    if text[i].isupper():
        uppercase_letter += text[i]
print(uppercase_letter)



# Ex1: Enter the string and display all letter one by one

text = input("Enter your text: ")
countLetter = 0
for i in range(len(text)):
    if text[i] > str(len(text)):
        countLetter += 1
    print(countLetter)


def count(number):
    count = 0
    for i in range(len(number)):
        if number[i] < 0:
            count += 1
    return count
number = [-1,11,2,0,-1,4]
print(count(number))



# EX6.Create function to count positive number in array [-1,11,2,0,-1,4]

def count(number):
    count = 0
    for i in range(len(number)):
        if number[i] >=0:
            count += 1
    return count
number = [-1,11,2,0,-1,4]
print(count(number))



# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]

def count(number):
    count = 0
    for i in range(len(number)):
        if number[i] ==5:
            count += 1
    return count
number = [2,3,5,0,11,5,2]
print(count(number))



# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]

def min_number(array):
    number = array[0]
    for i in range(len(array)):
        if array[i] < number:
            number = array[i]
    return number
max = [2,3,5,0,11,5,2]
print(min_number(max))



# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]

def max_number(array):
    number = array[0]
    for i in range(len(array)):
        if array[i] > number:
            number = array[i]
    return number
max = [2,3,5,0,11,5,2]
print(max_number(max))



# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum(number):
    sum = 0
    for i in range(len(number)):
        if number[i] !="," and int(number[i]) % 2 ==1:
            sum += int(number[i])
    return sum
number_input = input("enter number: ")
print(sum(number_input))



# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
def sum(number):
    sum = 0
    for i in range(len(number)):
        if number[i] !=",":
            sum += int(number[i])
    return sum
number_input = input("enter number: ")
print(sum(number_input))



# def welcome(name):
#     print("Good morning " + name + "!")
#     print("Good night sweet dream!")
#     print("Good bye!")
# welcome("name")




# def how(name):
#     print("Give me some exercise " + name)
#     print("How can I make the sentence")
# how("YOU")




# def findMax(text):
#     Max = text[0]
#     for i in range(len(text)):
#         if int(text[i]) > int(Max):
#             Max = text[i]
#     return Max
# numbers = ["1222334569","2244912","3282736"]
# for i in range(len(numbers)):
    # print(findMax(numbers[i]))




# list1 = [5,4,7,3,1]
# list2 = list1

# list1[0] = 99
# print(list1[0])
# print(list2[0])


# list1 = [2]
# list2 = [2]
# print(list1 == list2)




# a = 5
# b = a
# a = 7
# print(b)



# a = [18,24]
# b = a
# a[1] = 3
# print(b[1])




# def number(num1,num2):
#     number = num1 + num2
#     return number
# print(number(3,5))






# def sum(num1,num2):
#     return num1 + num2
# print(sum(int(input("Please enter number1: ")),int(input("Please enter number2: "))))



# def sum(num1,num2):
#     return num1 + num2
# num_input1 = int(input("Pleas enter your number:"))
# num_input2 = int(input("Pleas enter your number:"))
# print(sum(num_input1,num_input2))



# def sum(num1,num2):
#     return num1 + num2
# for i in range(2):
#     num_input1 = int(input("enter number: "))
#     num_input2 = int(input("enter number: "))
#     print(sum(num_input1,num_input2))



# def sum(num1,num2):
#     return num1 + num2
# result = ""
# for i in range(2):
#     num_input1 = int(input("enter number: "))
#     num_input2 = int(input("enter number: "))
#     if sum(num_input1,num_input2) > 50:
#         result ="Pass"
#     else:
#         result ="False"
#     print(result)


# Ex1.create function to sum number in string "1 2 3 4 5 6"
# def sum(num1,num2,num3,num4,num5,num6):
#     return num1+num2+num3+num4+num5+num6
# print(sum(1,2,3,4,5,6))

# def sum(string):
#     sum = 0
#     for i in range(len(string)):
#         if string[i] !=" ":
#             sum += int(string[i])
#     return sum
#             # print(string[i])
# string_number = input("enter number: ")
# print(sum(string_number))

# Ex2.create function to sum old number in string "1 2 3 4 5 6"

# def sum(string):
#     sum = 0
#     for i in range(len(string)):
#         if string[i] !=" " and int(string[i]) % 2 ==1:
#             sum += int(string[i])
#     return sum
#             # print(string[i])
# string_number = input("enter number: ")
# print(sum(string_number))



# Ex3.create function to find min number in string "1 2 6 3 4 0 5"
# def min(string):
#     min_number = 0
#     result = ""
#     for i in range(len(string)):
#         if str(string[i]) < min_number:
#             result += int(string[i])
#     return result
# string_number = int(input("enter number: "))
# print(sum(string_number))


# EX4.create function to reverse string "abc" =>cda
# Ex5.create function to count letter "B" or "b" in string "abcdbeB"


















# def remove_minus(string):
#     result =""
#     for i in range(len(string)):
#         if string[i] !="-":
#             result += string[i]
#     return result

# letter = "Y"
# while letter =="Y":
#     user_input = input("Please enter word: ")
#     print(remove_minus(user_input))
#     letter = input("Do you want to coutinue(Y/N)?: ")
#     letter = letter.upper()




#  create a function with key def = define
# def he():
#     return "Hello"
# print(he())



# def hi(name):
#     return "Hi"+ "," + name
# print(hi("Yon"))
# print(hi("Piseth"))


# def hi(name,age):
#     return "Hi" + "," + name + "your age is " + str(age)
# print(hi("Yon",12))



# def sum(num1,num2):
#     sum = num1 + num2
#     return sum
# print(sum(12,23))



# def subtract(num1,num2):
#     subtract = num1 - num2
#     return subtract
# print(subtract(20,10))
# print(subtract(30,10))
# print(subtract(90,80))




# def Multiply(num1,num2):
#     Multiply = num1 * num2
#     return Multiply
# print(Multiply(12,8))

# def Distribution(num1,num2):
#     Distribution = num1 / num2
#     return Distribution
# print(Distribution(10,2))


# def name(num1,num2):
#     name = num1 + num2
#     return name
# print(name(20,30))




# def informationStudent(name,age,gender,city,phoneNumber,email):
#     return name + str(age) + gender + city + phoneNumber + email
# print(informationStudent("Yen Yon ",12," Male"," PP"," 096750534"," yenyon@gmail.com"))


# def studentName(name,age,drade):
#     studentName = 


# text ="3 4 5 6"

# sum = 0
# for i in range(len(text)):
#     if text[i] !=" ":
#         sum += int(text[i])
# print(sum)

number = input("enter number: ")
sum = 0
for i in range(len(number)):
    if number[i] != 0:
        sum += int(number[i])
print(sum)



text = input("Please enter text: ")
result = ""
for i in range(len(text)):
    if text[i] .isupper():
        result=("Yes")
    else:
        result=("No")
print(result)


text = input("Please enter text: ")
result =""
for i in range(len(text)):
    if text[i] =="a" or text[i] =="A":
        if len(text)-1:
             result = result + str(i)+"-"
        else:
            result = result + str(i)
print(result)



text = input("Please enter text: ")
result = ""
for i in range(len(text)):
    if text[i] !=" ":
        print(text[i])


user_name1 = int(input("Please enter your number:"))
user_name2 = int(input("Please enter your number:"))
user_name3 = int(input("Please enter your number:"))
print("The sum all of {} , {} and {} is:{}".format (user_name1,user_name2,user_name3, user_name1+user_name2+user_name3))



# count letter in list A = 6

fruits = ["banana", "mango", "apple", "orange"]
# countA = " "
# # for i in range(len(fruits)):
# #     for j in range(len(fruits[i])):
# #         if fruits[i][j] == "a" or fruits[i][j] =="A":
# #             counta += 1
# # print(counta)

# for i in range(len(fruits)):
#     if fruits[i] == "a" or fruits[i] =="A":
#         countA += 1
# print(countA)
count=""
for i in range(len(fruits)):
    for j in range(len(fruits[i])):
        if fruits[i][j] == "a" or fruits[i][j] == "A":
            count += str(len(fruits[i]))
        else:
            count += str(len(fruits[i]))+"-"
print(count)


fruits = ["banana", "mango", "apple", "orange"]
result = " "
for i in range(len(fruits)):
    if i == len(fruits)-1:
        result += str(len(fruits[i]))
    else:
        result += str(len(fruits[i]))+ "-"
print(result)
    # print(len(fruits[i]))



isAdmin = False
count = 0
while not isAdmin and count <= 3:
    user = input("Enter name: ")
    if user == "admin":
        isAdmin = True
    else:
        print("Try again!")
        count += 1
if isAdmin:
    print("yes,correct")
else:
    print("user acount is block")



n = int(input("Enter number: "))
result =""
factorial = 1
for i in range(1,n+1):
    factorial *= i
    if i == n:
      result += str(i) 
    else:
       result += str(i) + "x"
print(result,"=", factorial)




n = int(input("Please enter your numner: "))
for i in range(10):
    print(n"x",i"=",n*i)



# 1 find minimum number
numbers = [1,2,3,4,10,7]
min_number = numbers[0]
for i in range(len(numbers)):
    if numbers[i] < min_number:
        min_number = numbers[i]
print(min_number)


# 2 find max numbe
numbers = [1,2,3,4,10,7]
max_number = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
print(max_number)


# 3 sum even numbe
numbers = [1,2,3,4,10,7]
sum = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        sum += numbers[i]
print(sum)



# 4 sum odd number
numbers = [1,2,3,4,10,7]
sum = 0
for i in range(len(numbers)):
    if numbers[i] % 2 ==1:
        sum += numbers[i]
print(sum)



 
# 5 find of max odd number 
numbers = [1,2,3,4,10,7]

max_odd = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 1 and numbers[i]:
        max_odd = numbers[i]
print(max_odd)


# 7 find mini of odd number

numbers = [1,2,3,4,10,7]

min_odd = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 1 and numbers[i]:
        min_odd = numbers[i]
print(min_odd)



# 9 sum number are greater than 5
numbers = [1,2,3,4,10,7]
sum = 0
for i in range(len(numbers)):
    if numbers[i] > 5:
        sum += i
print(numbers)



# 10 find number at the last
numbers = [1, 2, 0, 3, 4, 10, 7]
last_number =numbers[-1]
print("The last number is:",last_number)



# 12 sum two numbber first + last
numbers = [1,2,3,4,10,7]
lastNumber = 0
for last in numbers:
    lastNumber = last
index = False
firstNumber = 0
for first in numbers:
    if not index:
        firstNumber = first
        index = True
sum = firstNumber + lastNumber
print(sum)




# text = input("Please enter your text: ")
# countB = 0
# countC = 0
# countD = 0
# for i in range(len(text)):
#     if text[i] == "b" or text[i] == "B":
#         countB += 1
#     elif text[i] =="c" or text[i] =="C":
#         countC += 1
#     elif text[i] == "d" or text[i] =="D":
#         countD += 1
# sum = countB +countC + countD
# print(sum)



text = input ("Please enter text: ")
result = ""
for i in range(len(text)):
    if text[i] == "C" or text[i] =="c":
        if i != len(text) - 1:
            result =result + str(i)+ "-"
        else:
            result = result + str(i)
print(result)



text = input("please enter now: ")
result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i]
print(result)



# numberAsText = input("Enter text as number: ")
# total = 0
# for i in range(len(numberAsText)):
#     total += int(numberAsText[i])
# print("Total:", total)


number = input("Please enter number: ")
total = 0
for i in range(len(number)):
    total += int(number[i])
print("Total:", total)



isLetterA = False
while not isLetterA:
    letter = input("Enter letter: ")
    if letter == "a" or letter =="A":
        isLetterA = True
    else:
        print("Try again!")
print("Found Letter A")



# while True:
#     password = int(input(" Please enter your password:"))
#     if password == 123:
#         print("your password is correctly")
#     else:
#         print("Try again")



# ex1 mesage "number of enter :2"
# number1: 10
# # number2: 5
# # sum of nuber is 15
# user_input = input("Please enter number:")
# total = 0
# for i in range(int(user_input)):
#     number_input = input("number"+str(i+1)+": ")
#     total += int(number_input)
# print("Sum of number is " + str(total))

# ex2
# number of enter :2
# enter arimatic operator: -
# number1 : 10
# number2 : 5
# result : 5
user_input = input("Please enter number: ")
user_sign = input("Please enter sign: ")
total = 0
for i in range(int(user_input)):
    number_input = input("Number"+str(i+1)+": ")
    if user_sign == '-':
        if i == 0:
            total = int(number_input)
        else:
            total -= int(number_input)
    elif user_sign =='*':
        if i == 0:
            total = int(number_input)
        else:
            total *= int(number_input)
    elif user_sign == '/':
        if i == 0:
            total = int(user_input)
        else:
            total /= int(user_input)
    else:
        total += int(number_input)
print("Result: " + str(total))



user_input = input()
length_user_input = len(user_input)
result = ""
if length_user_input <= 3:
    result = "It's small"
elif length_user_input >= 4 and length_user_input <= 6 or length_user_input >=8 and length_user_input <= 10:
    result = "It's medium"
elif length_user_input == 7:
    result = "it's exactly the average!"
elif length_user_input >= 11:
    result = "It's big!"
print(result)



products = [
    {"name": "Apple", "price": 1.50, "quantity": 100, "expired": True},
    {"name": "Banana", "price": 0.75, "quantity": 50, "expired": False},
    {"name": "Orange", "price": 1.25, "quantity": 80, "expired": True}
]
# count = 0
# for i in range(len(products)):
#     if products[i]["expired"] == True:
#         count +=1
# print(count)
# total = 0
# for i in range(len(products)):
#     if products[i]["price"] > total:
#         total += products[i]["price"]
# print(total)
# total = 0
# for i in range(len(products)):
#     if products[i]["quantity"]< 80:
#         total = products[i]["quantity"]
# print(total)
# total = 0
# for i in range(len(products)):
#     if products[i]["quantity"] < 80:
#         total += products[i]["quantity"]
# print(total)



# user_input1 = input()
# user_input2 = input()
# user_input3 = input()
# user_input4 = input()
# user_input5 = input()
# result = str(len(user_input1))+'-'+str(len(user_input2))+'-'+str(len(user_input3))+'-'+str(len(user_input4))+'-'+str(len(user_input5))
# print(result)
user_input1 = input()
text = ""
for i in range(len(user_input1)):
    if user_input1 and 3 :
        print("It's small")



products = [
    {"name": "Apple", "price": 1.50, "quantity": 100, "expired": True},
    {"name": "Banana", "price": 0.75, "quantity": 50, "expired": False},
    {"name": "Orange", "price": 1.25, "quantity": 80, "expired": True}
    ]
count = 0
for i in range(len(products)):
    if products[i]["expired"] == True:
        count +=1
print(count)



# enter your password : 123
# if you enter correct "123" mesage "your password is correct"
# if you enter wrong password will measage : "Try again"
while True:
    password = int(input("Please enter your password"))
    if password == 123:
        print("Your password is correctly")
    else:
        print("Please try again")


user_input = input()
text = ""
for i in range(len(user_input)):
    text += "Y"
print(text)


user_input1 = input()
user_input2 = input()
user_input3 = input()
result = str(len(user_input1))+'-'+str(len(user_input2))+'-'+str(len(user_input3))
print(result)



students =[
    {
        "name":"Yon","age":32,
        "scores":[90,95]
    },
    {
        "name":"Pich","age":15,
        "scores":[80,85]
    }
]
for student in students:
    total = 0
    for score in student["scores"]:
        total += score
    print(student["name"]+" has total score: "+str(total))




text = "banana"
isFound = False
for i in range(len(text)):
    if (text[i] =="a" or text[i] == "A") and not isFound:
        print(i)
        isFound = True


text = input("Please enter: ")
n = len(text)
mesage =""
if n > 4 and n < 8:
    result =("It is small")
elif n > 10 and n < 15:
    result = ("It is average")
elif n > 15:
    result = ("It is big")
print(result)



while  True:
    letter = input("Please enter your letter: ").strip()
    if letter.lower() == "a":
        print("Found letter A")
        break
    else:
        print("Try again!")



number = input("Enter text:")
sum = 0
for i in range (len(number)):
    sum += int(number[i])
print("Total:",sum)


text =input("Enter text:")
print(text[0::2])



text = input("Enter text: ")
position =0
for i in range(len(text)):
    if i%2==0:
        position+=1
print(position)


text = input("Enter text: ")
sum =0
for i in range(len(text)):
    if text[i]=="B"or text[i]=="b" or text[i] =="C" or text[i] =="c" or text[i] == "D" or text[i] =="d":
        sum += 1
print("Total",sum)



text = input("Please enter your text now: ")
countA = 0
countB = 0
for i in range(len(text)):
    if text[i] == "A" or text[i] == "a" and text[i]!= "B":
        countA += 1
        countB += 1
print("count letter A and a: ",countA, "and count letter b:",countB)



text = input("Please enter your text: ")
is_storng_password = False
for i in range(len(text)):
    if text[i] == '@':
        is_storng_password = True
if is_storng_password:
    print("Strong password")
else:
    print("Weak password")



text = input("Enter your text: ")
result = " "
if len(text) < 3:
    result = "Small"
elif len(text) <= 8:
    result = "Medium"
elif len(text) > 9:
    result ="Big"
print(result)



x = 0
y = 0
z = 0
if x == 5:
    if y < 6:
        if z <= 11:
            print("nothing")
        else:
            print(2)
    else:
        print(1)
else:
    if y > 3:
        print(3)
    else:
        print("nothing")



x = 0
y = 0
if x > 4:
    if y < 2:
        print("nothing")
    else:
        print(1)
else:
    if y > 3:
        print(3)
    else:
        print("nothing")


nbRepeat = 5
for i in range(int(nbRepeat)):
    if nbRepeat == 5:
        print("Hello world")



number = int(input())
while number > 5:
    print(number)
    number = number-2



user_name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("My name is " + user_name + " and I am " + str(age) + " years old.")



# number = 25
# if number < 25 :
#     print (« Dog »)
# elif number <= 30 :
#     print(«Cat»)
# else :
#     print(«Cow »)
number = 25
if number < 25 :
    print ("Dog")
elif number > 30 :
    print("Cat")
else :
    print("Cow")



value = 10
if value >= 5 :
    print("Apple")
elif value <= 10 :
    print("Banana")



user_input = input()
text = ""
for i in range(len(user_input)):
    text += "X"
print(text)