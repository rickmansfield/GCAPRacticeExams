# Problem
​
Given an integer ```n``` your task is to reverse its digits in pairs. More formally, if ```n = d[1],d[2],d[3]```... (where ```d[i]``` is the ith digit in the decimal representation of ```n``` then the answer should be ```d[2], d[1], d[4], d[3]```... If the number of digits is odd, the last digit should stay in the same position.
​
# Example
​
* for ```n = 123456```, the output should be ```solution(n) = 214365```
* for ```n = 72328```, the output should be ```solution(n) = 27238```
    * Since ```n``` has an odd number of digits, the last digit ```8``` is not swapped with any other digit.
​
# Input/Output
​
* A 32 bit integer. It is guaranteed that:
    * The second digit of ```n``` is not zero.
    * The number after reversing digits in pairs also fits in a 32-bit integer type.
​
* Guarenteed constraints:
    * ```1 <= n <= 10<sup>9</sup>```
​
* **[Output] Integer**
    * An integer, obtained by reversing the digits of n pairs.