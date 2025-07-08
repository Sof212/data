```latex
\begin{exercise}{
Id: 001
Title_exo: Simplification d'expressions logarithmiques
Modules: Logarithmes
Recommended_execution_time: 8
Ex_Level: Elementary
Chap: Fonctions usuelles
Involved_Concepts: Propriétés des logarithmes
Visibility: All
}
{
Exprimer chacune des expressions suivantes sous la forme $\ln(a)$, où $a>0$.

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = ln(56)
\end{python}
$A := \ln(7) + \ln(8)$
}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice
Utiliser la propriété $\ln(a) + \ln(b) = \ln(ab)$
}
{ % La réponse correcte est :
$\py{bonne_valeur}$
}
{ % Solution détaillée
Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement positifs :

\begin{equation}
\ln(a) + \ln(b) = \ln(ab)
\end{equation}

En utilisant cette propriété, on peut écrire :  
\begin{equation*}
\ln(7) + \ln(8) = \ln(7 \cdot 8) = \ln(56)
\end{equation*}
Ainsi, nous avons $A = \ln(56)$.
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = ln(5)
\end{python}
$B := \ln(20) - \ln(4)$
}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice
Utiliser la propriété $\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)$
}
{ % La réponse correcte est :
$\py{bonne_valeur}$
}
{ % Solution détaillée
Nous utilisons la propriété des logarithmes :
\begin{equation}
\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)
\end{equation}

On peut donc écrire :  
\begin{equation*}
\ln(20) - \ln(4) = \ln\left(\frac{20}{4}\right) = \ln(5)
\end{equation*}
Ainsi, nous avons $B = \ln(5)$.
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = ln(7)
\end{python}
$C := -\ln(4) + \ln(28)$
}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice
Commencer par réordonner les termes puis utiliser les propriétés des logarithmes
}
{ % La réponse correcte est :
$\py{bonne_valeur}$
}
{ % Solution détaillée
On peut reformuler l'expression $C$ en écrivant :
\begin{equation*}
C = -\ln(4) + \ln(28) = \ln(28) - \ln(4)
\end{equation*}

En utilisant la propriété :
\begin{equation}
\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)
\end{equation}

On obtient :  
\begin{equation*}
C = \ln\left(\frac{28}{4}\right) = \ln(7)
\end{equation*}
Ainsi, nous avons $C = \ln(7)$.
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