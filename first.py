#task_weekendActivity_DS

#1)Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
lst=[]
n = int(input("Enter number of elements : ")) 
iterating till the range 
for i in range(0, 9): 
    ele = int(input()) 
    lst.append(ele) 
print(lst)

#2)Create a list of size 5 and execute the slicing structure 
x = [11,22,"red",33,44]
print (x)
print(x[1 : 2])
print(x[ : 3])
print(x[2: ])
print(x[ : ])
print(x[ : : 2])

# #3)Create a list of given structure and run
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
index_list = x[5:-9]
print(index_list)

#4)Create a list of thousand numbers using range and xrange and see the difference between each other.
s1 = range(1,1000)
s2 = xrange(1,1000)
print("Return type of range() is : ")
print(type(s1))
print(type(s2))

#5)How Tuple is beneficial as compared to the list?
# List has mutable nature i.e., list can be changed 
# or modified after its creation according to needs 
# whereas tuple has immutable nature i.e., tuple can't be changed or modified after its creation.
#ans: Tuple is not mutable whereas a list is mutable data structure and a list has a variable size while a tuple has a fixed size.

#6)Write a program in Python to iterate through the list of numbers in the range of 1,100 
# and print the number which is divisible by 3 and a multiple of 2.
for i in range(1,1100):
    if((i%3 == 0) & (i%2 == 0)):
        print (i)

#7)Write a program in Python to reverse a string
def reverse(s): 
str = "" 
for i in s: 
    str = i + str
return str
s = "Consultadd" 
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 

#8)Write a program in Python to iterate through the string “hello my name is Abcde” 
# and print the string which has even length of the word.
# def printWords(s): 
      
#     # split the string  
s = s.split(' ')  
      # iterate in words of string  
for word in s:            
        # if length is even  
    if len(word)%2==0: 
        print(word)  
# Driver Code  
s = "i am mini" 
printWords(s) 

#9)Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
for (int i = 0; i < n; i++) 
        for (int j = i + 1; j < n; j++) 
            if (arr[i] + arr[j] == sum) 
                cout << "(" << arr[i] << ", "
                     << arr[j] << ")" << endl; 

  
# // Driver function to test the above function 
int main() 

    int arr[] = { 1, 5, 7, -1, 5 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int sum = 6; 
    printPairs(arr, n, sum); 
    return 0; 

#10)Write a program in Python to complete the following task:
#Create two different lists as in even_list and odd_list
# Ask the user to enter the number in the range of 1,50 and make sure if the entered number is even appended it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 elements calculate the sum of the list and return the maximum out of the list.

even_list = []
odd_list = []

for num in range(1,50):
    if(num%2 == 0):
        even_list.append(num)
    elif(num%2 != 0):
        odd_list.append(num)
e_list5 = even_list[:5]
o_list5 = odd_list[:5]
print(e_list5)
print(o_list5)
sum_even = sum(e_list5)
sum_odd = sum(o_list5)
print(sum_even)
print(sum_odd)

#11)Write a program to find out the occurrence of a specific word from an alphanumeric statement.
li = '12abcbacbaba344ab'
a={}

for i in li:
    if(i.isalpha())==True:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
print(a)

#12)Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
tuple1 = (1,2,3,4,5,6,7,8,9,10)
tuple2 = tupple(list1)
for item in tuple1:
    if(item%2 == 0):
        list1.append(item)
print(tuple2)