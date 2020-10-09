"""
Exercise 1: Write a program to read through a file and print the contents of
the file (line by line) all in upper case. Executing the program will look as
follows:
"""

fileName = input('Enter a file name: ')
fhand = open(fileName)
for line in fhand:
    capital = line.upper().strip()
    print(capital)
