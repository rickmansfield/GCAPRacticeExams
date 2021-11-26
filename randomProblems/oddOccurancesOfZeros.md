 Problem:
​
You are given an array of non-negative integers ```a```. Your task is to calculate how many elements of ```a``` have an odd number of occurrences of the digit ```0```.
​
For example, for ```[4, 50, 100, 65, 2000, 700, 1, 10]```, the answer should be ```3```. These numbers are ```50```, ```2000```, ```10```.
​
# Example:
​
For ```a = [20, 11, 10, 10070, 7]```, the output should be ```solution(a) = 3```
​
* in ```a[1] = 11 and a[4] = 7``` the digit ```0``` does not occur, so these elements do not count (since zero is an even number).
* in ```a[0] = 20``` and ```a[2] = 10``` the digit ```0``` occurs one time (which is an odd number), so these elements do count.
* in ```a[3] = 10070``` the digit ```0``` occurs three times (which is an odd number), so these elements do count.
​
# Input / Output
​
* **[execution time limit] 4 seconds (py3)**
* **[input] array.integer a**
    * An array of integers.
    * Guaranteed constraints:
        * ```1 <= numbers.length <= 10<sup>5</sup> ```.
        * ```-10<sup>9</sup> <= numbers[i] <= 10<sup>9</sup>```.
* **[output]integer**
    * The number of elements of the given array ```a``` that have an odd number of occurances of the digit ```0```.