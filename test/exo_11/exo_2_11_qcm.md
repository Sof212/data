```latex
\begin{exercise}{
Title_exo: \fr{Primitives de fonctions polynomiales}\en{Primitives of polynomial functions}
Modules: Calcul_intégral % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Intégration, Primitives % NameID des chapitres
Involved_Concepts: Primitive, Fonction_polynomiale % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
Comment: % Commentaire de l'exercice (optionnel)
}
{

\begin{python}
from sympy import *
x = symbols('x')

# --- QCM 1: f(x) ---
f_expr = (x**2 - 2*x + 1)/3
bonne_valeur_f = integrate(f_expr, x)
# Erreurs typiques pour f(x)
fausse_f1 = integrate((x**2 - 2*x)/3, x) + x/3 # Oubli du +1 dans l'intégrale, mais le x/3 est là
fausse_f2 = integrate((x**2 - 2*x + 1), x) # Oubli du /3
fausse_f3 = integrate((x**2 + 2*x + 1)/3, x) # Erreur de signe sur 2x

# --- QCM 2: g(x) ---
g_expr = x**4 - 4*x**3 + x**2 - 4*x + 3
bonne_valeur_g = integrate(g_expr, x)
# Erreurs typiques pour g(x)
fausse_g1 = integrate(x**4 - 4*x**3 + x**2 - 4*x, x) # Oubli du +3
fausse_g2 = integrate(x**4 - 4*x**3 + x**2 - 4*x + 6, x) # Erreur constante (3 devient 6)
fausse_g3 = integrate(x**4 - 2*x**3 + x**2 - 4*x + 3, x) # Erreur de coefficient sur x^3 (-4 devient -2)
\end{python}

\qcm{
\fr{Soit $f:\mathbf{R}^{*}_+ \rightarrow \mathbf{R}$ la fonction définie par $f(x) := \frac{x^{2}-2 x+1}{3}$. Une primitive de $f$ est :}\en{Let $f:\mathbf{R}^{*}_+ \rightarrow \mathbf{R}$ be the function defined by $f(x) := \frac{x^{2}-2 x+1}{3}$. A primitive of $f$ is:}
}{
\right{$\displaystyle \sympy{bonne_valeur_f} + C$}
\wrong{$\displaystyle \sympy{fausse_f2} + C$}
\wrong{$\displaystyle \sympy{fausse_f1} + C$}
\wrong{$\displaystyle \sympy{fausse_f3} + C$}
\wronger % (aucune proposition correcte)
\righter % (toutes propositions correctes)
}
{
\fr{Penser à intégrer terme à terme après avoir distribué le coefficient $1/3$.}\en{Remember to integrate term by term after distributing the coefficient $1/3$.}
}
{
\fr{On peut écrire:}\en{We can write:}
\begin{equation*}
\begin{align*}
\int f(x) \ dx 
&= \int \frac{x^{2}-2 x+1}{3} \ dx 
= \frac{1}{3} \int (x^{2}-2 x+1) \ dx \\
&= \frac{1}{3} \left[ \frac{x^{3}}{3}- 2\frac{x^2}{2} + x \right] + C
= \frac{x^{3}}{9} - \frac{x^{2}}{3} + \frac{x}{3} + C
\end{align*}
\end{equation*}
\fr{où $C$ désigne un nombre réel.}\en{where $C$ denotes a real number.}
}
{
logic: 20
abstraction: 20
reasoning: 30
calculation: 30
}

\qcm{
\fr{Soit $g:\mathbf{R}^{*}_+ \rightarrow \mathbf{R}$ la fonction définie par $g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$. Une primitive de $g$ est :}\en{Let $g:\mathbf{R}^{*}_+ \rightarrow \mathbf{R}$ be the function defined by $g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$. A primitive of $g$ is:}
}{
\right{$\displaystyle \sympy{bonne_valeur_g} + C$}
\wrong{$\displaystyle \sympy{fausse_g1} + C$}
\wrong{$\displaystyle \sympy{fausse_g2} + C$}
\wrong{$\displaystyle \sympy{fausse_g3} + C$}
\wronger % (aucune proposition correcte)
\righter % (toutes propositions correctes)
}
{
\fr{Intégrer chaque terme du polynôme séparément en appliquant la formule $\int x^n dx = \frac{x^{n+1}}{n+1}$.}\en{Integrate each term of the polynomial separately by applying the formula $\int x^n dx = \frac{x^{n+1}}{n+1}$.}
}
{
\fr{On intègre terme à terme :}\en{We integrate term by term:}
\begin{equation*}
\begin{align*}
\int g(x) \ dx 
&= \int (x^{4}-4x^{3}+x^{2}-4x+3) \, dx \\
&= \frac{x^{5}}{5} - \frac{4x^{4}}{4} + \frac{x^{3}}{3} - \frac{4x^2}{2} + 3x + C \\
&= \frac{x^{5}}{5} - x^{4} + \frac{x^{3}}{3} - 2x^2 + 3x + C
\end{align*}
\end{equation*}
\fr{où $C$ désigne un nombre réel.}\en{where $C$ denotes a real number.}
}
{
logic: 20
abstraction: 20
reasoning: 30
calculation: 30
}
}
\end{exercise}
```