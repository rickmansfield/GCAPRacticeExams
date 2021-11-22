def solution(a):
    # create dict
    # loop through array
    # put in counter for each letter in dict
    # add 1 to count of each key in dict
    # check dict for the biggest value
    # create list
    # add keys to list that have the established biggest value
    # sort and return list

    hash_map = {}
    
    for i in range(len(a)):
      some_string = str(a[i])
      for x in some_string:
        if x not in hash_map:
          hash_map[x] = 0
        hash_map[x] += 1

    print(hash_map)

    # max_val = 0
    # for key in hash_map:
    #   if hash_map[key] > max_val:
    #     max_val = hash_map[key]
    max_val = max(hash_map.values())

    print(max_val)

    output = []
    for key in hash_map:
      if hash_map[key] == max_val:
        output.append(int(key))
    
    return sorted(output)
        

        
# print(solution([25,2,3,57,38,41,])) # [2,3,5]
print(solution([25,2,3,57,38,41,25,2,3,57,38,41,25,2,3,57,38,41,25,2,3,57,38,41,25,2,3,57,38,41,25,2,3,57,38,41,25,2,3,57,38,41,25,2,3,57,38,41])) # [2,3,5]