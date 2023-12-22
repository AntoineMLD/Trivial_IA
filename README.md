# Projet TrivIA Pursuit

# Contexte
Réalisé dans le cadre de la formation **Ecole Microsoft by SIMPLON**

## Contributeurs:
- Antoine MLD
- Farid Igouti
- Grégory Martin

# Install 🛠️
Réalisé avec Python 3.10, vraisemblablement compatible à partir de Python 3.7

- `git clone https://github.com/AntoineMLD/Trivial_IA.git`
- `pip install -r requirements.txt`

# Description
## Objectif
Il s'agissait de réaliser un jeu de quizz sur différents thèmes abordés au cours de la formation, à savoir:

- Le marché du travail
- Le langage SQL
- L'actualité IA
- La maîtrise du Shell UNIX
- Le versioning avec Git/GitHub
- Le langage Python

## Choix d'implémentation
Nous avons décidé d'implémenter un clone du Trivial Pursuit, en respectant le plateau original et en restant aussi fidèle que possible aux règles officielles.

La reproduction du plateau et du déroulement du jeu nous a amené à choisir d'utiliser la bibliothèque externe `pygame`

### Plateau
Le plateau est circulaire, avec 3 diamètres régulièrement espacés.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/p4FT3P9/Board.png" alt="Board" border="0"></a>

### Catégories
- 🟫 : **Spé** (Marché du travail) 
- 🟦 : **SQL** 
- 🟧 : **IA** (Actualité IA)
- 🟨 : **Shell** (Maîtrise du Shell UNIX)
- 🟪 : **Git** (Versioning avec Git/GitHub)
- 🟩 : **Python**

### Quelques éléments de règles
#### Principes généraux
Le jeu officiel peut compter jusque 6 joueurs et fonctionne en tour par tour, avec des déplacements sur plateau déterminés par un lancer de dé, au début du tour de chaque joueur.

Chaque joueur démarre la partie sur la case centrale.

#### Types de cases
Il y a 3 types de cases:
- les cases **relance**, grises. Si un joueur arrive sur ce type de case, il doit relancer le dé. (*ce lancer se fait au clic*)
- les cases **camembert**, aux extrémités des diamètres. Si un joueur arrive sur ce type de case, il doit répondre à une question du thème correspondant à la couleur de la case. S'il répond correctement, il obtient un "camembert" (point) de la catégorie (voir *condition de victoire*, plus loin) et a le droit de rejouer un tour supplémentaire ensuite. Sinon, il passe la main au joueur suivant.
- les cases **question**, qui sont toutes les autres cases. Si un joueur arrive sur ce type de case, il doit répondre à une question du thème correspondant à la couleur de la case. S'il répond correctement, il a le droit de rejouer un tour supplémentaire.

#### Condition de victoire
La partie s'achève quand un joueur remporte un camembert pour chaque thème. Il est alors le vainqueur de la partie.

# Implémentation
- Les joueurs saisissent leur nom dans la zone de texte dévolue à cet effet, dans le panneau de droite, **quand il n'y a plus de nom à saisir, appuyez à nouveau sur ENTREE**. (Le nombre maximal de joueurs est 6)
- L'ordre des joueurs est alors défini aléatoirement. Il apparait dans la zone d'affichage des scores (en bas à droite). Cette dernière est rafraichie à chaque tour, **le joueur actif apparaissant systématiquement en haut**.
- Pour **lancer le dé**, un bouton dé apparaît dans le panneau de droite, en haut. Un clic sur celui-ci déclenche le lancer ainsi que l'affichage du résultat obtenu sur ce bouton.
- En fonction de ce résultat, les positions de déplacement possibles pour le joueur apparaissent sur le board à gauche, sous forme d'anneau rouge autour des cases atteignables.

**lien du canva de présentation :**
https://www.canva.com/design/DAF3mLYLNy4/816Tqt4utMTnmeozwoY51w/edit?utm_content=DAF3mLYLNy4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
# Releases
## Version 1.0
Le jeu est encore en mode monojoueur
