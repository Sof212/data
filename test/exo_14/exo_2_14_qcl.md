```latex
\begin{exercise}{
Id: 001
Title_exo: Résolution d'équations exponentielles et logarithmiques
Modules: M1_10_Logarithms_Exponentials
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Logarithms_Exponentials
Involved_Concepts: Exponential_Equations, Logarithmic_Equations
Original_source: null
Visibility: All
}
{
Résoudre les équations suivantes.

\qcl{
\begin{python}
from sympy import *
# Solution pour Eq1
bonne_valeur = ln(2)
\end{python}
Résoudre l'équation : $\mathrm{e}^{x} = 2$
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
La solution est $x = \ln 2$
}
{
Pour résoudre $\mathrm{e}^{x} = 2$, on prend le logarithme népérien de chaque côté :
\begin{equation*}
\mathrm{e}^{x} = 2 \Longleftrightarrow x = \ln 2
\end{equation*}
L'unique solution est donc $x = \ln 2$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Solution pour Eq2
bonne_valeur = -ln(4)
\end{python}
Résoudre l'équation : $\mathrm{e}^{x} = \frac{1}{4}$
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
La solution est $x = -\ln 4$
}
{
Pour résoudre $\mathrm{e}^{x} = \frac{1}{4}$, on prend le logarithme népérien :
\begin{equation*}
\mathrm{e}^{x} = \frac{1}{4} \Longleftrightarrow x = \ln\left(\frac{1}{4}\right) = \ln 1 - \ln 4 = -\ln 4
\end{equation*}
L'unique solution est donc $x = -\ln 4$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Solution pour Eq3
bonne_valeur = sqrt(5)
\end{python}
Résoudre l'équation : $\ln(x) = \frac{\ln(5)}{2}$
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
La solution est $x = \sqrt{5}$
}
{
Pour résoudre $\ln(x) = \frac{\ln(5)}{2}$, on prend l'exponentielle :
\begin{equation*}
\ln(x) = \frac{\ln(5)}{2} \Longleftrightarrow x = e^{\frac{\ln(5)}{2}} = \left(e^{\ln 5}\right)^{\frac{1}{2}} = 5^{\frac{1}{2}} = \sqrt{5}
\end{equation*}
L'unique solution est donc $x = \sqrt{5}$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import *
# Solution pour Eq4
bonne_valeur = Rational(1,9)
\end{python}
Résoudre l'équation : $\ln(x) = -\ln(9)$
}
{
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
La solution est $x = \frac{1}{9}$
}
{
Pour résoudre $\ln(x) = -\ln(9)$, on prend l'exponentielle :
\begin{equation*}
\ln(x) = -\ln(9) \Longleftrightarrow x = e^{-\ln9} = e^{\ln(9^{-1})} = 9^{-1} = \frac{1}{9}
\end{equation*}
L'unique solution est donc $x = \frac{1}{9}$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}
}
\end{exercise}
```