# Problem
​
You are given a text represented as a string ```"t"```, and a string ```"s"``` of a length of 3. Your task is to count the number of indicies ```"i"```, such that ```t[i]```, ```t[i+2]```, ```t[i+4] = s```.
​
# Example
​
* For ```t = "azcabcab"``` and ```s = "abc"```, the output should be ```solution(t, s)= 2```.
    * ```t[0], t[2], t[4] = "abc" = s```;
    * ```t[1], t[3], t[5] = "zac" != s```;
    * ```t[2], t[4], t[6] = "cba" != s```;
    * ```t[3], t[5], t[7] = "acb" = s```.
* For ```t = ""``` and ```s = "xyz"```, the output should be ```soultion(t, s) = 0```.
​
# Input / Output
​
* **[execution time limit] .5 seconds (cpp)**
* **[input] string t**
    * A text represented as a string consisting of lowercase English letters.
    * Guraranteed constraints:
        * ```0 <= len(t) <= 1000```
* **[input] string s**
    * A string of length 3 consisting of lowercase English letters.
    * Guaranteed constraints:
        * ```len(s) = 3```
* **[output] integer**
    * The number of indices ```i```, such that ```t[i], t[i+2], t[i+4] = s```.