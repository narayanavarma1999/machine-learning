# String is a sequence of characters enclosed within quotes
# can contain letters, symbols , special characters , numbers, whitespace characters, unicode characters

name = "Akshith"
language = "Python"

# print(language[0])

poem ='''Welcome to Python Learning  Bootcamp'''


city ="Hyderabad"
temp = 41
weather_report = "The temperature in "+ city + " is " + str(temp) + " degrees"
report  = f"The temperature in {city} * is {temp} degrees"
print(report)

# length of any string can be determined by len() function

a = "hello"
print(len(a))

word = "Python Programming"
# slicing the string word
print(word[0:7])

# slicing the string to get word pro
print(word[7:10])

# slicing the word and skiping the word with 2 letters gap in between as here the 2 specifies intervals
print(word[0:7:2])

# slicing the word but printing the full word without and start & end indices
print(word[:])

# slicing and priniting the word in reverse manner
print(word[::-1])

# String methods

txt = "hello Python one"

print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.capitalize())

txt1 = " Hello Python Learning "

print(txt1.strip())
print(txt1.lstrip())
print(txt1.rstrip())
print(txt1.find('P'))

txt2 = "Python is amazing, Python is Fun"

# finds the specified word after the specified index
# string.find(substring, start , end)
print(txt2.find("is",19))

#count
print(txt2.count("Python"))

#index - the index method works similar to find but if no specified word or string is not found it would throw an error
print(txt1.index('P'))

#replace
welcomeText = "Hello World"
print(welcomeText.replace("World","Python"))

#startswith
print(welcomeText.startswith("Hello"))

#endswith
print(welcomeText.endswith("World"))

#split converts string to list 
print(welcomeText.split(" "))


list = welcomeText.split(" ")

#join converts list to string
print(",".join(list))


#format() method is used like a placeholder for specifing the values
messgae =  "Hello, My name is {}, age is {}".format("Narayana", 25)
print("message one: "+ messgae)
messgae =  "Hello, My name is {p2}, age is {p1}".format(p1="Narayana", p2=25)

print(messgae)

age = 25
name = "Venkat"
# with per  centage specifier
messgae = "My name is %s, my age is %d" %(name,age)


#String Immutability

# In Python strings are completely immutability which means they would not be changed (or manipulated) instead it creates an new string

s = "Hello"
#id - specifies the address of the object

print(id(s))
# this statement would throw error as strings are immutable --->   s[0]="M"
# instead we can modify the string by
 
s = "M"+s[1:];
print(s)

#here we can see the difference where s with the same variable name but it points out to different memory locations 
print(id(s))

#raw string
print(r"He\llo")
print(r"Hello\"")

# String Method chaining 
# Strip , captailize the first letter of each word, and replace the word "Skills" with "Expertise"
  
data = "python Programming Skills"

print(data.replace("Skills","Expertise"))

s = "Python Programming Language"
print(s[::2])
print(s[::-1])
print(s[-20:-9])


# string concatenation

# create a new string by extracting the first letter of each word 
text = "python is easy to learn"


result = text[0] + text[7] + text[10] + text[15] + text[18]
print(result)


# palindrome check

text = "radar"
print(text == text[::-1])

text = "wow"
print(text == text[::-1])

text = "mississippi"

# find the count from the words of 'i','s','p' and 'm'
count_i = text.count("i")
count_s = text.count("s")
count_p = text.count("p")
count_m = text.count("m")

print(count_i,
      count_s,
      count_p,
      count_m,
)








