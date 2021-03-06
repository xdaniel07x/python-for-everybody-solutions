"""
Exercise  7.3: Sometimes when programmers get vored or want to have a bit of
fun, they adda harmless Easter Egg to their program. Modify the program that
prompts the user for a file name so that is prints a funny message when the
the user types in the exact file name "na na boo boo". the program should
behave normally for all other files which exist and don't exit. Here is a
sample execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
count = 0

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    else:
        print('File cannot be opened:', fname)
        quit()

for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)
