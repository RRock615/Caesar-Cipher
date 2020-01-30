# Cryptanalysis of Caesar Cipher

This program provides the results of a statistical analysis that calculates how likely a given value, i, will be useful in converting a encrypted string of charachters into an English message following the principles of the Caesar Cipher. 

# Info
This program utalizes a table of character frequencies for every letter of the English alphabet. Different tables have different frequencies. As such, answers will vary depending on the frequencies used. 

# Algorithm
φ(i)=∑_(i=0)^25▒〖f(c)p(c-i)〗

Where the values correspond as follows: 
* f(c): Represents the number of occurences of a charachter in the encrypted string divided by the length of the encrypted string.
** f(c)=  (number of times character appears in encrypted string)/(length of encrypted string)
* φ(i): For each value i such that 0 ≤ i ≤ 25, let φ(i)
For all values of i such that 0 ≤ i ≤ 25, find  
For every character in encrypted string, 



