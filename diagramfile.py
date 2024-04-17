def cont_frac_exp1(p,q):

    result=[]

    while q != 0:

        r=p//q

        s=p%q # Making use of the modulo arthimatic

        result.append(r)

        p, q = q, s

    return result

def print_crossing(type):
    """ draws very rough crossings for 2-bridge knots. Gives one crossing in either of the two positions and signs."""
    if type == 1:
        print("| |  \ / ")
        print("| |   /  ")
        print("| |  / \ ")
    elif type ==-1:
        print("| |  \ / ")
        print("| |   \  ")
        print("| |  / \ ")
    elif type == 2:
        print("| \ /  | ")
        print("|  /   | ")
        print("| / \  | ")
    elif type == -2:
        print("| \ /  | ")
        print("|  \   | ")
        print("| / \  | ")
        
    elif type == 10:
        print(" ______  ")
        print("|  __  | ")
        print("| |  | | ")
    
    elif type == -10:
        
        print("| |__| | ")
        print("|______|  ")

    elif type == -20:
        print("| |  | |")
        print("|_|  |_|" )
     
        
def diagram(array):
    
    num = len(array)
    
    print_crossing(10)
    
    for i in range(num):
        

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
            
    if num%2 == 0:
        print_crossing(-20)
    else:
        print_crossing(-10)
