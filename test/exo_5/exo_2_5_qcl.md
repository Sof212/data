```latex
\begin{exercise}{
Id: 973dbb6a-07b5-45b3-a431-3d5d382f9151
Title_exo: Exercice d'I.A. 
Modules: Paul_Module1 
Recommended_execution_time: 20 
Ex_Level: Intermediate 
Chap: Paul_Chapitre1_Module1 
Involved_Concepts:  
Original_source:  
Visibility: All 
}
{
\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
det_beta_prime = P.det()
\end{python}
Soit $\beta:=(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3})$ la base canonique de $\mathbf{R}^{3}$. 
Soit $u$ l'endomorphisme de $\mathbf{R}^{3}$ dont la matrice dans la base canonique est $A = \py{latex(A, mat_delim='(')}$.

On définit les vecteurs :
$\boldsymbol{a}:=\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3}$,
$\boldsymbol{b}:=2\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3}$,
$\boldsymbol{c}:=2\boldsymbol{e}_{1}-2\boldsymbol{e}_{2}+\boldsymbol{e}_{3}$.

Calculer le déterminant de la matrice $(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ pour vérifier que $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ est une base.
}
{
[["CL","\py{det_beta_prime}"],["0"]]
}
{
Le déterminant de la famille de vecteurs doit être non nul pour qu'elle forme une base.
}
{
Le déterminant vaut \py{det_beta_prime}.
}
{
Calcul du déterminant :

\[
\begin{vmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{vmatrix}
=
\begin{vmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
0 & 0 & -1
\end{vmatrix}
=
\begin{vmatrix}
1 & 2 \\
-1 & -1
\end{vmatrix}
\times (-1) = -1 \neq 0
\]

Ce qui prouve que $\beta'$ est bien une base.
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
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
# P_latex = latex(P, mat_delim='(', mat_str='pmatrix') # Pas nécessaire, latex() gère déjà
\end{python}
Calculer la matrice de passage $P$ de la base $\beta$ à la base $\beta^{\prime}$.
}
{
[["CL","\py{latex(P, mat_delim='(')}"],["0"]]
}
{
La matrice de passage contient en colonnes les coordonnées des vecteurs de la nouvelle base dans l'ancienne base.
}
{
La matrice de passage est \py{latex(P, mat_delim='(')}.
}
{
La matrice de passage $P$ s'obtient en écrivant en colonnes les coordonnées des vecteurs de $\beta'$ dans $\beta$ :

\[
P = 
\begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
\]

Cette matrice représente l'application identité de $(\mathbf{R}^3,\beta')$ vers $(\mathbf{R}^3,\beta)$.
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
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_inv = P.inv()
# P_inv_latex = latex(P_inv, mat_delim='(', mat_str='pmatrix') # Pas nécessaire
\end{python}
Calculer l'inverse $P^{-1}$ de la matrice de passage $P$.
}
{
[["CL","\py{latex(P_inv, mat_delim='(')}"],["0"]]
}
{
Utiliser la méthode d'inversion des matrices 3x3.
}
{
La matrice inverse est \py{latex(P_inv, mat_delim='(')}.
}
{
Calcul de l'inverse :

\[
P^{-1} = \frac{1}{\det P} \text{com}(P)^T = -\text{com}(P)^T = \py{latex(P_inv, mat_delim='(')}
\]

Où $\text{com}(P)$ est la matrice des cofacteurs de $P$.
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
A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_inv = P.inv()
R = P_inv*A*P
# R_latex = latex(R, mat_delim='(', mat_str='pmatrix') # Pas nécessaire
\end{python}
Calculer la matrice $R$ de l'endomorphisme $u$ dans la base $\beta^{\prime}$.
}
{
[["CL","\py{latex(R, mat_delim='(')}"],["0"]]
}
{
Utiliser la formule de changement de base : $R = P^{-1}AP$.
}
{
La matrice dans la nouvelle base est \py{latex(R, mat_delim='(')}.
}
{
La matrice $R$ dans la nouvelle base se calcule par :

\[
R = P^{-1}AP = \py{latex(P_inv, mat_delim='(')} \times \py{latex(A, mat_delim='(')} \times \py{latex(P, mat_delim='(')} = \py{latex(R, mat_delim='(')}
\]

Cette matrice représente le même endomorphisme mais exprimé dans la nouvelle base $\beta'$.
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
A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_inv = P.inv()
R = P_inv*A*P
R_2 = R**2
# R_2_latex = latex(R_2, mat_delim='(', mat_str='pmatrix') # Pas nécessaire
\end{python}
Calculer $R^2$ où $R$ est la matrice de $u$ dans la base $\beta^{\prime}$.
}
{
[["CL","\py{latex(R_2, mat_delim='(')}"],["0"]]
}
{
Effectuer le produit matriciel $R \times R$.
}
{
Le carré de la matrice est \py{latex(R_2, mat_delim='(')}.
}
{
Calcul de $R^2$ :

\[
R^2 = R \times R = \py{latex(R, mat_delim='(')} \times \py{latex(R, mat_delim='(')} = \py{latex(R_2, mat_delim='(')}
\]

Cette opération permet d'obtenir la matrice de $u^2$ dans la base $\beta'$.
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
A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_inv = P.inv()
R = P_inv*A*P
R_4 = R**4
# R_4_latex = latex(R_4, mat_delim='(', mat_str='pmatrix') # Pas nécessaire
\end{python}
Calculer $R^4$ où $R$ est la matrice de $u$ dans la base $\beta^{\prime}$.
}
{
[["CL","\py{latex(R_4, mat_delim='(')}"],["0"]]
}
{
Calculer d'abord $R^2$ puis élever au carré le résultat.
}
{
La puissance quatrième est \py{latex(R_4, mat_delim='(')}.
}
{
Calcul de $R^4$ :

\[
R^4 = (R^2)^2 = \py{latex(R_2, mat_delim='(')} \times \py{latex(R_2, mat_delim='(')} = \py{latex(R_4, mat_delim='(')}
\]

Cette matrice représente $u^4$ dans la base $\beta'$.
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