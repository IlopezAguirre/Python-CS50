##First Lecture day of Harvard CS50's Introduction to programming with python
#name = input("What's your name? ") #"The function input already takes an string argument"
##print(name)
##Arguments, an argument is an input to a function that somehow influences is behavior
## a bug is a mistake in a program.
##return values are input getters that hand values or data back to the user
##variables are containers that can store values inside of a computer. 
##comments are notes to you rself that don't interfere wirth the code, usually use to explain what a block of code is doing.
##comments also selve for pseudo code.
name = input("What's your name? ")
#print("hello" ,name)
##parameters are the ones that tell you what you what kinda and how many arguments you can pass to a function.
## \n is the new line character
#print("hello, ", end="") ## end add string text  to the end of the print function
#print(name)
## to print double quotes use \"  or  ' '
#print("\"Hello\"")

##python has built in string functions
#Remove whitespace from str
name = name.strip().title() ## This function will remove whitespaces

#Capitalize user's name 
##name = name.capitalize()
##name = name.title()
##split(), splits one string into two substrings
#split use'r name into fisrt name and last name
first, last = name.split(" ")


print(f"hello, {first}") ##This is an f string
##A method is a fucntion that's built in the program like functions are.


