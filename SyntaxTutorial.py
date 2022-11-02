#Python Syntax Tutorial
#Prepared by: Mehmet Mert Menevşe

#Print and Format Function, Comment Lines
print("Python")
print("Mehmet",23,"Mert","Menevşe")
print("Mehmet\nMert\nMenevşe")
print("19","09","1999",sep= "/") #19/09/1999
print("{} + {} = {}".format(2,3,2+3)) #2 + 3 = 5
#Single comment line
"""
Multiple 
Comment 
Lines
"""

print("---------------------------------------------------------")

#Variables, Data Types
a = 3 #int
b = 3.14 #float
c = "Python" #String
d = [1,2,3,4,5,"Python"] #List
e = (1,2,3,4,5,"Python") #tuble
f = {"Apple":3,"Pear":4,"Cherry":5} #dict
g = True #boolean

print(type(a)) #<class 'int'>
print(type(b)) #<class 'float'>
print(type(c)) #<class 'str'>
print(type(d)) #<class 'list'>
print(type(e)) #<class 'tuple'>
print(type(f)) #<class 'dict'>
print(type(g)) #<class 'bool'>

print(a,b,c) #3 3.14 Python

print("---------------------------------------------------------")

#Math Operators
print(3 + 4) #7
print(10 - 3) #7
print(10 * 3) #30
print(10 / 4) #2.5
print(10 // 4) #2
print(10 % 4) #2

#Example1
a = 5
b = 10
c = a + 2 * b
print(c) #25

#Example2
a = "Python "
b = "Programming "
c = "Language "
d = a + b + c
print(d) #Python Programming Language

#Example3
a = "Python"
print(a * 5) #PythonPythonPythonPythonPython

#Example4
print("* " * 1)#*
print("* " * 2)#* *
print("* " * 3)#* * *
print("* " * 4)#* * * *
print("* " * 5)#* * * * *

print("---------------------------------------------------------")

#Indexing Strings and Lists
a = "Python"
b = [1,2,3,4,5,6,7]
print(a[0]) #P
print(a[2]) #t
print(len(a)) #6
print(len(b)) #7
print(a[len(a)-1]) #n  last element
print(b[len(b)-1]) #7  last element
print(a[0:2]) #Py
print(a[2:]) #thon
print(a[:4]) #Pyth
print(b[2:]) #[3, 4, 5, 6, 7]
print(b[0:6:2]) #[1, 3, 5]
print(b[::2]) #[1, 3, 5, 7]

#Example1
a = {"Apple":3,"Pear":4,"Cherry":5}
print(a["Apple"]) #3
print(a["Cherry"]) #5
print(a["Strawberry"]) #KeyError: 'Strawberry'

print("---------------------------------------------------------")

#Input
age = input("Enter Your Age") #Enter Your Age34
print("Your Age= ",age) #Your Age=  34

#Example1
a = input("a:") #a:3
b = input("b:") #b:4
c = input("c:") #c:5
print("Total",a+b+c) #Total 345

#Example2
a = int(input("a:")) #a:3
b = int(input("b:")) #b:4
c = int(input("c:")) #c:5
print("Total",a+b+c) #Total 12

print("---------------------------------------------------------")

#if-elif-else
"""
<
>
<=
>=
==
!=
"""
age = int(input("Enter Your Age:"))#Enter Your Age:17

if age < 18:
    print("You cannot enter the venue...")#You cannot enter the venue...
else:
    print("Welcome...")

#Example1
process = int(input("Enter Transaction:")) #Enter Transaction:4

if process == 1:
    print("You chose action 1...")
elif process == 2:
    print("You chose action 2")
elif process == 3:
    print("You chose action 3")
else:
    print("Invalid transaction...") #Invalid transaction...

print("---------------------------------------------------------")

#Logical Operators
a = 3
b = 4
#and
if a == 3 and b == 4:
    print("Yes") #Yes
else:
    print("No")
#or
if a == 3 or b == 4:
    print("Yes") #Yes
else:
    print("No")
#not
if (not (3 > 4)):
    print("Yes")#Yes

print("---------------------------------------------------------")

#While Loop
i = 0
while i < 10:
    print("i:",i)
    i += 1 # i = i + 1
"""
i: 0
i: 1
i: 2
i: 3
i: 4
i: 5
i: 6
i: 7
i: 8
i: 9
"""
#Example1
i = 1
while(i < 1000):
    print("i:",i)
    i *= 2 # i = i  * 2
"""
i: 1
i: 2
i: 4
i: 8
i: 16
i: 32
i: 64
i: 128
i: 256
i: 512
"""

print("---------------------------------------------------------")

#break and continue
#break
i = 0
while(i < 10):
    if i == 5:
        break
    print("i:",i)
    i += 1
"""
i: 0
i: 1
i: 2
i: 3
i: 4
"""
#continue
i = 0
while (i < 10):
    if i== 3 or i==5:
        i += 1
        continue
    print("i:",i)
    i += 1
"""
i: 0
i: 1
i: 2
i: 4
i: 6
i: 7
i: 8
i: 9
"""

print("---------------------------------------------------------")

#For loop and range Function
a = [1,2,3,4,5,6]

for element in a:
    print(element)
"""
1
2
3
4
5
6
"""

b = "Python"
for character in b:
    print(character)
"""
P
y
t
h
o
n
"""

#range
for number in range(0,100):
    print(number)
"""
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
"""
for number in range(10,100,2):
    print(number)
"""
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
"""

print("---------------------------------------------------------")

#Functions
def hi():
    print("Hello")
    print("How are you?")

hi()
"""
Hello
How are you?
"""

#Parameterized Function
def hi(name):
    print("Hello",name)

hi("Mehmet Mert Menevşe") #Hello Mehmet Mert Menevşe

#Example
def total(a,b,c):
    print("Total:",a+b+c)

total(3,4,5)#Total: 12

#return
def total(a,b,c):
    return a+b+c

sum = total(3,4,5)
print(sum) #12

print("---------------------------------------------------------")

#Some methods of Lists and Strings
list = [1,2,3,4,5,6]
a = "araba"

print(a.startswith("a"))#True
print(a.startswith("b"))#False
print(a.startswith("ar"))#True

print(a.endswith("a"))#True
print(a.endswith("s"))#False

a = a.replace("a","o")
print(a) #orobo

list.append("Python")
print(list) #[1, 2, 3, 4, 5, 6, 'Python']

list.pop()
print(list) #[1, 2, 3, 4, 5, 6]
list.pop(0)
print(list) #[2, 3, 4, 5, 6]

print("---------------------------------------------------------")

#Folders
file = open("dosya.txt","a")
file.write("What's up Python\n")
file.write("What's up Java\n")
file.write("What's up C++")

file = open("dosya.txt","r")
data = file.read()
print(data)
"""
What's up Python
What's up Java
What's up C++
"""
data = file.read(10) #What's up

for line in file:
    print(line)
"""
What's up Python

What's up Java

What's up C++

"""
file.close()

print("---------------------------------------------------------")

#OOP(Object Oriented Programming)
class Account:
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
    def accountInfo(self):
        print("Name : ",self.name)
        print("Number : ",self.number)
        print("Balance : ",self.balance)
    def withdrawMoney(self,quantity):
        if(self.balance - quantity < 0):
            print("Your balance is not enough...")
        else:
            self.balance -= quantity
            print("New balance:",self.balance)
    def depositMoney(self,quantity):
        self.balance += quantity
        print("New balance:",self.balance)
account = Account("Mehmet Mert Menevşe",123456,1000)
account.accountInfo()

account.withdrawMoney(800)
account.accountInfo()
"""
Name :  Mehmet Mert Menevşe
Number :  123456
Balance :  1000
New balance: 200
Name :  Mehmet Mert Menevşe
Number :  123456
Balance :  200
"""














