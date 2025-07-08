```latex
\begin{exercise}{
Title_exo: \fr{Calcul de valeurs trigonométriques exactes}\en{Calculation of exact trigonometric values}
Modules: Trigonométrie
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Relations_trigonometriques
Involved_Concepts: sin, cos, identite_trigonometrique, angles_associes
Original_source:
Visibility: All
}
{
% Contenu de l'exercice
On donne $\cos \left(\frac{\pi}{5}\right)=\frac{1+\sqrt{5}}{4}$.

\begin{python}
from sympy import *
# === Calcul bonne réponse ===
cos_pi_sur_5 = Rational(1 + sqrt(5), 4)
sin_pi_sur_5_val = sqrt(1 - cos_pi_sur_5**2)
bonne_valeur = sin_pi_sur_5_val
bonne_valeur_latex = latex(bonne_valeur, fold_frac_powers=True)

# === Propositions fausses calculées ===
fausse_1 = sqrt(1 + cos_pi_sur_5**2) # Erreur de signe dans l'identité
fausse_1_latex = latex(fausse_1, fold_frac_powers=True)

fausse_2 = sqrt(1 - cos_pi_sur_5**2) / 2 # Oubli du 2 au dénominateur
fausse_2_latex = latex(fausse_2, fold_frac_powers=True)

fausse_3 = cos_pi_sur_5 # Confusion sin et cos
fausse_3_latex = latex(fausse_3, fold_frac_powers=True)
\end{python}
\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Calculer la valeur exacte de $\sin \left(\frac{\pi}{5}\right)$.
}
{
\right{$\displaystyle \mathbf{latex(bonne_valeur_latex)}$}
\wrong{$\displaystyle \mathbf{latex(fausse_1_latex)}$}
\wrong{$\displaystyle \mathbf{latex(fausse_2_latex)}$}
\wrong{$\displaystyle \mathbf{latex(fausse_3_latex)}$}
\wronger
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

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
\sin^2\left(\frac{\pi}{5}\right)
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
\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}

}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# Valeurs de la question précédente
cos_pi_sur_5 = Rational(1 + sqrt(5), 4)
sin_pi_sur_5 = sqrt(Rational(5 - sqrt(5), 8))

# === Calcul bonne réponse ===
sin_4pi_sur_5 = sin_pi_sur_5
cos_4pi_sur_5 = -cos_pi_sur_5

sin_4pi_sur_5_latex = latex(sin_4pi_sur_5, fold_frac_powers=True)
cos_4pi_sur_5_latex = latex(cos_4pi_sur_5, fold_frac_powers=True)

# === Propositions fausses calculées ===
fausse_1_sin = sqrt(Rational(5 + sqrt(5), 8)) # Erreur de signe dans le radical
fausse_1_sin_latex = latex(fausse_1_sin, fold_frac_powers=True)

fausse_2_cos = cos_pi_sur_5 # Erreur de signe pour le cosinus
fausse_2_cos_latex = latex(fausse_2_cos, fold_frac_powers=True)

fausse_3_sin = -sin_pi_sur_5 # Erreur de signe pour le sinus
fausse_3_sin_latex = latex(fausse_3_sin, fold_frac_powers=True)
\end{python}
\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
 En déduire les valeurs exactes du sinus et du cosinus de $\frac{4 \pi}{5}$
}
{
\right{$\sin\left(\frac{4\pi}{5}\right) = \mathbf{latex(sin_4pi_sur_5_latex)}$ et $\cos\left(\frac{4\pi}{5}\right) = \mathbf{latex(cos_4pi_sur_5_latex)}$}
\wrong{$\sin\left(\frac{4\pi}{5}\right) = \mathbf{latex(fausse_1_sin_latex)}$ et $\cos\left(\frac{4\pi}{5}\right) = \mathbf{latex(cos_4pi_sur_5_latex)}$}
\wrong{$\sin\left(\frac{4\pi}{5}\right) = \mathbf{latex(sin_4pi_sur_5_latex)}$ et $\cos\left(\frac{4\pi}{5}\right) = \mathbf{latex(fausse_2_cos_latex)}$}
\wrong{$\sin\left(\frac{4\pi}{5}\right) = \mathbf{latex(fausse_3_sin_latex)}$ et $\cos\left(\frac{4\pi}{5}\right) = \mathbf{latex(cos_4pi_sur_5_latex)}$}
\wrong{$\sin\left(\frac{4\pi}{5}\right) = \mathbf{latex(fausse_3_sin_latex)}$ et $\cos\left(\frac{4\pi}{5}\right) = \mathbf{latex(fausse_2_cos_latex)}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
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
\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}
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
-\frac{1+\sqrt{5}}{4}.
\end{align*}
\end{equation*}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# Valeurs de la question précédente
cos_pi_sur_5 = Rational(1 + sqrt(5), 4)
sin_pi_sur_5 = sqrt(Rational(5 - sqrt(5), 8))

# === Calcul bonne réponse ===
sin_9pi_sur_5 = -sin_pi_sur_5
cos_9pi_sur_5 = cos_pi_sur_5

sin_9pi_sur_5_latex = latex(sin_9pi_sur_5, fold_frac_powers=True)
cos_9pi_sur_5_latex = latex(cos_9pi_sur_5, fold_frac_powers=True)

# === Propositions fausses calculées ===
fausse_1_sin = sin_pi_sur_5 # Erreur de signe pour le sinus
fausse_1_sin_latex = latex(fausse_1_sin, fold_frac_powers=True)

fausse_2_cos = -cos_pi_sur_5 # Erreur de signe pour le cosinus
fausse_2_cos_latex = latex(fausse_2_cos, fold_frac_powers=True)

fausse_3_sin = -sqrt(Rational(5 + sqrt(5), 8)) # Erreur de signe dans le radical et pour le sinus
fausse_3_sin_latex = latex(fausse_3_sin, fold_frac_powers=True)
\end{python}
\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
En déduire les valeurs exactes du sinus et du cosinus de  $\frac{9 \pi}{5}$
}
{
\right{$\sin\left(\frac{9\pi}{5}\right) = \mathbf{latex(sin_9pi_sur_5_latex)}$ et $\cos\left(\frac{9\pi}{5}\right) = \mathbf{latex(cos_9pi_sur_5_latex)}$}
\wrong{$\sin\left(\frac{9\pi}{5}\right) = \mathbf{latex(fausse_1_sin_latex)}$ et $\cos\left(\frac{9\pi}{5}\right) = \mathbf{latex(cos_9pi_sur_5_latex)}$}
\wrong{$\sin\left(\frac{9\pi}{5}\right) = \mathbf{latex(sin_9pi_sur_5_latex)}$ et $\cos\left(\frac{9\pi}{5}\right) = \mathbf{latex(fausse_2_cos_latex)}$}
\wrong{$\sin\left(\frac{9\pi}{5}\right) = \mathbf{latex(fausse_3_sin_latex)}$ et $\cos\left(\frac{9\pi}{5}\right) = \mathbf{latex(cos_9pi_sur_5_latex)}$}
\wrong{$\sin\left(\frac{9\pi}{5}\right) = \mathbf{latex(fausse_3_sin_latex)}$ et $\cos\left(\frac{9\pi}{5}\right) = \mathbf{latex(fausse_2_cos_latex)}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.


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
-\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}
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
\frac{1+\sqrt{5}}{4}.
\end{align*}
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