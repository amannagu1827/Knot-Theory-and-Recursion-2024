# I added new types for the final link
# The diagram generating fucntion uses cont_frac_exp1()

from Cont_Frac_Exp1 import *

def print_crossing(type):
    """ draws very rough crossings for 2-bridge knots. Gives one crossing in either of the two positions and signs."""
    if type == 1:
        print("| |  \ / ")
        print("| |   /  ")
        print("| |  / \ ")
    elif type == -1:
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
    elif type == 3:
        print("| |  \ / ")
        print("| |   /  ")
        print("| |__/ \ ")
    elif type == -3:
        print("| |  \ / ")
        print("| |   \  ")
        print("| |__/ \ ")
    elif type == 4:
        print("| \ /  | ")
        print("|  /   | ")
        print("| /_\  | ")
    elif type == -4:
        print("| \ /  | ")
        print("|  \   | ")
        print("| /_\  | ")

def generate_diagram(p,q):
    L = cont_frac_exp1(p,q)
    print(" ______")
    print("/ ___  \ ")
    for i in range(len(L)-1):
        
        if i % 2 == 0 and L[i] > 0:
            for j in range(L[i]):
                print_crossing(1)   
          
        elif i % 2 == 0 and L[i] < 0:
            for j in range(-L[i]):
                print_crossing(-1)
          
        elif i % 2 == 1 and L[i] > 0:
            for j in range(L[i]):
                print_crossing(2)
          
        elif i % 2 == 1 and L[i] < 0:
            for j in range(-L[i]):
                print_crossing(-2)
                       
    if len(L) % 2 == 1 and L[-1] > 0:
            print_crossing(3)
            
    elif len(L) % 2 == 1 and L[-1] < 0:
        print_crossing(-3)
    
    elif len(L) % 2 == 0 and L[-1] > 0:
        print_crossing(4)
        
    elif len(L) % 2 == 0 and L[-1] < 0:
        print_crossing(-4)
          
    print("\______/")
