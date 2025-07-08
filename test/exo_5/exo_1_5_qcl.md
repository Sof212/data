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

# Code Python : Ecrivez ci-dessous votre code Python

import sympy
from sympy import *

A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
A_latex = latex(A, mat_delim='(', mat_str='pmatrix')

P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_latex = latex(P, mat_delim='(', mat_str='pmatrix')

P_inv = P.inv()
P_invlatex = latex(P_inv, mat_delim='(', mat_str='pmatrix')

R = P.inv()*A*P
R_latex = latex(R, mat_delim='(', mat_str='pmatrix')

R_2 = R**2
R_2latex = latex(R_2, mat_delim='(', mat_str='pmatrix')

R_4 = R**4
R_4latex = latex(R_4, mat_delim='(', mat_str='pmatrix')

det_abc = P.det()

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
bonne_valeur = det_abc
\end{python}
Calculate the determinant of the matrix formed by the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$.}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice
The determinant of a matrix formed by vectors can be calculated using the formula for the determinant of a 3x3 matrix.
}
{ % Solution brève fournie à l'utilisateur
The determinant is $\py{bonne_valeur}$.
}
{ % Solution détaillée
The determinant of the matrix formed by the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is calculated as follows:

\[
\begin{vmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{vmatrix}
= 1 \cdot \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} - 2 \cdot \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} + 2 \cdot \begin{vmatrix} -1 & -1 \\ 1 & 1 \end{vmatrix}
= 1 \cdot ( (-1)(1) - (-2)(1) ) - 2 \cdot ( (-1)(1) - (-2)(1) ) + 2 \cdot ( (-1)(1) - (-1)(1) )
= 1 \cdot ( -1 + 2 ) - 2 \cdot ( -1 + 2 ) + 2 \cdot ( -1 + 1 )
= 1 \cdot 1 - 2 \cdot 1 + 2 \cdot 0
= 1 - 2 + 0
= -1
\]
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
bonne_valeur = P
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}
Find the change of basis matrix $P$ from the standard basis $\beta$ to the basis $\beta' = (\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$.}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur_latex}"],["0"]]
}
{ % Indice
The change of basis matrix $P$ is formed by writing the vectors of $\beta'$ as columns in the standard basis.
}
{ % Solution brève fournie à l'utilisateur
The change of basis matrix $P$ is $\py{P_latex}$.
}
{ % Solution détaillée
The change of basis matrix $P$ from the standard basis $\beta$ to the basis $\beta' = (\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ is formed by writing the vectors of $\beta'$ as columns in the standard basis. Therefore, we have:

\[
P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
\]
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
bonne_valeur = P_inv
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}
Calculate the inverse of the matrix $P$.}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur_latex}"],["0"]]
}
{ % Indice
The inverse of a matrix can be calculated using the formula for the inverse of a 3x3 matrix.
}
{ % Solution brève fournie à l'utilisateur
The inverse of $P$ is $\py{P_invlatex}$.
}
{ % Solution détaillée
The inverse of the matrix $P$ is calculated as follows:

\[
P^{-1} = \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix}
\]
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
bonne_valeur = R
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}
Calculate the matrix $R = P^{-1}AP$.}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur_latex}"],["0"]]
}
{ % Indice
The matrix $R$ is calculated by multiplying $P^{-1}$, $A$, and $P$ in that order.
}
{ % Solution brève fournie à l'utilisateur
The matrix $R$ is $\py{R_latex}$.
}
{ % Solution détaillée
The matrix $R$ is calculated as follows:

\[
R = P^{-1}AP = \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix} \begin{pmatrix}
1 & 4 & 4 \\
-1 & -3 & -3 \\
0 & 2 & 3
\end{pmatrix} \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
\]
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
bonne_valeur = R_2
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}
Calculate $R^2$.}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur_latex}"],["0"]]
}
{ % Indice
$R^2$ is calculated by multiplying $R$ by itself.
}
{ % Solution brève fournie à l'utilisateur
$R^2$ is $\py{R_2latex}$.
}
{ % Solution détaillée
$R^2$ is calculated as follows:

\[
R^2 = R \times R = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix} \times \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
\]
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
bonne_valeur = R_4
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
\end{python}
Calculate $R^4$.}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur_latex}"],["0"]]
}
{ % Indice
$R^4$ is calculated by multiplying $R^2$ by itself.
}
{ % Solution brève fournie à l'utilisateur
$R^4$ is $\py{R_4latex}$.
}
{ % Solution détaillée
$R^4$ is calculated as follows:

\[
R^4 = R^2 \times R^2 = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix} \times \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
\]
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