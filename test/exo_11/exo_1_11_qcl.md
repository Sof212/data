```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Calcul de primitives de fonctions polynomiales
Modules: M1_1_Analyse
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Integration
Involved_Concepts: Primitive_of_polynomials
Original_source: null
Visibility: All
}
{
Déterminer une primitive de chacune des fonctions définies ci-dessous.

\qcl{
\begin{python}
from sympy import *
x = symbols('x')
f_expr = (x**2 - 2*x + 1) / 3
primitive_f = integrate(f_expr, x)
primitive_f_latex = latex(primitive_f) + ' + C'
\end{python}
Soit $f:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction $\ds f(x) := \frac{x^{2}-2 x+1}{3}$.
Calculer $\int f(x) \, dx$.
}
{
[["CL","$\py{primitive_f_latex}$"],["0"]]
}
{
}
{
$\py{primitive_f_latex}$
}
{
On peut écrire:
\begin{equation*}
\begin{align*}
\int f(x) \ dx
&=
\int  \frac{x^{2}-2 x+1}{3} \ dx
=
 \frac{1}{3} \int (x^{2}-2 x+1) \ dx \\
&=
 \frac{1}{3} \left[ \frac{x^{3}}{3}- 2\frac{x^2}{2} + x \right] + C \\
&=
\frac{x^{3}}{9} - \frac{x^{2}}{3} + \frac{x}{3} + C,
\end{align*}
\end{equation*}
\fr{où $C$ désigne un nombre réel}%
\en{where $C$ is any real number}.
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
g_expr = x**4 - 4*x**3 + x**2 - 4*x + 3
primitive_g = integrate(g_expr, x)
primitive_g_latex = latex(primitive_g) + ' + C'
\end{python}
Soit $g:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction définie par:
$\ds g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$.
Calculer $\int g(x) \, dx$.
}
{
[["CL","$\py{primitive_g_latex}$"],["0"]]
}
{
}
{
$\py{primitive_g_latex}$
}
{
On peut écrire:
\begin{equation*}
\begin{align*}
\int g(x) \ dx
&=
\int (x^{4}-4x^{3}+x^{2}-4x+3) \, dx \\
&=
\frac{x^{5}}{5} - x^{4} + \frac{x^{3}}{3} - 2x^2 + 3x + C,
\end{align*}
\end{equation*}
\fr{où $C$ désigne un nombre réel}%
\en{where $C$ is any real number}.
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