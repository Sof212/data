```latex
\begin{exercise}{
Title_exo: \fr{Primitives de fonction rationnelle}\en{Antiderivatives of rational function}
Modules: Calculus % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Integration, Rational_Functions % NameID des chapitres
Involved_Concepts: Partial_Fraction_Decomposition, Antiderivative % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Cet exercice décompose la recherche de primitives d'une fonction rationnelle en plusieurs étapes.
}
{ % Contenu de l'exercice

Le but de l'exercice est de trouver les primitives de la fonction $f$ définie
sur ${\bfR}^{*}_{+}$ par
\begin{equation*}
f(x)
=
\frac{x^{2}+2 x+2}{x^{2}+x}.
\end{equation*}

\begin{python}
from sympy import *

# Définition des symboles
x = symbols('x')

# Fonction f(x)
f_x = (x**2 + 2*x + 2) / (x**2 + x)

# Décomposition en éléments simples: a + b/x + c/(x+1)
# On peut utiliser sympy pour la décomposition, mais l'exercice demande de trouver a, b, c
# par identification, donc on va simuler le processus.

# Étape 1: Identification des coefficients
# f(x) = (a*x*(x+1) + b*(x+1) + c*x) / (x*(x+1))
# f(x) = (a*x^2 + a*x + b*x + b + c*x) / (x^2 + x)
# f(x) = (a*x^2 + (a+b+c)*x + b) / (x^2 + x)

# En comparant avec (x^2 + 2*x + 2) / (x^2 + x):
# Coefficient de x^2: a = 1
# Terme constant: b = 2
# Coefficient de x: a + b + c = 2

# Calcul des bonnes réponses
bonne_a = 1
bonne_b = 2
bonne_c = 2 - bonne_a - bonne_b  # 2 - 1 - 2 = -1

# Génération de propositions fausses intelligentes
# Pour 'a':
fausse_a_1 = 0  # Erreur courante: oublier le terme constant
fausse_a_2 = 2  # Erreur de calcul ou d'identification

# Pour 'b':
fausse_b_1 = 1  # Erreur de calcul ou d'identification
fausse_b_2 = 0  # Erreur courante: oublier le terme constant

# Pour 'c':
fausse_c_1 = 1  # Erreur de signe
fausse_c_2 = 0  # Erreur de calcul
fausse_c_3 = 2  # Erreur de calcul
\end{python}
\qcm{ % Enoncé de la question
\fr{Déterminer le réel $a$ tel que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.}
\en{Determine the real number $a$ such that $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.}
}
{
\right{$\py{bonne_a}$}
\wrong{$\py{fausse_a_1}$}
\wrong{$\py{fausse_a_2}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{ % Solution détaillée
\fr{Nous cherchons $a, b, c$ tels que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
En réduisant au même dénominateur, on obtient:
$$a+\frac{b}{x}+\frac{c}{x+1} = \frac{ax(x+1) + b(x+1) + cx}{x(x+1)} = \frac{ax^2 + ax + bx + b + cx}{x^2+x} = \frac{ax^2 + (a+b+c)x + b}{x^2+x}$$
En comparant avec $f(x) = \frac{x^{2}+2 x+2}{x^{2}+x}$, on identifie les coefficients:
\begin{itemize}
    \item Coefficient de $x^2$: $a = 1$
    \item Terme constant: $b = 2$
    \item Coefficient de $x$: $a+b+c = 2$
\end{itemize}
De la première équation, on trouve $a=1$.}
\en{We are looking for $a, b, c$ such that $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
By reducing to a common denominator, we get:
$$a+\frac{b}{x}+\frac{c}{x+1} = \frac{ax(x+1) + b(x+1) + cx}{x(x+1)} = \frac{ax^2 + ax + bx + b + cx}{x^2+x} = \frac{ax^2 + (a+b+c)x + b}{x^2+x}$$
By comparing with $f(x) = \frac{x^{2}+2 x+2}{x^{2}+x}$, we identify the coefficients:
\begin{itemize}
    \item Coefficient of $x^2$: $a = 1$
    \item Constant term: $b = 2$
    \item Coefficient of $x$: $a+b+c = 2$
\end{itemize}
From the first equation, we find $a=1$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *

# Calcul des bonnes réponses (reprises du bloc Python principal)
bonne_a = 1
bonne_b = 2
bonne_c = -1

# Génération de propositions fausses intelligentes pour 'b'
fausse_b_1 = 1  # Erreur de calcul ou d'identification
fausse_b_2 = 0  # Erreur courante: oublier le terme constant
\end{python}
\qcm{ % Enoncé de la question
\fr{Déterminer le réel $b$ tel que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.}
\en{Determine the real number $b$ such that $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.}
}
{
\right{$\py{bonne_b}$}
\wrong{$\py{fausse_b_1}$}
\wrong{$\py{fausse_b_2}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{ % Solution détaillée
\fr{Nous cherchons $a, b, c$ tels que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
En réduisant au même dénominateur, on obtient:
$$a+\frac{b}{x}+\frac{c}{x+1} = \frac{ax^2 + (a+b+c)x + b}{x^2+x}$$
En comparant avec $f(x) = \frac{x^{2}+2 x+2}{x^{2}+x}$, on identifie les coefficients:
\begin{itemize}
    \item Coefficient de $x^2$: $a = 1$
    \item Terme constant: $b = 2$
    \item Coefficient de $x$: $a+b+c = 2$
\end{itemize}
De la deuxième équation, on trouve $b=2$.}
\en{We are looking for $a, b, c$ such that $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
By reducing to a common denominator, we get:
$$a+\frac{b}{x}+\frac{c}{x+1} = \frac{ax^2 + (a+b+c)x + b}{x^2+x}$$
By comparing with $f(x) = \frac{x^{2}+2 x+2}{x^{2}+x}$, we identify the coefficients:
\begin{itemize}
    \item Coefficient of $x^2$: $a = 1$
    \item Constant term: $b = 2$
    \item Coefficient of $x$: $a+b+c = 2$
\end{itemize}
From the second equation, we find $b=2$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *

# Calcul des bonnes réponses (reprises du bloc Python principal)
bonne_a = 1
bonne_b = 2
bonne_c = -1

# Génération de propositions fausses intelligentes pour 'c'
fausse_c_1 = 1  # Erreur de signe
fausse_c_2 = 0  # Erreur de calcul
fausse_c_3 = 2  # Erreur de calcul
\end{python}
\qcm{ % Enoncé de la question
\fr{Déterminer le réel $c$ tel que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.}
\en{Determine the real number $c$ such that $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.}
}
{
\right{$\py{bonne_c}$}
\wrong{$\py{fausse_c_1}$}
\wrong{$\py{fausse_c_2}$}
\wrong{$\py{fausse_c_3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{ % Solution détaillée
\fr{Nous cherchons $a, b, c$ tels que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
En réduisant au même dénominateur, on obtient:
$$a+\frac{b}{x}+\frac{c}{x+1} = \frac{ax^2 + (a+b+c)x + b}{x^2+x}$$
En comparant avec $f(x) = \frac{x^{2}+2 x+2}{x^{2}+x}$, on identifie les coefficients:
\begin{itemize}
    \item Coefficient de $x^2$: $a = 1$
    \item Terme constant: $b = 2$
    \item Coefficient de $x$: $a+b+c = 2$
\end{itemize}
Avec $a=1$ et $b=2$, la troisième équation devient $1+2+c=2$, ce qui donne $3+c=2$, et donc $c=-1$.
Ainsi, on a montré l'égalité suivante:
\begin{equation*}
f(x)=1+\frac{2}{x}+\frac{-1}{x+1}.
\end{equation*}}
\en{We are looking for $a, b, c$ such that $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
By reducing to a common denominator, we get:
$$a+\frac{b}{x}+\frac{c}{x+1} = \frac{ax^2 + (a+b+c)x + b}{x^2+x}$$
By comparing with $f(x) = \frac{x^{2}+2 x+2}{x^{2}+x}$, we identify the coefficients:
\begin{itemize}
    \item Coefficient of $x^2$: $a = 1$
    \item Constant term: $b = 2$
    \item Coefficient of $x$: $a+b+c = 2$
\end{itemize}
With $a=1$ and $b=2$, the third equation becomes $1+2+c=2$, which gives $3+c=2$, and thus $c=-1$.
Therefore, we have shown the following equality:
\begin{equation*}
f(x)=1+\frac{2}{x}+\frac{-1}{x+1}.
\end{equation*}}
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