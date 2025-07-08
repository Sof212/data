```latex
\begin{exercise}{
Title_exo: \fr{Calcul de valeurs trigonométriques exactes}\en{Calculation of exact trigonometric values}
Modules: Trigonometry
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Trigonometric_Functions
Involved_Concepts: Trigonometric_identities, Unit_circle
Original_source:
Visibility: All
Comment: Conversion d'un exercice QST en QCM, décliné en plusieurs questions pour chaque calcul demandé.
}
{ % Contenu de l'exercice

On donne $\cos \left(\frac{\pi}{5}\right)=\frac{1+\sqrt{5}}{4}$.

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
cos_pi_sur_5 = (1 + sqrt(5)) / 4
sin_pi_sur_5_squared = 1 - cos_pi_sur_5**2
bonne_valeur = sqrt(sin_pi_sur_5_squared)
bonne_valeur_latex = latex(bonne_valeur)
# === Propositions fausses calculées ===
fausse_1 = -bonne_valeur  # Erreur méthodologique typique (signe)
fausse_2 = sqrt(Rational(5 + sqrt(5), 8))  # Variante calcul incorrecte (signe dans le numérateur)
fausse_3 = sqrt(Rational(5 - sqrt(5), 4))  # Approximation erronée (dénominateur incorrect)
\end{python}
\qcm{ % Enoncé de la question:
\fr{Calculer la valeur exacte de $\sin \left(\frac{\pi}{5}\right)$.}
\en{Calculate the exact value of $\sin \left(\frac{\pi}{5}\right)$.}
}
{
\right{$\py{bonne_valeur_latex}$}
\wrong{$\py{latex(fausse_1)}$}
\wrong{$\py{latex(fausse_2)}$}
\wrong{$\py{latex(fausse_3)}$}
}
{ % Indice:
\fr{Utilisez l'identité fondamentale de la trigonométrie : $\sin^2(\theta) + \cos^2(\theta) = 1$.}
\en{Use the fundamental trigonometric identity: $\sin^2(\theta) + \cos^2(\theta) = 1$.}
}
{ % Solution détaillée:
\fr{Nous savons que pour n'importe quel angle, noté $\theta$, on a l'égalité:
\begin{equation*}
\sin^2(\theta) + \cos^2(\theta) = 1
\end{equation*}
Dans notre cas, nous avons $\theta = \frac{\pi}{5}$ et nous savons que
$\cos\left(\frac{\pi}{5}\right) = \frac{1 + \sqrt{5}}{4} $. En appliquant cette identité
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
Puisque $\frac{\pi}{5}$ est dans le premier quadrant du cercle trigonométrique, $\sin\left(\frac{\pi}{5}\right) > 0$.
La seule possibilité est donc:
\begin{equation*}
\begin{align*}
\sin\left(\frac{\pi}{5}\right)
=
\sqrt{\frac{5 - \sqrt{5}}{8}}
=
\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}
=
\frac{\sqrt{10 - 2\sqrt{5}}}{4}.
\end{align*}
\end{equation*}
}
\en{We know that for any angle, denoted $\theta$, we have the equality:
\begin{equation*}
\sin^2(\theta) + \cos^2(\theta) = 1
\end{equation*}
In our case, we have $\theta = \frac{\pi}{5}$ and we know that
$\cos\left(\frac{\pi}{5}\right) = \frac{1 + \sqrt{5}}{4} $. Applying this identity
to the angle $\pi/5$, we can write:

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
Since $\frac{\pi}{5}$ is in the first quadrant of the trigonometric circle, $\sin\left(\frac{\pi}{5}\right) > 0$.
The only possibility is therefore:
\begin{equation*}
\begin{align*}
\sin\left(\frac{\pi}{5}\right)
=
\sqrt{\frac{5 - \sqrt{5}}{8}}
=
\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}
=
\frac{\sqrt{10 - 2\sqrt{5}}}{4}.
\end{align*}
\end{equation*}
}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
cos_pi_sur_5 = (1 + sqrt(5)) / 4
sin_pi_sur_5 = sqrt(Rational(5 - sqrt(5), 8))
bonne_valeur = sin_pi_sur_5
bonne_valeur_latex = latex(bonne_valeur)
# === Propositions fausses calculées ===
fausse_1 = -bonne_valeur # Erreur de signe
fausse_2 = cos_pi_sur_5 # Confusion sin/cos
fausse_3 = -cos_pi_sur_5 # Confusion sin/cos et erreur de signe
\end{python}
\qcm{ % Enoncé de la question:
\fr{En déduire la valeur exacte de $\sin \left(\frac{4 \pi}{5}\right)$.}
\en{Deduce the exact value of $\sin \left(\frac{4 \pi}{5}\right)$.}
}
{
\right{$\py{bonne_valeur_latex}$}
\wrong{$\py{latex(fausse_1)}$}
\wrong{$\py{latex(fausse_2)}$}
\wrong{$\py{latex(fausse_3)}$}
}
{ % Indice:
\fr{Utilisez la relation $\sin(\pi - x) = \sin(x)$.}
\en{Use the relation $\sin(\pi - x) = \sin(x)$.}
}
{ % Solution détaillée:
\fr{De l'égalité $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, on déduit que l'on peut écrire:
\begin{equation*}
\sin\left(\frac{4\pi}{5}\right)
=
\sin\left(\pi - \frac{\pi}{5}\right)
\end{equation*}
Et puisque $\sin(\pi - x) = \sin(x)$, pour tout réel $x$, on peut écrire:
\begin{equation*}
\begin{align*}
\sin\left(\frac{4\pi}{5}\right)
=
\sin\left( \frac{\pi}{5} \right)
=
\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}
}
\en{From the equality $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, we deduce that we can write:
\begin{equation*}
\sin\left(\frac{4\pi}{5}\right)
=
\sin\left(\pi - \frac{\pi}{5}\right)
\end{equation*}
And since $\sin(\pi - x) = \sin(x)$, for any real $x$, we can write:
\begin{equation*}
\begin{align*}
\sin\left(\frac{4\pi}{5}\right)
=
\sin\left( \frac{\pi}{5} \right)
=
\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}
}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
cos_pi_sur_5 = (1 + sqrt(5)) / 4
sin_pi_sur_5 = sqrt(Rational(5 - sqrt(5), 8))
bonne_valeur = -cos_pi_sur_5
bonne_valeur_latex = latex(bonne_valeur)
# === Propositions fausses calculées ===
fausse_1 = cos_pi_sur_5 # Erreur de signe
fausse_2 = sin_pi_sur_5 # Confusion sin/cos
fausse_3 = -sin_pi_sur_5 # Confusion sin/cos et erreur de signe
\end{python}
\qcm{ % Enoncé de la question:
\fr{En déduire la valeur exacte de $\cos \left(\frac{4 \pi}{5}\right)$.}
\en{Deduce the exact value of $\cos \left(\frac{4 \pi}{5}\right)$.}
}
{
\right{$\py{bonne_valeur_latex}$}
\wrong{$\py{latex(fausse_1)}$}
\wrong{$\py{latex(fausse_2)}$}
\wrong{$\py{latex(fausse_3)}$}
}
{ % Indice:
\fr{Utilisez la relation $\cos(\pi - x) = -\cos(x)$.}
\en{Use the relation $\cos(\pi - x) = -\cos(x)$.}
}
{ % Solution détaillée:
\fr{De l'égalité $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, on déduit que l'on peut écrire:
\begin{equation*}
\cos\left(\frac{4\pi}{5}\right)
=
\cos\left(\pi - \frac{\pi}{5}\right)
\end{equation*}
Et puisque $\cos(\pi - x) = -\cos(x)$, pour tout réel $x$, on peut écrire:
\begin{equation*}
\begin{align*}
\cos\left(\frac{4\pi}{5}\right)
=
-\cos\left( \frac{\pi}{5} \right)
=
-\frac{1+\sqrt{5}}{4}.
\end{align*}
\end{equation*}
}
\en{From the equality $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, we deduce that we can write:
\begin{equation*}
\cos\left(\frac{4\pi}{5}\right)
=
\cos\left(\pi - \frac{\pi}{5}\right)
\end{equation*}
And since $\cos(\pi - x) = -\cos(x)$, for any real $x$, we can write:
\begin{equation*}
\begin{align*}
\cos\left(\frac{4\pi}{5}\right)
=
-\cos\left( \frac{\pi}{5} \right)
=
-\frac{1+\sqrt{5}}{4}.
\end{align*}
\end{equation*}
}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
cos_pi_sur_5 = (1 + sqrt(5)) / 4
sin_pi_sur_5 = sqrt(Rational(5 - sqrt(5), 8))
bonne_valeur = -sin_pi_sur_5
bonne_valeur_latex = latex(bonne_valeur)
# === Propositions fausses calculées ===
fausse_1 = sin_pi_sur_5 # Erreur de signe
fausse_2 = cos_pi_sur_5 # Confusion sin/cos
fausse_3 = -cos_pi_sur_5 # Confusion sin/cos et erreur de signe
\end{python}
\qcm{ % Enoncé de la question:
\fr{En déduire la valeur exacte de $\sin \left(\frac{9 \pi}{5}\right)$.}
\en{Deduce the exact value of $\sin \left(\frac{9 \pi}{5}\right)$.}
}
{
\right{$\py{bonne_valeur_latex}$}
\wrong{$\py{latex(fausse_1)}$}
\wrong{$\py{latex(fausse_2)}$}
\wrong{$\py{latex(fausse_3)}$}
}
{ % Indice:
\fr{Utilisez la relation $\sin(2\pi - x) = -\sin(x)$.}
\en{Use the relation $\sin(2\pi - x) = -\sin(x)$.}
}
{ % Solution détaillée:
\fr{De l'égalité $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$, on déduit que l'on peut écrire:
\begin{equation*}
\sin\left(\frac{9\pi}{5}\right)
=
\sin\left(2\pi - \frac{\pi}{5}\right)
\end{equation*}
Et puisque $\sin(2\pi - x) = -\sin(x)$, pour tout réel $x$, on peut écrire:
\begin{equation*}
\begin{align*}
\sin\left(\frac{9\pi}{5}\right)
=
-\sin\left(\frac{\pi}{5} \right)
=
-\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}
}
\en{From the equality $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$, we deduce that we can write:
\begin{equation*}
\sin\left(\frac{9\pi}{5}\right)
=
\sin\left(2\pi - \frac{\pi}{5}\right)
\end{equation*}
And since $\sin(2\pi - x) = -\sin(x)$, for any real $x$, we can write:
\begin{equation*}
\begin{align*}
\sin\left(\frac{9\pi}{5}\right)
=
-\sin\left(\frac{\pi}{5} \right)
=
-\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}
}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
cos_pi_sur_5 = (1 + sqrt(5)) / 4
sin_pi_sur_5 = sqrt(Rational(5 - sqrt(5), 8))
bonne_valeur = cos_pi_sur_5
bonne_valeur_latex = latex(bonne_valeur)
# === Propositions fausses calculées ===
fausse_1 = -cos_pi_sur_5 # Erreur de signe
fausse_2 = sin_pi_sur_5 # Confusion sin/cos
fausse_3 = -sin_pi_sur_5 # Confusion sin/cos et erreur de signe
\end{python}
\qcm{ % Enoncé de la question:
\fr{En déduire la valeur exacte de $\cos \left(\frac{9 \pi}{5}\right)$.}
\en{Deduce the exact value of $\cos \left(\frac{9 \pi}{5}\right)$.}
}
{
\right{$\py{bonne_valeur_latex}$}
\wrong{$\py{latex(fausse_1)}$}
\wrong{$\py{latex(fausse_2)}$}
\wrong{$\py{latex(fausse_3)}$}
}
{ % Indice:
\fr{Utilisez la relation $\cos(2\pi - x) = \cos(x)$.}
\en{Use the relation $\cos(2\pi - x) = \cos(x)$.}
}
{ % Solution détaillée:
\fr{De l'égalité $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$, on déduit que l'on peut écrire:
\begin{equation*}
\cos\left(\frac{9\pi}{5}\right)
=
\cos\left(2\pi - \frac{\pi}{5}\right)
\end{equation*}
Et puisque $\cos(2\pi - x) = \cos(x)$, pour tout réel $x$, on peut écrire:
\begin{equation*}
\begin{align*}
\cos\left(\frac{9\pi}{5}\right)
=
\cos\left(\frac{\pi}{5}\right)
=
\frac{1+\sqrt{5}}{4}.
\end{align*}
\end{equation*}
}
\en{From the equality $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$, we deduce that we can write:
\begin{equation*}
\cos\left(\frac{9\pi}{5}\right)
=
\cos\left(2\pi - \frac{\pi}{5}\right)
\end{equation*}
And since $\cos(2\pi - x) = \cos(x)$, for any real $x$, we can write:
\begin{equation*}
\begin{align*}
\cos\left(\frac{9\pi}{5}\right)
=
\cos\left(\frac{\pi}{5}\right)
=
\frac{1+\sqrt{5}}{4}.
\end{align*}
\end{equation*}
}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

}
\end{exercise}
```