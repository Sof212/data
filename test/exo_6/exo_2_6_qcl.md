```latex
\begin{exercise}{
Id: 00000000-0000-0000-0000-000000000001
Title_exo: Suites récurrentes
Modules: Analyse
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Suites numériques
Involved_Concepts: Suite_recurrente, Fonction_associee
Original_source: 
Visibility: All
}
{
Pour chaque suite définie par une relation de récurrence, donner la fonction f telle que u_{n+1} = f(u_n).

\qcl{
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = 2*x - 3
\end{python}
Soit la suite $(u_n)$ définie par :
$\begin{cases}
u_0 = 4 \\
u_{n+1} = 2u_n - 3
\end{cases}$
Donner l'expression de la fonction $f$ telle que $u_{n+1} = f(u_n)$.
}
{[["CL","\py{latex(bonne_valeur)}"],["0"]]}
{}
{La fonction est $f(x) = \py{latex(bonne_valeur)}$}
{
Pour la suite définie par la relation de récurrence $u_{n+1} = 2u_n - 3$, 
on identifie directement la fonction $f$ qui est donnée par :
$$f(x) = 2x - 3$$
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = sqrt(1 + x**2)
\end{python}
Soit la suite $(u_n)$ définie par :
$\begin{cases}
u_0 = 0 \\
u_{n+1} = \sqrt{1 + u_n^2}
\end{cases}$
Donner l'expression de la fonction $f$ telle que $u_{n+1} = f(u_n)$.
}
{[["CL","\py{latex(bonne_valeur)}"],["0"]]}
{}
{La fonction est $f(x) = \py{latex(bonne_valeur)}$}
{
Pour cette suite, la relation de récurrence est $u_{n+1} = \sqrt{1 + u_n^2}$. 
La fonction $f$ correspondante est :
$$f(x) = \sqrt{1 + x^2}$$
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = sin(x)
\end{python}
Soit la suite $(u_n)$ définie par :
$\begin{cases}
u_0 = 2 \\
u_{n+1} = \sin(u_n)
\end{cases}$
Donner l'expression de la fonction $f$ telle que $u_{n+1} = f(u_n)$.
}
{[["CL","\py{latex(bonne_valeur)}"],["0"]]}
{}
{La fonction est $f(x) = \py{latex(bonne_valeur)}$}
{
Dans ce cas, la relation de récurrence est $u_{n+1} = \sin(u_n)$. 
La fonction $f$ correspondante est :
$$f(x) = \sin(x)$$
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = (x - 1)/(x + 1)
\end{python}
Soit la suite $(u_n)$ définie par :
$\begin{cases}
u_0 = 4 \\
u_{n+1} = \frac{u_n - 1}{u_n + 1}
\end{cases}$
Donner l'expression de la fonction $f$ telle que $u_{n+1} = f(u_n)$.
}
{[["CL","\py{latex(bonne_valeur)}"],["0"]]}
{}
{La fonction est $f(x) = \py{latex(bonne_valeur)}$}
{
Pour cette suite, la relation de récurrence est $u_{n+1} = \frac{u_n - 1}{u_n + 1}$. 
La fonction $f$ correspondante est :
$$f(x) = \frac{x - 1}{x + 1}$$
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