```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Résolution d'une équation quadratique
Modules: Algèbre
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Équations
Involved_Concepts: Équations_quadratiques, Discriminant
Original_source: null
Visibility: All
}
{
\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
# Pour l'équation X^2 - 2X - 15 = 0
# a = 1, b = -2, c = -15
# Discriminant delta = b^2 - 4ac = (-2)^2 - 4*1*(-15) = 4 + 60 = 64
# Solutions x1 = (-b - sqrt(delta)) / 2a = (2 - 8) / 2 = -6 / 2 = -3
# Solutions x2 = (-b + sqrt(delta)) / 2a = (2 + 8) / 2 = 10 / 2 = 5
bonne_valeur = 5
\end{python}
Résoudre l'équation 
\begin{equation}
\label{eq:quad1}
X^{2}-2 X-15=0.
\end{equation}
Donnez la plus grande solution.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Calculez le discriminant de l'équation quadratique.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La plus grande solution est $\py{bonne_valeur}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Commençons par calculer le discriminant, noté $\Delta$, de l'équation \eqref{eq:quad1}. L'équation est de la forme $aX^2 + bX + c = 0$ avec $a=1$, $b=-2$, et $c=-15$.
On a :
\begin{equation*}
\Delta 
=
b^{2}-4ac
=
(-2)^{2}-4 \cdot (1) \cdot (-15)
=
4+60
=
64
=
8^2.
\end{equation*}
Puisque $\Delta > 0$, l'équation \eqref{eq:quad1} admet deux solutions réelles distinctes, 
notées $s_1$ et $s_2$. On a:
\begin{equation*}
\begin{align*}
&s_1 
=
 \frac{-b-\sqrt{\Delta}}{2a}
=
 \frac{-(-2)-8}{2\cdot 1}
=
 \frac{2-8}{2}
=
 \frac{-6}{2}
=-3&
&\&&
&s_2 
=
 \frac{-b+\sqrt{\Delta}}{2a}
=
 \frac{-(-2)+8}{2\cdot 1}
=
 \frac{2+8}{2}
=
 \frac{10}{2}
=5&
\end{align*}
\end{equation*}
Ainsi, les solutions de l'équation \eqref{eq:quad1} sont :  $\boxed{5 \quad \text{et} \quad -3}$. La plus grande solution est $\py{bonne_valeur}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
# Pour l'équation X^2 - 2X - 15 = 0
# a = 1, b = -2, c = -15
# Discriminant delta = b^2 - 4ac = (-2)^2 - 4*1*(-15) = 4 + 60 = 64
# Solutions x1 = (-b - sqrt(delta)) / 2a = (2 - 8) / 2 = -6 / 2 = -3
# Solutions x2 = (-b + sqrt(delta)) / 2a = (2 + 8) / 2 = 10 / 2 = 5
bonne_valeur = -3
\end{python}
Résoudre l'équation 
\begin{equation}
\label{eq:quad2}
X^{2}-2 X-15=0.
\end{equation}
Donnez la plus petite solution.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez la formule quadratique pour trouver les racines.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La plus petite solution est $\py{bonne_valeur}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Commençons par calculer le discriminant, noté $\Delta$, de l'équation \eqref{eq:quad2}. L'équation est de la forme $aX^2 + bX + c = 0$ avec $a=1$, $b=-2$, et $c=-15$.
On a :
\begin{equation*}
\Delta 
=
b^{2}-4ac
=
(-2)^{2}-4 \cdot (1) \cdot (-15)
=
4+60
=
64
=
8^2.
\end{equation*}
Puisque $\Delta > 0$, l'équation \eqref{eq:quad2} admet deux solutions réelles distinctes, 
notées $s_1$ et $s_2$. On a:
\begin{equation*}
\begin{align*}
&s_1 
=
 \frac{-b-\sqrt{\Delta}}{2a}
=
 \frac{-(-2)-8}{2\cdot 1}
=
 \frac{2-8}{2}
=
 \frac{-6}{2}
=-3&
&\&&
&s_2 
=
 \frac{-b+\sqrt{\Delta}}{2a}
=
 \frac{-(-2)+8}{2\cdot 1}
=
 \frac{2+8}{2}
=
 \frac{10}{2}
=5&
\end{align*}
\end{equation*}
Ainsi, les solutions de l'équation \eqref{eq:quad2} sont :  $\boxed{5 \quad \text{et} \quad -3}$. La plus petite solution est $\py{bonne_valeur}$.
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