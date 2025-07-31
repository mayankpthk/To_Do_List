#TYPES OF OPERATORS

#Arithmatic operators
a = 5
b = 2

print(a + b) #add 
print(a - b) #sub
print(a * b) #multi
print(a / b) #div
print(a % b) #remainder
print(a ** b) #tothepower

#Relational / Comparisional Relation

print(a == b) #equality
print(a != b) #notequality
print(a >= b) #greaterthanequal
print(a > b) #greater
print(a <= b) #smallerthanequal
print(a < b) #smaller

#Assignment Operators

num = 10
num += 10
print("num :", num)  

# Indexing
     # (M, a, y, a, n, k,  , P, a, t,  h,  a,  k)
     # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
str1 = ("Mayank Pathak")

 

# slicing

print(str1[0:3]) #May
# Last number exluded i.e. 3

print(str1[4:11])

# Minus Slicing
# Negative Index

# (M, a, y, a, n, k)
# (-6 -5 -4 -3 -2 -1)

str2 = "Mayank"

print(str2[-6:-2])
print(str2[-4: ])

#String Function

str3 = "I am a coder"

print(str3.endswith("er")) #Returns true if string ends with substr
print(str3.endswith("co")) #false

print(str3.capitalize()) #Capitalize first letter

print(str3.replace("coder", "writer")) #to replace words

print(str3.find("coder")) #it will tell the word's starting index

print(str3.count("a")) #number of inputs


#CONDITIONAL STATEMENT

#if-elif-else(SYNTAX)

'''if(condition):
        statement1
elif(condition):
        #statement2
else:
        statementN'''

a = float(input("enter first digit:"))
b = float(input("enter second digit:"))
c = float(input("enter third digit:"))

if(a>b and a>c):
    print(a, "is greater.")
elif(b>c):
    print(b, "is greater.")
else:
    print(c, "is greater.")
    
#Nesting

age = 34

if(age >= 18):
        if(age >= 80):
                print("Cannot Drive")
        print("Can Drive")
else:
        print("cannot drive")


#LIST IN PYTHON

#A built in data type that stores set of values.
#It can store elements of different types (integer, float, string, etc.)

marks = [95, 87, 76, 93, 84]
        #(0,  1,  2,  3,  4)
        
print(marks)
print(len(marks))
print(type(marks))

print(marks[1])
print(marks[4])
print(marks[2:4])

list = ["arjun", "delhi", 83, "india"]

print(list[0])  
print("marks of the student is:", list[2]) 

#list allow to change the data stored in them

student = ["arjun", 95.4, 17, "delhi"]
print(student[0])

student[0] = "Kartik"
print(student[0])


#List Methods

str = [2, 1, 3]

str.append(4)  #Adds one element at the end
print(str)

str.sort()  #Sorts in ascending order
print(str)

str.sort(reverse=True) #Sorts in decending order
print(str)

str2 = ["Banana", "dog", "Apple", "cat"]
str2.sort()
print(str2)

str2.sort(reverse=True)
print(str2)

str3 = ['b', 'c', 'a', 'd']
str3.reverse()
print(str3)


str4 = [1, 4, 3, 2]
str4.insert(2, 5)  #Insert an element at a particular index
print(str4)


str5 = [2, 1, 3, 1] 
str5.remove(1) #remove the first occurence of element
print(str5)

str5.pop(2)  #Remove element at particular index
print(str5)

#tuples

tup = (2, 1, 3)
print(tup[1])
print(tup[0])

# (2, 3, 4)
# (1, )
# In tuples (,) comma is imp to classify it as a tuple otherwise it will behave as a str only.

print(tup[1:3])

#Tuple methodes

tup_methode = (2, 1, 3, 1)

print(tup_methode.index(1))  #Return the index of first occurence
print(tup_methode.count(1))  #Count total occurence 

#LOOPS

#while loop

#Print numbers from 1 to 100

i = 1

while i <= 100:
        print(i)
        i += 1
        
#Print number from 100 to 0

i = 100

while i >= 1:
    print(i)
    i -= 1
    
#Print the multiplication table of n

i = 1

n = 3
while i <= 10:
    print(n * i)
    i += 1
    
#Print the element of the following list using loop
    #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   
idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1 
    
#Search for a number x in this tuple using loop.
    #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
i = 0
x = 49

while i < len(num):
    if num[i] == x:
        print(f"{x} is found at index {i}.")
        break
    i += 1
else:
    print("not found")
    
n = 7
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print(sum)

#write a programme to find the factorial of 5.

n = 5
fact = 1
i = 1
while i <= 5:
    fact *= i
    i += 1
print(f"factorial is {fact}.")
    
#Continue

i = 1

while i <= 5:
    if i == 3:
        i += 1
        continue
    
    print(i)
    i += 1
    
#For Loop

#Print the elements of the following list using a loop.
       #[1, 9, 16, 25, 36, 49, 64, 81, 100]
   
num = [1, 9, 16, 25, 36, 49, 64, 81, 100]
  
for i in num:
    print(i)
    
#Search for a number x in this tuple using loop.
       #[1, 9, 16, 25, 36, 49, 64, 81, 100]
   
num = [1, 9, 16, 25, 36, 49, 64, 81, 100]
x = 64

idx = 0 
for el in num:
    if el == x:
        print(f"found at index {el}")
        idx += 1
        
#for loop in Range

#Print number from 1 to 100.

for i in range(1, 101):
    print(i)
    
#Print number from 100 to 1.

for i in range(100, 0, -1):
    print(i)
    
#Print the multilpication table of a number n.

x = int(input("Enter a number : "))

for el in range(1, 11):
    print(x * el)
    
#FUNCTION

def digit_sum(a, b):
    sum = a + b
    print(sum)
    return sum

digit_sum(3, 7)

def char(n):
    rem = n % 2
    if (rem == 0):
        print("EVEN")
    else:
        print("ODD")
        return n
    
#Write a function to count the number of vowels in a given string.

def count_vowels(a):
    vowels = "aeiouAEIOU"
    count = 0
    for char in a:
        if char in vowels:
            count += 1
    print(count)
    return a

count_vowels("MY NAME IS MAYANK PATHAK")

# Write a function that returns the sum of all numbers in a list.

def list_sum(a):
    sum = 0
    for char in list:
        sum += char
    print(sum)
    return sum

list = [1, 2, 3, 4, 5]
list_sum(list)

#Write a function to count vowels in a given string.

def count_vowel(a):
    count = 0
    lis = []
    for char in a:
        if char in "AEIOUaeiou":
            lis.append(char)
            lis.sort()
    print(lis)
    return lis

ent = input("Enter a String : ")
count_vowel(ent)
