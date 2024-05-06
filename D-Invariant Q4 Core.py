Does it completely distinguish between 2-bridge links. In other words, is it true that whenever S(p,q1) and S(p,q2) are inequivalent links they have differing d invariants? Check this for a collection of example, such as when p < 100. If possible, try to refine your code to work for all p < 200 or p < 1000.

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
    _____________________________________________
Code from previous parts 
New code for this question BELOW vvvvvvv


# Function to distinguish between 2-bridge links for a given range of p values
def distinguish_2_bridge_links(p_max):
    # Iterate over all possible values of p
    for p in range(2, p_max):
        # Iterate over all possible values of q_1 and q_2 that satisfy the co-primality condition
        for q_1 in range(1, p):
            for q_2 in range(1, p):
                # Compute d invariants for both pairs
                d_1 = compute_d_invariants(p, q_1)
                d_2 = compute_d_invariants(p, q_2)
                # If d invariants are different, print a message and return
                if d_1 != d_2:
                    print("S(p,q_1) and S(p,q_2) are inequivalent, and hence have differing d-invariants.")
                    return
    # If no differing d invariants found, print a message
    print("Inequivalent 2-bridge links can have the same d-invariant.")


