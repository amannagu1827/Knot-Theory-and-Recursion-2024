from fractions import Fraction
from sympy import divisors

def d_invariant(p, q, i):
    if p <= 0 or q <= 0:
        raise ValueError("p and q must be positive integers.")

    # Base case: when p = 1
    if p == 1:
        return 0 if i < q else None

    # Reduce to the case where p > q
    if p < q:
        return d_invariant(q, p, i)

    # Reduce i modulo p+q
    i %= p + q

    # Recursive definition
    if q == 0:
        return 0
    elif i < q:
        return 0
    elif i < p + q - 1:
        numerator = (2 * i + 1 - p - q) ** 2 - p * q
        return Fraction(numerator, 4 * p * q) - d_invariant(q, p, i)
    else:
        return -d_invariant(q, p, i)


def d_invariants(p, q):
    if p <= 0 or q <= 0:
        raise ValueError("p and q must be positive integers.")

    def d_invariant_recursive(p, q, i):
        # Base case: when p = 1
        if p == 1:
            return [0] if i < q else []

        # Reduce to the case where p > q
        if p < q:
            return d_invariant_recursive(q, p, i)

        # Reduce i modulo p+q
        i %= p + q

        # Recursive definition
        if q == 0:
            return [0]
        elif i < q:
            return [0]
        elif i < p + q - 1:
            numerator = (2 * i + 1 - p - q) ** 2 - p * q
            return [Fraction(numerator, 4 * p * q)] + d_invariant_recursive(q, p, i)
        else:
            return [-d for d in d_invariant_recursive(q, p, i)]

    d_values = [d_invariant_recursive(p, q, i) for i in range(p + q)]
    return d_values

def d_invariant(p, q):
    if p <= 0 or q <= 0:
        raise ValueError("p and q must be positive integers.")

    # Reduce to the case where p > q
    if p < q:
        p, q = q, p

    # Compute the d invariant
    d_values = []
    for i in range(p + q):
        if q == 0 or i < q:
            d_values.append(0)
        elif i < p + q - 1:
            numerator = (2 * i + 1 - p - q) ** 2 - p * q
            d_values.append(Fraction(numerator, 4 * p * q))
        else:
            d_values.append(-d_values[i - q])

    return d_values

def generate_2_bridge_links(p_limit):
    links = set()
    for p in range(2, p_limit):
        divs = divisors(p)
        for q in divs:
            if q >= 2 and q < p // 2 + 1:
                links.add((p, q))
    return links

def check_d_invariants(p_limit):
    inequivalent_links = generate_2_bridge_links(p_limit)
    inequivalent_d_invariants = {}
    for p, q in inequivalent_links:
        d_values = d_invariant(p, q)
        if tuple(d_values) not in inequivalent_d_invariants:
            inequivalent_d_invariants[tuple(d_values)] = [(p, q)]
        else:
            inequivalent_d_invariants[tuple(d_values)].append((p, q))
    return inequivalent_d_invariants

def d_invariant(p, q):
    if p <= 0 or q <= 0:
        raise ValueError("p and q must be positive integers.")

    # Reduce to the case where p > q
    if p < q:
        p, q = q, p

    # Compute the d invariant
    d_values = []
    for i in range(p + q):
        if q == 0 or i < q:
            d_values.append(0)
        elif i < p + q - 1:
            numerator = (2 * i + 1 - p - q) ** 2 - p * q
            d_values.append(Fraction(numerator, 4 * p * q))
        else:
            d_values.append(-d_values[i - q])

    return d_values

def generate_2_bridge_links(p_limit):
    links = set()
    for p in range(2, p_limit):
        divs = divisors(p)
        for q in divs:
            if q >= 2 and q < p // 2 + 1:
                links.add((p, q))
    return links

def find_slice_knots(p_limit):
    slice_knots = []
    for m in range(1, (p_limit // 2) + 1):
        p = m ** 2
        if p % 2 == 1:
            zero_count = 0
            for q in range(2, p // 2 + 1):
                d_values = d_invariant(p, q)
                if d_values.count(0) == m:
                    zero_count += 1
            if zero_count == m:
                slice_knots.append(p)
    return slice_knots

