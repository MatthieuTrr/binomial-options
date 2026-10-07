import numpy as np
#cd OneDrive/Documents/PolytechNS/MAM5/Projets Persos Finance/binomial-options/src/binomial
def payoff(S,K):
    return np.maximum(S-K,0)

def CRR_param(sig,r,dt):
    """
    sig: volatilité, r: taux sans risque, dt: pas de temps
    """
    u=np.exp(sig*np.sqrt(dt))
    d=1/u
    p=(np.exp(r*dt)-d)/(u-d)
    # vérification de l'absence d'arbitrage
    if not (d < np.exp(r*dt) < u):
        raise ValueError("Arbitrage detected: d < exp(r*dt) < u condition not satisfied.")
    return u,d,p

def CRR_Tree(u,d,p,T,S0,K):
    # vérification de l'absence d'arbitrage
    if not (d < np.exp(r*dt) < u):
        return
    n=int(round(T/dt))
    stock_tree=np.zeros((n+1,n+1))
    stock_tree[0,0]=S0
    for i in range (0,n+1):
        for j in range (0,n+1):
            stock_tree[i,j]=S0*u**(j-i)*d**i

    opt_tree=np.zeros((n+1,n+1))
    opt_tree[:,n]=payoff(stock_tree[:,n],K)
    for i in range(0,n):
        for j in range(0,n-i):
            opt_tree[j,n-i-1]=np.exp(-r*dt)*(p*opt_tree[j,n-i]+(1-p)*opt_tree[j+1,n-i])
    return opt_tree[0,0]

sig=0.2
r=0.05
dt=1/12
T=1
S0=100
K=100
print(CRR_Tree(sig,r,dt,T,S0,K))