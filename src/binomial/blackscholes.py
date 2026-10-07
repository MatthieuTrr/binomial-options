# Pricing d'une option européenne de type call ou put avec le modèle de Black-Scholes
import numpy as np
from scipy.stats import norm

def black_scholes_price(sig,r,T,S0,K,option_type='call'):
    """
    sig: volatilité, r: taux sans risque, T: maturité, S0: prix initial du sous-jacent
    K: strike, option_type: 'call' ou 'put'
    """
    d1=np.log(S0/K)+(r+0.5*sig**2)*T
    d1=d1/(sig*np.sqrt(T))
    d2=d1-sig*np.sqrt(T)
    if option_type=='call':
        price=S0*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
    elif option_type=='put':
        price=K*np.exp(-r*T)*norm.cdf(-d2)-S0*norm.cdf(-d1)
    return price