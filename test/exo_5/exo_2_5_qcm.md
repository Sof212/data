```latex
\begin{exercise}{
Id: 973dbb6a-07b5-45b3-a431-3d5d382f9151
Title_exo: \fr{Exercice d'I.A.}\en{AI Exercise}
Modules: Paul_Module1
Recommended_execution_time: 20
Ex_Level: Intermediate
Chap: Paul_Chapitre1_Module1
Involved_Concepts: Matrix_determinant, Change_of_basis_matrix, Matrix_inverse
Original_source:
Visibility: All
}
{
\begin{python}
from sympy import Matrix, latex

# Définition des matrices et vecteurs
A = Matrix([[1,4,4], [-1,-3,-3], [0,2,3]])
P = Matrix([[1,2,2], [-1,-1,-2], [1,1,1]])
P_inv = P.inv()

# === Calcul bonne réponse (extraite corrigé original) ===
# QCM 1: Déterminant de la matrice formée par (a, b, c)
bonne_valeur_det = P.det()

# QCM 2: Matrice de changement de base P
bonne_valeur_P = P

# QCM 3: Inverse de la matrice P
bonne_valeur_P_inv = P_inv

# === Matrices UNIQUEMENT ===
bonne_valeur_P_latex = latex(bonne_valeur_P, mat_delim='', mat_str='pmatrix')
bonne_valeur_P_inv_latex = latex(bonne_valeur_P_inv, mat_delim='', mat_str='pmatrix')

# === Propositions fausses calculées ===

# QCM 1: Déterminant
fausse_det_1 = 0  # Erreur méthodologique typique (ex: oubli d'un signe, erreur de calcul mineure)
fausse_det_2 = 1  # Variante calcul incorrecte (ex: erreur de signe ou de multiplication)
fausse_det_3 = 2  # Approximation erronée (ex: erreur de calcul grossière)

# QCM 2: Matrice P
fausse_P_1 = Matrix([[1,2,2], [1,1,2], [1,1,1]]) # Erreur de signe sur une ligne
fausse_P_2 = Matrix([[1,2,2], [-1,-1,-2], [0,0,0]]) # Erreur de recopie ou de compréhension (ligne de zéros)
fausse_P_3 = Matrix([[1,-1,1], [2,-1,1], [2,-2,1]]) # Transposée de P

# QCM 3: Inverse de P
fausse_P_inv_1 = P_inv * 2 # Erreur de facteur
fausse_P_inv_2 = P_inv + Matrix([[0,0,1],[0,0,0],[0,0,0]]) # Erreur d'un élément
fausse_P_inv_3 = P # Confusion avec la matrice originale
\end{python}

\qcm{
\fr{Soit $\beta:=(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3})$ la base canonique de $\mathbf{R}^{3}$.
Définir les vecteurs:
$\boldsymbol{a}:=\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3}$,
$\boldsymbol{b}:=2\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+e_{3}$,
$\boldsymbol{c}:=2\boldsymbol{e}_{1}-2\boldsymbol{e}_{2}+e_{3}$.

Quel est le déterminant de la matrice formée par $(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$?}
\en{Let $\beta:=(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3})$ be the standard basis of $\mathbf{R}^{3}$.
Define the vectors:
$\boldsymbol{a}:=\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+\boldsymbol{e}_{3}$,
$\boldsymbol{b}:=2\boldsymbol{e}_{1}-\boldsymbol{e}_{2}+e_{3}$,
$\boldsymbol{c}:=2\boldsymbol{e}_{1}-2\boldsymbol{e}_{2}+e_{3}$.

What is the determinant of the matrix formed by $(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$?}
}
{
\right{$\bonne_valeur_det$}
\wrong{$fausse_det_1$}
\wrong{$fausse_det_2$}
\wrong{$fausse_det_3$}
\wronger
\righter
}
{
\fr{Le calcul du déterminant permet de vérifier si les vecteurs sont linéairement indépendants.}
\en{The determinant calculation shows the vectors are linearly independent.}
}
{
\fr{La matrice formée par les vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ en colonnes est :
$$ P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix} $$
Le déterminant de cette matrice est calculé comme suit :
$$ \det(P) = 1 \cdot ((-1)(1) - (-2)(1)) - 2 \cdot ((-1)(1) - (-2)(1)) + 2 \cdot ((-1)(1) - (-1)(1)) $$
$$ = 1 \cdot (-1 + 2) - 2 \cdot (-1 + 2) + 2 \cdot (-1 + 1) $$
$$ = 1 \cdot (1) - 2 \cdot (1) + 2 \cdot (0) $$
$$ = 1 - 2 + 0 = -1 $$
Ainsi, le déterminant est $\boxed{-1}$.}
\en{The matrix formed by the vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ as columns is:
$$ P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix} $$
The determinant of this matrix is calculated as follows:
$$ \det(P) = 1 \cdot ((-1)(1) - (-2)(1)) - 2 \cdot ((-1)(1) - (-2)(1)) + 2 \cdot ((-1)(1) - (-1)(1)) $$
$$ = 1 \cdot (-1 + 2) - 2 \cdot (-1 + 2) + 2 \cdot (-1 + 1) $$
$$ = 1 \cdot (1) - 2 \cdot (1) + 2 \cdot (0) $$
$$ = 1 - 2 + 0 = -1 $$
Thus, the determinant is $\boxed{-1}$.}
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\qcm{
\fr{Pour les mêmes vecteurs, quelle est la matrice de changement de base $P$ de $\beta$ à $\beta'=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$?}
\en{For the same vectors, what is the change of basis matrix $P$ from $\beta$ to $\beta'=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$?}
}
{
\right{$\bonne_valeur_P_latex$}
\wrong{$fausse_P_1$}
\wrong{$fausse_P_2$}
\wrong{$fausse_P_3$}
\wronger
\righter
}
{
\fr{La matrice $P$ est formée en écrivant les vecteurs de la nouvelle base en colonnes.}
\en{$P$ is formed by writing the new basis vectors as columns.}
}
{
\fr{La matrice de changement de base $P$ de la base canonique $\beta$ à la base $\beta'=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ est obtenue en plaçant les coordonnées des vecteurs $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ en colonnes.
$$ \boldsymbol{a} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad \boldsymbol{b} = \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}, \quad \boldsymbol{c} = \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix} $$
Donc, la matrice $P$ est :
$$ P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix} $$}
\en{The change of basis matrix $P$ from the standard basis $\beta$ to the basis $\beta'=(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c})$ is obtained by placing the coordinates of vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ as columns.
$$ \boldsymbol{a} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad \boldsymbol{b} = \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}, \quad \boldsymbol{c} = \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix} $$
Thus, the matrix $P$ is:
$$ P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix} $$}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{
\fr{Quelle est l'inverse de la matrice de changement de base $P$?}
\en{What is the inverse of the change of basis matrix $P$?}
}
{
\right{$\bonne_valeur_P_inv_latex$}
\wrong{$fausse_P_inv_1$}
\wrong{$fausse_P_inv_2$}
\wrong{$fausse_P_inv_3$}
\wronger
\righter
}
{
\fr{La matrice inverse peut être calculée en utilisant des méthodes standards.}
\en{The inverse matrix can be computed using standard methods.}
}
{
\fr{Pour calculer l'inverse de la matrice $P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}$, on peut utiliser la formule $P^{-1} = \frac{1}{\det(P)} \text{adj}(P)$, où $\text{adj}(P)$ est la matrice adjointe de $P$.
Nous avons déjà calculé $\det(P) = -1$.
Calculons la matrice des cofacteurs $C$:
$$ C = \begin{pmatrix}
+(-1+2) & -(-1+2) & +(-1+1) \\
-(2-2) & +(1-2) & -(1-2) \\
+(-4+2) & -(-2+2) & +(-1+2)
\end{pmatrix} = \begin{pmatrix}
1 & -1 & 0 \\
0 & -1 & 1 \\
-2 & 0 & 1
\end{pmatrix} $$
La matrice adjointe est la transposée de la matrice des cofacteurs :
$$ \text{adj}(P) = C^T = \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix} $$
Enfin, l'inverse est :
$$ P^{-1} = \frac{1}{-1} \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix} = \begin{pmatrix}
-1 & 0 & 2 \\
1 & 1 & 0 \\
0 & -1 & -1
\end{pmatrix} $$}
\en{To calculate the inverse of the matrix $P = \begin{pmatrix}
1 & 2 & 2 \\
-1 & -1 & -2 \\
1 & 1 & 1
\end{pmatrix}$, we can use the formula $P^{-1} = \frac{1}{\det(P)} \text{adj}(P)$, where $\text{adj}(P)$ is the adjugate matrix of $P$.
We have already calculated $\det(P) = -1$.
Let's calculate the cofactor matrix $C$:
$$ C = \begin{pmatrix}
+(-1+2) & -(-1+2) & +(-1+1) \\
-(2-2) & +(1-2) & -(1-2) \\
+(-4+2) & -(-2+2) & +(-1+2)
\end{pmatrix} = \begin{pmatrix}
1 & -1 & 0 \\
0 & -1 & 1 \\
-2 & 0 & 1
\end{pmatrix} $$
The adjugate matrix is the transpose of the cofactor matrix:
$$ \text{adj}(P) = C^T = \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix} $$
Finally, the inverse is:
$$ P^{-1} = \frac{1}{-1} \begin{pmatrix}
1 & 0 & -2 \\
-1 & -1 & 0 \\
0 & 1 & 1
\end{pmatrix} = \begin{pmatrix}
-1 & 0 & 2 \\
1 & 1 & 0 \\
0 & -1 & -1
\end{pmatrix} $$}
}
{
logic: 20
abstraction: 30
reasoning: 20
calculation: 30
}
}
\end{exercise}
```