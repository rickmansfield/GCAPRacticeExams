# UPER
# create final Results array []
# loop the array "numbers" from i:i+2:3
# while i is < len(numbers)-2
# ?? might create a stack/queue out of the integers 
# check if a < b > c or a > b < c is true
# append final results array with 1
# else append with 0
def solution(numbers):
    output = []
    m = len(numbers) -2
    while not m < 3:
        for i in range(len(numbers)-2):
            for v in numbers[i:i+2:3]:
                print("v = ", v)
                if (numbers[v] < numbers[v+1] > numbers[v+2]) or (numbers[v] > numbers[v+1] < numbers[v+2]):
                    output.append(1)
                    print("output", output)
                else:
                     output.appent(0)
            return output
print(solution([1, 2, 1, 3, 4]))
