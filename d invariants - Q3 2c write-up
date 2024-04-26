We have shown in Chapter 2, Section 2.2 that if $n \in \mathbb{Z}$ and $p,q$ are co-prime then $S(p,q) = S(p,q+np)$. Now we will illustrate that
when this is the case, the two 2-bridge links generate the same $d$-invariants.

First let us define a function which checks if the $d$-invariants of two fractions f1 and f2 are the same.

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

We also define a function which generates two random co-prime integers so that we can check the $d$-invariants of random inputs. For this, we first define 
divisors() which returns a set of the divisors of an integer $x$ and then define the full function.

def divisors(x):                 
    divs = set()                    # Use a set so that we can use python's intersection() function later
    for i in range(1,x+1):
        if x % i == 0:
            divs.add(i)
    return divs

from random inport randrange
def coprime_pair_generator(n):       
    num1 = randrange(n+1)
    num1_divs = divisors(num1)       # Choose the first number randomly and generate its set of divisors 
    done = False
    while done == False:
        num2 = randrange(n+1)
        if divisors(num2).intersection(num1_divs) == {1}:   # If num1 and num2 only have 1 in common in their sets of divisors       
            done = True                                     # This num2 works so break out of the while loop
    return (num1,num2)

First let us check a simple example we've seen earlier, $S(9,7)$ and pick $n=2$ so check this against $S(9,25)$.
Note that if $p,q$ are co-prime and $n\in\mathbb{Z}$ then $p,q+np$ are co-prime so we don't need to worry about new inputs.

d1 = (9,7)
d2 = (9,25)
tol = 1e-5
d_invariant_checker(d1,d2,tol)

So this works. Now let us check with random inputs for $n$ and $p,q$ using coprime_pair_generator().

random_pair = coprime_pair_generator(1000)
n = randrange(100)
modified_rp = (random_pair[0],random_pair[0] + n*random_pair[1])

Now repeatedly run this next line to convince yourself that the $d$-invariants are the same.

d_invariant_checker(random_pair, modified_rp, tol)


