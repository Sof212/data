```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Résolution d'une équation quadratique
Modules: Algèbre
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Équations
Involved_Concepts: Équations_quadratiques, Discriminant, Solutions_réelles
Original_source: null
Visibility: All
}
{
\begin{python}
from sympy import *
# Coefficients de l'équation ax^2 + bx + c = 0
a_val = 1
b_val = -2
c_val = -15

# Calcul du discriminant
delta = b_val**2 - 4 * a_val * c_val

# Calcul des solutions
s1 = ( -b_val - sqrt(delta) ) / (2 * a_val)
s2 = ( -b_val + sqrt(delta) ) / (2 * a_val)

# Valeurs pour les réponses
bonne_valeur_delta = delta
bonne_valeur_min_sol = min(s1, s2)
bonne_valeur_max_sol = max(s1, s2)
\end{python}

\qcl{Calculer le discriminant $\Delta$ de l'équation $X^{2}-2 X-15=0$.}
{
[["CL","\py{bonne_valeur_delta}"],["0"]]
}
{
Le discriminant $\Delta$ d'une équation quadratique $aX^2 + bX + c = 0$ est donné par la formule $\Delta = b^2 - 4ac$.
}
{
Le discriminant est $\Delta = \py{bonne_valeur_delta}$.
}
{
L'équation donnée est $X^{2}-2 X-15=0$.
Elle est de la forme $aX^2 + bX + c = 0$ avec $a=1$, $b=-2$, et $c=-15$.
Le discriminant $\Delta$ est calculé par la formule :
$\Delta = b^2 - 4ac$
$\Delta = (-2)^2 - 4 \cdot (1) \cdot (-15)$
$\Delta = 4 - (-60)$
$\Delta = 4 + 60$
$\Delta = 64$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la plus petite solution de l'équation $X^{2}-2 X-15=0$.}
{
[["CL","\py{bonne_valeur_min_sol}"],["0"]]
}
{
Si le discriminant $\Delta$ est positif, les solutions sont données par $X = \frac{-b \pm \sqrt{\Delta}}{2a}$.
}
{
La plus petite solution est \py{bonne_valeur_min_sol}.
}
{
L'équation est $X^{2}-2 X-15=0$.
Nous avons calculé le discriminant $\Delta = 64$.
Puisque $\Delta > 0$, l'équation admet deux solutions réelles distinctes, $s_1$ et $s_2$, données par les formules :
$s_1 = \frac{-b - \sqrt{\Delta}}{2a}$ et $s_2 = \frac{-b + \sqrt{\Delta}}{2a}$.
Avec $a=1$, $b=-2$, $c=-15$ et $\sqrt{\Delta} = \sqrt{64} = 8$:
$s_1 = \frac{-(-2) - 8}{2 \cdot 1} = \frac{2 - 8}{2} = \frac{-6}{2} = -3$.
$s_2 = \frac{-(-2) + 8}{2 \cdot 1} = \frac{2 + 8}{2} = \frac{10}{2} = 5$.
La plus petite solution est donc $-3$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la plus grande solution de l'équation $X^{2}-2 X-15=0$.}
{
[["CL","\py{bonne_valeur_max_sol}"],["0"]]
}
{
Si le discriminant $\Delta$ est positif, les solutions sont données par $X = \frac{-b \pm \sqrt{\Delta}}{2a}$.
}
{
La plus grande solution est \py{bonne_valeur_max_sol}.
}
{
L'équation est $X^{2}-2 X-15=0$.
Nous avons calculé le discriminant $\Delta = 64$.
Puisque $\Delta > 0$, l'équation admet deux solutions réelles distinctes, $s_1$ et $s_2$, données par les formules :
$s_1 = \frac{-b - \sqrt{\Delta}}{2a}$ et $s_2 = \frac{-b + \sqrt{\Delta}}{2a}$.
Avec $a=1$, $b=-2$, $c=-15$ et $\sqrt{\Delta} = \sqrt{64} = 8$:
$s_1 = \frac{-(-2) - 8}{2 \cdot 1} = \frac{2 - 8}{2} = \frac{-6}{2} = -3$.
$s_2 = \frac{-(-2) + 8}{2 \cdot 1} = \frac{2 + 8}{2} = \frac{10}{2} = 5$.
La plus grande solution est donc $5$.
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