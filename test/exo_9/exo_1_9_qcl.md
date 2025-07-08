```latex
\begin{exercise}{
Id: 001
Title_exo: Expressions logarithmiques
Modules: M1_1_Logarithms % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Logarithms % NameID des chapitres
Involved_Concepts: Logarithm_Properties % ID ou NameID des notions
Original_source: null % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
}
{
% Contenu de l'exercice
 Exprimer chacun des expressions suivantes sous la forme $\ln (a)$, où $a>0$.

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = ln(56)
\end{python}
$A:= \ln (7)+\ln (8)$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{latex(bonne_valeur)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(bonne_valeur)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement 
positifs.% et pour tout entier $k\geq 1$.

\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
%
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
%[](#fer1) et aussi [](#fer2)
\end{equation}


En utilisant [](#fer1), on peut écrire:  
\begin{equation*}
\begin{align*}
\ln(7) + \ln(8) = \ln(7 \cdot 8) = \ln(56).
\end{align*}
\end{equation*}
   Ainsi, nous avons $A = \py{latex(bonne_valeur)}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = ln(5)
\end{python}
$B:=\ln(20) - \ln(4)$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{latex(bonne_valeur)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(bonne_valeur)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 En utilisant [](#fer2), on peut écrire:  
\begin{equation*}
\begin{align*}
\ln(20) - \ln(4) = \ln\left(\frac{20}{4}\right) = \ln(5).
\end{align*}
\end{equation*}
   Ainsi, nous avons $B = \py{latex(bonne_valeur)}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = ln(7)
\end{python}
$C := -\ln (4)+\ln (28)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{latex(bonne_valeur)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(bonne_valeur)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 On peut reformuler l'expression $C$ en écrivant:
$C =  -\ln (4) + \ln (28) =\ln (28)-\ln (4) $.
En utilisant [](#fer2), on peut écrire:   
\begin{equation*}
\begin{align*}
C =  \ln (28)-\ln (4) 
= 
 \ln\left(\frac{28}{4}\right) = \ln 7.
\end{align*}
\end{equation*}
Ainsi, nous avons $C = \py{latex(bonne_valeur)}$.
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