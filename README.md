# daily-improvements

Data science appliquée à la finance : risque, trading, portefeuille.
Une petite amélioration validée par jour (doc, test, correction, exemple), proposée par pull request.

## Projets
- `risk/var/` : Value-at-Risk (historique, paramétrique) et Expected Shortfall.
- `trading/backtest/` : backtest vectorisé d'une stratégie de croisement de moyennes mobiles.

Les données sont **simulées** (aucune donnée de marché réelle, aucun conseil financier).

## Lancer
```bash
pip install -r requirements.txt
pytest -q
```
