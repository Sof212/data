```latex
\begin{exercise}{
Title_exo: \fr{Suite géométrique et somme partielle}\en{Geometric sequence and partial sum}
Modules: Suites_numeriques % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Suites_Series % NameID des chapitres
Involved_Concepts: Suite_geometrique, Somme_partielle, Limite % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Exercice sur les suites géométriques et les sommes partielles. % Comment: % Commentaire de l'exercice (optionnel)
}
{
\begin{python}
from sympy import *
n = symbols('n')
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_sn = 6*(1 - Rational(1,2)**(n+1))
# === Propositions fausses calculées ===
fausse_sn1 = 3*(1 - Rational(1,2)**n)  # Oubli du +1 et facteur 3 au lieu de 6
fausse_sn2 = 6*(1 + Rational(1,2)**(n+1))  # Erreur de signe
fausse_sn3 = 3*(1 - Rational(1,2)**(n+1))  # Facteur 3 au lieu de 6
\end{python}
\qcm{ \fr{Soit $(u_n)_{n \geqslant 0}$ la suite géométrique de terme initial 3 et de raison $\frac{1}{2}$. 
Soit $(s_n)_{n \geqslant 0}$ la somme partielle définie par $s_n = \sum_{k=0}^n u_k$.

Quelle est l'expression explicite de $s_n$ ?}\en{Let $(u_n)_{n \geqslant 0}$ be the geometric sequence with initial term 3 and common ratio $\frac{1}{2}$. 
Let $(s_n)_{n \geqslant 0}$ be the partial sum defined by $s_n = \sum_{k=0}^n u_k$.

What is the explicit expression for $s_n$?}
}
{
\right{$\displaystyle \py{latex(bonne_sn)}$}
\wrong{$\displaystyle \py{latex(fausse_sn1)}$}
\wrong{$\displaystyle \py{latex(fausse_sn2)}$}
\wrong{$\displaystyle \py{latex(fausse_sn3)}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{L'expression du terme général d'une suite géométrique est $u_k = u_0 \times q^k$. Ici, $u_0 = 3$ et $q = \frac{1}{2}$, donc $u_k = 3 \times \left(\frac{1}{2}\right)^k$.
La somme des $n+1$ premiers termes d'une suite géométrique est donnée par la formule $s_n = u_0 \frac{1-q^{n+1}}{1-q}$.
En substituant les valeurs, on obtient :
$s_n = 3 \times \frac{1-\left(\frac{1}{2}\right)^{n+1}}{1-\frac{1}{2}} = 3 \times \frac{1-\frac{1}{2^{n+1}}}{\frac{1}{2}} = 3 \times 2 \times \left(1-\frac{1}{2^{n+1}}\right) = 6\left(1-\frac{1}{2^{n+1}}\right)$.
Ainsi, l'expression explicite de $s_n$ est $\boxed{6\left(1-\frac{1}{2^{n+1}}\right)}$.}\en{The explicit form of a geometric sequence is $u_k = u_0 \times q^k$. Here, $u_0 = 3$ and $q = \frac{1}{2}$, so $u_k = 3 \times \left(\frac{1}{2}\right)^k$.
The sum of the first $n+1$ terms of a geometric sequence is given by the formula $s_n = u_0 \frac{1-q^{n+1}}{1-q}$.
Substituting the values, we get:
$s_n = 3 \times \frac{1-\left(\frac{1}{2}\right)^{n+1}}{1-\frac{1}{2}} = 3 \times \frac{1-\frac{1}{2^{n+1}}}{\frac{1}{2}} = 3 \times 2 \times \left(1-\frac{1}{2^{n+1}}\right) = 6\left(1-\frac{1}{2^{n+1}}\right)$.
Thus, the explicit expression for $s_n$ is $\boxed{6\left(1-\frac{1}{2^{n+1}}\right)}$.}
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_lim = 6
# === Propositions fausses calculées ===
fausse_lim1 = 3  # Valeur initiale
fausse_lim2 = 0  # Limite de u_n
fausse_lim3 = S.Infinity  # Croissance de n
\end{python}
\qcm{ \fr{Quelle est la limite de la suite $(s_n)_{n \geqslant 0}$ lorsque $n$ tend vers $+\infty$ ?}\en{What is the limit of the sequence $(s_n)_{n \geqslant 0}$ as $n$ approaches $+\infty$?}
}
{
\right{$\displaystyle \py{bonne_lim}$}
\wrong{$\displaystyle \py{fausse_lim1}$}
\wrong{$\displaystyle \py{fausse_lim2}$}
\wrong{$\displaystyle \py{fausse_lim3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{Nous avons trouvé que l'expression explicite de $s_n$ est $s_n = 6\left(1-\frac{1}{2^{n+1}}\right)$.
Pour trouver la limite de $s_n$ lorsque $n \to +\infty$, nous devons évaluer la limite du terme $\frac{1}{2^{n+1}}$.
Comme la base de l'exponentielle $2$ est supérieure à $1$, $\lim_{n\to+\infty} 2^{n+1} = +\infty$.
Par conséquent, $\lim_{n\to+\infty} \frac{1}{2^{n+1}} = 0$.
En substituant cette limite dans l'expression de $s_n$ :
$\lim_{n\to+\infty} s_n = 6(1-0) = 6$.
La limite de la suite $(s_n)_{n \geqslant 0}$ est $\boxed{6}$.}\en{We found that the explicit expression for $s_n$ is $s_n = 6\left(1-\frac{1}{2^{n+1}}\right)$.
To find the limit of $s_n$ as $n \to +\infty$, we need to evaluate the limit of the term $\frac{1}{2^{n+1}}$.
Since the base of the exponential $2$ is greater than $1$, $\lim_{n\to+\infty} 2^{n+1} = +\infty$.
Therefore, $\lim_{n\to+\infty} \frac{1}{2^{n+1}} = 0$.
Substituting this limit into the expression for $s_n$:
$\lim_{n\to+\infty} s_n = 6(1-0) = 6$.
The limit of the sequence $(s_n)_{n \geqslant 0}$ is $\boxed{6}$.}
}
}
\end{exercise}
```