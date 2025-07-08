```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Primitives de fonctions polynomiales
Modules: R2_10_Calcul_Integral
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Integration
Involved_Concepts: Primitive, Polynomial
Original_source: Exercice original
Visibility: All
}
{
\begin{python}
from sympy import symbols, integrate, Rational, latex

x = symbols('x')
f_expr = (x**2 - 2*x + 1)/3
g_expr = x**4 - 4*x**3 + x**2 - 4*x + 3

f_primitive = integrate(f_expr, x)
g_primitive = integrate(g_expr, x)

f_primitive_latex = latex(f_primitive)
g_primitive_latex = latex(g_primitive)
\end{python}

\qcl{
Soit $f:\mathbb{R}^{*}_+ \rightarrow \mathbb{R}$ la fonction définie par $f(x) = \frac{x^{2}-2x+1}{3}$. 
Calculer une primitive de $f$ sous la forme développée (sans constante d'intégration).
}
{
[["CL","\py{f_primitive_latex}"],["0"]]
}
{
Indice: Intégrer terme à terme en utilisant la formule $\int x^n dx = \frac{x^{n+1}}{n+1}$ pour chaque terme.
}
{
Solution brève : Une primitive est $\py{f_primitive_latex}$
}
{
Solution détaillée :
On peut écrire:
\begin{equation*}
\begin{align*}
\int f(x) \ dx 
&=
\int  \frac{x^{2}-2x+1}{3} \ dx 
=
 \frac{1}{3} \int (x^{2}-2x+1) \ dx \\
&=
 \frac{1}{3} \left[ \frac{x^{3}}{3}- 2\frac{x^2}{2} + x \right] + C
=
\frac{x^{3}}{9} - \frac{x^{2}}{3} + \frac{x}{3} + C,
\end{align*}
\end{equation*}
où $C$ désigne un nombre réel.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Soit $g:\mathbb{R}^{*}_+ \rightarrow \mathbb{R}$ la fonction définie par $g(x) = x^{4}-4x^{3}+x^{2}-4x+3$.
Calculer une primitive de $g$ sous la forme développée (sans constante d'intégration).
}
{
[["CL","\py{g_primitive_latex}"],["0"]]
}
{
Indice: Intégrer chaque terme du polynôme séparément en utilisant la formule de l'intégrale des puissances de x.
}
{
Solution brève : Une primitive est $\py{g_primitive_latex}$
}
{
Solution détaillée :
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
où $C$ désigne un nombre réel.
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