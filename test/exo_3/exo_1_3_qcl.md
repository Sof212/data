```latex
\begin{exercise}{
Id: 00000000-0000-0000-0000-000000000001
Title_exo: Conversion de radians en degrés
Modules: Trigonométrie
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Conversion d'angles
Involved_Concepts : Conversion d'angles, Trigonométrie
Visibility: All
}
{
Convertir en degrés les mesures d'angle suivantes, exprimées en radians :

\qcl{
\begin{python}
from sympy import *
theta1_rad = Rational(1, 5) * pi
bonne_valeur_theta1 = (theta1_rad * 180 / pi).simplify()
\end{python}
$\theta_1:= \frac{\pi}{5}.$
}
{
[["CL","\py{bonne_valeur_theta1}"],["0"]]
}
{
Utilisez la relation de conversion : $\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}$.
}
{
La mesure de l'angle $\theta_1$ est $\py{bonne_valeur_theta1}^{\circ}$.
}
{
On sait que $180$ degrés correspondent à $\pi$ radians. Par conséquent, pour exprimer en degrés un angle exprimé en radians, on utilise la relation :

\begin{equation*}
\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}
\end{equation*}

####  Conversion de $\frac{\pi}{5}$ en degrés :
On a donc
\begin{equation*}
\frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = \sympy{bonne_valeur_theta1}.
\end{equation*}
La mesure de l'angle $\theta_1$ est donc $\sympy{bonne_valeur_theta1}^{\circ}$.
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
theta2_rad = Rational(3, 10) * pi
bonne_valeur_theta2 = (theta2_rad * 180 / pi).simplify()
\end{python}
$\theta_2 :=\frac{3 \pi}{10}$.
}
{
[["CL","\py{bonne_valeur_theta2}"],["0"]]
}
{
Utilisez la relation de conversion : $\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}$.
}
{
La mesure de l'angle $\theta_2$ est $\py{bonne_valeur_theta2}^{\circ}$.
}
{
####  Conversion de $\frac{3\pi}{10}$ en degrés :
On a donc
\begin{equation*}
\frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = \sympy{bonne_valeur_theta2}.
\end{equation*}
La mesure de l'angle $\theta_2$ est donc $\sympy{bonne_valeur_theta2}^{\circ}$.
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
theta3_rad = Rational(5, 12) * pi
bonne_valeur_theta3 = (theta3_rad * 180 / pi).simplify()
\end{python}
$\theta_3 :=\frac{5 \pi}{12}$.
}
{
[["CL","\py{bonne_valeur_theta3}"],["0"]]
}
{
Utilisez la relation de conversion : $\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}$.
}
{
La mesure de l'angle $\theta_3$ est $\py{bonne_valeur_theta3}^{\circ}$.
}
{
####  Conversion de $\frac{5\pi}{12}$ en degrés 

On a donc:
\begin{equation*}
\frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = \sympy{bonne_valeur_theta3}.
\end{equation*}
La mesure de l'angle $\theta_3$ est donc $\sympy{bonne_valeur_theta3}^{\circ}$.
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
theta4_rad = Rational(3, 4) * pi
bonne_valeur_theta4 = (theta4_rad * 180 / pi).simplify()
\end{python}
$\theta_4:=\frac{3 \pi}{4}$
}
{
[["CL","\py{bonne_valeur_theta4}"],["0"]]
}
{
Utilisez la relation de conversion : $\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}$.
}
{
La mesure de l'angle $\theta_4$ est $\py{bonne_valeur_theta4}^{\circ}$.
}
{
#### Conversion de $\frac{3\pi}{4}$ en degrés :

On a donc:
\begin{equation*}
\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = \sympy{bonne_valeur_theta4}.
\end{equation*}
La mesure de l'angle $\theta_4$ est donc $\sympy{bonne_valeur_theta4}^{\circ}$.
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