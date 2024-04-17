import random
from Cont_Frac_Exp1 import *

def cont_frac_exp2(p, q):
    result_exp1 = cont_frac_exp1(p, q)
    result = []
    while True:
        random_int = random.randint(1, 5)
        if random_int != result_exp1[0]:  # Check if it's different from the first element of result_exp1
            result.append(random_int)
            break
    if q == 0:
        raise ZeroDivisionError("The denominator of the Fraction cannot be zero.")
    while result[0] != result_exp1[0]:
        if result[0] == p // q:
            print('This will give you the same expansion list as cont_frac_exp1, please try a different p and q')
        elif result[0] > p // q:
            if q > abs(p - q * result[0]):
                p, q = -q, abs(result[0] * q - p)
                r, s = p // q, abs(p % q)
                result.append(r)
                p, q = q, s
                Normal_exp1 = cont_frac_exp1(p, q)
                for i in Normal_exp1:
                    result.append(i)
                return result
            else:
                p, q = abs(p - q * result[0]) - q, abs(p - q * result[0])
                result.append(-1)
                p, q = q, p
                Normal_exp2 = cont_frac_exp2(p, q)
                for i in Normal_exp2:
                    result.append(i)
                return result
        else:
            if q > p - (q * result[0]):
                p, q = q, p % q
                r = p // q
                result.append(r)
                Normal_exp3 = cont_frac_exp2(p, q)
                for i in Normal_exp3:
                    result.append(i)
                return result
            else:
                p, q = q, p - (q * result[0])
                result.append(1)
                p, q = -q, q - p
                Normal_exp4 = cont_frac_exp2(p, q)
                for i in Normal_exp4:
                    result.append(i)
                return result
            
