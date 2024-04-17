import random

def cont_frac_exp2(p, q):
    result_exp1 = cont_frac_exp1(p, q)
    result = []
    while True: # We want a continued fraction expansion that will always be different to cont_frac_exp1
        random_int = random.randint(1, 5) # We will generate a random number between 1 and 5 as the first number in the cont_frac_exp2, a dif its the same as cont_frac_exp1, then it will generate another interger between 1 and 5        if random_int != result_exp1[0]:  # Check if it's different from the first element of result_exp1
        result.append(random_int)
        break
    if q == 0: # Can't divide by zero
        raise ZeroDivisionError("The denominator of the Fraction cannot be zero.")
    while result[0] != result_exp1[0]:
        if result[0] == p // q:
            print('This will give you the same expansion list as cont_frac_exp1, please try a different p and q')
        elif result[0] > p // q: # There are 4 cases in which we need to consider when doing the expansion with a random integer
            if q > abs(p - q * result[0]):# Case 1 and 2 are when the first term in the results list is bigger than p(modq)   
                p, q = -q, abs(result[0] * q - p) # Case 1 is when q is bigger than the absolute value of the numerator subtracted from q*result[0]
                r, s = p // q, abs(p % q) # Doing Euclid Algorithm by hand to compute the first terms of p and q
                result.append(r)
                p, q = q, s
                Normal_exp1 = cont_frac_exp1(p, q)
                for i in Normal_exp1:
                    result.append(i)
                return result
            else: # Case 2 is when q is smaller than the absolute value of the numerator subtracted from q*result[0]
                p, q = abs(p - q * result[0]) - q, abs(p - q * result[0])
                result.append(-1)
                p, q = q, p
                Normal_exp2 = cont_frac_exp1(p, q)
                for i in Normal_exp2:
                    result.append(i)
                return result
        else: # Case 3 and 4 are when the first term in the results list is smaller than p(modq)
            if q > p - (q * result[0]): # Case 3 is when q is bigger than the absolute value of the numerator subtracted from q*result[0]
                p, q = q, p % q
                r = p // q
                result.append(r)
                Normal_exp3 = cont_frac_exp1(p, q)
                for i in Normal_exp3:
                    result.append(i)
                return result
            else: # Case 4 is when q is smaller than the absolute value of the numerator subtracted from q*result[0]
                p, q = q, p - (q * result[0])
                result.append(1)
                p, q = -q, q - p
                Normal_exp4 = cont_frac_exp1(p, q)
                for i in Normal_exp4:
                    result.append(i)
                return result
            
