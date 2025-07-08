```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Calculs trigonométriques avec $\pi/5$
Modules: M1_10_Trigonometry
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Trigonometry
Involved_Concepts: Trigonometric_Identities, Unit_Circle
Original_source: null
Visibility: All
}
{
\begin{python}
from sympy import *

# Valeur donnée de cos(pi/5)
cos_pi_sur_5 = (1 + sqrt(5))/4

# Calcul de sin(pi/5)
sin_pi_sur_5_squared = 1 - cos_pi_sur_5**2
sin_pi_sur_5 = sqrt(sin_pi_sur_5_squared)
sin_pi_sur_5_latex = latex(sin_pi_sur_5)

# Calcul de sin(4pi/5)
sin_4pi_sur_5 = sin_pi_sur_5
sin_4pi_sur_5_latex = latex(sin_4pi_sur_5)

# Calcul de cos(4pi/5)
cos_4pi_sur_5 = -cos_pi_sur_5
cos_4pi_sur_5_latex = latex(cos_4pi_sur_5)

# Calcul de sin(9pi/5)
sin_9pi_sur_5 = -sin_pi_sur_5
sin_9pi_sur_5_latex = latex(sin_9pi_sur_5)

# Calcul de cos(9pi/5)
cos_9pi_sur_5 = cos_pi_sur_5
cos_9pi_sur_5_latex = latex(cos_9pi_sur_5)
\end{python}

On donne $\cos \left(\frac{\pi}{5}\right)=\frac{1+\sqrt{5}}{4}$.

\qcl{Calculer la valeur exacte de $\sin \left(\frac{\pi}{5}\right)$.}
{
[["CL","\py{sin_pi_sur_5_latex}"],["0"]]
}
{}
{
$\sin \left(\frac{\pi}{5}\right) = \py{sin_pi_sur_5_latex}$
}
{
Nous savons que pour n'importe quel angle, noté $\theta$, on a l'égalité:  
\begin{equation}
\label{okko}
\sin^2(\theta) + \cos^2(\theta) = 1 
\end{equation}
Dans notre cas, nous avons $\theta = \frac{\pi}{5}$ et nous savons que 
$\cos\left(\frac{\pi}{5}\right) = \frac{1 + \sqrt{5}}{4} $.  En appliquant [](#okko) 
à l'angle $\pi/5$, on peut écrire:

\begin{equation*}
\begin{align*}
\sin^2\left(\frac{\pi}{5}\right) 
&=
 1 - \cos^2\left(\frac{\pi}{5}\right) \\
&=
1- \left(\frac{1 + \sqrt{5}}{4}\right)^2
=
1- \frac{(1 + \sqrt{5})^2}{16} 
=
1- \frac{1 + 2\sqrt{5} + 5}{16} \\
&=
1-\frac{6 + 2\sqrt{5}}{16} 
=
1-\frac{3 + \sqrt{5}}{8} 
=
\frac{8-3 - \sqrt{5}}{8} \\
&=
\frac{5 - \sqrt{5}}{8}. 
\end{align*}
\end{equation*}
Puisque $5 - \sqrt{5}>0$, nous pouvons prendre la racine carrée de 
$\frac{5 - \sqrt{5}}{8}$. Cette dernière vaut $\frac{\sqrt{5 - \sqrt{5}}}{\sqrt{8}}$ soit encore 
$\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$. On a donc:

\begin{equation*}
\begin{align*}
\sin\left(\frac{\pi}{5}\right) 
=
\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}
Nous savons donc que $\sin\left(\frac{\pi}{5}\right)$ vaut soit $-\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$ soit
$\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$. Puisque l'angle $\frac{\pi}{5}$ est dans
 le premier quadrant du cercle trigonométrique, nous savons que 
 $\sin\left(\frac{\pi}{5}\right) >0$.	La seule possibilité est donc:
\begin{equation*}
\begin{align*}
\sin\left(\frac{\pi}{5}\right) 
=
\py{sin_pi_sur_5_latex}.
\end{align*}
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la valeur exacte de $\sin \left(\frac{4\pi}{5}\right)$.}
{
[["CL","\py{sin_4pi_sur_5_latex}"],["0"]]
}
{}
{
$\sin \left(\frac{4\pi}{5}\right) = \py{sin_4pi_sur_5_latex}$
}
{
De l'égalité $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, on déduit que l'on peut écrire:
 \begin{equation}
\label{dzoeidjez}
\begin{align*}
\sin\left(\frac{4\pi}{5}\right) 
=
\sin\left(\pi - \frac{\pi}{5}\right) 
\end{align*}
\end{equation}
Et puisque $\sin(\pi - x) = \sin  x $, pour tout réel $x$, on peut repartir de
 [](#dzoeidjez) pour écrire:
 \begin{equation*}
\begin{align*}
\sin\left(\frac{4\pi}{5}\right) 
=
\sin\left(\pi - \frac{\pi}{5}\right) 
=
\sin\left( \frac{\pi}{5} \right)
=
\py{sin_4pi_sur_5_latex}.
\end{align*}
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la valeur exacte de $\cos \left(\frac{4\pi}{5}\right)$.}
{
[["CL","\py{cos_4pi_sur_5_latex}"],["0"]]
}
{}
{
$\cos \left(\frac{4\pi}{5}\right) = \py{cos_4pi_sur_5_latex}$
}
{
De même pour le cosinus. On repart de l'égalité $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, 
et on écrit:
%
 \begin{equation}
\label{dzoeidjezss}
\begin{align*}
\cos\left(\frac{4\pi}{5}\right) 
=
\cos\left(\pi - \frac{\pi}{5}\right) 
\end{align*}
\end{equation}
Et puisque $\cos(\pi - x) = -\cos  x $, pour tout réel $x$, on peut repartir de
 [](#dzoeidjezss) pour écrire:
 \begin{equation*}
\begin{align*}
\cos\left(\frac{4\pi}{5}\right) 
=
\cos\left(\pi - \frac{\pi}{5}\right) 
=
-\cos\left( \frac{\pi}{5} \right)
=
\py{cos_4pi_sur_5_latex}.
\end{align*}
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la valeur exacte de $\sin \left(\frac{9\pi}{5}\right)$.}
{
[["CL","\py{sin_9pi_sur_5_latex}"],["0"]]
}
{}
{
$\sin \left(\frac{9\pi}{5}\right) = \py{sin_9pi_sur_5_latex}$
}
{
De l'égalité $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$, on déduit que l'on peut écrire:
 \begin{equation}
\label{dzoeidjezdezedz}
\begin{align*}
\sin\left(\frac{9\pi}{5}\right) 
=
\sin\left(2\pi - \frac{\pi}{5}\right) 
\end{align*}
\end{equation}
Et puisque $\sin(2\pi - x) = \sin (-x) =-\sin x $, pour tout réel $x$, on peut repartir de
 [](#dzoeidjezdezedz) pour écrire:
 \begin{equation*}
\begin{align*}
\sin\left(\frac{9\pi}{5}\right) 
=
\sin\left(-\frac{\pi}{5}\right) 
=
-\sin\left(\frac{\pi}{5} \right)
=
\py{sin_9pi_sur_5_latex}.
\end{align*}
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la valeur exacte de $\cos \left(\frac{9\pi}{5}\right)$.}
{
[["CL","\py{cos_9pi_sur_5_latex}"],["0"]]
}
{}
{
$\cos \left(\frac{9\pi}{5}\right) = \py{cos_9pi_sur_5_latex}$
}
{
De même pour le cosinus. On repart de l'égalité $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$, 
et on écrit:
%
 \begin{equation}
\label{dzoeidjezssdzedez}
\begin{align*}
\cos\left(\frac{9\pi}{5}\right) 
=
\cos\left(2\pi - \frac{\pi}{5}\right) 
\end{align*}
\end{equation}
Et puisque $\cos(2\pi - x) = \cos (-x) =  \cos x  $, pour tout réel $x$, on peut repartir de
 [](#dzoeidjezssdzedez) pour écrire:
 \begin{equation*}
\begin{align*}
\cos\left(\frac{9\pi}{5}\right) 
=
\cos\left(-\frac{\pi}{5}\right) 
=
\cos\left(\frac{\pi}{5}\right) 
=
\py{cos_9pi_sur_5_latex}.
\end{align*}
\end{equation*}
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