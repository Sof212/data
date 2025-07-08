```latex
\begin{exercise}{
Id: 8a4b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d
Title_exo: Conversion d'angles radians en degrés
Modules: M1_10_Trigonometry
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Angles
Involved_Concepts: Angles, Radians, Degrés, Conversion
Visibility: All
}
{
Convertir en degrés les mesures d'angle suivantes, exprimées en radians :

\qcl{%Enoncé de la question:
Quelle est la mesure en degrés de l'angle $\theta_1:= \frac{\pi}{5}$ radians ?
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
theta1_rad = pi/5
bonne_valeur = (theta1_rad * 180 / pi)
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice:
Utilisez la relation de conversion entre radians et degrés : $180^\circ = \pi$ radians.
}
{%Solution brève fournie à l'utilisateur:
La mesure de l'angle $\theta_1$ est $\py{bonne_valeur}^\circ$.
}
{%Solution détaillée:
On sait que $180$ degrés correspondent à $\pi$ radians. Par conséquent, pour exprimer en degrés un angle exprimé en radians, on utilise la relation :

\begin{equation*}
\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}
\end{equation*}

#### Conversion de $\frac{\pi}{5}$ en degrés :
On a donc
\begin{equation*}
\frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = \py{bonne_valeur}.
\end{equation*}
La mesure de l'angle $\theta_1$ est donc $\py{bonne_valeur}^{\circ}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Quelle est la mesure en degrés de l'angle $\theta_2 := \frac{3 \pi}{10}$ radians ?
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
theta2_rad = 3*pi/10
bonne_valeur = (theta2_rad * 180 / pi)
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice:
Rappelez-vous que $\pi$ radians équivaut à $180$ degrés.
}
{%Solution brève fournie à l'utilisateur:
La mesure de l'angle $\theta_2$ est $\py{bonne_valeur}^\circ$.
}
{%Solution détaillée:
On sait que $180$ degrés correspondent à $\pi$ radians. Par conséquent, pour exprimer en degrés un angle exprimé en radians, on utilise la relation :

\begin{equation*}
\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}
\end{equation*}

#### Conversion de $\frac{3\pi}{10}$ en degrés :
On a donc
\begin{equation*}
\frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = \py{bonne_valeur}.
\end{equation*}
La mesure de l'angle $\theta_2$ est donc $\py{bonne_valeur}^{\circ}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Quelle est la mesure en degrés de l'angle $\theta_3 := \frac{5 \pi}{12}$ radians ?
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
theta3_rad = 5*pi/12
bonne_valeur = (theta3_rad * 180 / pi)
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice:
La formule de conversion est $\text{degrés} = \text{radians} \times \frac{180}{\pi}$.
}
{%Solution brève fournie à l'utilisateur:
La mesure de l'angle $\theta_3$ est $\py{bonne_valeur}^\circ$.
}
{%Solution détaillée:
On sait que $180$ degrés correspondent à $\pi$ radians. Par conséquent, pour exprimer en degrés un angle exprimé en radians, on utilise la relation :

\begin{equation*}
\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}
\end{equation*}

#### Conversion de $\frac{5\pi}{12}$ en degrés :
On a donc:
\begin{equation*}
\frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = \py{bonne_valeur}.
\end{equation*}
La mesure de l'angle $\theta_3$ est donc $\py{bonne_valeur}^{\circ}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Quelle est la mesure en degrés de l'angle $\theta_4 := \frac{3 \pi}{4}$ radians ?
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
theta4_rad = 3*pi/4
bonne_valeur = (theta4_rad * 180 / pi)
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice:
N'oubliez pas que $\pi$ radians est égal à $180$ degrés.
}
{%Solution brève fournie à l'utilisateur:
La mesure de l'angle $\theta_4$ est $\py{bonne_valeur}^\circ$.
}
{%Solution détaillée:
On sait que $180$ degrés correspondent à $\pi$ radians. Par conséquent, pour exprimer en degrés un angle exprimé en radians, on utilise la relation :

\begin{equation*}
\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}
\end{equation*}

#### Conversion de $\frac{3\pi}{4}$ en degrés :
On a donc:
\begin{equation*}
\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = \py{bonne_valeur}.
\end{equation*}
La mesure de l'angle $\theta_4$ est donc $\py{bonne_valeur}^{\circ}$.
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