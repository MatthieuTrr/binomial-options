import numpy as np
from binomial.tree import payoff
from binomial.blackscholes import black_scholes_coeffs

def h_function(z,n):
    # inversion de Peizer-Pratt
    return 0.5+np.sign(z)*0.5*np.sqrt(1-np.exp(-(z/(n+1/3+0.1/(n+1)))**2*(n+1/6)))

def tree_params(d1, d2, n, T, r):
    #calcul du up et down pour l'arbre binomial de Leisen Reimer
    p = h_function(d2, n)
    pprime = h_function(d1, n)
    h = T / n
    u = np.exp(r*h) * pprime / p
    d = (np.exp(r*h) - p*u) / (1 - p)
    return u, d, p


def leisen_reimer_pricing(sig,r,T,S0,K,option_type='call',n=101):
    # price l'option par arbre binomial de Leisen-Reimer
    if n%2==0:
        raise ValueError("n doit être impair pour que la méthode de Leisen Reimer converge.")
    d1,d2 = black_scholes_coeffs(r,T,S0,K,sig)
    u,d,p = tree_params(d1,d2,n,T,r)
    j = np.arange(n+1)
    C = payoff(S0*u**(n-j)*d**j, K, option_type)
    disc = np.exp(-r*T/n)
    for _ in range(n):
        C = disc*(p*C[:-1] + (1-p)*C[1:])
    return C[0]