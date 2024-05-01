# Code to display various twists in a 2-bridge link.
from Cont_Frac_Exp1 import *

def print_crossing(type):
    output = []
    if type == 1:
        output.append(r'| |  \ / ')
        output.append(r'| |   /  ')
        output.append(r'| |  / \ ')
    elif type == -1:
        output.append(r'| |  \ / ')
        output.append(r'| |   \  ')
        output.append(r'| |  / \ ')
    elif type == 2:
        output.append(r'| \ /  | ')
        output.append(r'|  /   | ')
        output.append(r'| / \  | ')
    elif type == -2:
        output.append(r'| \ /  | ')
        output.append(r'|  \   | ')
        output.append(r'| / \  | ')
    elif type == 10:
        output.append(r' ______  ')
        output.append(r'|  __  | ')
        output.append(r'| |  | | ')
    elif type == -10:
        output.append(r'| |__| | ')
        output.append(r'|______| ')
    elif type == -20:
        output.append(r'| |  | | ')
        output.append(r'|_|  |_| ')
    return output

def make_diagram(p,q):

    array = cont_frac_exp1(p,q)

    num = len(array)

    output = []

    output += print_crossing(10)

    for i in range(num):
        if array[i] > 0 and (i+1)%2 != 0:
            for j in range(array[i]):
                output += print_crossing(1)
        elif array[i-1] < 0 and (i+1)%2 != 0:
            for j in range(abs(array[i])):
                output += print_crossing(-1)
        elif array[i-1] > 0 and (i+1)%2 == 0:
            for j in range(abs(array[i])):
                output += print_crossing(-2)
        elif array[i-1] < 0 and (i+1)%2 == 0:
            for j in range(abs(array[i])):
                output += print_crossing(2)  
    
    if num%2 == 0:
        output += print_crossing(-20)
    else:
        output += print_crossing(-10)

    return output


def print_diagrams(*diagrams):
    final_diagram = []
    final_diagram_length = max([len(diagram) for diagram in diagrams])
    for i in range(final_diagram_length):
        final_diagram.append([])
    for diagram in diagrams:
        for key in range(final_diagram_length):
            if key < len(diagram):
                final_diagram[key] += [diagram[key]]
            else:
                final_diagram[key] += ['         ']
    for line in final_diagram:
        print("   ".join(line))

if __name__ == "__main__":
    print_diagrams(make_diagram(9, 7), make_diagram(9, 2), make_diagram(2, 3), make_diagram(17, 5))