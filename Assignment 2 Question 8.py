#COMPLETED
#TESTED

"""
Given a text file (pages.txt) which has lines of the form: 
URLnn, init_importance: text containing some URLnn. 
Each line represents a page with the first URLnn being its URL and init_importance 
is a number between 0 and 1.0, which gives the initial importance of this page. 
The URLnn in the rest of the line refers to the URL links to other pages that this 
page contains. (To simplify, instead of giving a full path, we are using URLnn, 
and instead of having separate files for each page, we are giving the text of a page 
as a line in the file). Example:

URL00, 0.5: This is page zero, and has references to URL01, URL09, and also to URL08. 
It may have repeated references - so there are two references to URL09.
URL02, 0.6: This is another page (page is represented as a line in this). 
This has reference to URL05, URL04, and URL00
…

Pages are ranked according to their overall importance. Let the total number of 
unique links in a page i be links[i] (i.e. these many unique pages this page refers to). 
The overall importance of a page i is sum over all the pages (j) which have a link to 
page i of: init_importance[j]/ links[j] (i.e. all the pages to which the page j 
has a link are distributed the importance of this page equally)

Your program has to find the highest ranking N pages 
(N can be set in a variable or taken as input) for a given input file. 

It seems natural to create a dictionary with page URL as the index, 
and having its init_importance, overall importance, the set of URLs it accesses, etc 
in it. 

Note. This simplified version has only one round of computation for the overall 
importance from the init_importance. The ranking algorithm actually takes the current 
importance (starting with init_importance, which is often set to 1) and then updates 
the importance repeatedly till the changes are very small. If you want, you can extend 
your program to implement this.

Source of code for sorting dictionary by value: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/#howtosortadictionarywiththesortedmethod
"""

urls = {}
initial_imps = {}
final_imps = {}

n = int(input("Enter n: "))

with open("pages.txt","r") as file:
    input_lst = file.readlines()

for i in input_lst:
    s = i.replace("\n","")
    s = s.split(": ")
    imp = s[0].split(", ")
    initial_imps[imp[0]] = initial_imps.get(imp[0],float(imp[1]))

    for j in range(len(s[1])):
        if s[1][j:j+3]=="URL" and (s[1][j+3]).isnumeric() and s[1][j+4].isnumeric():
            urls[imp[0]] = urls.get(imp[0],[]) 
            if s[1][j:j+5] not in urls[imp[0]]:
                urls[imp[0]] += [s[1][j:j+5]] 

for i in urls:
    temp = initial_imps[i]/len(urls[i])
    for j in urls[i]:
        final_imps[j] = final_imps.get(j,0) + temp

sorted_final_imps_by_value = sorted(final_imps.items(), key=lambda x:x[1], reverse=True)
printout = list(sorted_final_imps_by_value)

for i in printout[:n]:
    print(i)