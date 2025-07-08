```latex
\begin{exercise}{
Id: 001
Title_exo: Suites géométriques et sommes
Modules: M1_10_Suites
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Suites
Involved_Concepts: Suites_Geometriques, Sommes_Suites
Original_source: null
Visibility: All
}
{
\begin{python}
from sympy import *

# Variables initiales
u0 = 3
q = Rational(1, 2)

# Calculs pour u_5
n5 = 5
u5 = u0 * q**n5
u5_latex = latex(u5)

# Calculs pour s_5
s5 = u0 * (1 - q**(n5 + 1)) / (1 - q)
s5_latex = latex(s5)

# Calculs pour la limite de s_n
lim_sn = u0 / (1 - q)
lim_sn_latex = latex(lim_sn)

# Calculs pour u_10
n10 = 10
u10 = u0 * q**n10
u10_latex = latex(u10)

# Calculs pour s_10
s10 = u0 * (1 - q**(n10 + 1)) / (1 - q)
s10_latex = latex(s10)
\end{python}

Soit $\left(u_{n}\right)_{n \geqslant 0}$ la suite géométrique de terme initial $3$ et 
de raison $1/2$. Soit $\left(s_{n}\right)_{n \geqslant 0}$ la suite définie pour tout $n$ par

\begin{equation*}
s_{n}=u_{0}+u_{1}+\cdots+u_{n}
\end{equation*}

\qcl{Calculer le terme $u_5$ de la suite $\left(u_{n}\right)_{n \geqslant 0}$.}
{
[["CL","\py{u5_latex}"],["0"]]
}
{
Utilisez la formule du terme général d'une suite géométrique.
}
{
$u_5 = \py{u5_latex}$
}
{
Le terme général de la suite géométrique $\left(u_{n}\right)_{n \geqslant 0}$ est donné par :
\[ u_n = u_0 \cdot q^n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n} \]
Pour $n = 5$, on a :
\[ u_5 = \frac{3}{2^5} = \frac{3}{32} \]
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la somme $s_5$ de la suite $\left(s_{n}\right)_{n \geqslant 0}$.}
{
[["CL","\py{s5_latex}"],["0"]]
}
{
Utilisez la formule de la somme des termes d'une suite géométrique.
}
{
$s_5 = \py{s5_latex}$
}
{
La somme $s_n$ des $n+1$ premiers termes de la suite géométrique $\left(u_{n}\right)_{n \geqslant 0}$ est donnée par :
\[ s_n = u_0 \frac{1 - q^{n+1}}{1 - q} = 3 \frac{1 - \left(\frac{1}{2}\right)^{n+1}}{1 - \frac{1}{2}} = 3 \frac{1 - \frac{1}{2^{n+1}}}{\frac{1}{2}} = 6\left(1 - \frac{1}{2^{n+1}}\right) \]
Pour $n = 5$, on a :
\[ s_5 = 6\left(1 - \frac{1}{2^{6}}\right) = 6\left(1 - \frac{1}{64}\right) = 6 \cdot \frac{63}{64} = \frac{378}{64} = \frac{189}{32} \]
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la limite de la suite $\left(s_{n}\right)_{n \geqslant 0}$.}
{
[["CL","\py{lim_sn_latex}"],["0"]]
}
{
Utilisez la formule de la somme des termes d'une suite géométrique et faites tendre $n$ vers l'infini.
}
{
La limite de la suite $\left(s_{n}\right)_{n \geqslant 0}$ est $\py{lim_sn_latex}$.
}
{
La somme $s_n$ des $n+1$ premiers termes de la suite géométrique $\left(u_{n}\right)_{n \geqslant 0}$ est donnée par :
\[ s_n = 6\left(1 - \frac{1}{2^{n+1}}\right) \]
Lorsque $n$ tend vers l'infini, $\frac{1}{2^{n+1}}$ tend vers 0, donc :
\[ \lim_{n \to \infty} s_n = 6 \]
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer le terme $u_{10}$ de la suite $\left(u_{n}\right)_{n \geqslant 0}$.}
{
[["CL","\py{u10_latex}"],["0"]]
}
{
Utilisez la formule du terme général d'une suite géométrique.
}
{
$u_{10} = \py{u10_latex}$
}
{
Le terme général de la suite géométrique $\left(u_{n}\right)_{n \geqslant 0}$ est donné par :
\[ u_n = u_0 \cdot q^n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n} \]
Pour $n = 10$, on a :
\[ u_{10} = \frac{3}{2^{10}} = \frac{3}{1024} \]
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{Calculer la somme $s_{10}$ de la suite $\left(s_{n}\right)_{n \geqslant 0}$.}
{
[["CL","\py{s10_latex}"],["0"]]
}
{
Utilisez la formule de la somme des termes d'une suite géométrique.
}
{
$s_{10} = \py{s10_latex}$
}
{
La somme $s_n$ des $n+1$ premiers termes de la suite géométrique $\left(u_{n}\right)_{n \geqslant 0}$ est donnée par :
\[ s_n = 6\left(1 - \frac{1}{2^{n+1}}\right) \]
Pour $n = 10$, on a :
\[ s_{10} = 6\left(1 - \frac{1}{2^{11}}\right) = 6\left(1 - \frac{1}{2048}\right) = 6 \cdot \frac{2047}{2048} = \frac{12282}{2048} = \frac{6141}{1024} \]
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