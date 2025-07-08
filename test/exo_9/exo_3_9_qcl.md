```latex
\begin{exercise}{
Id: 001
Title_exo: Propriétés des logarithmes
Modules: M1_1_Logarithms
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Logarithms
Involved_Concepts: Logarithm_Properties
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
 Exprimer chacun des expressions suivantes sous la forme $\ln (a)$, où $a>0$.

\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur_A = 56
\end{python}

\qcl{ %% [ÉNONCÉ \qst ORIGINAL INTÉGRALEMENT REPRIS - MODIFICATION MINIMALE]
Calculer la valeur de $a$ telle que $A = \ln (7)+\ln (8) = \ln(a)$.
}
{[["CL","\py{bonne_valeur_A}"],["0"]]}
{%% Indication : Utilisez la propriété $\ln(x) + \ln(y) = \ln(xy)$.}
{%% Solution brève : La réponse est \py{bonne_valeur_A}}
{%% Solution détaillée : Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement 
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
   Ainsi, nous avons $A = \ln(56)$, donc $a=\py{bonne_valeur_A}$.
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
# Variables et calculs de la réponse exacte
bonne_valeur_B = 5
\end{python}

\qcl{ %% [ÉNONCÉ \qst ORIGINAL INTÉGRALEMENT REPRIS - MODIFICATION MINIMALE]
Calculer la valeur de $a$ telle que $B:=\ln(20) - \ln(4) = \ln(a)$.
}
{[["CL","\py{bonne_valeur_B}"],["0"]]}
{%% Indication : Utilisez la propriété $\ln(x) - \ln(y) = \ln(x/y)$.}
{%% Solution brève : La réponse est \py{bonne_valeur_B}}
{%% Solution détaillée : En utilisant la propriété $\ln(x) - \ln(y) = \ln(x/y)$, on peut écrire:  
\begin{equation*}
\begin{align*}
\ln(20) - \ln(4) = \ln\left(\frac{20}{4}\right) = \ln(5).
\end{align*}
\end{equation*}
   Ainsi, nous avons $B = \ln(5)$, donc $a=\py{bonne_valeur_B}$.
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
# Variables et calculs de la réponse exacte
bonne_valeur_C = 7
\end{python}

\qcl{ %% [ÉNONCÉ \qst ORIGINAL INTÉGRALEMENT REPRIS - MODIFICATION MINIMALE]
Calculer la valeur de $a$ telle que $C := -\ln (4)+\ln (28) = \ln(a)$.
}
{[["CL","\py{bonne_valeur_C}"],["0"]]}
{%% Indication : Réarrangez l'expression et utilisez la propriété $\ln(x) - \ln(y) = \ln(x/y)$.}
{%% Solution brève : La réponse est \py{bonne_valeur_C}}
{%% Solution détaillée : On peut reformuler l'expression $C$ en écrivant:
$C =  -\ln (4) + \ln (28) =\ln (28)-\ln (4) $.
En utilisant la propriété $\ln(x) - \ln(y) = \ln(x/y)$, on peut écrire:   
\begin{equation*}
\begin{align*}
C =  \ln (28)-\ln (4) 
= 
 \ln\left(\frac{28}{4}\right) = \ln 7.
\end{align*}
\end{equation*}
Ainsi, nous avons $C = \ln 7$, donc $a=\py{bonne_valeur_C}$.
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