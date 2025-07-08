```latex
\begin{exercise}{
Id: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d
Title_exo: Fonctions de récurrence
Modules: M1_1_Suites
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Suites_Numeriques
Involved_Concepts: Suites_recurrentes
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
Les suites suivantes sont définies par des relations de récurrence $u_{n+1}=f\left(u_{n}\right)$. 
Donner la fonction $f$ correspondante dans chacun des cas.

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = 2*x - 3
bonne_valeur_latex = latex(bonne_valeur)
\end{python}
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
u _ { 0 }  & { = 4 } \\
   { u _ { n + 1 } } & { = 2 u _ { n } - 3 }
\end{cases}
$. Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{bonne_valeur_latex}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
La fonction $f$ est définie par la relation de récurrence $u_{n+1} = f(u_n)$. Ici, $u_{n+1} = 2u_n - 3$.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La fonction $f$ est $\py{bonne_valeur_latex}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour les suites définies par les relations de récurrence données, 
notre objectif est d'extraire la fonction $ f $ correspondante selon la forme générale 
$ u_{n+1} = f(u_n) $. 
   
Ici, la relation de récurrence étant $ u_{n+1} = 2 u_n - 3 $, on identifie aisément
la fonction $f$ qui est donnée par : 
 $f(x) = \py{bonne_valeur_latex}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = sqrt(1 + x**2)
bonne_valeur_latex = latex(bonne_valeur)
\end{python}
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
    u _ { 0 } &{=} 0  \\
    {u _ { n + 1 }} &{= \sqrt { 1 + u _ { n } ^ { 2 }}}
\end{cases}
$. Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{bonne_valeur_latex}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
La fonction $f$ est définie par la relation de récurrence $u_{n+1} = f(u_n)$. Ici, $u_{n+1} = \sqrt{1 + u_n^2}$.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La fonction $f$ est $\py{bonne_valeur_latex}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour cette suite, la relation de récurrence est $ u_{n+1} = \sqrt{1 + u_n^2} $. 
On identifie aisément
la fonction $f$ qui est donnée par : 
   $
      f(x) = \py{bonne_valeur_latex}.
   $
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = sin(x)
bonne_valeur_latex = latex(bonne_valeur)
\end{python}
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
   { u _ { 0 }} &{= } 2  \\
   { u _ { n + 1 }} &{= \operatorname { s i n } ( u _ { n } ) }
\end{cases}
$. Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{bonne_valeur_latex}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
La fonction $f$ est définie par la relation de récurrence $u_{n+1} = f(u_n)$. Ici, $u_{n+1} = \sin(u_n)$.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La fonction $f$ est $\py{bonne_valeur_latex}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Dans ce cas, la relation de récurrence est  $ u_{n+1} = \sin(u_n) $. 
On identifie aisément
la fonction $f$ qui est donnée par : 
   $
      f(x) = \py{bonne_valeur_latex}.
   $
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = (x - 1)/(x + 1)
bonne_valeur_latex = latex(bonne_valeur)
\end{python}
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
   u_{0}&{=}4 \\
   u_{n+1}&=\frac{u_{n}-1}{u_{n}+1}
\end{cases}
$. Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{bonne_valeur_latex}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
La fonction $f$ est définie par la relation de récurrence $u_{n+1} = f(u_n)$. Ici, $u_{n+1} = \frac{u_n - 1}{u_n + 1}$.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La fonction $f$ est $\py{bonne_valeur_latex}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Enfin, pour cette suite, la relation de récurrence est $ u_{n+1} = \frac{u_n - 1}{u_n + 1} $. 
Nous pouvons identifier la fonction $ f $ comme : 
   $
      f(x) = \py{bonne_valeur_latex}.
   $
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}
}
\end{exercise}
```