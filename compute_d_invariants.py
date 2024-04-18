from compute_d_invariant import calculate_d_invariant


def compute_d_invariants(p, q):
    d_invariants = []
    for i in range(p):
        d_invariants.append(calculate_d_invariant(p, q, i))
    return d_invariants
