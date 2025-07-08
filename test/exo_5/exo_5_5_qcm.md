
\begin{exercise}{
Id: 47051ae5-7506-4f27-8792-601e017e0777
Title_exo: \fr{Exercice d'I.A.} \en{A.I Exercise} % Nom de l'exercice
Modules: module_pres % NameID des modules
Recommended_execution_time: 30 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Intermediate % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Linear_Algebra, Matrices, Endomorphisms % NameID des chapitres
Involved_Concepts: Basis, Change_of_basis, Matrix_representation, Matrix_powers % ID ou NameID des notions 
Original_source:  % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
% Comment: % Commentaire de l'exercice (optionnel)
}
{


\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
# Code Python : Ecrivez ci-dessous votre code Python

import sympy
from sympy import *

A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
A_latex = latex(A, mat_delim='(')

P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_latex = latex(P, mat_delim='(')

P_inv = P.inv()
P_invlatex = latex(P_inv, mat_delim='(')

R = P.inv()*A*P
R_latex = latex(R, mat_delim='(')

R_2 = R**2
R_2latex = latex(R_2, mat_delim='(')

R_4 = R**4
R_4latex = latex(R_4, mat_delim='(')

# Pour la question 1 (déterminant)
det_P = P.det()
det_P_wrong1 = det_P + 1 # Erreur simple
det_P_wrong2 = -det_P # Erreur de signe

# Pour la question 2 (P et P_inv)
P_wrong1 = Matrix([[1,2,2], [1,-1,-2], [1,1,1]]) # Erreur de signe
P_wrong2 = Matrix([[1,2,2], [-1,-1,-2], [0,1,1]]) # Erreur de valeur
P_inv_wrong1 = P.transpose() # Erreur conceptuelle
P_inv_wrong2 = P.inv() + Matrix([[Rational(1,10),0,0],[0,Rational(1,10),0],[0,0,Rational(1,10)]]) # Erreur de calcul
P_wrong1=latex(P_wrong1, mat_delim='(')
P_wrong2=latex(P_wrong2, mat_delim='(')
P_inv_wrong1 =latex(P_inv_wrong1, mat_delim='(')
P_inv_wrong2=latex(P_inv_wrong2, mat_delim='(')
# Pour la question 3 (Matrice R)
R_wrong1 = A # Erreur conceptuelle
R_wrong2 = P*A*P_inv # Erreur d'ordre
R_wrong3 = R + Matrix([[1,0,0],[0,1,0],[0,0,1]]) # Erreur de calcul

# Pour la question 4 (P_inv A P)
PAP_wrong1 = A # Erreur conceptuelle
PAP_wrong2 = P*A*P_inv # Erreur d'ordre
PAP_wrong3 = R + Matrix([[0,0,0],[0,0,0],[0,0,1]]) # Erreur de calcul

# Pour la question 5 (R^4)
R4_wrong1 = R_2 # Erreur de puissance
R4_wrong2 = R**3 # Erreur de puissance
R4_wrong3 = R_4 + Matrix([[1,0,0],[0,0,0],[0,0,0]]) # Erreur de calcul

# Pour la question 6 (A^4n)
I3 = eye(3)
I3_latex = latex(I3, mat_delim='(')
A4n_wrong1 = A # Erreur conceptuelle
A4n_wrong2 = R # Erreur conceptuelle
A4n_wrong3 = I3 * 2 # Erreur de valeur
A4n_wrong4 = Matrix([[1,0,0],[0,1,0],[0,0,0]]) # Erreur de calcul
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

\begin{python}
from sympy import *
# Calcul de la bonne réponse
bonne_valeur = det_P
bonne_valeur_latex = latex(bonne_valeur)
\end{python}
\qcm{
\fr{Quelle est la valeur du déterminant de la matrice formée par les vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ dans la base standard $\beta$ ?}
\en{What is the value of the determinant of the matrix formed by the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ in the standard basis $\beta$?}
}{
\right{$ \py{det_P} $}
\wrong{$ \py{det_P_wrong1} $}
\wrong{$ \py{det_P_wrong2} $}
\wrong{$ \py{det_P_wrong2 +2} $}
}
{ % Indice

}
{%% Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur
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

\begin{python}
from sympy import *
# Calcul de la bonne réponse
bonne_valeur_P = P
bonne_valeur_P_latex = latex(bonne_valeur_P, mat_delim='', mat_str='pmatrix')
bonne_valeur_P_inv = P_inv
bonne_valeur_P_inv_latex = latex(bonne_valeur_P_inv, mat_delim='', mat_str='pmatrix')
\end{python}
\qcm{
\fr{Déterminez la matrice de passage $P$ de la base $\beta$ à la base $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ }
\en{Determine the change of basis matrix $P$ from basis $\beta$ to basis $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ }
}{
\right{$P = \py{P_latex}  $}
\wrong{$P = \py{P_wrong1}  $}
\wrong{$P = \py{P_wrong2}  $}
\wrong{$P = \py{P_invlatex} $}
}
{ % Indice

}
{%% Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur
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
}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}





}
\end{exercise}



