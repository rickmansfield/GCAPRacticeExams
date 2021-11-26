# Problem:
​
You are given an array of strings ```"a"```. Your task is to construct an array of strings of the same length, where the ith element is equal to the first character of ```a[i]```, concatenated with the last character of the ```a[i+1]```.
​
If there is no ```a[i+1]```, cycle back to the beginning of the array. In other words, for the final element, concatenate the first character of a[a.length - 1] with the last character of ```a[0]```.
​
Retrun the resulting array of the 2-character strings.
​
# Example
​
* for ```a = ["cat", "dog", "farret", "scorpion"]```, the output should be ```solution(a) = ["cg", "dt", "fn", "st"]```.
* for ```a = ["I", "have", "a", "nice", "suprise"]```, the output should be ```solution(a) = ["Ie", "ha", "ae", "ne", "sI"]```.
* for ```a = ["singularity"]```, the output should be ```solution(a) = ["sy"]```.
​
# Input / Output
​
* **[execution time limit] 4 seconds (py3)**
* **[input] array.string ```a```**
    * An array of strings consisting of alphanumeric characters
    * Guaranteed constraints:
        * ```1 <= a.length <= 100```
        * ```1 <= a[i].length <= 100```