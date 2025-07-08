```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Fonctions de récurrence de suites
Modules: M1_1_Suites
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Suites_numeriques
Involved_Concepts: Suites_recurrentes, Fonctions
Original_source: null
Visibility: All
}
{
\begin{python}
from sympy import *
x = symbols('x')
# Pour la première question
f1_expr = 2*x - 3
f1_latex = latex(f1_expr)

# Pour la deuxième question
f2_expr = sqrt(1 + x**2)
f2_latex = latex(f2_expr)

# Pour la troisième question
f3_expr = sin(x)
f3_latex = latex(f3_expr)

# Pour la quatrième question
f4_expr = (x - 1) / (x + 1)
f4_latex = latex(f4_expr)
\end{python}

\qcl{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
u _ { 0 }  & { = 4 } \\
   { u _ { n + 1 } } & { = 2 u _ { n } - 3 }
\end{cases}
$.
Donnez l'expression de la fonction $f(x)$ telle que $u_{n+1} = f(u_n)$.
}
{
[["CL","\py{f1_latex}"],["0"]]
}
{
Identifiez la partie de l'expression de $u_{n+1}$ qui dépend de $u_n$.
}
{
La fonction $f(x)$ est $\py{f1_latex}$.
}
{
Pour les suites définies par les relations de récurrence données, 
notre objectif est d'extraire la fonction $ f $ correspondante selon la forme générale 
$ u_{n+1} = f(u_n) $. 
   
Ici, la relation de récurrence étant $ u_{n+1} = 2 u_n - 3 $, on identifie aisément
la fonction $f$ qui est donnée par : 
 $f(x) = 2x - 3$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
    u _ { 0 } &{=} 0  \\
    {u _ { n + 1 }} &{= \sqrt { 1 + u _ { n } ^ { 2 }}}
\end{cases}
$
Donnez l'expression de la fonction $f(x)$ telle que $u_{n+1} = f(u_n)$.
}
{
[["CL","\py{f2_latex}"],["0"]]
}
{
Identifiez la partie de l'expression de $u_{n+1}$ qui dépend de $u_n$.
}
{
La fonction $f(x)$ est $\py{f2_latex}$.
}
{
Pour cette suite, la relation de récurrence est $ u_{n+1} = \sqrt{1 + u_n^2} $. 
On identifie aisément
la fonction $f$ qui est donnée par : 
   $
      f(x) = \sqrt{1 + x^2}.
   $
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
   { u _ { 0 }} &{= } 2  \\
   { u _ { n + 1 }} &{= \operatorname { s i n } ( u _ { n } ) }
\end{cases}
$
Donnez l'expression de la fonction $f(x)$ telle que $u_{n+1} = f(u_n)$.
}
{
[["CL","\py{f3_latex}"],["0"]]
}
{
Identifiez la partie de l'expression de $u_{n+1}$ qui dépend de $u_n$.
}
{
La fonction $f(x)$ est $\py{f3_latex}$.
}
{
 
    Dans ce cas, la relation de récurrence est  $ u_{n+1} = \sin(u_n) $. 
On identifie aisément
la fonction $f$ qui est donnée par : 
   $
      f(x) = \sin(x).
   $
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
   u_{0}&{=}4 \\
   u_{n+1}&=\frac{u_{n}-1}{u_{n}+1}
\end{cases}
$
Donnez l'expression de la fonction $f(x)$ telle que $u_{n+1} = f(u_n)$.
}
{
[["CL","\py{f4_latex}"],["0"]]
}
{
Identifiez la partie de l'expression de $u_{n+1}$ qui dépend de $u_n$.
}
{
La fonction $f(x)$ est $\py{f4_latex}$.
}
{
      Enfin, pour cette suite, la relation de récurrence est $ u_{n+1} = \frac{u_n - 1}{u_n + 1} $. 
Nous pouvons identifier la fonction $ f $ comme : 
   $
      f(x) = \frac{x - 1}{x + 1}.
   $
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}
}
\end{exercise}
```