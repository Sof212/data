```latex
\begin{exercise}{
Title_exo: \fr{Résolution d'une équation du second degré}\en{Solving a quadratic equation}
Modules: Algèbre % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Équations du second degré % NameID des chapitres
Involved_Concepts: Discriminant, Solutions d'une équation du second degré % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: Teacher % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
}
{
\begin{python}
from sympy import *

# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur_s1 = -3
bonne_valeur_s2 = 5

# === Propositions fausses calculées ===
# Erreur méthodologique typique: inversion des signes des solutions
fausse_1_s1 = 3
fausse_1_s2 = -5

# Variante calcul incorrecte: erreur sur le discriminant ou la formule
# Par exemple, si Delta = 64, mais on prend sqrt(Delta) = 4 au lieu de 8
# s1 = (-(-2) - 4) / 2 = -1
# s2 = (-(-2) + 4) / 2 = 3
fausse_2_s1 = -1
fausse_2_s2 = 3

# Approximation erronée ou erreur de calcul simple
# Par exemple, si on oublie le 2a au dénominateur ou on fait une erreur de signe
# s1 = -(-2) - 8 = -6
# s2 = -(-2) + 8 = 10
fausse_3_s1 = -6
fausse_3_s2 = 10

# Autre erreur de signe
fausse_4_s1 = -5
fausse_4_s2 = -3

# Erreur de calcul simple
fausse_5_s1 = 2.5
fausse_5_s2 = -6
\end{python}
\qcm{ \fr{Résoudre l'équation \( X^{2} - 2X - 15 = 0 \).} \en{Solve the equation \( X^{2} - 2X - 15 = 0 \).}
}
{
\right{\fr{\( \sympy{bonne_valeur_s2} \text{ et } \sympy{bonne_valeur_s1} \)}\en{\( \sympy{bonne_valeur_s2} \text{ and } \sympy{bonne_valeur_s1} \)}}
\wrong{\fr{\( \sympy{fausse_1_s2} \text{ et } \sympy{fausse_1_s1} \)}\en{\( \sympy{fausse_1_s2} \text{ and } \sympy{fausse_1_s1} \)}}
\wrong{\fr{\( \sympy{fausse_2_s2} \text{ et } \sympy{fausse_2_s1} \)}\en{\( \sympy{fausse_2_s2} \text{ and } \sympy{fausse_2_s1} \)}}
\wrong{\fr{\( \sympy{fausse_3_s2} \text{ et } \sympy{fausse_3_s1} \)}\en{\( \sympy{fausse_3_s2} \text{ and } \sympy{fausse_3_s1} \)}}
\wrong{\fr{\( \sympy{fausse_4_s2} \text{ et } \sympy{fausse_4_s1} \)}\en{\( \sympy{fausse_4_s2} \text{ and } \sympy{fausse_4_s1} \)}}
\wrong{\fr{\( \sympy{fausse_5_s2} \text{ et } \sympy{fausse_5_s1} \)}\en{\( \sympy{fausse_5_s2} \text{ and } \sympy{fausse_5_s1} \)}}
}
{
% Indice
}
{
%% Solution détaillée : \fr{Commençons par calculer le discriminant, noté $\Delta$, de l'équation $X^{2} - 2X - 15 = 0$. On a :
% \[
% \Delta = (-2)^{2} - 4 \cdot (-15) = 4 + 60 = 64 = 8^2.
% \]
% Nous savons donc que l'équation admet deux solutions réelles distinctes, notées $s_1$ et $s_2$. On a :
% \[
% s_1 = \frac{-(-2) - 8}{2 \cdot 1} = \frac{-6}{2} = -3 \quad \text{et} \quad s_2 = \frac{-(-2) + 8}{2 \cdot 1} = \frac{10}{2} = 5.
% \]
% Ainsi, les solutions de l'équation sont : $\boxed{5 \text{ et } -3}$.}\en{Let's start by calculating the discriminant, denoted $\Delta$, of the equation $X^{2} - 2X - 15 = 0$. We have:
% \[
% \Delta = (-2)^{2} - 4 \cdot (-15) = 4 + 60 = 64 = 8^2.
% \]
% We therefore know that the equation has two distinct real solutions, denoted $s_1$ and $s_2$. We have:
% \[
% s_1 = \frac{-(-2) - 8}{2 \cdot 1} = \frac{-6}{2} = -3 \quad \text{and} \quad s_2 = \frac{-(-2) + 8}{2 \cdot 1} = \frac{10}{2} = 5.
% \]
% Thus, the solutions of the equation are: $\boxed{5 \text{ and } -3}$.}
\fr{Commençons par calculer le discriminant, noté $\Delta$, de l'équation $X^{2} - 2X - 15 = 0$. On a :
\[
\Delta = (-2)^{2} - 4 \cdot (-15) = 4 + 60 = 64 = 8^2.
\]
Nous savons donc que l'équation admet deux solutions réelles distinctes, notées $s_1$ et $s_2$. On a :
\[
s_1 = \frac{-(-2) - 8}{2 \cdot 1} = \frac{-6}{2} = -3 \quad \text{et} \quad s_2 = \frac{-(-2) + 8}{2 \cdot 1} = \frac{10}{2} = 5.
\]
Ainsi, les solutions de l'équation sont : $\boxed{5 \text{ et } -3}$.}\en{Let's start by calculating the discriminant, denoted $\Delta$, of the equation $X^{2} - 2X - 15 = 0$. We have:
\[
\Delta = (-2)^{2} - 4 \cdot (-15) = 4 + 60 = 64 = 8^2.
\]
We therefore know that the equation has two distinct real solutions, denoted $s_1$ and $s_2$. We have:
\[
s_1 = \frac{-(-2) - 8}{2 \cdot 1} = \frac{-6}{2} = -3 \quad \text{and} \quad s_2 = \frac{-(-2) + 8}{2 \cdot 1} = \frac{10}{2} = 5.
\]
Thus, the solutions of the equation are: $\boxed{5 \text{ and } -3}$.}
}
{
% Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}
}
\end{exercise}
```