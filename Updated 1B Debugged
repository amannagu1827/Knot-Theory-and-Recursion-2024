from fractions import Fraction

def recalc_rat_num1(cont_frac_exp1, p, q): # For the first cont frac exp
    result = cont_frac_exp1(p, q)
    original = [] # A new list to store a reverse running sum of values to find the Original fraction
    if len(result) < 2:
        raise ValueError("The continued fraction expansion must have at least two elements.")
    new_value1 = (result[-1] * result[-2]) + 1
    if new_value1 == 0:
        raise ValueError("Zero error: The calculated value of new_value1 is zero.")
    original.append(new_value1)
    if len(result) == 2:
        return Fraction(original[-1], result[-1])
    new_value2 = (original[0]) * (result[-3]) + (result[-1])
    original.append(new_value2)
    if len(result) > 3:
        for i in range(len(result) - 3): # As len(result)>len(original), we can use the index from len(result) to iterate
            new_value3 = (original[i + 1] * result[-(i + 4)]) + original[i]
            original.append(new_value3)
        print(original)
        return Fraction(original[-1], original[-2])
    else: # When len(result) = 3
        print(original)
        return Fraction(original[-1], original[-2])


from fractions import Fraction # For the 2nd continued fraction expansion

def recalc_rat_num2(cont_frac_exp2, p, q):
    result = cont_frac_exp2(p, q)
    original = [] # A new list to store a reverse running sum of values to find the Original fraction
    if len(result) < 2:
        raise ValueError("The continued fraction expansion must have at least two elements.")
    new_value1 = (result[-1] * result[-2]) + 1
    if new_value1 == 0:
        raise ValueError("Zero error: The calculated value of new_value1 is zero.")
    original.append(new_value1)
    if len(result) == 2:
        return Fraction(original[-1], result[-1])
    new_value2 = (original[0]) * (result[-3]) + (result[-1])
    original.append(new_value2)
    if len(result) > 3:
        for i in range(len(result) - 3): # As len(result)>len(original), we can use the index from len(result) to iterate
            new_value3 = (original[i + 1] * result[-(i + 4)]) + original[i]
            original.append(new_value3)
        print(original)
        return Fraction(original[-1], original[-2])
    else: # When len(result) = 3
        print(original)
        return Fraction(original[-1], original[-2])
