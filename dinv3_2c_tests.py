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

# 

