def cont_frac_exp1(p,q):

    result=[]

    while q != 0:

        r=p//q

        s=p%q # Making use of the modulo arthimatic

        result.append(r)

        p, q = q, s

    return result


def diagram(p,q):
    
    array = cont_frac_exp1(p,q)
    
    num = len(array)
    
    print_crossing(10)
    
    for i in range(num):
    #while i < num:    

        if array[i] > 0 and (i+1)%2 != 0:
            for j in range(array[i]):
                print_crossing(1)
        elif array[i-1] < 0 and (i+1)%2 != 0:
            for j in range(abs(array[i])):
                print_crossing(-1)
        elif array[i-1] > 0 and (i+1)%2 == 0:
            for j in range(abs(array[i])):
                print_crossing(-2)
        elif array[i-1] < 0 and (i+1)%2 == 0:
            for j in range(abs(array[i])):
                print_crossing(2)  
            
    print_crossing(-10)
