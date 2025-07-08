```latex
\begin{exercise}{
Id: 001
Title_exo: Résolution d'équations avec exponentielles et logarithmes
Modules: M1_10_Logarithms_Exponentials
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Logarithms_Exponentials
Involved_Concepts: Logarithm, Exponential
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
 Résoudre les équations suivantes.

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{equation}
\label{Eq1}
\mathrm{e}^{x} = 2
\end{equation}
}
{
\begin{python}
from sympy import *
bonne_valeur = log(2)
\end{python}
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez la fonction logarithme népérien.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(bonne_valeur)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre [](#Eq1), et puisqu'on peut prendre le logarithme de $2$, il suffit de prendre 
le logarithme népérien de chaque côté de  [](#Eq1). On a donc: 
\begin{equation*}
\label{Eq1}
\mathrm{e}^{x} = 2
\Longleftrightarrow
x = \ln 2.
\end{equation*}
On a donc montré que l'unique solution de l'équation [](#Eq1) est $x = \ln 2$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
  
\begin{equation}
\label{Eq2}
\mathrm{e}^{x} = \frac{1}{4}
\end{equation}
}
{
\begin{python}
from sympy import *
bonne_valeur = -log(4)
\end{python}
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez les propriétés des logarithmes.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(bonne_valeur)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre [](#Eq2), et puisqu'on peut prendre le logarithme de $\frac{1}{4}$, il suffit de prendre 
le logarithme népérien de chaque côté de  [](#Eq2). On a donc: 
\begin{equation*}
\label{Eq1}
\mathrm{e}^{x} = \frac{1}{4}
\Longleftrightarrow
x = \ln\left(\frac{1}{4}\right)
\Longleftrightarrow
x = \ln 1 -  \ln4
\Longleftrightarrow
x = -  \ln4.
\end{equation*}
On a donc montré que l'unique solution de l'équation [](#Eq2) est $x = -  \ln4$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{equation}
\label{Eq3}
\ln(x) = \frac{\ln(5)}{2}
\end{equation}
}
{
\begin{python}
from sympy import *
bonne_valeur = sqrt(5)
\end{python}
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez la fonction exponentielle.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(bonne_valeur)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre [](#Eq3), il suffit de prendre l'exponentielle de chaque côté de  [](#Eq3).
On a donc: 
\begin{equation*}
\ln(x) = \frac{\ln(5)}{2}
&\Longleftrightarrow
x = e^{\large\frac{\ln(5)}{2}}
\Longleftrightarrow
x = {\left(e^{\ln 5}\right)}^{\frac{1}{2}}
\Longleftrightarrow
x = {5}^{\frac{1}{2}}\\
&\Longleftrightarrow
x = \sqrt{5}.
\end{equation*}
On a donc montré que l'unique solution de l'équation [](#Eq3) est $x =  \sqrt{5}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
 
\begin{equation}
\label{Eq4}
\ln(x) = -\ln(9).
\end{equation}

}
{
\begin{python}
from sympy import *
bonne_valeur = Rational(1, 9)
\end{python}
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez les propriétés des logarithmes et la fonction exponentielle.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(bonne_valeur)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre [](#Eq4), il suffit, là encore, de prendre l'exponentielle de chaque côté de
  [](#Eq4). On a donc: 
\begin{equation*}
\ln(x) = -\ln9
&\Longleftrightarrow
x = e^{-\ln9}
\Longleftrightarrow
x = e^{\ln(9^{-1})}
\Longleftrightarrow
x =9^{-1}\\
&\Longleftrightarrow
x = \frac{1}{9}.
\end{equation*}
On a donc montré que l'unique solution de l'équation   [](#Eq4) est $x = \frac{1}{9}.$
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