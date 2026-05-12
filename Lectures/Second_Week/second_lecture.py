def main():
    hello()
    name = (input("What's your name?"))
    hello(name)

#python has an interactive mode that allows us to run python inside of the terminal and completely execute code without compiling 
#def is short for define, it is used when trying to define a new function in python.

def hello(to="world"): # in case the user doesn't call hello with an argument inside the function, we can assign a default arg
    print(f"hello {to}")#default argument can be assigned like this to="world"

#A function must exist before being called

main()#by calling the main function runs the code inside of the main function
#SCOPE IS a variable only existing in the context in which you define it, global and local scope differ.
#The return() keyword returns a value explicitly.