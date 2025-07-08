
\begin{exercise}{
Id: 47051ae5-7506-4f27-8792-601e017e0777
Title_exo: \fr{Exercice d'I.A.} \en{A.I Exercise} % Nom de l'exercice
Modules: module_pres % NameID des modules
Recommended_execution_time: 30 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Intermediate % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap:  % NameID des chapitres
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
A_latex = latex(A, mat_delim='', mat_str='pmatrix')

P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_latex = latex(P, mat_delim='', mat_str='pmatrix')

P_inv = P.inv()
P_inv_latex = latex(P_inv, mat_delim='', mat_str='pmatrix')

R = P.inv()*A*P
R_latex = latex(R, mat_delim='', mat_str='pmatrix')

R_2 = R**2
R_2_latex = latex(R_2, mat_delim='', mat_str='pmatrix')

R_4 = R**4
R_4_latex = latex(R_4, mat_delim='', mat_str='pmatrix')

det_beta_prime = P.det()
det_beta_prime_latex = latex(det_beta_prime)

I3 = eye(3)
I3_latex = latex(I3, mat_delim='', mat_str='pmatrix')

A4 = P * R_4 * P_inv
A4_latex = latex(A4, mat_delim='', mat_str='pmatrix')

# Pour la question 3, on calcule les images des vecteurs de la nouvelle base par u
u_a = A * Matrix([1, -1, 1])
u_b = A * Matrix([2, -1, 1])
u_c = A * Matrix([2, -2, 1])

# On exprime ces images dans la base beta'
# u(a) = 1*a + 0*b + 0*c
# u(b) = 0*a + 0*b + 1*c
# u(c) = 0*a - 1*b + 0*c
# Donc R = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
# C'est déjà calculé par R = P.inv()*A*P, on vérifie juste la cohérence.
# R_expected = Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
# assert R == R_expected, "La matrice R calculée ne correspond pas à la description dans la solution détaillée."

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

\qcl{\fr{Quelle est la valeur du déterminant de la matrice formée par les vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ dans la base standard $\beta$ ?}
\en{What is the value of the determinant of the matrix formed by the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ in the standard basis $\beta$?}
}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{det_beta_prime}"],["0"]]
}
{ % Indice
Pour montrer que $\beta'$ est une base, vous pouvez calculer le déterminant de la matrice dont les colonnes sont les coordonnées des vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ dans la base standard.
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\operatorname{det}(\boldsymbol{\beta'})= \py{det_beta_prime}.$
}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.


\begin{equation*}
\begin{align*}
\operatorname{det}(\boldsymbol{\beta'})
=
\operatorname{det}(\boldsymbol a, \boldsymbol b, \boldsymbol c)
&=
\begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
=
\begin{vmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
0 & 0 & -1
\end{vmatrix}
=
\begin{vmatrix*}
1 & 2 \\
-1 & -1
\end{vmatrix*}\\
&=-1 

\end{align*}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\fr{Déterminez la matrice de passage $P$ de la base $\beta$ à la base $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ }
\en{Determine the change of basis matrix $P$ from basis $\beta$ to basis $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$

}
}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{P_latex}"],["0"]]
}
{ % Indice
La matrice de passage $P$ a pour colonnes les coordonnées des 
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
 $P =$ $\py{P_latex}$.
}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Since $P$ is nothing but the change of basis matrix from $\bs \beta$ to $\bs \beta'$,
we have:




\begin{equation*}
\begin{align*}


&P 
= 
\left[\operatorname{Id}_{{\bfR}^{3}}\right]_{\bs\beta^{\prime}}^{\bs\beta}
=
\begin{array}{l}
& \\
&\left(\hspace{-3ex}
\begin{array}{ll}
 &  \\
 &  \\
 &  \\
 \end{array}
\right.&

 \end{array}&


\hspace{-7ex}\begin{array}{ll}
 \textcolor{black}{\bs a}&   \textcolor{black}{ \bs b} &   \textcolor{black}{\bs c}  &\\
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1 
\end{array}


&\begin{array}{l}
& \\
&\left.
\begin{array}{ll}
 &  \\
 &  \\
 &  \\
 \end{array}
\hspace{-16ex}\right)&

 \end{array}&


&\hspace{-10ex}\begin{array}{ll}
 & \\
\textcolor{black}{ \boldsymbol{e_1}}& \\
\textcolor{black}{ \boldsymbol{e_2}}& \\
\textcolor{black}{ \boldsymbol{e_3}}& 
\end{array}&
\end{align*}
\end{equation*}
\end{align*}

}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}





}
\end{exercise}