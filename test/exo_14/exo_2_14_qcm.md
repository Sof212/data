```latex
\begin{exercise}{
Title_exo: \fr{Résolution d'équations exponentielles et logarithmiques}\en{Solving Exponential and Logarithmic Equations}
Modules: Fonctions, Équations % NameID des modules
Recommended_execution_time: 15 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Fonctions_transcendantes % NameID des chapitres
Involved_Concepts: Exponentielle, Logarithme, Résolution_équation % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
Comment: Cet exercice est un QCM sur la résolution d'équations exponentielles et logarithmiques. % Comment: % Commentaire de l'exercice (optionnel)
}
{
(quest1)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = ln(2)
# === Propositions fausses calculées ===
fausse_1 = ln(4)  # Erreur de valeur
fausse_2 = S(2)  # Oubli du logarithme
fausse_3 = exp(2)  # Inversion exponentielle/logarithme
\end{python}
\qcm{ \fr{Résoudre l'équation : $\mathrm{e}^{x} = 2$}\en{Solve the equation: $\mathrm{e}^{x} = 2$}
}
{
\right{$x = \ln 2$}
\wrong{$x = \ln 4$}
\wrong{$x = 2$}
\wrong{$x = e^{2}$}
}
{%% Solution détaillée : \fr{Pour résoudre $\mathrm{e}^{x} = 2$, on prend le logarithme népérien des deux côtés :
$\mathrm{e}^{x} = 2 \Longleftrightarrow x = \ln 2$}\en{To solve $\mathrm{e}^{x} = 2$, we take the natural logarithm of both sides:
$\mathrm{e}^{x} = 2 \Longleftrightarrow x = \ln 2$}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

(quest2)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = -ln(4)
# === Propositions fausses calculées ===
fausse_1 = ln(4)  # Oubli du signe -
fausse_2 = -ln(2)  # Erreur de dénominateur
fausse_3 = Rational(1,4)  # Confusion avec la valeur initiale
\end{python}
\qcm{ \fr{Résoudre l'équation : $\mathrm{e}^{x} = \frac{1}{4}$}\en{Solve the equation: $\mathrm{e}^{x} = \frac{1}{4}$}
}
{
\right{$x = -\ln 4$}
\wrong{$x = \ln 4$}
\wrong{$x = -\ln 2$}
\wrong{$x = \frac{1}{4}$}
}
{%% Solution détaillée : \fr{Solution : $\mathrm{e}^{x} = \frac{1}{4} \Longleftrightarrow x = \ln\left(\frac{1}{4}\right) = \ln 1 - \ln 4 = -\ln 4$}\en{Solution: $\mathrm{e}^{x} = \frac{1}{4} \Longleftrightarrow x = \ln\left(\frac{1}{4}\right) = \ln 1 - \ln 4 = -\ln 4$}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

(quest3)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = sqrt(5)
# === Propositions fausses calculées ===
fausse_1 = ln(5)/S(2)  # Oubli de l'exponentielle
fausse_2 = Rational(5,2)  # Simplification incorrecte
fausse_3 = exp(5)  # Erreur d'exposant
\end{python}
\qcm{ \fr{Résoudre l'équation : $\ln(x) = \frac{\ln(5)}{2}$}\en{Solve the equation: $\ln(x) = \frac{\ln(5)}{2}$}
}
{
\right{$x = \sqrt{5}$}
\wrong{$x = \frac{\ln(5)}{2}$}
\wrong{$x = \frac{5}{2}$}
\wrong{$x = e^{5}$}
}
{%% Solution détaillée : \fr{Solution : $\ln(x) = \frac{\ln(5)}{2} \Longleftrightarrow x = e^{\frac{\ln(5)}{2}} = \sqrt{5}$}\en{Solution: $\ln(x) = \frac{\ln(5)}{2} \Longleftrightarrow x = e^{\frac{\ln(5)}{2}} = \sqrt{5}$}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

(quest4)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Rational(1,9)
# === Propositions fausses calculées ===
fausse_1 = S(-9)  # Confusion signe et exponentielle
fausse_2 = ln(9)  # Oubli de l'exponentielle et du signe
fausse_3 = S(9)  # Oubli de l'inverse
\end{python}
\qcm{ \fr{Résoudre l'équation : $\ln(x) = -\ln(9)$}\en{Solve the equation: $\ln(x) = -\ln(9)$}
}
{
\right{$x = \frac{1}{9}$}
\wrong{$x = -9$}
\wrong{$x = \ln(9)$}
\wrong{$x = 9$}
}
{%% Solution détaillée : \fr{Solution : $\ln(x) = -\ln9 \Longleftrightarrow x = e^{-\ln9} = \frac{1}{9}$}\en{Solution: $\ln(x) = -\ln9 \Longleftrightarrow x = e^{-\ln9} = \frac{1}{9}$}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}
}
\end{exercise}
```