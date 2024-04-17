from fractions import Fraction

def recalc_rat_num1(result):
    original = [] # A new list to store a reverse running sum of values to find the Original fraction
    new_value1 = (result[-1] * result[-2]) + 1
    original.append(new_value1)
    new_value2 = (original[0]) * (result[-3]) + (result[-1])
    original.append(new_value2)
    if original[-1] == 0: # The denominator can't be zero
        raise ZeroDivisionError("The denominator of the Fraction cannot be zero.")
    else:    
        if len(result) < 2:
            raise ValueError("The continued fraction expansion must have at least two elements.")
        elif len(result) > 3:
            for i in range(len(result) - 3):
                new_value3 = (original[i + 1] * result[-(i + 4)]) + original[i] # As len(result)>len(original), we can use the index from len(result) to iterate over len(original) and need to a separate for loop that iterates over len(original)
                original.append(new_value3)
            print(original)    
            return Fraction(original[-1], original[-2]) # The numerator over the denominator
        else: # Special case when len(result) = 3
            print(original)
            return Fraction(original[-1], original[-2])
