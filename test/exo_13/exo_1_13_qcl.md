```latex
\begin{exercise}{
Id: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d
Title_exo: Décomposition en éléments simples
Modules: M1_10_Analyse
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Intégration
Involved_Concepts: Décomposition_éléments_simples
Original_source: null
Visibility: All
}
{
Le but de l'exercice est de trouver les primitives de la fonction $f$ définie
sur ${\bfR}^{*}_{+}$%$\mathbb{R}_{*}^{+}$
par
\begin{equation*}
f(x)
=
\frac{x^{2}+2 x+2}{x^{2}+x}.
\end{equation*}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
a_val = 1
b_val = 2
c_val = -1
\end{python}
Déterminer les réels $a, b$ et $c$ tels que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$a=\py{a_val}$, $b=\py{b_val}$, $c=\py{c_val}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$a=\py{a_val}$, $b=\py{b_val}$, $c=\py{c_val}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Nous pouvons procéder par équivalences et écrire, pour tout réel strictement positif $x$,
\begin{equation*}
\begin{align*}
f(x) = a + \frac{b}{x} + \frac{c}{x+1}
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
a + \frac{b}{x} + \frac{c}{x+1}\\
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
 \frac{a x(x+1)}{x(x+1)} + \frac{b(x+1)}{x(x+1)} + \frac{cx}{x(x+1)}\\
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
 \frac{a x(x+1) + b(x+1) + cx}{x(x+1)}\\
&\Longleftrightarrow
x^{2}+2 x+2
=
a x(x+1) + b(x+1) + cx\\
&\Longleftrightarrow
x^{2}+2 x+2
=
ax^2 + x(a+b+c) + b\\
&\Longleftrightarrow
(1-a)x^{2}+(2-(a+b+c)) x+2-b = 0.
\end{align*}
\end{equation*}
La dernière égalité étant vraie pour tout réel strictement positif $x$, 
on en conclut que tous les coefficients de la précédente équation polynomiale sont nuls.
On obtient donc le système suivant:
\begin{equation*}
\begin{align*}
(\cS):
\begin{cases}
1-a = 0 & \\
2-(a+b+c) = 0 & \\
2-b = 0 & 
\end{cases}
\end{align*}
\end{equation*}
Ce système se résout aisément et nous obtenons $(a,b,c) = (\py{a_val},\py{b_val},\py{c_val})$.
%
:::{dropdown} {color:blue}`Voir les détails de la résolution du système $(\cS)$ `
:close:
\begin{equation*}
\begin{align*}
(\cS)
\Longleftrightarrow
\begin{cases}
a = 1 & \\
b = 2 & \\
c = 2-a-b &
\end{cases}
\Longleftrightarrow
\begin{cases}
a = 1 & \\
b = 2 & \\
c = 2-1-2 &
\end{cases}
\Longleftrightarrow
\begin{cases}
a = \py{a_val} & \\
b = \py{b_val} & \\
c = \py{c_val} &
\end{cases}
\end{align*}
\end{equation*}
:::
On a donc montré l'égalité suivante:
\begin{equation*}
f(x)=\py{a_val}+\frac{\py{b_val}}{x}+\frac{\py{c_val}}{x+1}.
\end{equation*}
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