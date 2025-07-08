```latex
\begin{exercise}{
Title_exo: \fr{Résolution d'équations exponentielles et logarithmiques}\en{Solving exponential and logarithmic equations}
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Equations, Logarithms, Exponentials % NameID des chapitres
Involved_Concepts: Exponential_function, Logarithmic_function, Equation_solving % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Cet exercice décline la résolution d'équations exponentielles et logarithmiques en plusieurs questions QCM.
}
{ % Contenu de l'exercice

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur_q1 = ln(2)
# === Propositions fausses calculées ===
fausse_q1_1 = 2
fausse_q1_2 = ln(Rational(1,2))
fausse_q1_3 = 0
\end{python}
\qcm{ % Enoncé de la question:
\fr{Considérons l'équation suivante :
\begin{equation}
\label{Eq1}
\mathrm{e}^{x} = 2
\end{equation}
Quelle est la solution de cette équation ?}
\en{Consider the following equation:
\begin{equation}
\label{Eq1}
\mathrm{e}^{x} = 2
\end{equation}
What is the solution to this equation?}}
{
\right{$x = \sympy{bonne_valeur_q1}$}
\wrong{$x = \sympy{fausse_q1_1}$}
\wrong{$x = \sympy{fausse_q1_2}$}
\wrong{$x = \sympy{fausse_q1_3}$}
}
{ % Indice:
\fr{Pensez à la fonction réciproque de l'exponentielle.}
\en{Think about the inverse function of the exponential.}
}
{ % Solution détaillée:
\fr{Pour résoudre l'équation $\mathrm{e}^{x} = 2$, on applique la fonction logarithme népérien (ln) des deux côtés de l'équation, car c'est la fonction réciproque de l'exponentielle.
\begin{equation*}
\mathrm{e}^{x} = 2
\Longleftrightarrow
\ln(\mathrm{e}^{x}) = \ln(2)
\Longleftrightarrow
x = \ln(2).
\end{equation*}
L'unique solution de l'équation est donc $x = \ln(2)$.}
\en{To solve the equation $\mathrm{e}^{x} = 2$, we apply the natural logarithm function (ln) to both sides of the equation, as it is the inverse function of the exponential.
\begin{equation*}
\mathrm{e}^{x} = 2
\Longleftrightarrow
\ln(\mathrm{e}^{x}) = \ln(2)
\Longleftrightarrow
x = \ln(2).
\end{equation*}
The unique solution to the equation is therefore $x = \ln(2)$.}
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
bonne_valeur_q2 = -ln(4)
# === Propositions fausses calculées ===
fausse_q2_1 = ln(4)
fausse_q2_2 = Rational(1,4)
fausse_q2_3 = -2
\end{python}
\qcm{ % Enoncé de la question:
\fr{Considérons l'équation suivante :
\begin{equation}
\label{Eq2}
\mathrm{e}^{x} = \frac{1}{4}
\end{equation}
Quelle est la solution de cette équation ?}
\en{Consider the following equation:
\begin{equation}
\label{Eq2}
\mathrm{e}^{x} = \frac{1}{4}
\end{equation}
What is the solution to this equation?}}
{
\right{$x = \sympy{bonne_valeur_q2}$}
\wrong{$x = \sympy{fausse_q2_1}$}
\wrong{$x = \sympy{fausse_q2_2}$}
\wrong{$x = \sympy{fausse_q2_3}$}
}
{ % Indice:
\fr{Utilisez les propriétés des logarithmes, notamment $\ln(a/b) = \ln(a) - \ln(b)$ et $\ln(a^n) = n \ln(a)$.}
\en{Use the properties of logarithms, especially $\ln(a/b) = \ln(a) - \ln(b)$ and $\ln(a^n) = n \ln(a)$.}
}
{ % Solution détaillée:
\fr{Pour résoudre l'équation $\mathrm{e}^{x} = \frac{1}{4}$, on prend le logarithme népérien de chaque côté :
\begin{equation*}
\mathrm{e}^{x} = \frac{1}{4}
\Longleftrightarrow
\ln(\mathrm{e}^{x}) = \ln\left(\frac{1}{4}\right)
\Longleftrightarrow
x = \ln(1) - \ln(4)
\Longleftrightarrow
x = 0 - \ln(4)
\Longleftrightarrow
x = -\ln(4).
\end{equation*}
L'unique solution de l'équation est donc $x = -\ln(4)$.}
\en{To solve the equation $\mathrm{e}^{x} = \frac{1}{4}$, we take the natural logarithm of both sides:
\begin{equation*}
\mathrm{e}^{x} = \frac{1}{4}
\Longleftrightarrow
\ln(\mathrm{e}^{x}) = \ln\left(\frac{1}{4}\right)
\Longleftrightarrow
x = \ln(1) - \ln(4)
\Longleftrightarrow
x = 0 - \ln(4)
\Longleftrightarrow
x = -\ln(4).
\end{equation*}
The unique solution to the equation is therefore $x = -\ln(4)$.}
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
bonne_valeur_q3 = sqrt(5)
# === Propositions fausses calculées ===
fausse_q3_1 = Rational(5,2)
fausse_q3_2 = ln(5) / 2
fausse_q3_3 = 5**2
\end{python}
\qcm{ % Enoncé de la question:
\fr{Considérons l'équation suivante :
\begin{equation}
\label{Eq3}
\ln(x) = \frac{\ln(5)}{2}
\end{equation}
Quelle est la solution de cette équation ?}
\en{Consider the following equation:
\begin{equation}
\label{Eq3}
\ln(x) = \frac{\ln(5)}{2}
\end{equation}
What is the solution to this equation?}}
{
\right{$x = \sympy{bonne_valeur_q3}$}
\wrong{$x = \sympy{fausse_q3_1}$}
\wrong{$x = \sympy{fausse_q3_2}$}
\wrong{$x = \sympy{fausse_q3_3}$}
}
{ % Indice:
\fr{Utilisez la propriété $n \ln(a) = \ln(a^n)$ et la fonction exponentielle.}
\en{Use the property $n \ln(a) = \ln(a^n)$ and the exponential function.}
}
{ % Solution détaillée:
\fr{Pour résoudre l'équation $\ln(x) = \frac{\ln(5)}{2}$, on peut d'abord réécrire le membre de droite en utilisant la propriété des logarithmes $n \ln(a) = \ln(a^n)$ :
\begin{equation*}
\ln(x) = \frac{1}{2}\ln(5)
\Longleftrightarrow
\ln(x) = \ln(5^{1/2})
\Longleftrightarrow
\ln(x) = \ln(\sqrt{5}).
\end{equation*}
Ensuite, on applique la fonction exponentielle des deux côtés de l'équation :
\begin{equation*}
\mathrm{e}^{\ln(x)} = \mathrm{e}^{\ln(\sqrt{5})}
\Longleftrightarrow
x = \sqrt{5}.
\end{equation*}
L'unique solution de l'équation est donc $x = \sqrt{5}$.}
\en{To solve the equation $\ln(x) = \frac{\ln(5)}{2}$, we can first rewrite the right-hand side using the logarithm property $n \ln(a) = \ln(a^n)$:
\begin{equation*}
\ln(x) = \frac{1}{2}\ln(5)
\Longleftrightarrow
\ln(x) = \ln(5^{1/2})
\Longleftrightarrow
\ln(x) = \ln(\sqrt{5}).
\end{equation*}
Then, we apply the exponential function to both sides of the equation:
\begin{equation*}
\mathrm{e}^{\ln(x)} = \mathrm{e}^{\ln(\sqrt{5})}
\Longleftrightarrow
x = \sqrt{5}.
\end{equation*}
The unique solution to the equation is therefore $x = \sqrt{5}$.}
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
bonne_valeur_q4 = Rational(1, 9)
# === Propositions fausses calculées ===
fausse_q4_1 = 9
fausse_q4_2 = -ln(9)
fausse_q4_3 = -9
\end{python}
\qcm{ % Enoncé de la question:
\fr{Considérons l'équation suivante :
\begin{equation}
\label{Eq4}
\ln(x) = -\ln(9).
\end{equation}
Quelle est la solution de cette équation ?}
\en{Consider the following equation:
\begin{equation}
\label{Eq4}
\ln(x) = -\ln(9).
\end{equation}
What is the solution to this equation?}}
{
\right{$x = \sympy{bonne_valeur_q4}$}
\wrong{$x = \sympy{fausse_q4_1}$}
\wrong{$x = \sympy{fausse_q4_2}$}
\wrong{$x = \sympy{fausse_q4_3}$}
}
{ % Indice:
\fr{Rappelez-vous que $-\ln(a) = \ln(1/a)$.}
\en{Remember that $-\ln(a) = \ln(1/a)$.}
}
{ % Solution détaillée:
\fr{Pour résoudre l'équation $\ln(x) = -\ln(9)$, on utilise la propriété des logarithmes $-\ln(a) = \ln(a^{-1})$ ou $\ln(1/a)$ :
\begin{equation*}
\ln(x) = -\ln(9)
\Longleftrightarrow
\ln(x) = \ln(9^{-1})
\Longleftrightarrow
\ln(x) = \ln\left(\frac{1}{9}\right).
\end{equation*}
Ensuite, on applique la fonction exponentielle des deux côtés de l'équation :
\begin{equation*}
\mathrm{e}^{\ln(x)} = \mathrm{e}^{\ln\left(\frac{1}{9}\right)}
\Longleftrightarrow
x = \frac{1}{9}.
\end{equation*}
L'unique solution de l'équation est donc $x = \frac{1}{9}$.}
\en{To solve the equation $\ln(x) = -\ln(9)$, we use the logarithm property $-\ln(a) = \ln(a^{-1})$ or $\ln(1/a)$:
\begin{equation*}
\ln(x) = -\ln(9)
\Longleftrightarrow
\ln(x) = \ln(9^{-1})
\Longleftrightarrow
\ln(x) = \ln\left(\frac{1}{9}\right).
\end{equation*}
Then, we apply the exponential function to both sides of the equation:
\begin{equation*}
\mathrm{e}^{\ln(x)} = \mathrm{e}^{\ln\left(\frac{1}{9}\right)}
\Longleftrightarrow
x = \frac{1}{9}.
\end{equation*}
The unique solution to the equation is therefore $x = \frac{1}{9}$.}
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