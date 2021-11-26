# Problem:
​
Given an array of integers numbers, compare the sum of elements on even positions against the sum of elements on odd positions (0 - based). Return "even" if the sum of elements on even positions is greater, "odd" if the sum of elements on odd positions is greater, or "equal" if both sums are equal.
​
# Example:
* For ```numbers = [1, 2, 3, 4, 5] ```, the ouput should be ```solution(numbers)``` = "even".
    * ## Explanation:
        * Sum of elements on even positions is ```1 + 3 + 5 = 9```.
        * Sum of elements on odd positions is ```2 + 4 = 6```.
        * ```9 > 6```, so the expected ouput is "even".
* For ```numbers = [-1, 4, 3, -2]```, the ouput should be solution(numbers) = ```"equal"```.
    * ## Explanation:
        * Sum of elements on even positions is ```(-1) + 3 = 2```.
        * Sum of elements on odd positions is ```4 + - (2) = 2```.
        * ```2 = 2```, so the expected ouput is ```"equal"```.
​
# Input / Output
* **[execution time limit]**
* **[input] array.integer numbers.**
    * An array of integers.
    * Guaranteed constraints:
        * ```0 <= numbers.length <= 1000```.
        * ```-100 <= numbers[i] <= 1000```.
    * **[output]string**
        * Return one of these values: ```"even"```, ```"odd"```, ```"equal"```, depending on the conditions described above.