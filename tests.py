from diagram_generator_dan import generate_diagram as diagram_dan
from diagramfile import cont_frac_exp1, diagram as diagram_ella
from Cont_Frac_exp2 import *
from recalc_rat_num1 import *

if __name__ == "__main__":
    # making sure both diagrams print the same code
    diagram_dan(9, 7)
    diagram_ella(cont_frac_exp1(9, 7))
    diagram_ella(cont_frac_exp1(9, -7))
    diagram_ella(cont_frac_exp1(9, 2))
    # diagram_ella([2, -2, 2, 3])
    # diagram_ella(cont_frac_exp2(9, 7))
    print(recalc_rat_num1(cont_frac_exp1(9, 7)))
    print(recalc_rat_num1(cont_frac_exp1(9, -7)))
    print(recalc_rat_num1([2, -2, 2, -3]))
    print(recalc_rat_num1(cont_frac_exp2(9, 7)))