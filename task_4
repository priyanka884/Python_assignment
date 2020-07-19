# Task 4: functions
#1)Write a program to reverse a string. 
a = input("Enter a string: ")

def Rev_string(a):
    str = ""
    for i in a:     
        str = i + str
    return str

print("Reverse string: ", Rev_string(a))

#2)Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
s = input("Enter string: ")

def Cal_letter(s):
    count_upper = 0
    count_lower = 0
    for i in s:
        if(i.isupper()):
            count_upper = count_upper + 1
        elif(i.islower()):
            count_lower = count_lower + 1
    print("Upper case letter: ", count_upper)
    print("Lower case letter: ", count_lower)
print(Cal_letter(s))

#3)Create a function that takes a list and returns a new list with unique elements of the first list.
l = [1,2,2,2,3,3,4,5,6,4,5]
def unique_list(l):
    a = []
    for i in l:
        if(i not in a):
            a.append(i)
    return a
print(unique_list(l))
#4)Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))

#5)Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)

#6) Define a function that can receive two integral numbers in string form and compute their sum and print it in console.
def calculateSum (a,b):
	s = int(a) + int(b)
	return s 
num1 = input()
num2 = input()
sum = calculateSum (num1, num2)
print ("Sum = ", sum)

#8)Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
a=[(x,x**2) for x in range(l_range,u_range+1)]
b=tuple(a)
print(b)

#9) Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#10)Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
lis = [1,2,3,4,5,6,7,8,9,10] 
out = [] 
for num in lis: 
    if num % 2 == 0:  
        out.append(num)  
print(out) 

#11)Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
li = [1,2,3,4,5,6,7,8,9,10]
eve_num = map(lambda x: x**2, filter(lambda   x: x%2==0, li))
print(eve_num)

#12)Write a function to compute 5/0 and use try/except to catch the exceptions
try:
    x = 5 / 0
except:
    print("Error dividing by zero")

#13)Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#Goal : Turn [1,2,3,4,5,6,7] to 1234567
import itertools
list = [1,2,3,4,5,6,7]
joinedlist=list(itertool.chain(*lists))
print(joinedlist)

#14)(i) 
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#(ii) 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()
