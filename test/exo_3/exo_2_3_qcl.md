```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Conversion radians-degrés
Modules: Trigonométrie
Recommended_execution_time: 5
Ex_Level: Elementary
Chap: Angles
Involved_Concepts: Conversion d'unités
}
{
Convertir en degrés les mesures d'angle suivantes, exprimées en radians :

\qcl{
\begin{python}
from sympy import pi
# Variables et calculs de la réponse exacte
theta1 = pi/5
bonne_valeur = (theta1 * 180/pi).simplify()
\end{python}
Convertir $\theta_1 = \frac{\pi}{5}$ radians en degrés.
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Utiliser la relation : $1 \text{ rad} = \frac{180}{\pi} \text{ degrés}$
}
{
La réponse est \py{bonne_valeur}$^\circ$
}
{
On sait que $180$ degrés correspondent à $\pi$ radians. Par conséquent, pour exprimer en degrés un angle exprimé en radians, on utilise la relation :

\begin{equation*}
\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}
\end{equation*}

#### Conversion de $\frac{\pi}{5}$ en degrés :
On a donc
\begin{equation*}
\frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = 36.
\end{equation*}
La mesure de l'angle $\theta_1$ est donc $36^{\circ}$.
}
{
logic: 20
abstraction: 20
reasoning: 30
calculation: 30
}

\qcl{
\begin{python}
from sympy import pi
# Variables et calculs de la réponse exacte
theta2 = 3*pi/10
bonne_valeur = (theta2 * 180/pi).simplify()
\end{python}
Convertir $\theta_2 = \frac{3\pi}{10}$ radians en degrés.
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Utiliser la relation : $1 \text{ rad} = \frac{180}{\pi} \text{ degrés}$
}
{
La réponse est \py{bonne_valeur}$^\circ$
}
{
#### Conversion de $\frac{3\pi}{10}$ en degrés :
On a donc
\begin{equation*}
\frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = 54.
\end{equation*}
La mesure de l'angle $\theta_2$ est donc $54^{\circ}$.
}
{
logic: 20
abstraction: 20
reasoning: 30
calculation: 30
}

\qcl{
\begin{python}
from sympy import pi
# Variables et calculs de la réponse exacte
theta3 = 5*pi/12 
bonne_valeur = (theta3 * 180/pi).simplify()
\end{python}
Convertir $\theta_3 = \frac{5\pi}{12}$ radians en degrés.
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Utiliser la relation : $1 \text{ rad} = \frac{180}{\pi} \text{ degrés}$
}
{
La réponse est \py{bonne_valeur}$^\circ$
}
{
#### Conversion de $\frac{5\pi}{12}$ en degrés :
On a donc:
\begin{equation*}
\frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = 75.
\end{equation*}
La mesure de l'angle $\theta_3$ est donc $75^{\circ}$.
}
{
logic: 20
abstraction: 20
reasoning: 30
calculation: 30
}

\qcl{
\begin{python}
from sympy import pi
# Variables et calculs de la réponse exacte
theta4 = 3*pi/4
bonne_valeur = (theta4 * 180/pi).simplify()
\end{python}
Convertir $\theta_4 = \frac{3\pi}{4}$ radians en degrés.
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
Utiliser la relation : $1 \text{ rad} = \frac{180}{\pi} \text{ degrés}$
}
{
La réponse est \py{bonne_valeur}$^\circ$
}
{
#### Conversion de $\frac{3\pi}{4}$ en degrés :
On a donc:
\begin{equation*}
\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = 135.
\end{equation*}
La mesure de l'angle $\theta_4$ est donc $135^{\circ}$.
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