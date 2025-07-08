```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Trigonométrie exacte
Modules: Trigonométrie
Recommended_execution_time: 15
Ex_Level: Intermediary
Chap: Angles remarquables
Involved_Concepts: Identités trigonométriques, Angles associés
Original_source: Exercice original
Visibility: All
}
{
\qcl{
\begin{python}
from sympy import *
# Valeur donnée
cos_pi5 = (1 + sqrt(5))/4
# Calcul de sin(pi/5)
sin_pi5_val = sqrt(1 - cos_pi5**2)
sin_pi5_simplified = simplify(sin_pi5_val)
\end{python}
On donne $\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$. Calculer la valeur exacte de $\sin\left(\frac{\pi}{5}\right)$.
}
{
[["CL","\py{sin_pi5_simplified}"],["0"]]
}
{
Utiliser l'identité fondamentale $\sin^2(x) + \cos^2(x) = 1$.
}
{
La réponse est $\py{sin_pi5_simplified}$
}
{
Nous savons que pour tout angle $\theta$, on a $\sin^2(\theta) + \cos^2(\theta) = 1$.

Avec $\theta = \frac{\pi}{5}$ et $\cos\left(\frac{\pi}{5}\right) = \frac{1 + \sqrt{5}}{4}$, on a:

\[
\sin^2\left(\frac{\pi}{5}\right) = 1 - \left(\frac{1 + \sqrt{5}}{4}\right)^2 = 1 - \frac{1 + 2\sqrt{5} + 5}{16} = 1 - \frac{6 + 2\sqrt{5}}{16} = \frac{16 - (6 + 2\sqrt{5})}{16} = \frac{10 - 2\sqrt{5}}{16} = \frac{5 - \sqrt{5}}{8}
\]

Comme $\frac{\pi}{5}$ est dans le premier quadrant (entre $0$ et $\frac{\pi}{2}$), $\sin\left(\frac{\pi}{5}\right)$ est positif. On prend la racine positive:
\[
\sin\left(\frac{\pi}{5}\right) = \sqrt{\frac{5 - \sqrt{5}}{8}} = \frac{\sqrt{5 - \sqrt{5}}}{\sqrt{8}} = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}
\]
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
# Valeur donnée
cos_pi5 = (1 + sqrt(5))/4
# Calcul pour 4pi/5
cos_4pi5 = -cos_pi5
\end{python}
Calculer la valeur exacte de $\cos\left(\frac{4\pi}{5}\right)$.
}
{
[["CL","\py{cos_4pi5}"],["0"]]
}
{
Utiliser la relation $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$ et la formule $\cos(\pi - x) = -\cos(x)$.
}
{
La réponse est $\py{cos_4pi5}$
}
{
On utilise l'angle associé:
\[
\frac{4\pi}{5} = \pi - \frac{\pi}{5}
\]
Donc:
\[
\cos\left(\frac{4\pi}{5}\right) = \cos\left(\pi - \frac{\pi}{5}\right) = -\cos\left(\frac{\pi}{5}\right) = -\frac{1+\sqrt{5}}{4}
\]
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
# Valeur donnée
cos_pi5 = (1 + sqrt(5))/4
sin_pi5_val = sqrt(1 - cos_pi5**2)
sin_pi5_simplified = simplify(sin_pi5_val)
# Calcul pour 4pi/5
sin_4pi5 = sin_pi5_simplified
\end{python}
Calculer la valeur exacte de $\sin\left(\frac{4\pi}{5}\right)$.
}
{
[["CL","\py{sin_4pi5}"],["0"]]
}
{
Utiliser la relation $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$ et la formule $\sin(\pi - x) = \sin(x)$.
}
{
La réponse est $\py{sin_4pi5}$
}
{
On utilise l'angle associé:
\[
\frac{4\pi}{5} = \pi - \frac{\pi}{5}
\]
Donc:
\[
\sin\left(\frac{4\pi}{5}\right) = \sin\left(\pi - \frac{\pi}{5}\right) = \sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}
\]
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
# Valeur donnée
cos_pi5 = (1 + sqrt(5))/4
# Calcul pour 9pi/5
cos_9pi5 = cos_pi5
\end{python}
Calculer la valeur exacte de $\cos\left(\frac{9\pi}{5}\right)$.
}
{
[["CL","\py{cos_9pi5}"],["0"]]
}
{
Utiliser la relation $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$ et la formule $\cos(2\pi - x) = \cos(x)$.
}
{
La réponse est $\py{cos_9pi5}$
}
{
On utilise l'angle associé:
\[
\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}
\]
Donc:
\[
\cos\left(\frac{9\pi}{5}\right) = \cos\left(2\pi - \frac{\pi}{5}\right) = \cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}
\]
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
# Valeur donnée
cos_pi5 = (1 + sqrt(5))/4
sin_pi5_val = sqrt(1 - cos_pi5**2)
sin_pi5_simplified = simplify(sin_pi5_val)
# Calcul pour 9pi/5
sin_9pi5 = -sin_pi5_simplified
\end{python}
Calculer la valeur exacte de $\sin\left(\frac{9\pi}{5}\right)$.
}
{
[["CL","\py{sin_9pi5}"],["0"]]
}
{
Utiliser la relation $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$ et la formule $\sin(2\pi - x) = -\sin(x)$.
}
{
La réponse est $\py{sin_9pi5}$
}
{
On utilise l'angle associé:
\[
\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}
\]
Donc:
\[
\sin\left(\frac{9\pi}{5}\right) = \sin\left(2\pi - \frac{\pi}{5}\right) = -\sin\left(\frac{\pi}{5}\right) = -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}
\]
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