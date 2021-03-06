print "Hello World!"
x = "Hello World"
y = 42
print y
# commenting a single line
# we can even comment out coude
# print "this will not print!"
print "read below for more on multi-line comments in python!" #this would execute
# this line and below would not execute
'''
triple quotations allow us to comment acros multiple lines as long as
the trip quoted comment is not the first thing in your file.
You can use double or single quites!
'''
# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + 'from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'
print "this is a sample string"
name = "Zen"
print "My name is", name
name = "Zen"
print "My name is" + name
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name,last_name)
first_name = "Rich"
last_name = "Nam"
print "My name is {}{}".format(last_name, first_name)
#{}{} vs {}'space'{}
hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world
x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"
''''
string.count(substring): returns number of occurrences of substring in string.
string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
string.find(substring): returns the index of the start of the first occurrence of substring within string.
string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
'''
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens

x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]

x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3
'''enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence
https://docs.python.org/2/library/functions.html
'''
my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
# output:
# [1,5,2,8,4,7]
'''
list.extend(list2) adds all values from a second sequence to the end of the original sequence.
list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
list.index(value) returns the index position in a list for the given parameter.
http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch14s07.html

# if statement:
if <condition>:
  # do something
# if-else statement:
elif <condition>:
  # do something
else:
  # do this instead
'''
age = 21
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'
if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!'
'''
 for <counter> in <sequence or range>:
   do something
'''
#create new list remember lists can hold may data types, even lists

my_list = [4, 'dog', 20, ['watt', 'dsw', 99], 'fml']
for element in my_list:
    print element

# while <expression>
for val in "string":
  if val == "i":
    break
  print val

for val in "string":
  if val == "i":
    continue
  print val

'''
pass is used to nullify a statment or line of code
'''
