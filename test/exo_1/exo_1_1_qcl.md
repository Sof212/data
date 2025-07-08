```latex
\begin{exercise}{
Id: 001
Title_exo: Cadenas à code
Modules: Combinatorics
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Probability_and_Combinatorics
Involved_Concepts: Permutations, Combinations
Original_source: null
Visibility: All
}
{
Un cadenas possède un code a 3 chiffres, chacun de ces chiffres est compris entre 
$1$ et $9$. 

\qcl{
\begin{python}
from sympy import *
bonne_valeur = 9**3
\end{python}
Combien y a-t-il de codes possibles en tout?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
Il y a \py{bonne_valeur} codes possibles en tout.
}
{
Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, 
et il y a $9$ choix possibles pour chaque chiffre (puisque l'on choisit un chiffre 
entre $1$ et $9$ inclus). 
Donc, le nombre total de codes possibles est :

\begin{equation*}
9 \times 9 \times 9 = 9^3 = \py{bonne_valeur}.
\end{equation*}
Il y a donc $ \py{bonne_valeur}$ choix distincts possibles de codes à trois chiffres.
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
bonne_valeur = 9
\end{python}
Combien y a-t-il de codes possibles qui commencent et se terminent par le chiffre $2$?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
Il y a \py{bonne_valeur} codes possibles qui commencent et se terminent par le chiffre 2.
}
{
Pour résoudre ce problème, nous divisons la solution en deux parties distinctes, chacune utilisant des principes de combinatoire. 

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
1 \times 9 \times 1 = \py{bonne_valeur}.
\end{equation*}
Autrement dit, il existe $\py{bonne_valeur}$ façons distinctes de créer un code à $3$ chiffres, dont 
les premier et dernier chiffres sont un $2$.
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
bonne_valeur = 4*9*5
\end{python}
Combien y a-t-il de codes possibles commençant par un chiffre pair et finissant par un chiffre impair?
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
Il y a \py{bonne_valeur} codes possibles commençant par un chiffre pair et finissant par un chiffre impair.
}
{
Il y a $4$ chiffres pairs compris entre $1$ et $9$ (les chiffres $2, 4, 6$ et $8$) et cinq 
chiffres impairs $1, 3, 5, 7$ et $9$. Nous avons donc:
- $4$ possibilités pour le premier chiffre (pair)
- $9$ possibilités pour le deuxième chiffre (de $1$ à $9$). 
- $5$ possibilités pour le dernier chiffre (impair)

Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
4 \times 9 \times 5 = \py{bonne_valeur}.
\end{equation*}

Autrement dit, il existe $\py{bonne_valeur}$ façons distinctes de créer un code à $3$ chiffres, dont 
le premier chiffre est pair et le troisième impair.
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