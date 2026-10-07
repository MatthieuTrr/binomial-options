# Pricing d'options

## Description
Ce dépôt vise à pricer différents types d'options (européennes, américaines, à barrières) par différentes méthodes (arbre binomial, Black-Scholes).

## Installation
```bash
pip install -e .
pytest
```

## Travaux faits
- [x] Pricing d'un call/put européen par arbre binomial

- [x] Pricing d'un call/put européen par Black-Scholes (solution analytique)

- [x] Validation du pricing par arbre binomial, par comparaison avec Black-Scholes

## A faire
- [ ] Pricing par résolution de l'EDP de Black Scholes (différences finies, schéma explicite)

- [ ] Pricing par résolution de l'EDP de Black Scholes (schéma implicite)

- [ ] Pricing par arbre binomial des options américaines

- [ ] Pricing par arbre binomial des options à barrières

## Tests effectués
- Parité put/call
- Prix d'options positifs
- Comparaison des prix obtenus par Black-Scholes et arbre binomial
