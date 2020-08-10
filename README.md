# EPAI Session 4 Assignment by Sachin Dangayach

This is assignment submission for session 4. It deals with various concepts related to Numeric Types in Python like
Floats, Decimals and Boolean.

This repo has got two .py files named session4.py which is assignment and test_session4.py which is
used to test the submission

# Below are the key methods of Qualean Class
# Qualean Class
We have build a class named Qualean inspired by Boolean+Quantum concepts. We can assign it 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state but multiplying that state with a random number between (-1,1) using Bankers rounding to 10th decimal place.

## 0. State : 
Attribute of class holding imaginary state ( Random number between (-1,1))

Note: Q1 and Q2 are considered as class instance while describing the implementations below

## 1. __and__ : 
Impelement boolean 'and' between two Qualeans Q1 and Q2 result True only when both Q1 and Q2 are non zero

## 2.  __or__ : 
Impelement boolean 'or' between two Qualeans Q1 and Q2 result True if even anyone of Q1 or Q2 is non zero

## 3. __repr__ : 
Return the string representation of Qualean object in class constructor format  

## 4. __str__ : 
Return the string representation of Qualean object in readable text output

## 5. __add__ : 
Perform addition operation between two Qualeans Q1 and Q2 or Qualean and int, float or decimal input. Returns Not implemented for other types

## 6. __eq__ : 
Returns true if both Q1 and Q2 have similar value in attribute state

## 7.  __float__ : 
Return float representation of state attribute for a Qualean object

## 8. __ge__ : 
Returns True based of greater than or equals to check on  state attribute for a Qualean object Q1 and Q2 else return False

## 9. __gt__ : 
Returns True based of greater than to check on  state attribute for a Qualean object Q1 and Q2 else return False

## 10. __invertsign__ : 
Returns the Quelean with sign of state attribute changed

## 11.  __le__ : 
Returns True based of lesser than to check on  state attribute for a Qualean object Q1 and Q2 else return False

## 12. __lt__ : 
Returns True based of lesser than to check on  state attribute for a Qualean object Q1 and Q2 else return False 
## 13. __mul__ : 
Perform multiplication operation between two Qualeans Q1 and Q2 or Qualean and int, float or decimal input. Returns Not implemented for other types

## 14. __sqrt__ : 
Returns the square root of Qualean state attribute value 

## 15. __bool__ : 
Return False if state is 0 else True for a Qualean 

# Test Cases - test_Session.py

## 1. test_readme_exists : 
Test for readme exists

## 2. test_readme_contents : 
Test for readme contents are mor than 500 words

## 3. test_readme_proper_description : 
Test for all important functions/class described well in your README.md file

## 4. test_readme_file_for_formatting : 
Test for readme formatting

## 5. test_indentations : 
Test for source code formatting. No tabs but four spaces are used for indentation

## 6. test_function_name_had_cap_letters : 
Test for no function is with capitals in source code

## 7. test_innacurate_addition : 
Test for rounding errors in case we have a qualean added 100 times should be equal to 100* qualean. In this case, rounding to 6 digit is used as multiplication by 100 reduces the decimal digits. We have used a function named check_qualean_addition to implement this check

## 8. test_qualean_square_root : 
Returns the square root of the value of state attribute of Q1. If state is negative, returns complex number as output 

## 9. test_normal_dist_state : 
Generate 1 Million quals with state 1 and another million with state -1. Test their sum is near to 0 by using isclose

## 10. test_boolean_and : 
Test for boolen and operatoin on qualeans based on the value of state attribute for Q1 and Q2. Returns false it one of Q1 or Q2 state is 0

## 11. test_boolean_or : 
Test for boolen and operatoin on qualeans based on the value of state attribute for Q1 and Q2. Returns false it one of Q1 or Q2 state is 0

## 12. test_string_repr : 
test for qualean string for repr()

## 13. test_string_representation : 
test string representation in readable form

## 14. test_qualean_float : 
test conversion to float from qualean. The state attribute is used to convert to float

## 15. test_qualean_ge_inequality : 
Check for the greater than or equal to ineqaulity of qualeans

## 16. test_qualean_gt_inequality : 
Check for the greater than ineqaulity of qualeans

## 17. test_qualean_le_inequality : 
Check for the lesser than or equal to ineqaulity of qualeans

## 18. test_qualean_lt_inequality : 
Check for the lesser than or equal to ineqaulity of qualeans

## 19. test_sign_inversion : 
Test to check the inversion of sign for a qualean. sum of qualean and it's sign inversion should be 0

## 20. test_qual_to_bool : 
Check qual to bool conversion. It the state attribute is 0, it returns false else true

## 21. test_qualean_negative_square_root : 
Check the square root for qualean with state less than zero is a complex number

## 22. test_qual_creation : 
Check for the value passed to constructor for Qualean is either of 1,0 or -1. If anything else is passed, raise error.

## 23. test_qual_multiplication : 
Check for multiplication only Qualean, Decimal, int and float types input

## 24. test_qual_add : 
Check for addition is allowed for Qualean, Decimal, int and float types input

## 25. test_qualean_inequality : 
Test for ge, gt, le, lt should be allowed only between Qualeans