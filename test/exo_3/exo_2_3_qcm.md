```latex
\begin{exercise}{
Title_exo: \fr{Conversion radians-degrés}\en{Radians-Degrees Conversion}
Modules: Trigonométrie % NameID des modules
Recommended_execution_time: 8 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Angles et trigonométrie % NameID des chapitres
Involved_Concepts: Conversion d'angles, Radians, Degrés % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: Teacher % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Exercice de conversion d'angles radians-degrés. % Comment: % Commentaire de l'exercice (optionnel)
}
{
(quest1)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Rational(180, 5)
# === Propositions fausses calculées ===
fausse_1 = Rational(180, pi) / 5  # Oubli de multiplier par pi au dénominateur
fausse_2 = pi / 5  # Oubli de conversion
fausse_3 = Rational(180, 10)  # Erreur de calcul
\end{python}
\qcm{ \fr{
Convertir en degrés la mesure d'angle suivante exprimée en radians :
$\theta_1 = \frac{\pi}{5}$
}\en{
Convert the following angle measure from radians to degrees:
$\theta_1 = \frac{\pi}{5}$
}
}
{
\right{$\displaystyle \sympy{bonne_valeur}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_1}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_2}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_3}^{\circ}$}
\wronger
\righter
}
{%% Solution détaillée : \fr{On sait que $180^{\circ} = \pi$ radians. La conversion se fait par :
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}\en{We know that $180^{\circ} = \pi$ radians. The conversion is done by:
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}
}
{
\fr{$\frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = 36^{\circ}$}\en{$\frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = 36^{\circ}$}
}
{ % Répartition des poids (Total = 100)
reasoning: 20
logic: 20
abstraction: 30
calculation: 30
}

(quest2)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Rational(3 * 180, 10)
# === Propositions fausses calculées ===
fausse_1 = Rational(3 * 180, pi) / 10 # Oubli de multiplier par pi au dénominateur
fausse_2 = Rational(3 * pi, 10) # Oubli de conversion
fausse_3 = Rational(180, 3) # Erreur de calcul
\end{python}
\qcm{ \fr{
Convertir en degrés la mesure d'angle suivante exprimée en radians :
$\theta_2 = \frac{3\pi}{10}$
}\en{
Convert the following angle measure from radians to degrees:
$\theta_2 = \frac{3\pi}{10}$
}
}
{
\right{$\displaystyle \sympy{bonne_valeur}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_1}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_2}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_3}^{\circ}$}
\wronger
\righter
}
{%% Solution détaillée : \fr{Même méthode de conversion :
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}\en{Same conversion method:
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}
}
{
\fr{$\frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = 54^{\circ}$}\en{$\frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = 54^{\circ}$}
}
{ % Répartition des poids (Total = 100)
reasoning: 20
logic: 20
abstraction: 30
calculation: 30
}

(quest3)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Rational(5 * 180, 12)
# === Propositions fausses calculées ===
fausse_1 = Rational(5 * 180, pi) / 12 # Oubli de multiplier par pi au dénominateur
fausse_2 = Rational(5 * pi, 12) # Oubli de conversion
fausse_3 = Rational(180, 5) # Erreur de calcul
\end{python}
\qcm{ \fr{
Convertir en degrés la mesure d'angle suivante exprimée en radians :
$\theta_3 = \frac{5\pi}{12}$
}\en{
Convert the following angle measure from radians to degrees:
$\theta_3 = \frac{5\pi}{12}$
}
}
{
\right{$\displaystyle \sympy{bonne_valeur}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_1}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_2}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_3}^{\circ}$}
\wronger
\righter
}
{%% Solution détaillée : \fr{Même méthode de conversion :
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}\en{Same conversion method:
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}
}
{
\fr{$\frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = 75^{\circ}$}\en{$\frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = 75^{\circ}$}
}
{ % Répartition des poids (Total = 100)
reasoning: 20
logic: 20
abstraction: 30
calculation: 30
}

(quest4)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Rational(3 * 180, 4)
# === Propositions fausses calculées ===
fausse_1 = Rational(3 * 180, pi) / 4 # Oubli de multiplier par pi au dénominateur
fausse_2 = Rational(3 * pi, 4) # Oubli de conversion
fausse_3 = Rational(180, 3) # Erreur de calcul
\end{python}
\qcm{ \fr{
Convertir en degrés la mesure d'angle suivante exprimée en radians :
$\theta_4 = \frac{3\pi}{4}$
}\en{
Convert the following angle measure from radians to degrees:
$\theta_4 = \frac{3\pi}{4}$
}
}
{
\right{$\displaystyle \sympy{bonne_valeur}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_1}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_2}^{\circ}$}
\wrong{$\displaystyle \sympy{fausse_3}^{\circ}$}
\wronger
\righter
}
{%% Solution détaillée : \fr{Même méthode de conversion :
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}\en{Same conversion method:
$\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$}
}
{
\fr{$\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = 135^{\circ}$}\en{$\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = 135^{\circ}$}
}
{ % Répartition des poids (Total = 100)
reasoning: 20
logic: 20
abstraction: 30
calculation: 30
}
}
\end{exercise}
```