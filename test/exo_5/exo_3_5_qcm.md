```latex
\begin{exercise}{
Id: 973dbb6a-07b5-45b3-a431-3d5d382f9151
Title_exo: \fr{Exercice d'I.A. - Bases et Matrices de Passage}\en{AI Exercise - Bases and Change of Basis Matrices}
Modules: Paul_Module1
Recommended_execution_time: 20
Ex_Level: Intermediate
Chap: Paul_Chapitre1_Module1
Involved_Concepts: Base_vectorielle, Matrice_de_passage, Inverse_de_matrice
Original_source:
Visibility: All
}
{
Let $\beta:=\left(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ be the standard basis of $\mathbf{R}^{3}$.
Let $u$ be the endomorphism of $\mathbf{R}^{3}$, the matrix of which, in the standard basis is:

\begin{equation*}
A
:=
\begin{pmatrix} 1 & 4 & 4 \\ -1 & -3 & -3 \\ 0 & 2 & 3 \end{pmatrix}
\end{equation*}

Define the following three vectors of $\mathbf{R}^{3}$:
 $\boldsymbol{a}:=\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3},
\boldsymbol{b}:=2 \boldsymbol{e}_{1}-\boldsymbol{e}_{2}+e_{3}$,
and
$\boldsymbol{c}:=2 \boldsymbol{e}_{1}-2 \boldsymbol{e}_{2}+e_{3}$

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
bonne_valeur = P.det()
# === Propositions fausses calculées ===
fausse_1 = bonne_valeur + 1  # Erreur simple
fausse_2 = -bonne_valeur     # Erreur de signe
fausse_3 = 0                 # Cas où ce ne serait pas une base
\end{python}
\qcm{
\fr{Pour montrer que $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ est une base de $\mathbf{R}^{3}$, on peut calculer le déterminant de la matrice formée par ces vecteurs. Quelle est la valeur de ce déterminant ?}
\en{To show that $\beta^{\prime}:=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ is a basis of $\mathbf{R}^{3}$, one can compute the determinant of the matrix formed by these vectors. What is the value of this determinant?}
}
{
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
}
{ % Indice
\fr{Rappelez-vous que des vecteurs forment une base si et seulement si le déterminant de la matrice qu'ils forment est non nul.}
\en{Recall that vectors form a basis if and only if the determinant of the matrix they form is non-zero.}
}
{ % Solution détaillée
\fr{La matrice formée par les vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ est la matrice $P$ :
\begin{equation*}
P =
\begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
\end{equation*}
Le déterminant de cette matrice est calculé comme suit :
\begin{equation*}
\begin{align*}
\operatorname{det}(P) &= 1 \cdot ((-1) \cdot 1 - (-2) \cdot 1) - 2 \cdot ((-1) \cdot 1 - (-2) \cdot 1) + 2 \cdot ((-1) \cdot 1 - (-1) \cdot 1) \\
&= 1 \cdot (-1 + 2) - 2 \cdot (-1 + 2) + 2 \cdot (-1 + 1) \\
&= 1 \cdot 1 - 2 \cdot 1 + 2 \cdot 0 \\
&= 1 - 2 + 0 \\
&= -1
\end{align*}
Puisque $\operatorname{det}(P) = -1 \neq 0$, les vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ forment bien une base de $\mathbf{R}^{3}$.}
\en{The matrix formed by the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is matrix $P$:
\begin{equation*}
P =
\begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
\end{equation*}
The determinant of this matrix is calculated as follows:
\begin{equation*}
\begin{align*}
\operatorname{det}(P) &= 1 \cdot ((-1) \cdot 1 - (-2) \cdot 1) - 2 \cdot ((-1) \cdot 1 - (-2) \cdot 1) + 2 \cdot ((-1) \cdot 1 - (-1) \cdot 1) \\
&= 1 \cdot (-1 + 2) - 2 \cdot (-1 + 2) + 2 \cdot 0 \\
&= 1 - 2 + 0 \\
&= -1
\end{align*}
Since $\operatorname{det}(P) = -1 \neq 0$, the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ indeed form a basis of $\mathbf{R}^{3}$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
# === Matrices UNIQUEMENT ===
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
# === Propositions fausses calculées ===
fausse_1 = bonne_valeur.inv() # Inverse au lieu de la matrice elle-même
fausse_1_latex = latex(fausse_1, mat_delim='', mat_str='pmatrix')
fausse_2 = bonne_valeur.transpose() # Transposée
fausse_2_latex = latex(fausse_2, mat_delim='', mat_str='pmatrix')
fausse_3 = Matrix([[1,0,0],[0,1,0],[0,0,1]]) # Matrice identité
fausse_3_latex = latex(fausse_3, mat_delim='', mat_str='pmatrix')
\end{python}
\qcm{
\fr{Déterminez la matrice de changement de base, notée $P$, de la base $\beta$ à la base $\beta^{\prime}$.}
\en{Determine the change of basis matrix, denoted $P$, from basis $\beta$ to basis $\beta^{\prime}$.}
}
{
\right{$\displaystyle \mathbf{P} = \sympy{bonne_valeur_latex}$}
\wrong{$\displaystyle \mathbf{P} = \sympy{fausse_1_latex}$}
\wrong{$\displaystyle \mathbf{P} = \sympy{fausse_2_latex}$}
\wrong{$\displaystyle \mathbf{P} = \sympy{fausse_3_latex}$}
}
{ % Indice
\fr{La matrice de changement de base de $\beta$ à $\beta'$ a pour colonnes les coordonnées des vecteurs de $\beta'$ exprimés dans la base $\beta$.}
\en{The change of basis matrix from $\beta$ to $\beta'$ has as columns the coordinates of the vectors of $\beta'$ expressed in the basis $\beta$.}
}
{ % Solution détaillée
\fr{La matrice de changement de base $P$ de la base standard $\beta = (\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3})$ à la base $\beta^{\prime} = (\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ est formée en plaçant les coordonnées des vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ en colonnes.
\begin{align*}
\boldsymbol{a} &= 1\boldsymbol{e}_{1} - 1\boldsymbol{e}_{2} + 1\boldsymbol{e}_{3} \\
\boldsymbol{b} &= 2\boldsymbol{e}_{1} - 1\boldsymbol{e}_{2} + 1\boldsymbol{e}_{3} \\
\boldsymbol{c} &= 2\boldsymbol{e}_{1} - 2\boldsymbol{e}_{2} + 1\boldsymbol{e}_{3}
\end{align*}
Ainsi, la matrice $P$ est :
\begin{equation*}
P =
\begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
\end{equation*}
}
\en{The change of basis matrix $P$ from the standard basis $\beta = (\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3})$ to the basis $\beta^{\prime} = (\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ is formed by placing the coordinates of the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ as columns.
\begin{align*}
\boldsymbol{a} &= 1\boldsymbol{e}_{1} - 1\boldsymbol{e}_{2} + 1\boldsymbol{e}_{3} \\
\boldsymbol{b} &= 2\boldsymbol{e}_{1} - 1\boldsymbol{e}_{2} + 1\boldsymbol{e}_{3} \\
\boldsymbol{c} &= 2\boldsymbol{e}_{1} - 2\boldsymbol{e}_{2} + 1\boldsymbol{e}_{3}
\end{align*}
Thus, the matrix $P$ is:
\begin{equation*}
P =
\begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}
\end{equation*}
}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
bonne_valeur = P.inv()
# === Matrices UNIQUEMENT ===
bonne_valeur_latex = latex(bonne_valeur, mat_delim='', mat_str='pmatrix')
# === Propositions fausses calculées ===
fausse_1 = P # P au lieu de P_inv
fausse_1_latex = latex(fausse_1, mat_delim='', mat_str='pmatrix')
fausse_2 = P.transpose() # Transposée au lieu de l'inverse
fausse_2_latex = latex(fausse_2, mat_delim='', mat_str='pmatrix')
fausse_3 = Matrix([[1,0,0],[0,1,0],[0,0,1]]) # Matrice identité
fausse_3_latex = latex(fausse_3, mat_delim='', mat_str='pmatrix')
\end{python}
\qcm{
\fr{Calculez la matrice inverse $P^{-1}$.}
\en{Compute the inverse matrix $P^{-1}$.}
}
{
\right{$\displaystyle \mathbf{P}^{-1} = \sympy{bonne_valeur_latex}$}
\wrong{$\displaystyle \mathbf{P}^{-1} = \sympy{fausse_1_latex}$}
\wrong{$\displaystyle \mathbf{P}^{-1} = \sympy{fausse_2_latex}$}
\wrong{$\displaystyle \mathbf{P}^{-1} = \sympy{fausse_3_latex}$}
}
{ % Indice
\fr{Pour calculer l'inverse d'une matrice $M$, vous pouvez utiliser la formule $M^{-1} = \frac{1}{\operatorname{det}(M)} \operatorname{adj}(M)$, où $\operatorname{adj}(M)$ est la matrice adjointe de $M$.}
\en{To compute the inverse of a matrix $M$, you can use the formula $M^{-1} = \frac{1}{\operatorname{det}(M)} \operatorname{adj}(M)$, where $\operatorname{adj}(M)$ is the adjugate matrix of $M$.}
}
{ % Solution détaillée
\fr{Nous avons déjà calculé le déterminant de $P$ : $\operatorname{det}(P) = -1$.
Maintenant, calculons la matrice des cofacteurs de $P$:
\begin{align*}
C_{11} &= \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} = -1 - (-2) = 1 \\
C_{12} &= -\begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} = -(-1 - (-2)) = -1 \\
C_{13} &= \begin{vmatrix} -1 & -1 \\ 1 & 1 \end{vmatrix} = -1 - (-1) = 0 \\
C_{21} &= -\begin{vmatrix} 2 & 2 \\ 1 & 1 \end{vmatrix} = -(2 - 2) = 0 \\
C_{22} &= \begin{vmatrix} 1 & 2 \\ 1 & 1 \end{vmatrix} = 1 - 2 = -1 \\
C_{23} &= -\begin{vmatrix} 1 & 2 \\ 1 & 1 \end{vmatrix} = -(1 - 2) = 1 \\
C_{31} &= \begin{vmatrix} 2 & 2 \\ -1 & -2 \end{vmatrix} = -4 - (-2) = -2 \\
C_{32} &= -\begin{vmatrix} 1 & 2 \\ -1 & -2 \end{vmatrix} = -(-2 - (-2)) = 0 \\
C_{33} &= \begin{vmatrix} 1 & 2 \\ -1 & -1 \end{vmatrix} = -1 - (-2) = 1
\end{align*}
La matrice des cofacteurs est :
\begin{equation*}
C =
\begin{pmatrix}
1 & -1 & 0 \\
0 & -1 & 1 \\
-2 & 0 & 1
\end{pmatrix}
\end{equation*}
La matrice adjointe est la transposée de la matrice des cofacteurs :
\begin{equation*}
\operatorname{adj}(P) = C^T =
\begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix}
\end{equation*}
Enfin, l'inverse de $P$ est :
\begin{equation*}
P^{-1} = \frac{1}{\operatorname{det}(P)} \operatorname{adj}(P) = \frac{1}{-1}
\begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix}
=
\begin{pmatrix}
-1 & 0 & 2 \\
1 & 1 & 0 \\
0 & -1 & -1
\end{pmatrix}
\end{equation*}
}
\en{We have already calculated the determinant of $P$: $\operatorname{det}(P) = -1$.
Now, let's calculate the cofactor matrix of $P$:
\begin{align*}
C_{11} &= \begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} = -1 - (-2) = 1 \\
C_{12} &= -\begin{vmatrix} -1 & -2 \\ 1 & 1 \end{vmatrix} = -(-1 - (-2)) = -1 \\
C_{13} &= \begin{vmatrix} -1 & -1 \\ 1 & 1 \end{vmatrix} = -1 - (-1) = 0 \\
C_{21} &= -\begin{vmatrix} 2 & 2 \\ 1 & 1 \end{vmatrix} = -(2 - 2) = 0 \\
C_{22} &= \begin{vmatrix} 1 & 2 \\ 1 & 1 \end{vmatrix} = 1 - 2 = -1 \\
C_{23} &= -\begin{vmatrix} 1 & 2 \\ 1 & 1 \end{vmatrix} = -(1 - 2) = 1 \\
C_{31} &= \begin{vmatrix} 2 & 2 \\ -1 & -2 \end{vmatrix} = -4 - (-2) = -2 \\
C_{32} &= -\begin{vmatrix} 1 & 2 \\ -1 & -2 \end{vmatrix} = -(-2 - (-2)) = 0 \\
C_{33} &= \begin{vmatrix} 1 & 2 \\ -1 & -1 \end{vmatrix} = -1 - (-2) = 1
\end{align*}
The cofactor matrix is:
\begin{equation*}
C =
\begin{pmatrix}
1 & -1 & 0 \\
0 & -1 & 1 \\
-2 & 0 & 1
\end{pmatrix}
\end{equation*}
The adjugate matrix is the transpose of the cofactor matrix:
\begin{equation*}
\operatorname{adj}(P) = C^T =
\begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix}
\end{equation*}
Finally, the inverse of $P$ is:
\begin{equation*}
P^{-1} = \frac{1}{\operatorname{det}(P)} \operatorname{adj}(P) = \frac{1}{-1}
\begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix}
=
\begin{pmatrix}
-1 & 0 & 2 \\
1 & 1 & 0 \\
0 & -1 & -1
\end{pmatrix}
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
```