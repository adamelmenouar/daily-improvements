# daily-improvements

[![ci](https://github.com/adamelmenouar/daily-improvements/actions/workflows/ci.yml/badge.svg)](https://github.com/adamelmenouar/daily-improvements/actions/workflows/ci.yml)

Boîte à outils de **data science appliquée à la finance** : mesure du risque, stratégies de trading,
construction de portefeuille et pricing. Le dépôt grandit d'**une petite amélioration par jour**,
toujours accompagnée de tests.

> Toutes les données sont **simulées**. Ce code est pédagogique : ce n'est pas un conseil financier.

## Organisation

| Dossier | Contenu |
|---|---|
| `risk/` | Value-at-Risk, Expected Shortfall, drawdown, volatilité, tests de validation de modèles de risque |
| `trading/` | Backtests vectorisés, indicateurs techniques, ratios de performance, coûts de transaction |
| `portfolio/` | Optimisation et allocation de portefeuille, rééquilibrage |
| `pricing/` | Valorisation d'options et d'obligations |
| `tests/` | Un fichier de tests par module (`pytest`) |
| `backlog/` | Améliorations en attente, appliquées une par jour par le robot |

Les dossiers `portfolio/` et `pricing/` apparaissent au fil des jours, au moment où leur première
amélioration est appliquée. L'historique Git (`git log`) montre ce qui a été ajouté et quand.

## Démarrage rapide

```bash
git clone https://github.com/adamelmenouar/daily-improvements
cd daily-improvements
pip install -r requirements.txt
pytest -q
```

Testé avec Python 3.12 ; dépendances : `numpy`, `pandas`, `scipy`, `pytest`.

## Exemples

**Mesurer le risque d'une série de rendements**

```python
import numpy as np
from risk.var.var import historical_var, parametric_var, expected_shortfall

rendements = np.random.default_rng(0).normal(0.0004, 0.01, 1000)

print("VaR 95 % historique :", round(historical_var(rendements), 4))
print("VaR 95 % paramétrique:", round(parametric_var(rendements), 4))
print("Expected Shortfall  :", round(expected_shortfall(rendements), 4))
```

**Backtester un croisement de moyennes mobiles**

```python
from trading.backtest.ma_crossover import simulate_prices, backtest, sharpe

prix = simulate_prices(n=1000, seed=1)
print("Sharpe :", round(sharpe(backtest(prix, fast=20, slow=50)), 2))
```

Le signal est décalé d'un jour : la stratégie n'utilise jamais d'information du futur.

## Comment ça s'automatise 

1. Chaque amélioration prête est un dossier `backlog/NN-nom/` avec `message.txt` (message de commit)
   et `files/` (fichiers à ajouter, code + tests).
2. Chaque jour à 06:17 UTC, le workflow `daily-improvement` prend la première, lance `pytest`,
   puis fait un vrai commit et le pousse sur `main`.
3. Si les tests échouent, rien n'est commité. Si le backlog est vide, rien non plus : jamais de commit vide.
4. Aucune API payante, aucun secret : GitHub Actions est gratuit sur un dépôt public.

Pour ajouter une amélioration : créer `backlog/NN-nom/` avec un numéro supérieur au dernier,
vérifier que `pytest` passe une fois les fichiers copiés à la racine, puis pousser.

## Conventions

- Un module = un fichier + un fichier de tests dans `tests/`.
- Docstrings en français, noms de fonctions en anglais.
- Pas de données de marché réelles, pas de clés d'API.
- Signaux de trading toujours décalés d'un jour (pas de biais d'anticipation).
