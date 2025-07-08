```latex
\begin{exercise}{
Id: 001
Title_exo: Codes de cadenas
Modules: M1_10_Combinatorics
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Combinatorics
Involved_Concepts: Permutations_Combinations
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
Un cadenas possède un code a 3 chiffres, chacun de ces chiffres est compris entre 
$1$ et $9$. 

Combien y a-t-il de codes possibles:

\begin{python}
from sympy import *
# === Reproduction exacte du calcul du corrigé original ===
# [Variables et étapes du corrigé \qst]
bonne_valeur_q1 = 9**3
# Si matrice : bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}

\qcl{ %% [ÉNONCÉ \qst ORIGINAL INTÉGRALEMENT REPRIS - MODIFICATION MINIMALE]
Calculer le nombre total de codes possibles.
}

{[["CL","\py{bonne_valeur_q1}"],["0"]]}

{%% Indication : Considérez le nombre de choix pour chaque position du code.}

{%% Solution brève : Le nombre total de codes possibles est \py{bonne_valeur_q1}.}

{%% Solution détaillée : Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, 
et il y a $9$ choix possibles pour chaque chiffre (puisque l'on choisit un chiffre 
entre $1$ et $9$ inclus). 
Donc, le nombre total de codes possibles est :

\begin{equation*}
9 \times 9 \times 9 = 9^3 = \py{bonne_valeur_q1}.
\end{equation*}
Il y a donc $ \py{bonne_valeur_q1}$ choix distincts possibles de codes à trois chiffres.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Reproduction exacte du calcul du corrigé original ===
# [Variables et étapes du corrigé \qst]
bonne_valeur_q2 = 1 * 9 * 1
# Si matrice : bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}

\qcl{ %% [ÉNONCÉ \qst ORIGINAL INTÉGRALEMENT REPRIS - MODIFICATION MINIMALE]
Calculer le nombre de codes qui commencent et se terminent par le chiffre $2$.
}

{[["CL","\py{bonne_valeur_q2}"],["0"]]}

{%% Indication : Fixez les premier et dernier chiffres, puis déterminez les possibilités pour le chiffre du milieu.}

{%% Solution brève : Le nombre de codes qui commencent et se terminent par le chiffre $2$ est \py{bonne_valeur_q2}.}

{%% Solution détaillée : Pour résoudre ce problème, nous divisons la solution en deux parties distinctes, chacune utilisant des principes de combinatoire. 

Un code de $3$ chiffres est de la forme $XYZ$, où chaque
 lettre représente un chiffre compris entre $1$ et $9$. Pour ce cas particulier:  

- $X$ est le premier chiffre et doit être $2$.
- $Y$ est le deuxième chiffre et peut être n'importe quel chiffre entre $1$ et $9$.
- $Z$ est le troisième chiffre et doit également être $2$.

Donc, nous avons :  
- $1$ possibilité pour le premier chiffre
- $9$ possibilités pour le deuxième chiffre (de $1$ à $9$). 
- $1$ possibilité pour le dernier chiffre

Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
1 \times 9 \times 1 = \py{bonne_valeur_q2}.
\end{equation*}
Autrement dit, il existe $\py{bonne_valeur_q2}$ façons distinctes de créer un code à $3$ chiffres, dont 
les premier et dernier chiffres sont un $2$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Reproduction exacte du calcul du corrigé original ===
# [Variables et étapes du corrigé \qst]
bonne_valeur_q3 = 4 * 9 * 5
# Si matrice : bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}

\qcl{ %% [ÉNONCÉ \qst ORIGINAL INTÉGRALEMENT REPRIS - MODIFICATION MINIMALE]
Calculer le nombre de codes commençant par un chiffre pair et finissant par un chiffre impair.
}

{[["CL","\py{bonne_valeur_q3}"],["0"]]}

{%% Indication : Identifiez les chiffres pairs et impairs disponibles entre 1 et 9, puis calculez les combinaisons.}

{%% Solution brève : Le nombre de codes commençant par un chiffre pair et finissant par un chiffre impair est \py{bonne_valeur_q3}.}

{%% Solution détaillée : 
Il y a $4$ chiffres pairs compris entre $1$ et $9$ (les chiffres $2, 4, 6$ et $8$) et cinq 
chiffres impairs $1, 3, 5, 7$ et $9$. Nous avons donc:
- $4$ possibilités pour le premier chiffre (chiffre pair)
- $9$ possibilités pour le deuxième chiffre (de $1$ à $9$). 
- $5$ possibilités pour le dernier chiffre (chiffre impair)

Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
4 \times 9 \times 5 = \py{bonne_valeur_q3}.
\end{equation*}

Autrement dit, il existe $\py{bonne_valeur_q3}$ façons distinctes de créer un code à $3$ chiffres, dont 
le premier chiffre est pair et le troisième impair.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

}
\end{exercise}
```