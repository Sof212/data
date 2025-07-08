```latex
\begin{exercise}{
Id: 001
Title_exo: Résolution d'équation quadratique
Modules: Algèbre
Recommended_execution_time: 5
Ex_Level: Elementary 
Chap: Équations du second degré
Involved_Concepts: Discriminant, Solutions réelles
Original_source: Exercice original
Visibility: All
}
{

\begin{python}
from sympy import symbols, Eq, solve

# Variables pour la première question (plus petite solution)
x = symbols('x')
equation = x**2 - 2*x - 15
delta = (-2)**2 - 4*1*(-15)
solution1 = (-(-2) - 8)/2
solution2 = (-(-2) + 8)/2
\end{python}

\qcl{
Résoudre l'équation $X^{2}-2 X-15=0$ et donner la plus petite solution.
}
{
[["CL","\py{solution1}"],["0"]]
}
{
Indice: Calculez d'abord le discriminant.
}
{
La plus petite solution est \py{solution1}.
}
{
Commençons par calculer le discriminant, noté $\Delta$, de l'équation. On a :
\begin{equation*}
\Delta 
=
(-2)^{2}-4 \cdot (1) \cdot (-15)
=
4+60
=
64
=
8^2.
\end{equation*}
Nous savons donc que l'équation admet deux solutions réelles distinctes. 
La plus petite solution est :
\begin{equation*}
s_1 
=
 \frac{-(-2)-8}{2\cdot 1}
=
 \frac{2-8}{2}
=
 \frac{-6}{2}
=-3
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import symbols, Eq, solve

# Variables pour la deuxième question (plus grande solution)
x = symbols('x')
equation = x**2 - 2*x - 15
delta = (-2)**2 - 4*1*(-15)
solution1 = (-(-2) - 8)/2
solution2 = (-(-2) + 8)/2
\end{python}

\qcl{
Résoudre l'équation $X^{2}-2 X-15=0$ et donner la plus grande solution.
}
{
[["CL","\py{solution2}"],["0"]]
}
{
Indice: Calculez d'abord le discriminant.
}
{
La plus grande solution est \py{solution2}.
}
{
Commençons par calculer le discriminant, noté $\Delta$, de l'équation. On a :
\begin{equation*}
\Delta 
=
(-2)^{2}-4 \cdot (1) \cdot (-15)
=
4+60
=
64
=
8^2.
\end{equation*}
Nous savons donc que l'équation admet deux solutions réelles distinctes. 
La plus grande solution est :
\begin{equation*}
s_2 
=
 \frac{-(-2)+8}{2\cdot 1}
=
 \frac{2+8}{2}
=
 \frac{10}{2}
=5
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import symbols

# Variables pour la troisième question (discriminant)
delta = (-2)**2 - 4*1*(-15)
\end{python}

\qcl{
Calculer le discriminant de l'équation $X^{2}-2 X-15=0$.
}
{
[["CL","\py{delta}"],["0"]]
}
{
Indice: La formule du discriminant est $\Delta = b^2 - 4ac$.
}
{
Le discriminant vaut \py{delta}.
}
{
Le discriminant se calcule par :
\begin{equation*}
\Delta 
=
(-2)^{2}-4 \cdot (1) \cdot (-15)
=
4+60
=
64
\end{equation*}
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