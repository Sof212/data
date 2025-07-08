\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts: % ID ou NameID des notions
Original_source: % Source de l'exercice
}
{

\begin{python}

import sympy as sp
import numpy as np


x, C = sp.symbols('x C')



P1 = sp.Rational(1,9)*x**3 - sp.Rational(1,3)*x**2 + sp.Rational(1,3)*x + C

P1_expanded = sp.expand(P1)


P3 = sp.Rational(1,5)*x**5 - x**4 + sp.Rational(1,3)*x**3 - 2*x**2 + 3*x + C

P3_expanded = sp.expand(P3)




\end{python}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Soit $f:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction $\ds f(x) := \frac{x^{2}-2 x+1}{3}$. Déterminez une primitive de $f(x)$. Complétez l'expression suivante :

}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{sp.latex(P1_expanded)}$"],["0"]]

}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Simplifiez l'expression $f(x)$ avant d'intégrer.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{sp.latex(P1_expanded)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
On peut écrire l'intégrale de la manière suivante:
\begin{equation*}
\begin{align*}
\int f(x) \ dx 
&= \int  \frac{x^{2}-2 x+1}{3} \ dx 
= \frac{1}{3} \int (x^{2}-2 x+1) \ dx \\
&= \frac{1}{3} \left[ \frac{x^{3}}{3}- 2\frac{x^2}{2} + x \right] + C,
= \frac{x^{3}}{9} - \frac{x^{2}}{3} + \frac{x}{3} + C,
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
Soit $g:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction définie par $\ds g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$. Déterminez une primitive de $g(x)$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement

[["CL","$\py{sp.latex(P3_expanded)}$"],["0"]]

}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Intégrez chaque terme séparément.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\frac{x^{5}}{5} -x^{4} + \frac{x^{3}}{3} -2x^2 + 3x +C$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Nous allons intégrer terme à terme:
\begin{equation*}
\int g(x) \ dx 
= \int (x^{4}-4x^{3}+x^{2}-4x+3) \, dx \\
= \frac{x^{5}}{5} - x^{4} + \frac{x^{3}}{3} - 2x^2 + 3x + C,
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
