# Problem
​
You are given a string ```s```, which consists only of lowercase English letters. Your task is to find the number of adjacent triplets of unique characters with ```s```.. In other words, count the number of indices ```i```, such that ```s[i]```, ```s[i + 1]```, and ```s[i + 2]``` are all pairwise distinct.
​
# Example
​
* For ```s = "abcdaaae"```, the output should be ```solution(s) = 3```.
    * If ```i = 0```, ```s[0] = 'a'```, and ```s[2], 'c'```, which are pairwise disinct.
    * If ```i = 0```, ```s[0] = 'a'```, and ```s[2], 'c'```, which are pairwise disinct.
    * If ```i = 0```, ```s[0] = 'a'```, and ```s[2], 'c'```, which are pairwise disinct.
    * If ```i = 0```, ```s[0] = 'a'```, and ```s[2], 'c'```, which are not pairwise distinct because ```s[4]``` and ```s[5]``` are equal.
    * If ```i = 0```, ```s[0] = 'a'```, and ```s[2], 'c'```, which are not pairwise distinct because all pairs of characters are equal.
    * If ```i = 0```, ```s[0] = 'a'```, and ```s[2], 'c'```, which are not pairwise distinct because ```s[5]``` and ```s[6]``` are equal.
    * ```If i = 6``` or ```i = 7```, at least one of characters ```s[i + 1]``` or ```s[i + 2]``` won't exist.
* For ```s = "abacaba",``` the output should be ```solution(s) = 2```.
    * There are only ```2``` indices meeting the criteria.
        * ```i = 1```: ```s[1] = 'b'```, ```s[2] = 'a'```, and ```s[3] = 'c'```;
        * ```i = 3```: ```s[3] = 'c'```, ```s[4] = 'a'```, and ```s[5] = 'b'```.
    * All other triplets will contain more than ```a``` character.
​
# Input / Output
​
* **[execution time limit] .5 seconds (cpp)**
* **[input] string s**
    * A text represented as a string consisting of lowercase English letters.
    * Guraranteed constraints:
        * ```1 <= len(t) <= 1000```
* **[output] integer**
​