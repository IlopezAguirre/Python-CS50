#-----LISTS------
students = ["Hermione", "Harry", "Ron"]

#python itself assigns the variable of students to the values in students while traversing it.
#for student in students:
    #print(student)
#the function len will tell you the length of a list and other data structures that have any indexing logic 
#---EXAMPLE---
#for i in range(len(students)):
   # print(students[i]) #len helps you to ddinamically figure out or measure how many elements your list contains.


#----DICTIONARIES-------
#A python dictionary is another data structure that allows you to associate something with something else.
#students = {"Hermione": "Griffindor",
 #           "Harry" : "Griffindor",
  #          "Ron": "Gryffindor",
   #         "Draco": "Slytherin",}
#A dictionary stores items by association — a key maps to a value. There's no inherent order, so a position number would be meaningless:
#Keys exists in order to give a meaningful label of an arbitrary position. Data is labeled.

#for student in students:
    #print(student, students[student], sep=", ")##When you run a for loop on a dictionary in python, you iterate over the keys 

##----LIST OF DICTIONARIES-----
students =[
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name" :"Draco", "house": "Slytherin", "patronus": None}
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
    