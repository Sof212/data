```latex
\begin{exercise}{
Title_exo: \fr{Conversion d'angles radians en degrés}\en{Angle conversion from radians to degrees}
Modules: Trigonométrie % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Angles_Trigonometry % NameID des chapitres
Involved_Concepts: Angle_conversion % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Exercice de conversion d'angles radians en degrés.
}
{ % Contenu de l'exercice

\begin{python}
from sympy import *

# Define pi for calculations
pi_sym = pi

def convert_to_degrees(radians_expr):
    """Converts a SymPy expression in radians to degrees."""
    return (radians_expr * 180 / pi_sym).simplify()

# Question 1: theta_1 = pi/5
theta1_rad = pi_sym / 5
bonne_valeur_theta1 = convert_to_degrees(theta1_rad)
fausse_theta1_1 = bonne_valeur_theta1 + 10 # Erreur simple
fausse_theta1_2 = bonne_valeur_theta1 - 6 # Erreur simple
fausse_theta1_3 = bonne_valeur_theta1 * 2 # Erreur de facteur

# Question 2: theta_2 = 3*pi/10
theta2_rad = 3 * pi_sym / 10
bonne_valeur_theta2 = convert_to_degrees(theta2_rad)
fausse_theta2_1 = bonne_valeur_theta2 + 5 # Erreur simple
fausse_theta2_2 = bonne_valeur_theta2 - 4 # Erreur simple
fausse_theta2_3 = bonne_valeur_theta2 / 2 # Erreur de division

# Question 3: theta_3 = 5*pi/12
theta3_rad = 5 * pi_sym / 12
bonne_valeur_theta3 = convert_to_degrees(theta3_rad)
fausse_theta3_1 = bonne_valeur_theta3 + 15 # Erreur simple
fausse_theta3_2 = bonne_valeur_theta3 - 5 # Erreur simple
fausse_theta3_3 = bonne_valeur_theta3 * 1.5 # Erreur de facteur

# Question 4: theta_4 = 3*pi/4
theta4_rad = 3 * pi_sym / 4
bonne_valeur_theta4 = convert_to_degrees(theta4_rad)
fausse_theta4_1 = bonne_valeur_theta4 + 10 # Erreur simple
fausse_theta4_2 = bonne_valeur_theta4 - 15 # Erreur simple
fausse_theta4_3 = bonne_valeur_theta4 / 3 # Erreur de division
\end{python}

\qcm{ % Enoncé de la question
\fr{Convertir en degrés la mesure d'angle suivante, exprimée en radians : $\theta_1:= \frac{\pi}{5}$.}
\en{Convert the following angle measure, expressed in radians, to degrees: $\theta_1:= \frac{\pi}{5}$.}
}
{
\right{$\py{bonne_valeur_theta1}^{\circ}$}
\wrong{$\py{fausse_theta1_1}^{\circ}$}
\wrong{$\py{fausse_theta1_2}^{\circ}$}
\wrong{$\py{fausse_theta1_3}^{\circ}$}
\wronger
}
{ % Indice
\fr{Rappelez-vous la relation entre les radians et les degrés : $\pi$ radians correspondent à $180$ degrés.}
\en{Remember the relationship between radians and degrees: $\pi$ radians correspond to $180$ degrees.}
}
{ % Solution détaillée
\fr{On sait que $180$ degrés correspondent à $\pi$ radians. Par conséquent, pour exprimer en degrés un angle exprimé en radians, on utilise la relation :
\begin{equation*}
\theta \text{ (en degrés)} = \theta \text{ (en radians)} \times \frac{180}{\pi}
\end{equation*}
#### Conversion de $\frac{\pi}{5}$ en degrés :
On a donc
\begin{equation*}
\frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = 36.
\end{equation*}
La mesure de l'angle $\theta_1$ est donc $36^{\circ}$.}
\en{We know that $180$ degrees correspond to $\pi$ radians. Therefore, to express an angle in degrees from radians, we use the relation:
\begin{equation*}
\theta \text{ (in degrees)} = \theta \text{ (in radians)} \times \frac{180}{\pi}
\end{equation*}
#### Conversion of $\frac{\pi}{5}$ to degrees:
So we have
\begin{equation*}
\frac{\pi}{5} \times \frac{180}{\pi} = \frac{180}{5} = 36.
\end{equation*}
The measure of angle $\theta_1$ is therefore $36^{\circ}$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{ % Enoncé de la question
\fr{Convertir en degrés la mesure d'angle suivante, exprimée en radians : $\theta_2 :=\frac{3 \pi}{10}$.}
\en{Convert the following angle measure, expressed in radians, to degrees: $\theta_2 :=\frac{3 \pi}{10}$.}
}
{
\right{$\py{bonne_valeur_theta2}^{\circ}$}
\wrong{$\py{fausse_theta2_1}^{\circ}$}
\wrong{$\py{fausse_theta2_2}^{\circ}$}
\wrong{$\py{fausse_theta2_3}^{\circ}$}
\wronger
}
{ % Indice
\fr{Utilisez la même formule de conversion que pour la question précédente.}
\en{Use the same conversion formula as for the previous question.}
}
{ % Solution détaillée
\fr{#### Conversion de $\frac{3\pi}{10}$ en degrés :
On a donc
\begin{equation*}
\frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = 54.
\end{equation*}
La mesure de l'angle $\theta_2$ est donc $54^{\circ}$.}
\en{#### Conversion of $\frac{3\pi}{10}$ to degrees:
So we have
\begin{equation*}
\frac{3\pi}{10} \times \frac{180}{\pi} = \frac{3 \times 180}{10} = 54.
\end{equation*}
The measure of angle $\theta_2$ is therefore $54^{\circ}$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{ % Enoncé de la question
\fr{Convertir en degrés la mesure d'angle suivante, exprimée en radians : $\theta_3 :=\frac{5 \pi}{12}$.}
\en{Convert the following angle measure, expressed in radians, to degrees: $\theta_3 :=\frac{5 \pi}{12}$.}
}
{
\right{$\py{bonne_valeur_theta3}^{\circ}$}
\wrong{$\py{fausse_theta3_1}^{\circ}$}
\wrong{$\py{fausse_theta3_2}^{\circ}$}
\wrong{$\py{fausse_theta3_3}^{\circ}$}
\wronger
}
{ % Indice
\fr{N'oubliez pas de simplifier la fraction avant de multiplier.}
\en{Don't forget to simplify the fraction before multiplying.}
}
{ % Solution détaillée
\fr{#### Conversion de $\frac{5\pi}{12}$ en degrés :
On a donc:
\begin{equation*}
\frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = 75.
\end{equation*}
La mesure de l'angle $\theta_3$ est donc $75^{\circ}$.}
\en{#### Conversion of $\frac{5\pi}{12}$ to degrees:
So we have:
\begin{equation*}
\frac{5\pi}{12} \times \frac{180}{\pi} = \frac{5 \times 180}{12} = 75.
\end{equation*}
The measure of angle $\theta_3$ is therefore $75^{\circ}$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{ % Enoncé de la question
\fr{Convertir en degrés la mesure d'angle suivante, exprimée en radians : $\theta_4:=\frac{3 \pi}{4}$.}
\en{Convert the following angle measure, expressed in radians, to degrees: $\theta_4:=\frac{3 \pi}{4}$.}
}
{
\right{$\py{bonne_valeur_theta4}^{\circ}$}
\wrong{$\py{fausse_theta4_1}^{\circ}$}
\wrong{$\py{fausse_theta4_2}^{\circ}$}
\wrong{$\py{fausse_theta4_3}^{\circ}$}
\wronger
}
{ % Indice
\fr{Soyez attentif aux simplifications.}
\en{Pay attention to simplifications.}
}
{ % Solution détaillée
\fr{#### Conversion de $\frac{3\pi}{4}$ en degrés :
On a donc:
\begin{equation*}
\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = 135.
\end{equation*}
La mesure de l'angle $\theta_4$ est donc $135^{\circ}$.}
\en{#### Conversion of $\frac{3\pi}{4}$ to degrees:
So we have:
\begin{equation*}
\frac{3\pi}{4} \times \frac{180}{\pi} = \frac{3 \times 180}{4} = 135.
\end{equation*}
The measure of angle $\theta_4$ is therefore $135^{\circ}$.}
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