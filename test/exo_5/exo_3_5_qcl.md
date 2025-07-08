```latex
\begin{exercise}{
Id: 973dbb6a-07b5-45b3-a431-3d5d382f9151
Title_exo: Exercice d'I.A. % Nom de l'exercice
Modules: Paul_Module1 % NameID des modules
Recommended_execution_time: 20 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Intermediate % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Paul_Chapitre1_Module1 % NameID des chapitres
Involved_Concepts:  % ID ou NameID des notions 
Original_source:  % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
% Comment: % Commentaire de l'exercice (optionnel)
}
{
\begin{python}
import sympy
from sympy import *

A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
A_latex = latex(A, mat_delim='(', mat_str='pmatrix')

P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_latex = latex(P, mat_delim='(', mat_str='pmatrix')

P_inv = P.inv()
P_inv_latex = latex(P_inv, mat_delim='(', mat_str='pmatrix')

R = P.inv()*A*P
R_latex = latex(R, mat_delim='(', mat_str='pmatrix')

R_2 = R**2
R_2_latex = latex(R_2, mat_delim='(', mat_str='pmatrix')

R_4 = R**4
R_4_latex = latex(R_4, mat_delim='(', mat_str='pmatrix')

# Pour la question sur le déterminant de la base beta'
det_beta_prime = P.det()

# Pour la question sur la matrice de passage P
P_val = P

# Pour la question sur l'inverse de la matrice de passage P
P_inv_val = P_inv

\end{python}

Let $\beta:=\left(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ be the standard basis of $\mathbf{R}^{3}$.
 Let $u$ be the endomorphism of $\mathbf{R}^{3}$, the matrix of which, in the standard basis is:

\begin{equation*}
A
:=
\py{A_latex}
\end{equation*}

Define the following three vectors of $\mathbf{R}^{3}$:
 $\boldsymbol{a}:=\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3},
\boldsymbol{b}:=2 \boldsymbol{e}_{1}-\boldsymbol{e}_{2}+e_{3}$,
and
$\boldsymbol{c}:=2 \boldsymbol{e}_{1}-2 \boldsymbol{e}_{2}+e_{3}$

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
P_det = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]]).det()
bonne_valeur = P_det
\end{python}
Calculez le déterminant de la matrice formée par les vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ dans la base standard $\beta$.
}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice: Vous pouvez écrire une indication ci-dessous.
Pour montrer que $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ est une base de $\mathbf{R}^{3}$, calculez le déterminant de la matrice dont les colonnes sont les coordonnées des vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ dans la base standard.
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
Le déterminant est \py{det_beta_prime}.
}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Les coordonnées des vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ dans la base standard $\beta$ sont :
$\boldsymbol{a} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$,
$\boldsymbol{b} = \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}$,
$\boldsymbol{c} = \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix}$.

La matrice formée par ces vecteurs est :
$P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}$

Le déterminant de cette matrice est :
$\operatorname{det}(P) = \begin{vmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{vmatrix}$

Pour calculer le déterminant, nous pouvons utiliser la règle de Sarrus ou le développement par cofacteurs.
En développant par rapport à la première ligne :
$1 \times \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} - 2 \times \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} + 2 \times \begin{vmatrix} -1 & -1 \\ 1 & 1 \end{vmatrix}$
$= 1 \times ((-1)(1) - (-2)(1)) - 2 \times ((-1)(1) - (-2)(1)) + 2 \times ((-1)(1) - (-1)(1))$
$= 1 \times (-1 + 2) - 2 \times (-1 + 2) + 2 \times (-1 + 1)$
$= 1 \times (1) - 2 \times (1) + 2 \times (0)$
$= 1 - 2 + 0 = -1$.

Le déterminant est $-1$. Puisque le déterminant est non nul ($-1 \neq 0$), les vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ forment une base de $\mathbf{R}^{3}$.
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
P_matrix = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
bonne_valeur = P_matrix
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}
Donnez la matrice de passage $P$ de la base $\beta$ à la base $\beta^{\prime}$.
}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur_latex}"],["0"]]
}
{ % Indice: Vous pouvez écrire une indication ci-dessous.
La matrice de passage $P$ a pour colonnes les coordonnées des vecteurs de la nouvelle base $\beta'$ exprimés dans l'ancienne base $\beta$.
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La matrice de passage $P$ est $\py{P_latex}$.
}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
La matrice de passage $P$ de la base $\beta$ à la base $\beta^{\prime}$ est la matrice dont les colonnes sont les coordonnées des vecteurs de la base $\beta^{\prime}$ exprimés dans la base $\beta$.
Les vecteurs sont :
$\boldsymbol{a}:=\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3} \implies \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}_{\beta}$
$\boldsymbol{b}:=2 \boldsymbol{e}_{1}-\boldsymbol{e}_{2}+e_{3} \implies \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}_{\beta}$
$\boldsymbol{c}:=2 \boldsymbol{e}_{1}-2 \boldsymbol{e}_{2}+e_{3} \implies \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix}_{\beta}$

Donc, la matrice de passage $P$ est :
\begin{equation*}
P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
P_matrix = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_inv_matrix = P_matrix.inv()
bonne_valeur = P_inv_matrix
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}
Calculez la matrice inverse $P^{-1}$ de la matrice de passage $P$.
}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur_latex}"],["0"]]
}
{ % Indice: Vous pouvez écrire une indication ci-dessous.
Vous pouvez utiliser la formule $P^{-1} = \frac{1}{\det(P)} \operatorname{adj}(P)$, où $\operatorname{adj}(P)$ est la matrice adjointe de $P$.
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La matrice inverse $P^{-1}$ est $\py{P_inv_latex}$.
}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Nous avons la matrice de passage $P$:
$P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}$

Nous avons déjà calculé le déterminant de $P$, $\det(P) = -1$.

Maintenant, calculons la comatrice de $P$, notée $\operatorname{com}(P)$. La comatrice est la matrice des cofacteurs.
$C_{ij} = (-1)^{i+j} M_{ij}$, où $M_{ij}$ est le mineur de l'élément $a_{ij}$.

$C_{11} = (-1)^{1+1} \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} = 1 \times ((-1)(1) - (-2)(1)) = -1 + 2 = 1$
$C_{12} = (-1)^{1+2} \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} = -1 \times ((-1)(1) - (-2)(1)) = -1 \times (1) = -1$
$C_{13} = (-1)^{1+3} \begin{vmatrix} -1 & -1 \\ 1 & 1 \end{vmatrix} = 1 \times ((-1)(1) - (-1)(1)) = -1 + 1 = 0$

$C_{21} = (-1)^{2+1} \begin{vmatrix} 2 & 2 \\ 1 & 1 \end{vmatrix} = -1 \times ((2)(1) - (2)(1)) = -1 \times (0) = 0$
$C_{22} = (-1)^{2+2} \begin{vmatrix} 1 & 2 \\ 1 & 1 \end{vmatrix} = 1 \times ((1)(1) - (2)(1)) = 1 - 2 = -1$
$C_{23} = (-1)^{2+3} \begin{vmatrix} 1 & 2 \\ 1 & 1 \end{vmatrix} = -1 \times ((1)(1) - (2)(1)) = -1 \times (-1) = 1$

$C_{31} = (-1)^{3+1} \begin{vmatrix} 2 & 2 \\ -1 & -2 \end{vmatrix} = 1 \times ((2)(-2) - (2)(-1)) = -4 + 2 = -2$
$C_{32} = (-1)^{3+2} \begin{vmatrix} 1 & 2 \\ -1 & -2 \end{vmatrix} = -1 \times ((1)(-2) - (2)(-1)) = -1 \times (-2 + 2) = -1 \times (0) = 0$
$C_{33} = (-1)^{3+3} \begin{vmatrix} 1 & 2 \\ -1 & -1 \end{vmatrix} = 1 \times ((1)(-1) - (2)(-1)) = -1 + 2 = 1$

La comatrice est :
$\operatorname{com}(P) = \begin{pmatrix}
1 & -1 & 0 \\
0 & -1 & 1 \\
-2 & 0 & 1
\end{pmatrix}$

La matrice adjointe est la transposée de la comatrice :
$\operatorname{adj}(P) = (\operatorname{com}(P))^T = \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix}$

Enfin, l'inverse de $P$ est $P^{-1} = \frac{1}{\det(P)} \operatorname{adj}(P)$:
$P^{-1} = \frac{1}{-1} \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix} = \begin{pmatrix}
-1 & 0 & 2 \\
1 & 1 & 0 \\
0 & -1 & -1
\end{pmatrix}$
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

}
\end{exercise}
```