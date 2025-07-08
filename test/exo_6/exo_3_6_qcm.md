```latex
\begin{exercise}{
Title_exo: \fr{Suites définies par récurrence - Identification de la fonction f}\en{Sequences defined by recurrence - Identification of the function f}
Modules: Maths % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Suites_numériques % NameID des chapitres
Involved_Concepts: Suite_récurrente, Fonction_associée % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Conversion d'un exercice QST en QCM, décliné en plusieurs questions pour chaque suite.
}
{ % Contenu de l'exercice

\fr{Les suites suivantes sont définies par des relations de récurrence $u_{n+1}=f\left(u_{n}\right)$.
Donner la fonction $f$ correspondante dans chacun des cas.}\en{The following sequences are defined by recurrence relations $u_{n+1}=f\left(u_{n}\right)$.
Give the corresponding function $f$ in each case.}

\begin{python}
from sympy import *
# Bonne réponse
bonne_valeur = "2*x - 3"
# Propositions fausses
fausse_1 = "2*x + 3"
fausse_2 = "x - 3"
fausse_3 = "3*x - 2"
\end{python}

\qcm{ \fr{Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
u _ { 0 } & { = 4 } \\
{ u _ { n + 1 } } & { = 2 u _ { n } - 3 }
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?}\en{Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
u _ { 0 } & { = 4 } \\
{ u _ { n + 1 } } & { = 2 u _ { n } - 3 }
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$ ?}
}
{
\right{$f(x) = \py{bonne_valeur}$}
\wrong{$f(x) = \py{fausse_1}$}
\wrong{$f(x) = \py{fausse_2}$}
\wrong{$f(x) = \py{fausse_3}$}
}
{ % Indice:
\fr{Identifiez la partie de l'expression de $u_{n+1}$ qui dépend de $u_n$.}\en{Identify the part of the expression for $u_{n+1}$ that depends on $u_n$.}
}
{ % Solution détaillée:
\fr{Pour les suites définies par les relations de récurrence données,
notre objectif est d'extraire la fonction $ f $ correspondante selon la forme générale
$ u_{n+1} = f(u_n) $.

Ici, la relation de récurrence étant $ u_{n+1} = 2 u_n - 3 $, on identifie aisément
la fonction $f$ qui est donnée par :
$f(x) = 2x - 3$.}\en{For sequences defined by the given recurrence relations,
our goal is to extract the corresponding function $ f $ according to the general form
$ u_{n+1} = f(u_n) $.

Here, the recurrence relation being $ u_{n+1} = 2 u_n - 3 $, we easily identify
the function $f$ which is given by:
$f(x) = 2x - 3$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# Bonne réponse
bonne_valeur = "sqrt(1 + x**2)"
# Propositions fausses
fausse_1 = "1 + x**2"
fausse_2 = "sqrt(x**2)"
fausse_3 = "sqrt(1 - x**2)"
\end{python}

\qcm{ \fr{Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
u _ { 0 } &{=} 0 \\
{u _ { n + 1 }} &{= \sqrt { 1 + u _ { n } ^ { 2 }}}
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?}\en{Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
u _ { 0 } &{=} 0 \\
{u _ { n + 1 }} &{= \sqrt { 1 + u _ { n } ^ { 2 }}}
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$ ?}
}
{
\right{$f(x) = \py{bonne_valeur}$}
\wrong{$f(x) = \py{fausse_1}$}
\wrong{$f(x) = \py{fausse_2}$}
\wrong{$f(x) = \py{fausse_3}$}
}
{ % Indice:
\fr{La fonction $f$ est l'expression qui transforme $u_n$ en $u_{n+1}$.}\en{The function $f$ is the expression that transforms $u_n$ into $u_{n+1}$.}
}
{ % Solution détaillée:
\fr{Pour cette suite, la relation de récurrence est $ u_{n+1} = \sqrt{1 + u_n^2} $.
On identifie aisément
la fonction $f$ qui est donnée par :
$
f(x) = \sqrt{1 + x^2}.
$}\en{For this sequence, the recurrence relation is $ u_{n+1} = \sqrt{1 + u_n^2} $.
We easily identify
the function $f$ which is given by:
$
f(x) = \sqrt{1 + x^2}.
$}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# Bonne réponse
bonne_valeur = "sin(x)"
# Propositions fausses
fausse_1 = "cos(x)"
fausse_2 = "tan(x)"
fausse_3 = "x"
\end{python}

\qcm{ \fr{Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
{ u _ { 0 }} &{= } 2 \\
{ u _ { n + 1 }} &{= \operatorname { s i n } ( u _ { n } ) }
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?}\en{Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
{ u _ { 0 }} &{= } 2 \\
{ u _ { n + 1 }} &{= \operatorname { s i n } ( u _ { n } ) }
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$ ?}
}
{
\right{$f(x) = \py{bonne_valeur}$}
\wrong{$f(x) = \py{fausse_1}$}
\wrong{$f(x) = \py{fausse_2}$}
\wrong{$f(x) = \py{fausse_3}$}
}
{ % Indice:
\fr{La fonction $f$ est directement donnée par l'expression de $u_{n+1}$.}\en{The function $f$ is directly given by the expression for $u_{n+1}$.}
}
{ % Solution détaillée:
\fr{Dans ce cas, la relation de récurrence est $ u_{n+1} = \sin(u_n) $.
On identifie aisément
la fonction $f$ qui est donnée par :
$
f(x) = \sin(x).
$}\en{In this case, the recurrence relation is $ u_{n+1} = \sin(u_n) $.
We easily identify
the function $f$ which is given by:
$
f(x) = \sin(x).
$}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# Bonne réponse
bonne_valeur = "(x - 1)/(x + 1)"
# Propositions fausses
fausse_1 = "(x + 1)/(x - 1)"
fausse_2 = "x - 1"
fausse_3 = "x + 1"
\end{python}

\qcm{ \fr{Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
u_{0}&{=}4 \\
u_{n+1}&=\frac{u_{n}-1}{u_{n}+1}
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?}\en{Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
u_{0}&{=}4 \\
u_{n+1}&=\frac{u_{n}-1}{u_{n}+1}
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$ ?}
}
{
\right{$f(x) = \py{bonne_valeur}$}
\wrong{$f(x) = \py{fausse_1}$}
\wrong{$f(x) = \py{fausse_2}$}
\wrong{$f(x) = \py{fausse_3}$}
}
{ % Indice:
\fr{Remplacez $u_n$ par $x$ dans l'expression de $u_{n+1}$.}\en{Replace $u_n$ with $x$ in the expression for $u_{n+1}$.}
}
{ % Solution détaillée:
\fr{Enfin, pour cette suite, la relation de récurrence est $ u_{n+1} = \frac{u_n - 1}{u_n + 1} $.
Nous pouvons identifier la fonction $ f $ comme :
$
f(x) = \frac{x - 1}{x + 1}.
$}\en{Finally, for this sequence, the recurrence relation is $ u_{n+1} = \frac{u_n - 1}{u_n + 1} $.
We can identify the function $ f $ as:
$
f(x) = \frac{x - 1}{x + 1}.
$}
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