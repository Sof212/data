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
from sympy import *

# === Calcul bonne réponse (extraite corrigé original) ===
# Question 1: Déterminant de la matrice formée par a, b, c
mat_abc = Matrix([[1, 2, 2], [-1, -1, -2], [1, 1, 1]])
bonne_valeur_q1 = mat_abc.det()
bonne_valeur_q1_latex = latex(bonne_valeur_q1)

# Question 2: Matrice P et P_inv
P_q2 = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_q2_latex = latex(P_q2, mat_delim='', mat_str='pmatrix')
P_inv_q2 = P_q2.inv()
P_inv_q2_latex = latex(P_inv_q2, mat_delim='', mat_str='pmatrix')

# === Propositions fausses calculées pour Q1 ===
fausse_1_q1 = 0 # Erreur méthodologique typique (déterminant nul)
fausse_2_q1 = 1 # Variante calcul incorrecte
fausse_3_q1 = 2 # Approximation erronée
fausse_4_q1 = -2 # Autre erreur de calcul

# === Propositions fausses calculées pour Q2 ===
# P correct, P_inv identité (erreur conceptuelle)
fausse_1_P_q2_latex = P_q2_latex
fausse_1_P_inv_q2_latex = latex(eye(3), mat_delim='', mat_str='pmatrix')

# P avec erreur, P_inv correct (erreur de calcul)
fausse_2_P_q2 = Matrix([[1,2,2], [-1,-1,-1], [1,1,1]]) # Erreur dans la 2ème colonne
fausse_2_P_q2_latex = latex(fausse_2_P_q2, mat_delim='', mat_str='pmatrix')
fausse_2_P_inv_q2_latex = P_inv_q2_latex

# P correct, P_inv avec erreur (erreur de calcul)
fausse_3_P_q2_latex = P_q2_latex
fausse_3_P_inv_q2 = Matrix([[1,0,0], [0,1,0], [0,0,1]]) # Autre erreur
fausse_3_P_inv_q2_latex = latex(fausse_3_P_inv_q2, mat_delim='', mat_str='pmatrix')

# P et P_inv avec erreurs (erreurs multiples)
fausse_4_P_q2 = Matrix([[1,2,1], [-1,-1,-2], [1,1,1]])
fausse_4_P_q2_latex = latex(fausse_4_P_q2, mat_delim='', mat_str='pmatrix')
fausse_4_P_inv_q2 = Matrix([[1,1,0], [0,1,1], [1,0,1]])
fausse_4_P_inv_q2_latex = latex(fausse_4_P_inv_q2, mat_delim='', mat_str='pmatrix')

\end{python}

Let $\beta:=\left(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ be the standard basis of $\mathbf{R}^{3}$.
 Let $u$ be the endomorphism of $\mathbf{R}^{3}$, the matrix of which, in the standard basis is:

\begin{equation*}
A
:=
\begin{pmatrix}
1 & 4 & 4 \\
-1 & -3 & -3 \\
0 & 2 & 3
\end{pmatrix}
\end{equation*}

Define the following three vectors of $\mathbf{R}^{3}$:
 $\boldsymbol{a}:=\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3},
\boldsymbol{b}:=2 \boldsymbol{e}_{1}-\boldsymbol{e}_{2}+e_{3}$,
and
$\boldsymbol{c}:=2 \boldsymbol{e}_{1}-2 \boldsymbol{e}_{2}+e_{3}$

\qcm{Show that $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ is a basis of $\mathbf{R}^{3}$.}
{
\right{The determinant of the matrix formed by $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is $\sympy{bonne_valeur_q1} \neq 0$.}
\wrong{The determinant of the matrix formed by $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is $\sympy{fausse_1_q1}$.}
\wrong{The determinant of the matrix formed by $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is $\sympy{fausse_2_q1}$.}
\wrong{The determinant of the matrix formed by $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is $\sympy{fausse_3_q1}$.}
\wrong{The determinant of the matrix formed by $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is $\sympy{fausse_4_q1}$.}
}
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
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcm{Determine the change of basis matrix, denoted $P$, from basis $\beta$ to
 basis $\beta^{\prime}$. Compute $P^{-1}$.}
{
\right{$P = \begin{pmatrix} 1 & 2 & 2 \\ -1 & -1 & -2 \\ 1 & 1 & 1 \end{pmatrix}$ and $P^{-1} = \sympy{P_inv_q2_latex}$}
\wrong{$P = \sympy{fausse_1_P_q2_latex}$ and $P^{-1} = \sympy{fausse_1_P_inv_q2_latex}$}
\wrong{$P = \sympy{fausse_2_P_q2_latex}$ and $P^{-1} = \sympy{fausse_2_P_inv_q2_latex}$}
\wrong{$P = \sympy{fausse_3_P_q2_latex}$ and $P^{-1} = \sympy{fausse_3_P_inv_q2_latex}$}
\wrong{$P = \sympy{fausse_4_P_q2_latex}$ and $P^{-1} = \sympy{fausse_4_P_inv_q2_latex}$}
}
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

To compute $P^{-1}$, we can use the formula for the inverse of a $3 \times 3$ matrix or Gaussian elimination.
Using SymPy, we find:
\begin{equation*}
P^{-1} = \sympy{P_inv_q2_latex}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}
}
\end{exercise}
```