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

## Fonctionnement (100 % gratuit)
Le dossier `backlog/` contient des améliorations prêtes et testées (`NN-nom/files/` + `message.txt`).
Chaque jour à 06:17 UTC, le workflow applique la première, lance `pytest`, puis fait un commit réel
et le pousse sur `main`. Aucune API payante, aucun secret. Quand le backlog est vide, il ne fait rien.
Pour continuer : ajouter un dossier `backlog/NN-nom/`.
