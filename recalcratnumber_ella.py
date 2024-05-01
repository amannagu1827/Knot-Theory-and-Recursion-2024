cont_frac1 = []             #assigning an array; note we use cont_frac1 as our name as
                            #this code works for arrays generated from our function cont_frac_exp1(p,q)
def recalc_1(cont_frac1): 
    
    if not cont_frac1:
        return 0, 1         #if the continued fraction is empty return 0
    
    p, q = cont_frac1[-1], 1
    
    for term in cont_frac1[-2::-1]:     #iterating in reverse order
        p, q = term * p + q, p
        
    return p, q
