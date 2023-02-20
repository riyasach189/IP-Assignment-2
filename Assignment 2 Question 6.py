#COMPLETED
#TESTED

"""
For IP course, the performance in different elements of the class for students is 
given in a file (IPmarks.txt) - one line per student as comma separated values:

Roll_no,  m1, m2, m3, … 

Roll_no is a string, while m1, m2, … are integer marks the student got in assessment 
1, 2, …

Separately, the weight of each of the assessments is given as a list of tuples 
(you can hard code this in your program - assume that correct number of items is 
provided): 

wts = [(10, 5), (20, 5), (100, 15), (40, 10), …]

Where the first item is the maximum marks of the assessment, and the second is the 
weight in % this assessment carries in the final evaluation (the sum of weights 
should be 100). In the above, assessment 1 (say, a quiz) has maximum marks of 10 
and its weight in the final total is 5%; assessment 3 has max marks of 100, 
and its weight is 15).
 
For each student, compute the weighted sum of marks normalized to 100. 
(For weighted sum, assessment 1 marks can be normalized to 5, assessment 3 to 15, …), 
and the grade, and write it in a file (IPgrades.txt)  as: 

Roll_no, total_marks, grade

For grading, assume that A is above 80%, A- from 70, B from 60, B- from 50, C from 40, 
C- from 35, D from 30, and below 30 is F.
"""

ip_marks = {}
input_lst = []

with open("IPmarks.txt","r") as file:
    input_lst = file.readlines()

for i in input_lst:
    temp = i.split(", ")
    temp[-1] = temp[-1].replace(" \n","")
    temp1 = [int(elt) for elt in temp[1:]]
    ip_marks[temp[0]] = ip_marks.get(temp[0],temp1)

GRADES = {"A": 80, "A-":70, "B": 60, "B-": 50, "C": 40, "C-": 35, "D": 30, "F": 0}

WEIGHTS = [(10, 5), (20, 5), (100, 15), (40, 10), (50, 20), (100, 25), (70, 20)]

def final_marks(l1,WEIGHTS,GRADES):
    final_marks = 0
    grade = ""
    for i in range(len(l1)):
        val = l1[i]/WEIGHTS[i][0]*WEIGHTS[i][1]
        final_marks += val

    final_marks = round(final_marks,2)

    for i in GRADES:
        if final_marks>=GRADES[i]:
            grade = i
            break

    return final_marks,grade

with open("IPgrades.txt","w") as file:
    for i in ip_marks:
        rollno = i
        marks, grade = final_marks(ip_marks[i], WEIGHTS, GRADES)
        printout = f"{rollno}, {marks}, {grade}"
        file.write(printout+"\n")
