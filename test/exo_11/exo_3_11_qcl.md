```latex
\begin{exercise}{
Id: 001
Title_exo: Primitives de fonctions polynomiales
Modules: Analyse
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Intégration
Involved_Concepts: Primitives, Fonctions polynomiales
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
Déterminer une primitive de chacune des fonctions définies ci-dessous.

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Soit $f:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction $\ds f(x) := \frac{x^{2}-2 x+1}{3}$.
Donnez une primitive de $f(x)$.
}
{
\begin{python}
from sympy import *
x = symbols('x')
# Pour la première fonction f(x)
f_expr = (x**2 - 2*x + 1) / 3
primitive_f = integrate(f_expr, x)
# Formatage pour l'affichage LaTeX
primitive_f_latex = latex(primitive_f)
\end{python}
[["CL","\py{primitive_f_latex} + C"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Rappelez-vous les règles d'intégration pour les polynômes.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
Une primitive de $f(x)$ est $\py{primitive_f_latex} + C$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
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
où $C$ désigne un nombre réel.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Soit $g:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction définie par:
$\ds g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$.
Donnez une primitive de $g(x)$.
}
{
\begin{python}
from sympy import *
x = symbols('x')
# Pour la deuxième fonction g(x)
g_expr = x**4 - 4*x**3 + x**2 - 4*x + 3
primitive_g = integrate(g_expr, x)
# Formatage pour l'affichage LaTeX
primitive_g_latex = latex(primitive_g)
\end{python}
[["CL","\py{primitive_g_latex} + C"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Intégrez chaque terme du polynôme séparément.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
Une primitive de $g(x)$ est $\py{primitive_g_latex} + C$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Là encore nous allons intégrer terme à terme.
On peut écrire:
\begin{equation*}
\begin{align*}
\int g(x) \ dx 
&=
\int (x^{4}-4x^{3}+x^{2}-4x+3) \, dx \\
&=
\frac{x^{5}}{5} - 4\frac{x^{4}}{4} + \frac{x^{3}}{3} - 4\frac{x^2}{2} + 3x + C \\
&=
\frac{x^{5}}{5} - x^{4} + \frac{x^{3}}{3} - 2x^2 + 3x + C,
\end{align*}
\end{equation*}
où $C$ désigne un nombre réel.
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