# Cryptanalysis of Caesar Cipher

This program provides the results of a statistical analysis that calculates how likely a given value, i, will be useful in converting a encrypted string of characters into an English message following the principles of the Caesar Cipher. 

# Info
This program utalizes a table of character frequencies for every letter of the English alphabet. Different tables have different frequencies. As such, answers will vary depending on the frequencies used. 

Note: The algorithm below does not consider spaces as characters. It only considers characters in the alphabet. 

# Algorithm
φ(i)=∑_(i=0)^25▒〖f(c)p(c-i)〗

Where the values correspond as follows: 
* f(c): Represents the number of occurences of a character in the encrypted string divided by the length of the encrypted string.
* p(c-i): Represents, for each value of i such that 0 ≤ i ≤ 25, subtract i from the current location of the character, c, in the alphabet. Once a new character has been found, find the corresponding character frequency.
* Let z = f(c)p(c-i) such that every distinct character in our encrypted string has its own corresponding z value.
* φ(i): For each value i such that 0 ≤ i ≤ 25, let φ(i) be the summation of every z value for a given i. 

# Program Info
* Python 3
* Python 2: In main, change the input function from input to raw_input and execute program.
* Data Structures: Lists and Dictionaries
