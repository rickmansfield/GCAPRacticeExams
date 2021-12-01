# function which returns true if the pair with given sum k exists
# else it will return false
def checkPair(givenlist, value):
  # calculating the length of given list
    length = len(givenlist)
   # Traversing all elements in given list except the last
    for i in range(length - 1):
        # iterating from i+1 element to last element
        for j in range(i + 1, length):
            # if the given sum "value" is found then return true
            if givenlist[i] + givenlist[j] == value:
                # pair is found so it should return true
                return True
    # if no pair is found then we should return true
    return False
# given list
given_list = [5, 9, 2, 8, 7, 6]
# given element k
value = 10
# passing the given list and value to checkPair function
if(checkPair(given_list, value)):
    print("Pair with given sum of elements is found")
else:
    print("Pair with given sum of elements is not found")