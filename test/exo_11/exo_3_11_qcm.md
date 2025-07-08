```latex
\begin{exercise}{
Title_exo: Primitives de fonctions polynomiales
Modules: Analyse
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Calcul_Integral, Fonctions_Usuelles
Involved_Concepts: Primitive, Integration
Original_source: Exercice original
Visibility: All
Comment: Conversion d'un exercice de détermination de primitives en QCM.
}
{ % Contenu de l'exercice

\begin{python}
from sympy import *

# Define symbols
x = symbols('x')

# QST 1: f(x) = (x^2 - 2x + 1) / 3
f_x = (x**2 - 2*x + 1) / 3
bonne_valeur = integrate(f_x, x)

# Generate false answers for f(x)
# Erreur méthodologique typique: Oubli du facteur 1/3
fausse_1 = integrate(x**2 - 2*x + 1, x)
# Variante calcul incorrecte: Erreur de signe sur un terme
fausse_2 = (x**3/9 + x**2/3 + x/3)
# Approximation erronée: Erreur de puissance (ex: x^2 -> x^4/4)
fausse_3 = (x**4/12 - x**3/6 + x**2/6)
\end{python}
\qcm{ % Enoncé de la question
Soit $f:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction $\ds f(x) := \frac{x^{2}-2 x+1}{3}$.
Déterminer une primitive de $f(x)$.
}
{
\right{$\py{latex(bonne_valeur)} + C$}
\wrong{$\py{latex(fausse_1)} + C$}
\wrong{$\py{latex(fausse_2)} + C$}
\wrong{$\py{latex(fausse_3)} + C$}
\wrong{$\frac{x^{3}}{3} - x^{2} + x + C$}
}
{ % Indice
Rappelez-vous les règles d'intégration des polynômes et la linéarité de l'intégrale.
}
{ % Solution détaillée
Pour déterminer une primitive de $f(x) = \frac{x^{2}-2 x+1}{3}$, nous pouvons utiliser la linéarité de l'intégrale et les règles d'intégration des puissances de $x$:
$$ \int \frac{x^{2}-2 x+1}{3} \ dx = \frac{1}{3} \int (x^{2}-2 x+1) \ dx $$
En intégrant terme par terme:
$$ \int x^2 \ dx = \frac{x^{2+1}}{2+1} = \frac{x^3}{3} $$
$$ \int -2x \ dx = -2 \frac{x^{1+1}}{1+1} = -2 \frac{x^2}{2} = -x^2 $$
$$ \int 1 \ dx = x $$
Donc,
$$ \frac{1}{3} \left( \frac{x^3}{3} - x^2 + x \right) + C = \frac{x^3}{9} - \frac{x^2}{3} + \frac{x}{3} + C $$
où $C$ désigne un nombre réel.
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *

# Define symbols
x = symbols('x')

# QST 2: g(x) = x^4 - 4x^3 + x^2 - 4x + 3
g_x = x**4 - 4*x**3 + x**2 - 4*x + 3
bonne_valeur = integrate(g_x, x)

# Generate false answers for g(x)
# Erreur méthodologique typique: Oubli de coefficient ou erreur de calcul
fausse_1 = (x**5/5 - x**4 + x**3/3 - 4*x**2 + 3*x)
# Variante calcul incorrecte: Erreur de signe sur un terme
fausse_2 = (x**5/5 + x**4 + x**3/3 - 2*x**2 + 3*x)
# Approximation erronée: Erreur de puissance sur un terme
fausse_3 = (x**6/6 - x**5 + x**4/4 - 2*x**3 + 3*x**2)
\end{python}
\qcm{ % Enoncé de la question
Soit $g:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction définie par:
$\ds g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$.
Déterminer une primitive de $g(x)$.
}
{
\right{$\py{latex(bonne_valeur)} + C$}
\wrong{$\py{latex(fausse_1)} + C$}
\wrong{$\py{latex(fausse_2)} + C$}
\wrong{$\py{latex(fausse_3)} + C$}
\wrong{$x^{5} - x^{4} + x^{3} - x^{2} + x + C$}
}
{ % Indice
Intégrez chaque terme du polynôme séparément.
}
{ % Solution détaillée
Pour déterminer une primitive de $g(x) = x^{4}-4 x^{3}+x^{2}-4 x+3$, nous intégrons chaque terme du polynôme:
$$ \int (x^{4}-4x^{3}+x^{2}-4x+3) \, dx $$
$$ \int x^4 \ dx = \frac{x^5}{5} $$
$$ \int -4x^3 \ dx = -4 \frac{x^4}{4} = -x^4 $$
$$ \int x^2 \ dx = \frac{x^3}{3} $$
$$ \int -4x \ dx = -4 \frac{x^2}{2} = -2x^2 $$
$$ \int 3 \ dx = 3x $$
En combinant ces termes, nous obtenons:
$$ \frac{x^{5}}{5} - x^{4} + \frac{x^{3}}{3} - 2x^2 + 3x + C $$
où $C$ désigne un nombre réel.
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