import numpy as np
import pytest
from binomial.tree import CRR_Tree, CRR_param


PARAMS= [
    (100, 100, 0.2, 0.0861),
    (100, 130, 0.25486, 0.0315),
    (100, 90, 0.17310, 0.05321)
]
@pytest.mark.parametrize("S0,K,sig,r",PARAMS)
def test_put_call_parity(S0, K, sig, r):
    T = 1
    dt = 1/12
    u, d, p = CRR_param(sig, r, dt)
    call_price = CRR_Tree(u, d, p,r, T, dt, S0, K, option_type='call')
    put_price = CRR_Tree(u, d, p,r, T, dt, S0, K, option_type='put')
    # Vérification de la parité put-call
    assert call_price - put_price == pytest.approx(S0 - K * np.exp(-r * T), abs=1e-8)

@pytest.mark.parametrize("S0,K,sig,r",PARAMS)
def test_positive_prices(S0, K, sig, r):
    T = 1
    dt = 1/12
    u, d, p = CRR_param(sig, r, dt)
    call_price = CRR_Tree(u, d, p,r, T, dt, S0, K, option_type='call')
    put_price = CRR_Tree(u, d, p,r, T, dt, S0, K, option_type='put')
    assert call_price >= 0
    assert put_price >= 0