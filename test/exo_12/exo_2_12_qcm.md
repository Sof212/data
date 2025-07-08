```latex
\begin{exercise}{
Title_exo: \fr{Résolution d'équation quadratique}\en{Quadratic Equation Resolution}
Modules: Algèbre % NameID des modules
Recommended_execution_time: 5 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Équations % NameID des chapitres
Involved_Concepts: Équation quadratique, Discriminant % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: Teacher % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
Comment: Exercice QCM sur la résolution d'équations quadratiques. % Comment: % Commentaire de l'exercice (optionnel)
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
# L'équation est X^2 - 2X - 15 = 0
# Discriminant Delta = b^2 - 4ac = (-2)^2 - 4*1*(-15) = 4 + 60 = 64
# Solutions X = (-b +/- sqrt(Delta)) / 2a
# X1 = (2 - sqrt(64)) / 2 = (2 - 8) / 2 = -6 / 2 = -3
# X2 = (2 + sqrt(64)) / 2 = (2 + 8) / 2 = 10 / 2 = 5
bonne_valeur_1 = -3
bonne_valeur_2 = 5

# === Propositions fausses calculées ===
fausse_1 = 3   # Erreur de signe typique (oublier le signe négatif de la solution)
fausse_2 = -5  # Inversion des solutions (confondre X1 et X2 ou erreur de signe sur le discriminant)
fausse_3 = 8   # Confusion avec la valeur du discriminant ou sa racine carrée
fausse_4 = 0   # Valeur arbitraire incorrecte, souvent testée par les élèves
\end{python}

\qcm{ \fr{Résoudre l'équation $X^{2}-2X-15=0$. Quelles sont les solutions correctes ?}\en{Solve the equation $X^{2}-2X-15=0$. What are the correct solutions?}
}
{
\right{$\sympy{bonne_valeur_1}$}
\right{$\sympy{bonne_valeur_2}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wrong{$\sympy{fausse_4}$}
}
{ % Indice
\fr{Pour résoudre une équation quadratique $aX^2 + bX + c = 0$ :
\begin{enumerate}
    \item Calculer le discriminant $\Delta = b^2 - 4ac$.
    \item Si $\Delta > 0$, il y a deux solutions réelles distinctes.
    \item Appliquer la formule $X = \frac{-b \pm \sqrt{\Delta}}{2a}$.
\end{enumerate}
}\en{To solve a quadratic equation $aX^2 + bX + c = 0$:
\begin{enumerate}
    \item Calculate the discriminant $\Delta = b^2 - 4ac$.
    \item If $\Delta > 0$, there are two distinct real solutions.
    \item Apply the formula $X = \frac{-b \pm \sqrt{\Delta}}{2a}$.
\end{enumerate}
}
}
{ % Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{Le discriminant de l'équation $X^{2}-2X-15=0$ est :
$\Delta = (-2)^{2}-4 \cdot 1 \cdot (-15) = 4 + 60 = 64 = 8^2$

Les solutions sont donc :
\begin{align*}
X_1 &= \frac{-(-2) - \sqrt{64}}{2 \cdot 1} = \frac{2 - 8}{2} = \frac{-6}{2} = -3 \\
X_2 &= \frac{-(-2) + \sqrt{64}}{2 \cdot 1} = \frac{2 + 8}{2} = \frac{10}{2} = 5
\end{align*}

Ainsi, les solutions de l'équation sont $\boxed{-3}$ et $\boxed{5}$.
}\en{The discriminant of the equation $X^{2}-2X-15=0$ is:
$\Delta = (-2)^{2}-4 \cdot 1 \cdot (-15) = 4 + 60 = 64 = 8^2$

The solutions are therefore:
\begin{align*}
X_1 &= \frac{-(-2) - \sqrt{64}}{2 \cdot 1} = \frac{2 - 8}{2} = \frac{-6}{2} = -3 \\
X_2 &= \frac{-(-2) + \sqrt{64}}{2 \cdot 1} = \frac{2 + 8}{2} = \frac{10}{2} = 5
\end{align*}

Thus, the solutions to the equation are $\boxed{-3}$ and $\boxed{5}$.
}
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