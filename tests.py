from diagram_generator_dan import generate_diagram as diagram_dan
from diagramfile import diagram as diagram_ella

if __name__ == "__main__":
    # making sure both diagrams print the same code
    diagram_dan(9, 7)
    diagram_ella(9, 7)