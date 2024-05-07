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
   for i in range(p+q):
       d_invariants.append(calculate_d_invariant(p, q, i))
   return d_invariants

from math import gcd
from random import sample

# Function to print each term in a d-invariant to 3 decimal places
def dinvprint(array):
    output = "["
    for item in array:
        output += "{0:.3f}, ".format(item)
    return output[0:-2] + "]"

# Dictionary to memoize computed d-invariants
dinv_memo = {}
# Variable to count the number of function calls
calls = 0

# Function to compute d-invariants for all possible (p, q) pairs and memoize them
def precompute_d_invariants(p_max):
    global dinv_memo
    for p in range(2, p_max):
        for q in range(2, p):
            if gcd(p, q) == 1:
                dinv_memo[(p, q)] = compute_d_invariants(p, q)

# Function to compute d-invariant with memoization
def compute_dinv_memo(p, q):
    global calls
    calls += 1
    return dinv_memo[(p, q)]

# Function to distinguish between 2-bridge links for a given range of p values
def distinguish_2_bridge_links(p_max):
    # Precompute d-invariants for all possible (p, q) pairs
    precompute_d_invariants(p_max)
    
    # Initialize variables to store log of tests and successes
    log = []
    tests = 0
    successes = 0
    
    # Iterate over all possible values of p
    for p in range(2, p_max):
        # Iterate over all possible values of q_1 that satisfy the co-primality condition
        for q_1 in range(2, p):
            if gcd(p, q_1) == 1:
                # Iterate over all possible values of q_2 that satisfy the co-primality condition with q_1
                for q_2 in range(2, q_1):
                    if gcd(p, q_2) == 1:
                        tests += 1
                        # Compute the d-invariants for both pairs using memoization
                        d_1 = compute_dinv_memo(p, q_1)
                        d_2 = compute_dinv_memo(p, q_2)
                        # If d-invariants are different, record a success
                        if d_1 != d_2:
                            successes += 1
                            log.append("S({},{}) and S({},{}) are different knots, and therefore have differing d-invariants.\n".format(p, q_1, p, q_2) +
                                "S({},{}) has d-invariant {}. .\nS({},{}) has d-invariant {}.".format(p, q_1, dinvprint(d_1), p, q_2, dinvprint(d_2)))
                    else:
                        # Break the loop if gcd(p, q_2) != 1
                        break
            else:
                # Break the loop if gcd(p, q_1) != 1
                break
    
    # Print summary of tests and successes
    print("Number of function calls:", calls)
    print("We tested {} pairs of unequivalent knots and found that {} of them had different d-invariants, a {:.1f}% success rate".format(tests, successes, (successes / tests) * 100))
    # Print a random sample of 5 log entries
    for entry in sample(log, min(5, len(log))):
        print(entry)

# Call the function to check for p < 1000
distinguish_2_bridge_links(200)
