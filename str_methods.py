#capitalize()
a='abd'
b=a.capitalize()
print(b) #op Abd

#casefold()
a='ASF'
b=a.casefold()
print(b) #asf

#centre
a='gcdhjhcjchcjcj'
b=a.center(2)
print(b) 

#count()
a='dfghebb'
b=a.count('b')
print(b) #2

#encode returns encoded version
a='ddhcnbc'
b=a.encode()
print(b)

#endswith()
a='captain'
b=a.endswith('n')
print(b) #True

#expandtabs
a='silly'
b=a.expandtabs(10)
print(b)

#Find
a='capture'
b=a.find('p')
print(b) #2 return the index of element

#format()
a='expand'
b=a.format()
print(b)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) #format specified value in str

#format_map()
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))  #4 -5

#index()
s='fountain'
b=s.index('a')
print(b)  #op 5 index no of element

#isalnum
s='south'
s=a.isalnum()
print(s) #True

#isalpha
s='ben10'
p=s.isalpha()
print(p) #if all are letters return True else false

#isnumeric
a='1254'
b=a.isnumeric()
print(b) #return true if all are numeric

#isascii
a='gfv'
b=a.isascii()
print(b)

#isdecimal
a='1235'
b=a.isdecimal()
print(b) #true if all are whole no false if in float

#isdigit
a='1245'
print(a.isdigit())
#Returns True if all characters in the string are digits

#isidentifier
txt = "Demo"
x = txt.isidentifier()
p='sfdg12'
print(p.isidentifier())
print(x)
#The isidentifier() method returns True if the string is a valid identifier,
# otherwise False.

#islower()
a='dfgs'
print(a.islower())
#Returns True if all characters in the string are lower case

#isnumeric()
a='12478'
print(a.isnumeric())
b='1kn'
print(b.isnumeric())
#Returns True if all characters in the string are numeric

#isprintable()
a='hdfs'
print(a.isprintable())
#Returns True if all characters in the string are printable

#isspace()
a=' '
print(a.isspace()) #True
#Returns True if all characters in the string are whitespaces

#istitle()
a='Title'
print(a.istitle())
#Returns True if the string follows the rules of a title

#isupper()
a='ASDF'
print(a.isupper())
#Returns True if all characters in the string are upper case

#join()
a='sachin'
b='virat'
d=a.join(b) #vsachinisachinrsachinasachint
m='s'.join(b) #vsisrsast
print(m)
print(d)
#Joins the elements of an iterable to the end of the string

#ljust()
a='water'
m=a.ljust(10) #water      is my favorite fruit.
print(m,"is my favorite fruit.")
#Returns a left justified version of the string

#lower()
a='ASdgr'
m=a.lower()
print(m)
#Converts a string into lower case

#lstrip()
a='  melody     '
print(a.lstrip())  #melody
#Returns a left trim version of the string

#maketrans()
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
#Returns a translation table to be used in translations

#replace()
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#Returns a string where a specified value is replaced with a specified value

#rfind()
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
#Searches the string for a specified value and returns
# the last position of where it was found

#rindex()
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
#The rindex() method finds the last occurrence of the specified value.
#The rindex() method raises an exception if the value is not found.

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
# return right justified version of string

#rpartition()
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)#('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
#Returns a tuple where the string is parted into three parts

#rsplit()
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
#Returns a right trim version of the string

#split()
a='mumbai is in maharashtra'
d=a.split(' ')
print(d)
#Splits the string at the specified separator, and returns a list

#splitlines()
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)#['Thank you for the music', 'Welcome to the jungle']
#The splitlines() method splits a string into a list. The splitting is done at line breaks.

#startswith()
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
#Returns true if the string starts with the specified value

#strip()
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#op of all fruits banana is my favorite
#Returns true if the string starts with the specified value

#swapcase()
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x) #hELLO mY nAME iS peter
#Swaps cases, lower case becomes upper case and vice versa

#translate()
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict)) #Hello Pam!
#Returns a translated string

#title()
a='tommorow is holiday'
m=a.title()
print(m) #Tommorow Is Holiday
#Converts the first character of each word to upper case

#upper()
txt = "Hello my friends"
x = txt.upper() #HELLO MY FRIENDS
print(x)
#Converts a string into upper case

#zfill()
txt = "50"
x = txt.zfill(10)
print(x)
#Fills the string with a specified number of 0 values
# at the beginning








