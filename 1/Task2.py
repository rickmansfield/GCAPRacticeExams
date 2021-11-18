
"""
convert the list of integers to a list of strings using map() or str()
convert all number-strings into one long number-string
i.e. ['25', '2', '3', '57', '38', '41'] to 2523573841
convert string back to list i.e. ['2', '5', '2', '3', '5', '7', '3', '8', '4', '1']
convert list to dictionary and count frequency of keys using Counter()
i.e. Counter({2: 2, 5: 2, 3: 2, 7: 1, 8: 1, 4: 1, 1: 1})
return max Counted digit
append the list with any missing digit

"""
from collections import Counter
from typing import final
# print(help(slice))

def mostFrequentDigits(a):
    print("original list", a)
    
    x=map(str, a)
    y = list(x)
    print("converted list of integert to strings y", y)
    
    s = [str(i) for i in a]
    print("converted list of integers to strings s", s)
    
    res = "".join(s)
    print("heres res or s joined", res)
    
    backToStringsList = list(res)
    print("BackToStringList using list()", backToStringsList)

    for eachString in range(0, len(backToStringsList)):
        backToStringsList[eachString] = int(backToStringsList[eachString])
    print("Convert to int's", backToStringsList)
    
    countedDict = Counter(backToStringsList)
    print("countedDict = ", countedDict)
    
    s2 = [int(i) for i in countedDict]
    print("Converted list of numbers as strings back to integers (not useful)", s2)
    
    finalList = []
    for k in countedDict:
        if countedDict[k] == max(countedDict.values()):
            finalList.append(k)
            
    return finalList

print(mostFrequentDigits([25, 2, 3, 57, 38, 41]))