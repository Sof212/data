```latex
\begin{exercise}{
Id: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d
Title_exo: Résolution d'équations avec exponentielles et logarithmes
Modules: M1_10_Analyse
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Fonctions_Exponentielles_Logarithmes
Involved_Concepts: Equations_Exponentielles, Equations_Logarithmiques
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
 Résoudre les équations suivantes.

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Calculer la valeur de $x$ qui satisfait l'équation suivante :
\begin{equation}
\label{Eq1}
\mathrm{e}^{x} = 2
\end{equation}
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = ln(2)  # Calcul précis
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez la fonction logarithme népérien.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La solution est $x = \ln 2$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre l'équation $\mathrm{e}^{x} = 2$, et puisqu'on peut prendre le logarithme de $2$, il suffit de prendre 
le logarithme népérien de chaque côté de l'équation. On a donc: 
\begin{equation*}
\mathrm{e}^{x} = 2
\Longleftrightarrow
x = \ln 2.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x = \ln 2$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Calculer la valeur de $x$ qui satisfait l'équation suivante :
\begin{equation}
\label{Eq2}
\mathrm{e}^{x} = \frac{1}{4}
\end{equation}
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = -ln(4)  # Calcul précis
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez les propriétés du logarithme népérien.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La solution est $x = -\ln 4$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre l'équation $\mathrm{e}^{x} = \frac{1}{4}$, et puisqu'on peut prendre le logarithme de $\frac{1}{4}$, il suffit de prendre 
le logarithme népérien de chaque côté de l'équation. On a donc: 
\begin{equation*}
\mathrm{e}^{x} = \frac{1}{4}
\Longleftrightarrow
x = \ln\left(\frac{1}{4}\right)
\Longleftrightarrow
x = \ln 1 -  \ln4
\Longleftrightarrow
x = -  \ln4.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x = -  \ln4$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Calculer la valeur de $x$ qui satisfait l'équation suivante :
\begin{equation}
\label{Eq3}
\ln(x) = \frac{\ln(5)}{2}
\end{equation}
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = sqrt(5)  # Calcul précis
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez la fonction exponentielle et les propriétés des puissances.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La solution est $x = \sqrt{5}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre l'équation $\ln(x) = \frac{\ln(5)}{2}$, il suffit de prendre l'exponentielle de chaque côté de l'équation.
On a donc: 
\begin{equation*}
\ln(x) = \frac{\ln(5)}{2}
\Longleftrightarrow
x = e^{\large\frac{\ln(5)}{2}}
\Longleftrightarrow
x = {\left(e^{\ln 5}\right)}^{\frac{1}{2}}
\Longleftrightarrow
x = {5}^{\frac{1}{2}}\\
\Longleftrightarrow
x = \sqrt{5}.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x =  \sqrt{5}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Calculer la valeur de $x$ qui satisfait l'équation suivante :
\begin{equation}
\label{Eq4}
\ln(x) = -\ln(9).
\end{equation}
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = Rational(1, 9)  # Calcul précis
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez la fonction exponentielle et les propriétés des logarithmes.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La solution est $x = \frac{1}{9}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre l'équation $\ln(x) = -\ln(9)$, il suffit, là encore, de prendre l'exponentielle de chaque côté de
l'équation. On a donc: 
\begin{equation*}
\ln(x) = -\ln9
\Longleftrightarrow
x = e^{-\ln9}
\Longleftrightarrow
x = e^{\ln(9^{-1})}
\Longleftrightarrow
x =9^{-1}\\
\Longleftrightarrow
x = \frac{1}{9}.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x = \frac{1}{9}.$
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