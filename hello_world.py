#!/usr/bin/env python



print("Hello, World!")
print("2 + 2 is", 2 + 2)

# Not quite PI, but a credible simulation
a = 22.0/7
print("this is approx to pi %.5f " %  a)

#this is for loop
for i in range(4):
    print(i)


#this is string
s = "A string consists of characters"
print ("this is first char %s " % s[0])
print ("this is last char %s " % s[len(s) -1])

#math
a = 5
b = ~a
c = a >> 1 
d = a & b 
e = a | b 


print ("a = %d\n" % a)
print ("b = ~a = %d\n" % b)
print ("c = a >> 1 = %d\n" % c)
print ("d = a & b = %d\n" % d)
print ("e = a | b = %d\n" % e)

#stdin
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are are already " + str(age) + " years old, " + name + "!")

#conditional statement
age = input("Age of the dog: ")
print(age)
if age < 0:
	print "This can hardly be true!"
elif age == 1:
	print "about 14 human years"
elif age == 2:
	print "about 22 human years"
elif age > 2:
	human = 22 + (age -2)*5
	print "Human years: ", human


#while loop
n = 100
sum = 0
i = 1
while (i <= n):
    sum = sum + i
    i = i + 1

print "Sum of 1 until %d: %d" % (n,sum)

#for loop over a list
language_list = ["C", "C++", "Perl", "Python"] 
for x in language_list:
    print ("%s" % x )


#check if an element is in a list and then print the index 
element = "Perl"
if element in language_list:
    print language_list.index(element)


#math
from math import sqrt
a = input("first number ")
b = input("second number ")
c_square = a**2 + b**2
c = int(sqrt(c_square))
print a, b, c


#the in condition
abc = ["a","b","c","d","e"]
if "a" in abc:
     print ("a is in %s\n", abc)
else:
     print ("a is not in %s\n", abc)


#convert list to dict
abc = ["a","b","c","d","e"]
from itertools import izip
i = iter(abc)
b = dict(izip(i, i))


#tuples
list_cars = ("ford", "chevy", "buick")
print ("this is list_cars %s\n" % (list_cars,))
for x in range(0, len(list_cars)):
     print(list_cars[x])


#hash
food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
print(food)
for key in food:
    print("the key " + key + " has value " + food[key])

food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
print(food)
for key in food:
    print("the key %s has value %s \n" % (key, food[key]))

if "ham" in food: 
    print("ham is in food and the value is %s" % food["ham"])
else:
    print("ham is not in food\n")


#inserting into a hash
a = "egg"
test_dict = {}
test_dict[a] = 1

#increment the dictionary value
test_dict[a] += 1






#sets
colours = {"red" , "green"}
print ("this is the colours %s\n" % colours)
colours.add("yellow")
print ("this is the colours after adding %s\n" % colours)


#funcs
def add(x, y):
    return x + y


print add(4, 5)





