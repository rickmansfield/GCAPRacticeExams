
"""
convert the list of integers to a list of strings using map(str,a) or str() in a loop

"".join() to convert all number-strings into one long number-string
i.e. ['25', '2', '3', '57', '38', '41'] to 2523573841

list() to convert string back to list i.e. ['2', '5', '2', '3', '5', '7', '3', '8', '4', '1']

Use a "for Loop" to convert each string in the list to an integer
i.e. 
[2, 5, 2, 3, 5, 7, 3, 8, 4, 1]

Use Counter() to convert list to a dictionary and count frequency of each key and assign it to a variable "countDict"
i.e. Counter({2: 2, 5: 2, 3: 2, 7: 1, 8: 1, 4: 1, 1: 1})

initiate empyt array called finalList = []

loop over countDict dictionary 
    if values at each key are equal to the max frequency 
        append finalList[]
        (note this required using max() and values())
"""
from collections import Counter
from typing import final

def mostFrequentDigits(a):
    strOfNumbers = [str(i) for i in a]
    oneLongNumber = "".join(strOfNumbers)
    strOfSingleDigits = list(oneLongNumber)

    for i in range(0, len(strOfSingleDigits)):
        strOfSingleDigits[i] = int(strOfSingleDigits[i])
    countedDict = Counter(strOfSingleDigits)
    finalList = [key for key in countedDict if countedDict[key] == max(countedDict.values())]
    
    return sorted(finalList)
    
print(mostFrequentDigits([25, 2, 3, 57, 38, 41]))

