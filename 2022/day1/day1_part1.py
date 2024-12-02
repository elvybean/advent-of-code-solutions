#convert txt file into a 2D array/list
#when theres a space this repersents a new array/list

import csv

total = []

with open('day1_input.txt', 'r') as fd:
    reader = csv.reader(fd)
    temp = []
    for row in reader:
        match bool(row == ""):
            case False:
                temp.append(row)
            case True:
                total.append(temp)
                temp = []

    
print(total)

