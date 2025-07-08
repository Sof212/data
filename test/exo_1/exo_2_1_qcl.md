```latex
\begin{exercise}{
Title_exo: Combinaisons de codes à 3 chiffres
Modules: Combinatoire
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Dénombrement
Involved_Concepts: Principe multiplicatif, Permutations
Original_source: Exercice original
}
{
Un cadenas possède un code à 3 chiffres, chacun de ces chiffres est compris entre $1$ et $9$.

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = 9**3
\end{python}
Combien y a-t-il de codes possibles en tout ?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Utilisez le principe multiplicatif en considérant les choix indépendants pour chaque chiffre.
}
{
Le nombre total de codes possibles est \py{bonne_valeur}.
}
{
Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, 
et il y a $9$ choix possibles pour chaque chiffre (puisque l'on choisit un chiffre 
entre $1$ et $9$ inclus). 
Donc, le nombre total de codes possibles est :
\begin{equation*}
9 \times 9 \times 9 = 9^3 = \py{bonne_valeur}.
\end{equation*}
Il y a donc $\py{bonne_valeur}$ choix distincts possibles de codes à trois chiffres.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = 9
\end{python}
Combien y a-t-il de codes qui commencent et se terminent par le chiffre $2$ ?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Le premier et dernier chiffre sont fixés, seul le deuxième chiffre varie.
}
{
Le nombre de codes commençant et finissant par 2 est \py{bonne_valeur}.
}
{
Un code de $3$ chiffres est de la forme $XYZ$. Pour ce cas particulier:  
- $X = 2$ (1 possibilité)
- $Y$ quelconque entre 1 et 9 (9 possibilités)
- $Z = 2$ (1 possibilité)

Le nombre total est donc :
\begin{equation*}
1 \times 9 \times 1 = 9.
\end{equation*}
Il existe $9$ codes à 3 chiffres commençant et finissant par 2.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = 4*9*5
\end{python}
Combien y a-t-il de codes commençant par un chiffre pair et finissant par un chiffre impair ?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Décomposez le problème en considérant les chiffres pairs pour la première position et impairs pour la dernière.
}
{
Le nombre de codes est \py{bonne_valeur}.
}
{
Les chiffres pairs entre 1 et 9 sont $\{2,4,6,8\}$ (4 possibilités) et les chiffres impairs sont $\{1,3,5,7,9\}$ (5 possibilités). Le deuxième chiffre peut être quelconque (9 possibilités).

Le nombre total de codes est donc :
\begin{equation*}
4 \times 9 \times 5 = \py{bonne_valeur}.
\end{equation*}
Il existe $\py{bonne_valeur}$ codes satisfaisant cette condition.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = 9
\end{python}
Combien y a-t-il de codes dont tous les chiffres sont identiques ?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Un seul choix possible pour chaque chiffre une fois le premier choisi.
}
{
Le nombre de codes avec chiffres identiques est 9.
}
{
Il suffit de choisir le premier chiffre (9 possibilités), les deux autres doivent être identiques :
\begin{equation*}
9 \times 1 \times 1 = 9.
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = 3 * (9 * 8)
\end{python}
Combien y a-t-il de codes avec exactement deux chiffres identiques ?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Considérez les positions des chiffres identiques et les choix possibles.
}
{
Le nombre de codes avec exactement deux chiffres identiques est \py{bonne_valeur}.
}
{
Trois cas possibles pour la position du chiffre différent :
1. Premier et deuxième identiques, troisième différent : $9 \times 1 \times 8 = 72$
2. Premier et troisième identiques, deuxième différent : $9 \times 8 \times 1 = 72$
3. Deuxième et troisième identiques, premier différent : $8 \times 9 \times 1 = 72$ (le premier chiffre doit être différent du chiffre répété)

Total : $72 \times 3 = 216$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = 9 * 8 * 7
\end{python}
Combien y a-t-il de codes avec tous les chiffres différents ?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Utilisez le principe des arrangements sans répétition.
}
{
Le nombre de codes avec chiffres tous différents est \py{bonne_valeur}.
}
{
\begin{equation*}
9 \times 8 \times 7 = 504.
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}
}
\end{exercise}
```