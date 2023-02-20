#COMPLETED
#TESTED

"""
Write a program that will repeatedly take (for a student) input of this 
type: course_no, number_of_credits, and grade_received (eg. CSE101 4 A). 
These inputs are for the courses the student has done in the semester. 
If no input is given (i.e. just a return), that means no courses are left. 
From this data, print the transcript for the semester for the student as:

Course_no: grade
Course_no: grade
…

SGPA: n.nn  (two decimal places)

In the transcript, the records should be printed such that they are sorted by the 
course_no (hint: when sorting a list of tuples/lists, the default sorting is with the first 
element of the tuple/list).

The course numbers are an alphanumeric string with capital letters in the start and digits 
at the end (e.g. CSE101, CSSS21), credits can be 1, 2 or 4, and grade can be 
A+ (10), A(10), A-(9), B(8), B-(7), C(6), C-(5), D(4), F(2) 
(the number in () is their numeric equivalent for SGPA calculation.) 
The SGPA is computed as (sum of:  credits*grade/ total_credits). 
If any input is not valid, print a suitable message 
("improper course no", "incorrect credit", or "incorrect grade") and ignore that input.  

Suggestions: A list of tuples/lists may be a good structure to use. 
Read the input as tuples into a list. When inputs are done, process the list. 
First just write code to read the input, split it into a list, 
and pass it to a function to check for errors 
(recall string has operations like isdigit() to check if the string is integer). 
If input is valid, add to a list of tuples 
(initially, to check the course name structure just check if it is an alphanumeric string
- later write a function to check its valid structure - requires a bit of logic). 
Independently write a function which, given a list of tuples, can compute the SGPA. 
Then combine the two.
"""

def is_course_no(s):
    flag = True
    letters = []
    nums = []
    temp = 0

    for i in range(len(s)):
        if s[i].isalpha()==True:
            temp = i+1
            if s[i]==s[i].upper():
                letters.append(s[i])

        else:
            break

    for i in s[temp:]:
        if i.isnumeric()==True:
            nums.append(i)
        else:
            break

    if len(nums)+len(letters)!=len(s) or bool(nums)==0 or bool(letters)==0:
        flag = False
    
    return flag

def sgpa(credits, grades, GRADES):
    total_creds = 0
    sgpa = 0

    for i in credits:
        total_creds+=i

    for i in range(len(credits)):
        sgpa += credits[i]*GRADES[grades[i]]

    sgpa = sgpa/total_creds

    return sgpa


CREDITS = (1,2,4)
GRADES = {"A+":10,"A":10,"A-":9,"B":8,"B-":7,"C":6,"C-":5,"D":4,"F":2}

courses = {}
credits = []
grades = []

while(True):
    entry = input("Enter Course_No., Credits, Grade: ").split()    #program will give error if values are not entered in this order

    if entry==[]:
        break      #loop will break only at null input
                    
    try:
        entry[1] = int(entry[1])

    except ValueError:
        print("Invalid Input")
        continue

    if len(entry)!=3:
        print("Invalid Input")

    elif is_course_no(entry[0])==True and entry[1] in CREDITS and entry[2] in GRADES.keys():
        courses[entry[0]] = (entry[2])
        credits.append(int(entry[1]))
        grades.append(entry[2])

    else:
        print("Invalid Input")

lst = list(courses.keys())
lst.sort()

print("")

for i in lst:
    print(i+": "+courses[i])

sgpa = sgpa(credits,grades,GRADES)

print(f"SGPA: {round(sgpa,2)}")