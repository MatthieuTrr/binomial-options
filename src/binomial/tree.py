import numpy as np
def payoff(S,K,option_type='call'):
    """
    S: prix du sous-jacent
    K: strike
    """
    # calcul du payoff d'une option européenne de type call ou put à l'échéance
    if option_type == 'call':
        return np.maximum(S-K,0)
    elif option_type == 'put':
        return np.maximum(K-S,0)

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

def eu_opt_pricing(sig,r,T,dt,S0,K,option_type='call'):
    """
    S0: prix initial du sous-jacent
    """
    # Estimation du prix d'une opt° euro. par arbre binomial
    u,d,p=CRR_param(sig,r,dt)
    n=int(round(T/dt))
    j=np.arange(n+1)
    price=payoff(S0*u**j*d**(n-j),K,option_type)
    for i in range(n-1,-1,-1):
        price= np.exp(-r*dt)*(p*price[1:i+2]+(1-p)*price[0:i+1])
    return price[0]
