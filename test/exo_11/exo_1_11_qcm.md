```latex
\begin{exercise}{
Title_exo: \fr{Primitives de fonctions polynomiales}\en{Antiderivatives of polynomial functions}
Modules: Calculus_NYU % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Antiderivatives_and_integrals % NameID des chapitres
Involved_Concepts: Antiderivative, Polynomial_function % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Exercice simple sur le calcul de primitives de fonctions polynomiales.
}
{
% Contenu de l'exercice
\fr{Déterminer une primitive de chacune des fonctions définies ci-dessous.}\en{Determine an antiderivative for each of the functions defined below.}

\begin{python}
from sympy import *
# === Calcul bonne réponse ===
x = symbols('x')
f_expr = (x**2 - 2*x + 1) / 3
bonne_valeur = integrate(f_expr, x)
# === Propositions fausses calculées ===
fausse_1 = x**3/3 - x**2 + x
fausse_2 = x**3/9 - x**2/3 + x
fausse_3 = x**3/3 - x**2 + x/3
\end{python}
\qcm{\fr{Soit $f:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction $\ds f(x) := \frac{x^{2}-2 x+1}{3}$. Une primitive de $f$ est :}\en{Let $f:{\bfR}^{*}_+ \rightarrow \bfR$ be the function $\ds f(x) := \frac{x^{2}-2 x+1}{3}$. An antiderivative of $f$ is:}}
{
\right{$\displaystyle \sympy{bonne_valeur} + C$}
\wrong{$\displaystyle \sympy{fausse_1} + C$}
\wrong{$\displaystyle \sympy{fausse_2} + C$}
\wrong{$\displaystyle \sympy{fausse_3} + C$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
\fr{Rappelez-vous la règle d'intégration pour les puissances de $x$: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$.}\en{Recall the integration rule for powers of $x$: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$.}
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
\fr{On peut écrire:}\en{We can write:}
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
\fr{où $C$ désigne un nombre réel.}\en{where $C$ is any real number.}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse ===
x = symbols('x')
g_expr = x**4 - 4*x**3 + x**2 - 4*x + 3
bonne_valeur = integrate(g_expr, x)
# === Propositions fausses calculées ===
fausse_1 = x**5/5 - x**4 + x**3 - 2*x**2 + 3*x
fausse_2 = x**5/5 - 4*x**4 + x**3 - 4*x**2 + 3*x
fausse_3 = x**5/5 - x**4 + x**3/3 - 4*x**2 + 3*x
\end{python}
\qcm{\fr{Soit $g:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction définie par:
$\ds g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$. Une primitive de $g$ est :}\en{Let $g:{\bfR}^{*}_+ \rightarrow \bfR$ be the function defined by:
$\ds g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$. An antiderivative of $g$ is:}}
{
\right{$\displaystyle \sympy{bonne_valeur} + C$}
\wrong{$\displaystyle \sympy{fausse_1} + C$}
\wrong{$\displaystyle \sympy{fausse_2} + C$}
\wrong{$\displaystyle \sympy{fausse_3} + C$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
\fr{Intégrez chaque terme du polynôme séparément.}\en{Integrate each term of the polynomial separately.}
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
\fr{Là encore nous allons intégrer terme à terme.
On peut écrire:}\en{Again, we will integrate term by term.
We can write:}
\begin{equation*}
\begin{align*}
\int g(x) \ dx 
&=
\int (x^{4}-4x^{3}+x^{2}-4x+3) \, dx \\
&=
\frac{x^{5}}{5} - 4\frac{x^{4}}{4} + \frac{x^{3}}{3} - 4\frac{x^{2}}{2} + 3x + C \\
&=
\frac{x^{5}}{5} - x^{4} + \frac{x^{3}}{3} - 2x^2 + 3x + C,
\end{align*}
\end{equation*}
\fr{où $C$ désigne un nombre réel.}\en{where $C$ is any real number.}
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