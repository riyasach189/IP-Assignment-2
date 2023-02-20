#COMPLETED
#will not work for empty file
#TESTED

"""
Before you graduate, you get the signature from all your friends in your yearbook - 
which will be stored as a dictionary for the program. In this dictionary, the keys are the name 
of other students in the batch; the value is either 0 (for not signed) or 1 (for signed). 
Like you, all other students are also doing the same - and there is dictionary entry for each. 
For creating this dictionary, input is given in a file - if there are N students, 
then the file contains:

name1:
name2, 1
name3, 0
name4, 1
…
name2:
name1, 0
name3, 0
name4, 0
…

(Like this data is there for all the graduating students).

Write a program to determine who has the most signatures and who has the least 
(if there are more than one for max/min - print all).

Suggestion. Initially manually create a dictionary yearbook = {name1: {...}, name2: {....}, …}, 
and then determine students with most/least signatures. 
Then write a function to read the file and create this dictionary.
"""

yearbook = {}
input_lst = []
lst_1 = []
with open("records.txt","r") as file:
    input_lst = file.readlines()

for i in input_lst:
    if i!="\n":
        s = i.replace("\n","")
        lst_1.append(s)

for i in range(len(lst_1)):
    if lst_1[i][-1]==":":
        yearbook[lst_1[i][:-1]] = yearbook.get(lst_1[i][:-1],[])
        for j in lst_1[i+1:]:
            if j[-1]==":":
                break
            else:
                yearbook[lst_1[i][:-1]] = yearbook.get(lst_1[i][:-1],[]) + [j]

for i in yearbook:
    d = {}
    for j in yearbook[i]:
        s = j.split(",")
        d[s[0]] = d.get(s[0],0) + int(s[1])

    yearbook[i] = d

counter = {}

for i in yearbook:
    count = 0
    for j in yearbook[i]:
        count += yearbook[i][j]
    
    counter[i] = counter.get(i,count)

minimum = min(counter.values())
maximum = max(counter.values())

max_stu = [i for i in yearbook if counter[i]==maximum]
min_stu = [i for i in yearbook if counter[i]==minimum]

print(f"Students with maximum signatures: {max_stu}")
print(f"Students with minimum signatures: {min_stu}")