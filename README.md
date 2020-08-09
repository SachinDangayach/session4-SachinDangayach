# EPAI Session 3 Assignment by Sachin Dangayach

This is assignment submission for session 3. It deals with various concepts related to Numeric Types in Python like
Integer data types, bases, functions related to floats like equality test and rounding of floating point numbers  

This repo has got two .py files named session3.py which is assignment and test_session3.py which is
used to test the submission

# Below are the key terms and functions

## 1. int - Integer Data Type: 
Unlike Java, C etc. int object uses variable number of bits in Python. It can be 4 bytes, 8 bytes or more. We can 
create an object of type int by calling the int() function or int(num, base) function. Default base in 10. If we 
want to create an int object with a binary or octal number, we have to pass the respective base.

#### i. encoded_from_base10: 
This function returns a string encoding in the "base" for the "number" using the digit_map. The number is base 10 (decimal)
format and base and digit_map are used to encod. base can be any value between 2 to 36 and if the number can be positive or negative ('-' sign should be added to encoded string).
#### ii. digit_map: 
digit_map is input parameter. It contains the literals(symbols) used to represent the number in new encoding. It should have as many symbols as is value of base. For example, if base is 2, a possible digi_map value could be '01' or 'AB' and using 
them the encoded string for number '8' will be '1000' or 'BAAA' respectively.
#### iii. ValueError: 
Value errors are the exceptions raised in case of following conditions are not satisfied-
    - If the base is not between 2 to 36 both inclusive
    - base should be of type int
    - digit_map must have sufficient length to represent the base. Length of the digit_map string should be equal to the base for encoding as otherwise we cannot represent all possible digit in new nunber system,
    - digit_map should not have any repetition as it will result into conflict in representing the digits.
#### iv.  math :
math module is a powerful module having many important functions already implemented in python. We are not using the math module in our implementation
#### v. bin() - Binary numbers:
This function returns the binary representation of a number. Binary numbers is number system with base 2. It has got two digits '0' and '1'. Decimal 8 can be represented as 1000 in binary number format.
#### v. hex() - Hexadecimal numbers: 
This function returns the Hexadecimal representation of a number. Binary numbers is number system with base 16. It has got 16 digits '0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F'. Decimal 12 can be represented as 'B' in Hexadecimal format.

## 2. Floats - Floating Point Data Types : 
Floats represents real numbers with integer and the decimal part. It is the decimal part which is not always possible to 
convert into finite binary representation results into need for approximations like rounding.

### i. isclose: 
This function is used to test the equality of two floating point numbers. It is available in MATH module. As decimal part of floating point numbers can't be always converted to binary format in which python stores the numbers and hence it reults into issues which are required to be handled. isclose uses approximation based of relative or absolute tolerance to decide equality of two numbers.
### ii. absolute: 
Absolute tolerance is fixed value of tolerance used to check the similarity of two numbers. This is the maximum value by which they can differ. It works for small numbers near to zero but doesn't work good for large numbers. example, abs_tol can be 10^-14
### iii. relative: 
Relative tolerance is maximum allowed difference between two numbers relative to the magnitude of larger among them. This might not work in case if we have one number as zero and the other a small number less the one but greater than zero.
### iv. tolerance: 
Tolerance is the maximum allowed difference between two numbers to be called as equals. We have to combine the absolute and relative tolerances to find the similarity of two numbers.
### v. error: 
Using only one type of tolerance (absolute or relative) doesn't work for all cases and thus results into error and the max of these two should be considered as tolerance
### iv. equality: 
We can use the tolerances based method (using both relative and absolute) to decide the equality to two float numbers 
### iv. round: 
It is a built in function in python which is used to round a number x to the closest multiple of 10^(-n). If n is not specified, it is defaulted to zero
### v. truncation: 
This function returns the truncated part for the floating point input by ignoring everything after decimal point. For example,
10.7 will be truncated to 10.
### vi. zero: 
In the function for rounding numbers in case of ties we can have number rounded towards or away from zero based if based on the even or odd digit least significant digit.
### vii. away: 
In the function for rounding numbers in case of ties we can have number rounded towards or away from zero based if based on the even or odd digit least significant digit.

test_session3.py file contains the test script to test the corrections made in session3.py file.
