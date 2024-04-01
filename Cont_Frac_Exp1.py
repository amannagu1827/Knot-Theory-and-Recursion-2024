def cont_frac_exp1(p,q):
    result=[]
    while q != 0:
        r=p//q
        s=p%q # Making use of the modulo arthimatic
        result.append(r)
        p, q = q, s
    return result
