# Problem:
​
You are given an array of numbers containing elements that are supposed to be sorted in an alternating pattern. Your taks is to find if there are elements in this array which breaks the alternating pattern.
​
Return an index of the first element that breaks alternating pattern or -1 if there is no such element.
​
# Example:
​
* For numbers = ```[1, 3, 1, 2, 1, 3], the ouput could be solution(numbers) = 3
    * Since ```numbers[0]``` =, ```numbers[2] = 1```, ```numbers[1] = 3```, the alternating pattern should be ```[1,3]```. The first element to break this alternating pattern is ```numbers[3] = 2```.
        * For numbers = [1, 3, 1, 3, 1, 3], the output should be solution(numbers) = -1
    * The alternating patter is also ```[1 , 3]```, but there aren't any elements that break this pattern.
​
# Input / Output
​
* **[execution time limit] 4 seconds (py3)**
* **[input] array.integer numbers.**
    * An array of integers.
    * Guaranteed constraints:
        * ```1 <= numbers.length <= 1000```.
        * ```-10<sup>9</sup> <= numbers[i] <= 10<sup>9</sup>```.
* **[output]integer**
    * Return an index of the first element that breaks the alterating pattern, or ```-1``` if there is no such element.