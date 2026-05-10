"""
Week 0 — Practice 01: print() and variables

Goal: rebuild what David showed in lecture from memory.
After each section, run the file and verify the output is what I expected.

Rule: no looking at the lecture or googling unless I'm fully stuck.
"""

# ---- Section 1: basic output ----
# What does print() actually do?
# Try: print with one arg, multiple args, the sep parameter, the end parameter

print("hello, world")
print("hello", "world")
print("hello", "world", sep="-")
print("no newline", end="")
print(" right after")


# ---- Section 2: variables ----
# Variables are labels that point to values.
# Try: assign different types, reassign, multiple assignment

name = "Ian"
age = 19
gpa = 3.6

print(f"name: {name}, age: {age}, gpa: {gpa}")

# Reassignment — the variable doesn't have a fixed type
name = 42
print(f"name is now: {name}")

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)


# ---- Section 3: f-strings ----
# Try: embedding expressions, formatting numbers

pi = 3.14159265
print(f"pi to 2 decimals: {pi:.2f}")
print(f"pi rounded: {round(pi, 3)}")


# ---- What I learned ----
# - print() accepts multiple args separated by `sep`
# - end="" suppresses the newline
# - f-strings can do formatting with :.Nf for N decimal places
# - Python is dynamically typed — variables can change type

# ---- What I'm still unsure about ----
# - When should I use f-strings vs .format()? Going to find out next.
