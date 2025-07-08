```latex
\begin{exercise}{
Title_exo: \fr{Équations avec exponentielles et logarithmes}\en{Equations with exponentials and logarithms}
Modules: Analyse_NYU
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Fonctions_exponentielles_et_logarithmes
Involved_Concepts: Logarithm, Exponential
Original_source:
}
{
\begin{python}
from sympy import *
bonne_valeur = log(2)
fausse_1 = 2
fausse_2 = log(4)
fausse_3 = log(2) + 1
\end{python}
\qcm{\fr{Résoudre l'équation $\mathrm{e}^{x} = 2$.}\en{Solve the equation $\mathrm{e}^{x} = 2$.}}
{
\right{$x = \ln 2$}
\wrong{$x = 2$}
\wrong{$x = \ln 4$}
\wrong{$x = \ln 2 + 1$}
}
{
}
{
\fr{Pour résoudre $\mathrm{e}^{x} = 2$, et puisqu'on peut prendre le logarithme de $2$, il suffit de prendre le logarithme népérien de chaque côté de l'équation. On a donc:
\begin{equation*}
\mathrm{e}^{x} = 2 \Longleftrightarrow x = \ln 2.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x = \ln 2$.}\en{To solve $\mathrm{e}^{x} = 2$, and since we can take the logarithm of $2$, we just need to take the natural logarithm of each side of the equation. So we have:
\begin{equation*}
\mathrm{e}^{x} = 2 \Longleftrightarrow x = \ln 2.
\end{equation*}
We have thus shown that the unique solution to the equation is $x = \ln 2$.}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\begin{python}
from sympy import *
bonne_valeur = -log(4)
fausse_1 = log(4)
fausse_2 = -log(2)
fausse_3 = log(2)
\end{python}
\qcm{\fr{Résoudre l'équation $\mathrm{e}^{x} = \frac{1}{4}$.}\en{Solve the equation $\mathrm{e}^{x} = \frac{1}{4}$.}}
{
\right{$x = - \ln 4$}
\wrong{$x = \ln 4$}
\wrong{$x = - \ln 2$}
\wrong{$x = \ln 2$}
}
{
}
{
\fr{Pour résoudre $\mathrm{e}^{x} = \frac{1}{4}$, et puisqu'on peut prendre le logarithme de $\frac{1}{4}$, il suffit de prendre le logarithme népérien de chaque côté de l'équation. On a donc:
\begin{equation*}
\mathrm{e}^{x} = \frac{1}{4} \Longleftrightarrow x = \ln\left(\frac{1}{4}\right) \Longleftrightarrow x = \ln 1 - \ln 4 \Longleftrightarrow x = - \ln 4.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x = - \ln 4$.}\en{To solve $\mathrm{e}^{x} = \frac{1}{4}$, and since we can take the logarithm of $\frac{1}{4}$, we just need to take the natural logarithm of each side of the equation. So we have:
\begin{equation*}
\mathrm{e}^{x} = \frac{1}{4} \Longleftrightarrow x = \ln\left(\frac{1}{4}\right) \Longleftrightarrow x = \ln 1 - \ln 4 \Longleftrightarrow x = - \ln 4.
\end{equation*}
We have thus shown that the unique solution to the equation is $x = - \ln 4$.}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\begin{python}
from sympy import *
bonne_valeur = sqrt(5)
fausse_1 = log(5)/2
fausse_2 = exp(log(5))
fausse_3 = 5
\end{python}
\qcm{\fr{Résoudre l'équation $\ln(x) = \frac{\ln(5)}{2}$.}\en{Solve the equation $\ln(x) = \frac{\ln(5)}{2}$.}}
{
\right{$x = \sqrt{5}$}
\wrong{$x = \frac{\ln(5)}{2}$}
\wrong{$x = e^{\ln(5)}$}
\wrong{$x = 5$}
}
{
}
{
\fr{Pour résoudre $\ln(x) = \frac{\ln(5)}{2}$, il suffit de prendre l'exponentielle de chaque côté de l'équation. On a donc:
\begin{equation*}
\ln(x) = \frac{\ln(5)}{2} \Longleftrightarrow x = e^{\frac{\ln(5)}{2}} \Longleftrightarrow x = {\left(e^{\ln 5}\right)}^{\frac{1}{2}} \Longleftrightarrow x = {5}^{\frac{1}{2}} \Longleftrightarrow x = \sqrt{5}.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x = \sqrt{5}$.}\en{To solve $\ln(x) = \frac{\ln(5)}{2}$, we just need to take the exponential of each side of the equation. So we have:
\begin{equation*}
\ln(x) = \frac{\ln(5)}{2} \Longleftrightarrow x = e^{\frac{\ln(5)}{2}} \Longleftrightarrow x = {\left(e^{\ln 5}\right)}^{\frac{1}{2}} \Longleftrightarrow x = {5}^{\frac{1}{2}} \Longleftrightarrow x = \sqrt{5}.
\end{equation*}
We have thus shown that the unique solution to the equation is $x = \sqrt{5}$.}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\begin{python}
from sympy import *
bonne_valeur = Rational(1, 9)
fausse_1 = Rational(-1, 9)
fausse_2 = 9
fausse_3 = -9
\end{python}
\qcm{\fr{Résoudre l'équation $\ln(x) = -\ln(9)$.}\en{Solve the equation $\ln(x) = -\ln(9)$.}}
{
\right{$x = \frac{1}{9}$}
\wrong{$x = -\frac{1}{9}$}
\wrong{$x = 9$}
\wrong{$x = -9$}
}
{
}
{
\fr{Pour résoudre $\ln(x) = -\ln(9)$, il suffit de prendre l'exponentielle de chaque côté de l'équation. On a donc:
\begin{equation*}
\ln(x) = -\ln(9) \Longleftrightarrow x = e^{-\ln(9)} \Longleftrightarrow x = e^{\ln(9^{-1})} \Longleftrightarrow x = 9^{-1} \Longleftrightarrow x = \frac{1}{9}.
\end{equation*}
On a donc montré que l'unique solution de l'équation est $x = \frac{1}{9}$.}\en{To solve $\ln(x) = -\ln(9)$, we just need to take the exponential of each side of the equation. So we have:
\begin{equation*}
\ln(x) = -\ln(9) \Longleftrightarrow x = e^{-\ln(9)} \Longleftrightarrow x = e^{\ln(9^{-1})} \Longleftrightarrow x = 9^{-1} \Longleftrightarrow x = \frac{1}{9}.
\end{equation*}
We have thus shown that the unique solution to the equation is $x = \frac{1}{9}$.}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}
}
\end{exercise}
```