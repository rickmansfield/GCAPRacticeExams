def findPairs(array, s):
    pairs = []

    for i in range(len(array)-1):
        # print(array[i])
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == s:
                pairs.append([array[i], array[j]])
            else:
                continue
    return pairs

a = [3, 5, 2, -4, 8, 11]
print(findPairs(a, 7))