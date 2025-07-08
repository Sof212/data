








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

\end{python}

<!-- \begin{equation*}
\begin{align*}
&A = \py{A_latex}&
&P = \py{P_latex}&\\
&R = \py{R_latex}&
&R^2 = \py{R_2latex}&
&R^4 = \py{R_4latex}&
\end{align*}
\end{equation*}
 -->

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

\qst{Show that $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ is a basis of $\mathbf{R}^{3}$.}
{ % Indice

}
{ % Solution détaillée
The following equality:

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
\end{vmatrix*}
\\
&=-1 \neq 0.
\end{align*}
\end{equation*}

clearly shows that $\boldsymbol{\beta'}$ is a basis of $\mathbf{R}^{3}$.
}
{ % Répartition des poids (Total = 100)

}

\qst{Determine the change of basis matrix, denoted $P$, from basis $\beta$ to
 basis $\beta^{\prime}$. Compute $P^{-1}$.}
{ % Indice

}
{ % Solution détaillée
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
{ % Répartition des poids (Total = 100)

}

}
\end{exercise}









