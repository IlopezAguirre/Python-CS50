##Selection Sort I
def swap(input_list,index1, index2):
  key = input_list[index1]
  input_list[index1] = input_list[index2]
  input_list[index2] = key
  return input_list
  
numbers =[5,4,3,7,2,1]



lowest_index = 0
for i in range(len(numbers)):
  if  numbers[lowest_index] > numbers[i]:
    lowest_index = i
swap(numbers,0,lowest_index)    
print(numbers)

#Selection Sort II
def swap(input_list, index_1, index_2):
  key = input_list[index_1]
  input_list[index_1] = input_list[index_2]
  input_list[index_2] = key

my_list = [8, 15, 4, 2]
for j in range(len(my_list)):
  lowest_index = j
  for i in range(j,len(my_list)):
 
    if my_list[i] < my_list[lowest_index]:
      lowest_index = i
  swap(my_list, lowest_index, j)

print(my_list)



## ALGORITHMIC EFFICIENCY 
import random

# Generating a random list of 10 numbers
random_numbers = [random.randint(1, 100) for _ in range(95)]
print("Unsorted numbers")
print(random_numbers)

def selection_sort(input_list):
  count = 0
  for i in range(len(input_list)):  
    # Assume the first unsorted element is the smallest
    min_index = i
    for j in range(i+1, len(input_list)):
      count += 1
      if input_list[j] < input_list[min_index]:  
        min_index = j  
       
    # Swap the found minimum element with the first unsorted element
    input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
   
  print(f"Selection Sort did {count} comparisons")
  print(input_list)
 
def bubble_sort(input_list):
  n = len(input_list)
  count = 0  
  for i in range(n):  
    # Last i elements are already sorted, so we don't check them
    for j in range(n - 1 - i):  
      count += 1
      if input_list[j] > input_list[j + 1]:  
        # Swap elements if they are in the wrong order
        input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
       
  print(f"Bubble Sort did {count} comparisons")
  print(input_list)
 
def insertion_sort(input_list):
  count = 0
  for i in range(1, len(input_list)):  
    key = input_list[i]  
    j = i - 1
       
    # Move elements that are greater than 'key' one position ahead
    while j >= 0 and input_list[j] > key:
      count += 1
      input_list[j + 1] = input_list[j]
      j -= 1
       
    input_list[j + 1] = key  # Insert 'key' at the correct position
   
  print(f"Insertion Sort did {count} comparisons")
  print(input_list)

print('\n---------- SELECTION SORT ----------------')
selection_sort(random_numbers.copy())

print('\n---------- BUBBLE SORT ----------------')
bubble_sort(random_numbers.copy())

print('\n---------- INSERTION SORT ----------------')
insertion_sort(random_numbers.copy())