# Implement the Luhn Algorithm, which is used to help validate credit card numbers.
# Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.
# Algorithm:
# 1. If there are an even number of digits, double every other digit starting with the first; if there are an odd number of digits, double every other digit starting with the second.
# 2. If a resulting number is greater than 9, replace it with the sum of its own digits (which is the same as subtracting 9 from it).
# 3. Sum all of the final digits.
# 4. Take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid.

def validate(digits):
    # convert given number into an array of single digits
    num_array = [int(i) for i in str(digits)]
    
    # loop thrugh array's digits, starting with first index, until second-to-last index
    n = 0
    while n <= len(num_array) - 2:
       # if given odd number of digits
        if len(num_array) % 2 == 1:
            # double every other digit (starting with second index)
            num_array[n+1] *= 2
            # if new number > 9, replace it with sum of its digits
            if num_array[n+1] > 9:
                num_array[n+1] -= 9
            
        # if given even number of digits
        if len(num_array) % 2 == 0:
            # double every other digit (starting with first index)
            num_array[n] *= 2
            # if new number > 9, replace it with sum of its digits
            if num_array[n] > 9:
                num_array[n] -= 9
            
        n += 2
      
    # sum all final digits
    sum = 0
    for i in num_array:
        sum += i
    
    # divide sum by 10, if remainder is 0, original card number is VALID
    return True if sum % 10 == 0 else False

# --- Test Cases --- #
print(validate(1423))       # => False; because [1, 4, 2, 3] -> [2, 4, 4, 3] -> 13 (mod) 10 = 3
print(validate(87456))      # => False; because [8, 7, 4, 5, 6] -> [8, 14, 4, 10, 6] -> [8, 5, 4, 1, 6] -> 24 (mod) 10 = 4
print(validate(1214))       # => True; because [1, 2, 1, 4] -> [2, 2, 2, 4] -> 10 (mod) 10 = 0
print(validate(34769))      # => True; because [3, 4, 7, 6, 9] -> [3, 8, 7, 12, 9] -> [3, 8, 7, 3, 9] -> 30 (mod) 10 = 0
print(validate(563489))     # => False; because [5, 6, 3, 4, 8, 9] -> [10, 6, 6, 4, 16, 9] -> [1, 6, 6, 4, 7, 9] -> 33 (mod) 10 = 3