# Problem:
​
Since you love games of chance, you decided to participate in a dice-rolling competition. The competition involves rolling 6-sided dice, and the results of each die are represented by integers ```a```, ```b```, and ```c``` repectively. Scores are calculated according to the following rules:
​
* If all three dice had the same value ```(a = b = c)``` then you earn ```1000 * a```.
* If exactly two of them are the same you earn ```500 * x``` (where ```x``` is the value of the two equal dice).
* If all of them are different, you ```100 * min(a, b, c).
​
Given all the values of ```a```, ```b```, and ```c```, your task is to calculate and return your toal score.
​
# Example:
​
* for ```a <= 3```, ```b <= 3```, and ```c<=3``` the output should be ```solution(a, b, c) = 3000```.
    * Since all of the dice have the same value, your total socre is equal to ```1000 * 3 = 3000```.
* for ```a <= 3```, ```b <= 6```, and ```c<=3``` the output should be ```solution(a, b, c) = 1500```.
    * Since exactly two of the values are the same ```(a = c = 3)```, your total score is equal to ```500 * 3 = 1500```.
* for ```a <= 3```, ```b <= 2```, and ```c<=5``` the output should be ```solution(a, b, c) = 200```.
    * Since all of these values are different, your total socre is equal to ```100 * 2 = 200```.
​
# Input / Output
​
* **[execution time limit] 4 seconds **(py3)**
* **[input] integer a**
    * An integer of representing the value of the first die.
* **[output]integer b**
    * An integer of representing the value of the second die.
* **[output]integer c**
    * An integer of representing the value of the third die.