```latex
\begin{exercise}{
Title_exo: Conversion de radians en degrés
Modules: Trigonométrie
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Angles et cercles trigonométriques
Involved_Concepts: Conversion d'angles, Radians, Degrés
Original_source:  % Source de l'exercice
Visibility: Teacher % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Exercice de conversion d'angles radians en degrés.
}
{
\begin{python}
from sympy import *

# --- Calculs bonne réponse ---
theta1_rad = Rational(1, 5) * pi
theta1_deg = theta1_rad * (180 / pi)

theta2_rad = Rational(3, 10) * pi
theta2_deg = theta2_rad * (180 / pi)

theta3_rad = Rational(5, 12) * pi
theta3_deg = theta3_rad * (180 / pi)

theta4_rad = Rational(3, 4) * pi
theta4_deg = theta4_rad * (180 / pi)

# --- Propositions fausses calculées ---
# Erreur méthodologique typique: division par 2 ou multiplication par 2
fausse1_1 = theta1_deg / 2
fausse1_2 = theta1_deg * 2
fausse1_3 = theta1_deg + 9 # Erreur d'approximation ou de calcul simple

fausse2_1 = theta2_deg / 2
fausse2_2 = theta2_deg * 2
fausse2_3 = theta2_deg - 18 # Erreur d'approximation ou de calcul simple

fausse3_1 = theta3_deg * 2
fausse3_2 = theta3_deg / 2
fausse3_3 = theta3_deg + 15 # Erreur d'approximation ou de calcul simple

fausse4_1 = theta4_deg / 2
fausse4_2 = theta4_deg * 2
fausse4_3 = theta4_deg - 45 # Erreur d'approximation ou de calcul simple
\end{python}
\qcm{
Convertir en degrés les mesures d'angle suivantes, exprimées en radians :
\begin{enumerate}
    \item $\theta_1 = \frac{\pi}{5}$
    \item $\theta_2 = \frac{3\pi}{10}$
    \item $\theta_3 = \frac{5\pi}{12}$
    \item $\theta_4 = \frac{3\pi}{4}$
\end{enumerate}
}
{
\right{$\theta_1 = \sympy{theta1_deg}^{\circ}$}
\wrong{$\theta_1 = \sympy{fausse1_1}^{\circ}$}
\wrong{$\theta_1 = \sympy{fausse1_2}^{\circ}$}
\wrong{$\theta_1 = \sympy{fausse1_3}^{\circ}$}
\right{$\theta_2 = \sympy{theta2_deg}^{\circ}$}
\wrong{$\theta_2 = \sympy{fausse2_1}^{\circ}$}
\wrong{$\theta_2 = \sympy{fausse2_2}^{\circ}$}
\wrong{$\theta_2 = \sympy{fausse2_3}^{\circ}$}
\right{$\theta_3 = \sympy{theta3_deg}^{\circ}$}
\wrong{$\theta_3 = \sympy{fausse3_1}^{\circ}$}
\wrong{$\theta_3 = \sympy{fausse3_2}^{\circ}$}
\wrong{$\theta_3 = \sympy{fausse3_3}^{\circ}$}
\right{$\theta_4 = \sympy{theta4_deg}^{\circ}$}
\wrong{$\theta_4 = \sympy{fausse4_1}^{\circ}$}
\wrong{$\theta_4 = \sympy{fausse4_2}^{\circ}$}
\wrong{$\theta_4 = \sympy{fausse4_3}^{\circ}$}
}
{
Pour convertir un angle de radians en degrés, on utilise la formule : $\theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$.
}
{
%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
$\text{Pour convertir un angle de radians en degrés, on utilise la formule : } \theta_{\text{deg}} = \theta_{\text{rad}} \times \frac{180}{\pi}$.
\begin{enumerate}
    \item $\theta_1 = \frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = \sympy{theta1_deg}^{\circ}$
    \item $\theta_2 = \frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = 3 \times 18 = \sympy{theta2_deg}^{\circ}$
    \item $\theta_3 = \frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = 5 \times 15 = \sympy{theta3_deg}^{\circ}$
    \item $\theta_4 = \frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = 3 \times 45 = \sympy{theta4_deg}^{\circ}$
\end{enumerate}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}
}
\end{exercise}
```