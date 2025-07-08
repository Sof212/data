```latex
\begin{exercise}{
Title_exo: \fr{Décomposition en éléments simples}\en{Partial fraction decomposition}
Modules: Calculus % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Primitives_and_integrals % NameID des chapitres
Involved_Concepts: Partial_fraction_decomposition, Primitives % ID ou NameID des notions
Original_source: Exercice original % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Cet exercice est un QCM sur la décomposition en éléments simples. % Comment: % Commentaire de l'exercice (optionnel)
}
{
\begin{python}
from sympy import *

# === Calcul bonne réponse (extraite corrigé original) ===
a_correct = 1
b_correct = 2
c_correct = -1

# === Propositions fausses calculées ===
# Erreur méthodologique typique: inversion de signe
a_fausse_1 = a_correct
b_fausse_1 = -b_correct
c_fausse_1 = c_correct

# Variante calcul incorrecte: permutation de valeurs
a_fausse_2 = b_correct
b_fausse_2 = a_correct
c_fausse_2 = c_correct

# Approximation erronée: autre permutation et signe
a_fausse_3 = -a_correct
b_fausse_3 = b_correct
c_fausse_3 = -c_correct

# Autre erreur de calcul typique
a_fausse_4 = a_correct
b_fausse_4 = a_correct
c_fausse_4 = -b_correct

# Autre erreur de calcul typique
a_fausse_5 = b_correct
b_fausse_5 = -a_correct
c_fausse_5 = a_correct
\end{python}
\qcm{ \fr{
Déterminer trois réels \( a, b \) et \( c \) tels que \( f(x) = a + \frac{b}{x} + \frac{c}{x + 1} \), où \( f(x) = \frac{x^{2} + 2x + 2}{x^{2} + x} \).
}\en{
Determine three real numbers \( a, b \) and \( c \) such that \( f(x) = a + \frac{b}{x} + \frac{c}{x + 1} \), where \( f(x) = \frac{x^{2} + 2x + 2}{x^{2} + x} \).
}
}
{
\right{\fr{\( a = \sympy{a_correct}, b = \sympy{b_correct}, c = \sympy{c_correct} \)}\en{\( a = \sympy{a_correct}, b = \sympy{b_correct}, c = \sympy{c_correct} \)}}
\wrong{\fr{\( a = \sympy{a_fausse_1}, b = \sympy{b_fausse_1}, c = \sympy{c_fausse_1} \)}\en{\( a = \sympy{a_fausse_1}, b = \sympy{b_fausse_1}, c = \sympy{c_fausse_1} \)}}
\wrong{\fr{\( a = \sympy{a_fausse_2}, b = \sympy{b_fausse_2}, c = \sympy{c_fausse_2} \)}\en{\( a = \sympy{a_fausse_2}, b = \sympy{b_fausse_2}, c = \sympy{c_fausse_2} \)}}
\wrong{\fr{\( a = \sympy{a_fausse_3}, b = \sympy{b_fausse_3}, c = \sympy{c_fausse_3} \)}\en{\( a = \sympy{a_fausse_3}, b = \sympy{b_fausse_3}, c = \sympy{c_fausse_3} \)}}
\wrong{\fr{\( a = \sympy{a_fausse_4}, b = \sympy{b_fausse_4}, c = \sympy{c_fausse_4} \)}\en{\( a = \sympy{a_fausse_4}, b = \sympy{b_fausse_4}, c = \sympy{c_fausse_4} \)}}
\wrong{\fr{\( a = \sympy{a_fausse_5}, b = \sympy{b_fausse_5}, c = \sympy{c_fausse_5} \)}\en{\( a = \sympy{a_fausse_5}, b = \sympy{b_fausse_5}, c = \sympy{c_fausse_5} \)}}
}
{
\fr{Indice: Effectuez une décomposition en éléments simples de \( f(x) \).}\en{Hint: Perform a partial fraction decomposition of \( f(x) \).}
}
{
\fr{Solution détaillée:
Nous avons \( f(x) = \frac{x^{2} + 2x + 2}{x^{2} + x} \).
Puisque le degré du numérateur est égal au degré du dénominateur, nous commençons par une division euclidienne ou une manipulation algébrique.
On peut écrire \( x^2 + 2x + 2 = (x^2 + x) + x + 2 \).
Donc, \( f(x) = \frac{(x^2 + x) + x + 2}{x^2 + x} = 1 + \frac{x + 2}{x^2 + x} = 1 + \frac{x + 2}{x(x + 1)} \).

Maintenant, nous cherchons \( b \) et \( c \) tels que \( \frac{x + 2}{x(x + 1)} = \frac{b}{x} + \frac{c}{x + 1} \).
En réduisant au même dénominateur, on obtient \( \frac{b(x + 1) + cx}{x(x + 1)} = \frac{(b + c)x + b}{x(x + 1)} \).
Par identification des coefficients avec \( x + 2 \), nous avons le système:
\( \begin{cases} b + c = 1 \\ b = 2 \end{cases} \)
De la deuxième équation, \( b = 2 \). En substituant dans la première, \( 2 + c = 1 \), ce qui donne \( c = -1 \).
Ainsi, \( f(x) = 1 + \frac{2}{x} + \frac{-1}{x + 1} \).
Par conséquent, \( (a, b, c) = (\sympy{a_correct}, \sympy{b_correct}, \sympy{c_correct}) \).
}\en{Solution detailed:
We have \( f(x) = \frac{x^{2} + 2x + 2}{x^{2} + x} \).
Since the degree of the numerator is equal to the degree of the denominator, we start with Euclidean division or algebraic manipulation.
We can write \( x^2 + 2x + 2 = (x^2 + x) + x + 2 \).
So, \( f(x) = \frac{(x^2 + x) + x + 2}{x^2 + x} = 1 + \frac{x + 2}{x^2 + x} = 1 + \frac{x + 2}{x(x + 1)} \).

Now, we look for \( b \) and \( c \) such that \( \frac{x + 2}{x(x + 1)} = \frac{b}{x} + \frac{c}{x + 1} \).
By reducing to the same denominator, we get \( \frac{b(x + 1) + cx}{x(x + 1)} = \frac{(b + c)x + b}{x(x + 1)} \).
By identifying the coefficients with \( x + 2 \), we have the system:
\( \begin{cases} b + c = 1 \\ b = 2 \end{cases} \)
From the second equation, \( b = 2 \). Substituting into the first, \( 2 + c = 1 \), which gives \( c = -1 \).
Thus, \( f(x) = 1 + \frac{2}{x} + \frac{-1}{x + 1} \).
Therefore, \( (a, b, c) = (\sympy{a_correct}, \sympy{b_correct}, \sympy{c_correct}) \).
}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}
}
```