```latex
\begin{exercise}{
Title_exo: \fr{Propriétés du logarithme népérien}\en{Properties of the natural logarithm}
Modules: Analyse_NYU
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Logarithm_and_Exponential_Functions
Involved_Concepts: Logarithm_properties
Original_source:
}
{
\begin{python}
from sympy import *
bonne_valeur = ln(56)
fausse_1 = ln(15)
fausse_2 = ln(7) + ln(8) # Erreur méthodologique typique: ne pas simplifier
fausse_3 = ln(7 * 8) # Variante calcul incorrecte: laisser l'opération
\end{python}
\qcm{Exprimer l'expression suivante sous la forme $\ln (a)$, où $a>0$ : $A:= \ln (7)+\ln (8)$.}
{
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wrong{$\ln(7) \cdot \ln(8)$}
}
{
% Indice: Vous pouvez écrire une indication ci-dessous.
}
{
% Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement
positifs.

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
\end{equation}


En utilisant [](#fer1), on peut écrire:
\begin{equation*}
\begin{align*}
\ln(7) + \ln(8) = \ln(7 \cdot 8) = \ln(56).
\end{align*}
\end{equation*}
   Ainsi, nous avons $A = \ln(56)$.
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
bonne_valeur = ln(5)
fausse_1 = ln(16)
fausse_2 = ln(20) - ln(4) # Erreur méthodologique typique: ne pas simplifier
fausse_3 = ln(Rational(20,4)) # Variante calcul incorrecte: laisser l'opération
\end{python}
\qcm{Exprimer l'expression suivante sous la forme $\ln (a)$, où $a>0$ : $B:=\ln(20) - \ln(4)$.}
{
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wrong{$\ln(20) \cdot \ln(4)$}
}
{
% Indice: Vous pouvez écrire une indication ci-dessous.
}
{
% Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 En utilisant [](#fer2), on peut écrire:
\begin{equation*}
\begin{align*}
\ln(20) - \ln(4) = \ln\left(\frac{20}{4}\right) = \ln(5).
\end{align*}
\end{equation*}
   Ainsi, nous avons $B = \ln(5)$.
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
bonne_valeur = ln(7)
fausse_1 = ln(24)
fausse_2 = -ln(4) + ln(28) # Erreur méthodologique typique: ne pas simplifier
fausse_3 = ln(Rational(28,4)) # Variante calcul incorrecte: laisser l'opération
\end{python}
\qcm{Exprimer l'expression suivante sous la forme $\ln (a)$, où $a>0$ : $C := -\ln (4)+\ln (28)$.}
{
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wrong{$\ln(7) - \ln(4)$}
}
{
% Indice: Vous pouvez écrire une indication ci-dessous.
}
{
% Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
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
Ainsi, nous avons $C = \ln 7$.
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