```latex
\begin{exercise}{
Title_exo: \fr{Fonction de récurrence}\en{Recurrence function}
Modules: Analyse_NYU
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Suites_numeriques
Involved_Concepts: Suites_recurrence
Original_source:
}
{
% Contenu de l'exercice
Les suites suivantes sont définies par des relations de récurrence $u_{n+1}=f\left(u_{n}\right)$.
Donner la fonction $f$ correspondante dans chacun des cas.

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur_1 = "2x - 3"
# === Propositions fausses calculées ===
fausse_1_1 = "2x + 3"  # Erreur de signe
fausse_1_2 = "2x - 1"  # Erreur de constante
fausse_1_3 = "2x + 1"  # Erreur de signe et de constante
\end{python}
\qcm{ %% [Énoncé original intégralement conservé]
Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
u _ { 0 }  & { = 4 } \\
   { u _ { n + 1 } } & { = 2 u _ { n } - 3 }
\end{cases}
$.
Quelle est la fonction $f$ correspondante ?
}
{
\right{$f(x) = \sympy{bonne_valeur_1}$}
\wrong{$f(x) = \sympy{fausse_1_1}$}
\wrong{$f(x) = \sympy{fausse_1_2}$}
\wrong{$f(x) = \sympy{fausse_1_3}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
$\text{Pour les suites définies par les relations de récurrence données, notre objectif est d'extraire la fonction } f \text{ correspondante selon la forme générale } u_{n+1} = f(u_n).$

$\text{Ici, la relation de récurrence étant } u_{n+1} = 2 u_n - 3, \text{ on identifie aisément la fonction } f \text{ qui est donnée par : } f(x) = 2x - 3.$
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
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur_2 = "\\sqrt{1 + x^2}"
# === Propositions fausses calculées ===
fausse_2_1 = "\\sqrt{1 - x^2}"  # Erreur de signe
fausse_2_2 = "1 + x^2"          # Oubli de la racine
fausse_2_3 = "1 - x^2"          # Oubli de la racine et erreur de signe
\end{python}
\qcm{ %% [Énoncé original intégralement conservé]
$
\begin{cases}
    u _ { 0 } &{=} 0  \\
    {u _ { n + 1 }} &{= \sqrt { 1 + u _ { n } ^ { 2 }}}
\end{cases}
$
Quelle est la fonction $f$ correspondante ?
}
{
\right{$f(x) = \sympy{bonne_valeur_2}$}
\wrong{$f(x) = \sympy{fausse_2_1}$}
\wrong{$f(x) = \sympy{fausse_2_2}$}
\wrong{$f(x) = \sympy{fausse_2_3}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
$\text{Pour cette suite, la relation de récurrence est } u_{n+1} = \sqrt{1 + u_n^2}. \text{ On identifie aisément la fonction } f \text{ qui est donnée par : } f(x) = \sqrt{1 + x^2}.$
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
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur_3 = "\\sin(x)"
# === Propositions fausses calculées ===
fausse_3_1 = "\\cos(x)"      # Erreur de fonction trigonométrique
fausse_3_2 = "\\tan(x)"      # Erreur de fonction trigonométrique
fausse_3_3 = "\\sin(x) + 1"  # Ajout d'une constante
\end{python}
\qcm{ %% [Énoncé original intégralement conservé]
$
\begin{cases}
   { u _ { 0 }} &{= } 2  \\
   { u _ { n + 1 }} &{= \operatorname { s i n } ( u _ { n } ) }
\end{cases}
$
Quelle est la fonction $f$ correspondante ?
}
{
\right{$f(x) = \sympy{bonne_valeur_3}$}
\wrong{$f(x) = \sympy{fausse_3_1}$}
\wrong{$f(x) = \sympy{fausse_3_2}$}
\wrong{$f(x) = \sympy{fausse_3_3}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
$\text{Dans ce cas, la relation de récurrence est } u_{n+1} = \sin(u_n). \text{ On identifie aisément la fonction } f \text{ qui est donnée par : } f(x) = \sin(x).$
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
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur_4 = "\\frac{x - 1}{x + 1}"
# === Propositions fausses calculées ===
fausse_4_1 = "\\frac{x + 1}{x - 1}"  # Inversion numérateur/dénominateur
fausse_4_2 = "\\frac{1 - x}{1 + x}"  # Erreur de signe au numérateur
fausse_4_3 = "\\frac{1 + x}{1 - x}"  # Inversion et erreurs de signe
\end{python}
\qcm{ %% [Énoncé original intégralement conservé]
$
\begin{cases}
   u_{0}&{=}4 \\
   u_{n+1}&=\frac{u_{n}-1}{u_{n}+1}
\end{cases}
$
Quelle est la fonction $f$ correspondante ?
}
{
\right{$f(x) = \sympy{bonne_valeur_4}$}
\wrong{$f(x) = \sympy{fausse_4_1}$}
\wrong{$f(x) = \sympy{fausse_4_2}$}
\wrong{$f(x) = \sympy{fausse_4_3}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
$\text{Enfin, pour cette suite, la relation de récurrence est } u_{n+1} = \frac{u_n - 1}{u_n + 1}. \text{ Nous pouvons identifier la fonction } f \text{ comme : } f(x) = \frac{x - 1}{x + 1}.$
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