from random import randrange

def calculate_d_invariant(p, q, i):
    if p == 1:
        return 0
    p_mod_q = p % q
    i_mod_p = i % p
    if p_mod_q == 0:
        return 0
    else:
        return ((2 * i + 1 - p - q) ** 2 - p * q) / (4 * p * q) - calculate_d_invariant(q, p_mod_q, i_mod_p)

def compute_d_invariants(p, q):
    d_invariants = []
    for i in range(p + q):
        d_invariants.append(calculate_d_invariant(p, q, i))
    return d_invariants

# We have S(p,q) = S(p, q+np) is true from Q2c so check d invariants of some examples.
# First define a function to check if two d invariants are essentially the same

def d_invariant_checker(f1,f2,tolerance):              # Takes inputs f1 and f2 our two fractions which we will compute the d-invariants of, and a tolerance of difference
    L1 = compute_d_invariants(f1[0],f1[1])
    L2 = compute_d_invariants(f2[0],f2[1])
    length = len(L1)
    truth = []
    for i in range(length):
        if abs(L1[i] - L2[i]) < tolerance:             # If difference between values in L1 and L2 is sufficiently small 
            truth.append(True)                         # Add True to the list truth
        if all(truth):
            print(f"The d-invariants of {f1} and {f2} are the same.")
            return True                                # If all the elements in truth are True then the lists are essentially the same 
        else:
            print(f"The d-invariants of {f1} and {f2} are not the same.")
            return False                           

# It will also be useful to have a function which generates two random coprime integers

def divisors(x):                 # First a function which returns the set of the divisors of an integer x 
    divs = set()
    for i in range(1,x+1):
        if x % i == 0:
            divs.add(i)
    return divs


def coprime_pair_generator(n):       # Use divisors() to generate two random coprime integers less than or equal to n
    num1 = randrange(n+1)
    num1_divs = divisors(num1)       # Choose the first number randomly and generate its set of divisors 
    done = False
    while done == False:
        num2 = randrange(n+1)
        if divisors(num2).intersection(num1_divs) == {1}:   # If num1 and num2 only have 1 in common in their sets of divisors       
            done = True                                     # This num2 works so break out of the while loop
    return (num1,num2)

# Simple check first. Let n = 2 then 7 + 2*9 = 25. Note if p,q are coprime then p,q+np are also coprime.   

d1 = (9,7)
d2 = (9,25)
 
tol = 1e-5
d_invariant_checker(d1,d2,tol)

# Now try for random inputs of p,q and n. 

random_pair = coprime_pair_generator(1000)
n = randrange(100)
modified_rp = (random_pair[0],random_pair[0] + n*random_pair[1])

d_invariant_checker(random_pair, modified_rp, tol)

# Hence we see that when S(p,q) = S(p, q+np) then the d-invariants of the two-bridge links are equal

