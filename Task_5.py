#1)Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.
x=[1,214,21,3,6]
result = list(filter(lambda i:(i%3!=0 and i%7==0), x))
print("number ",result)

#2)Write a program in Python to  multiple the element of list by itself using a traditional function and pass the function to map to complete the operation.
a = [10,20,30,40,50]
result = list(map(lambda x:x*x, a))
print(result)

#3)Write a program to Python find out the character in a string which is uppercase using list comprehension.
str = 'abcRESUlt'
res = [i for i in str if(i.isupper())] 
print(res)

#4)Write a program to construct a dictionary from the two lists 
list_keys = ["aa","bb","cc"]
list_values = [11,22,33]
res = {}
for key in list_keys:
    for value in list_values:
        res[key]=value
        #list_values.remove(value)
        break
print(res)

#6)Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
print ("Code for task5 Q6 starts here:")

str_in = "Consultadd Training"

def reverse (x):
    yield (x[::-1])

str_out = reverse (str_in)

while True:
    try:
        print(next(str_out))
    except StopIteration:
        break


#7)Write any example on decorators.
def hello_decorator(func): 
    # inner1 is a Wrapper function in  
    # which the argument is called 
    # inner function can access the outer local 
    # functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
        # calling the actual function now 
        # inside the wrapper function. 
        func() 
        print("This is after function execution")        
    return inner1   
# defining a function, to be called inside wrapper 
def function_to_be_used(): 
    print("This is inside the function !!") 
# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used)  
# calling the function 
function_to_be_used()


#8)Learn about What is FRONT END and its Technologies and Tools
    In simple words, it is a set of technologies that are used in developing the user interface of web applications and webpages.
With the help of front-end technologies, developers create the design, structure, animation, 
and everything that you see on the screen while opening up a website, web application, or mobile app.
 
1) Visual Studio Code Source Editor - 
Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux and macOS.
Visual Studio Code is a source code editor released in April 2015 by Microsoft under MIT License.
Visual Studio Code empowers developers to be highly productive by highlighting the syntax, matching the bracket, selecting the box, and many more. 
It supports IntelliSense code completion, code refactoring, and semantic understanding.

2) ReactJS - 
Netflix uses React on Gibbon — their platform for low-performance TV devices and has been a favorite amongst the developer community. 
Other alluring features of ReactJS like initial loading period, runtime performance etc. are playing an important role in making Netflix as popular as it is today.
React. js is one of the trendiest JavaScript open source libraries available today. Created by Facebook, it is used not only to make Facebook products but has also been widely adopted 
in production by a variety of other popular companies like Instagram, Yahoo!, Airbnb, Sony, and others.

3) AngularJS - 
Weather.com is one of the top weather forecasting online report website. 
It’s also one the big websites using AngularJS.

4)NodeJS - 
World’s largest retail chain, Walmart, is ambitiously plunging into the online commerce space. 
This endeavor of theirs to go online is being supported by Node.js which is their framework of choice. 
Walmart chose to go with the trend and take the risk of involving a fairly newer technology than going with the tried and tested frameworks. 
The organization offered its clients with newer, more sophisticated features by entirely re-engineering their mobile application. 
Node.js’ asynchronous I/O mechanism along with its single threaded event loop models can help Walmart handle concurrent requests

5)Bootstrap - 
Bootstrap was released on 19th August 2011 under MIT license. 
It is an open-source CSS framework to build dynamic websites and web applications. 
It is built by Mark Otto at Twitter as a framework for consistency.

