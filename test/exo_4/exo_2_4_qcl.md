```latex
\begin{exercise}{
Id: 8a9b0c7d-1e2f-3g4h-5i6j-7k8l9m0n1o2p
Title_exo: Suites géométriques et sommes partielles
Modules: Suites, Séries
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Suites numériques
Involved_Concepts: Suite géométrique, Somme partielle, Limite de suite
Visibility: All
}
{
\begin{python}
from sympy import *
n = symbols('n', integer=True, positive=True)
u0 = 3
q = Rational(1,2)
un = u0 * q**n
sn = u0 * (1 - q**(n+1)) / (1 - q)
limite_sn = limit(sn, n, oo)
# Calcul pour la question a
val_a = simplify(sn / (1 - 1/(2**(n+1))))
# Calcul pour la question b
val_b = 2
# Calcul pour la question c
val_c = 1
# Calcul pour s_5
s5_val = sn.subs(n, 5)
\end{python}

\qcl{
Soit $(u_n)_{n \geqslant 0}$ la suite géométrique de terme initial $3$ et de raison $\frac{1}{2}$. 
Soit $(s_n)_{n \geqslant 0}$ la suite définie par $s_n = u_0 + u_1 + \cdots + u_n$.

Calculer l'expression explicite de $s_n$ sous la forme $a\left(1 - \frac{1}{b^{n+c}}\right)$ et donner la valeur de $a$.
}
{
[["CL","\py{val_a}"],["0"]]
}
{
Pensez à la formule de la somme des termes d'une suite géométrique.
}
{
La valeur de $a$ est \py{val_a}.
}
{
Commençons par analyser la suite géométrique $(u_n)_{n \geqslant 0}$ donnée.

\subsection*{Étape 1 : Expression de $u_n$}
La suite étant géométrique :
\begin{equation*}
u_n = u_0 \cdot q^n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n}
\end{equation*}

\subsection*{Étape 2 : Calcul de $s_n$}
La somme $s_n$ des $n+1$ premiers termes est :
\begin{equation*}
s_n = 3\left(1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}\right)
\end{equation*}

En utilisant la formule de la somme géométrique :
\begin{equation*}
s_n = 3 \cdot \frac{1 - \left(\frac{1}{2}\right)^{n+1}}{1 - \frac{1}{2}} = 6\left(1 - \frac{1}{2^{n+1}}\right)
\end{equation*}

La valeur de $a$ dans l'expression $a\left(1 - \frac{1}{b^{n+c}}\right)$ est donc $6$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Pour la même suite $(s_n)$, donner la valeur de $b$ dans l'expression $6\left(1 - \frac{1}{b^{n+c}}\right)$.
}
{
[["CL","\py{val_b}"],["0"]]
}
{
Examinez le dénominateur dans l'expression de $s_n$.
}
{
La valeur de $b$ est \py{val_b}.
}
{
D'après le calcul précédent, nous avons obtenu :
\begin{equation*}
s_n = 6\left(1 - \frac{1}{2^{n+1}}\right)
\end{equation*}

La valeur de $b$ est donc clairement $2$, qui correspond à l'inverse de la raison de la suite géométrique.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Pour la même suite $(s_n)$, donner la valeur de $c$ dans l'expression $6\left(1 - \frac{1}{2^{n+c}}\right)$.
}
{
[["CL","\py{val_c}"],["0"]]
}
{
Observez l'exposant du dénominateur dans l'expression développée.
}
{
La valeur de $c$ est \py{val_c}.
}
{
En comparant l'expression obtenue :
\begin{equation*}
s_n = 6\left(1 - \frac{1}{2^{n+1}}\right)
\end{equation*}
avec la forme générale $6\left(1 - \frac{1}{2^{n+c}}\right)$, on voit immédiatement que $c = 1$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Calculer la limite de la suite $(s_n)_{n \geqslant 0}$ lorsque $n$ tend vers $+\infty$.
}
{
[["CL","\py{limite_sn}"],["0"]]
}
{
Que devient le terme $\frac{1}{2^{n+1}}$ quand $n$ devient très grand ?
}
{
La limite est \py{limite_sn}.
}
{
Nous avons l'expression :
\begin{equation*}
s_n = 6\left(1 - \frac{1}{2^{n+1}}\right)
\end{equation*}

Quand $n \to +\infty$, $\frac{1}{2^{n+1}} \to 0$ car $0 < \frac{1}{2} < 1$.

Donc :
\begin{equation*}
\lim_{n \to +\infty} s_n = 6(1 - 0) = 6
\end{equation*}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
Calculer la valeur exacte de $s_5$ (somme des 6 premiers termes).
}
{
[["CL","\py{latex(s5_val)}"],["0"]]
}
{
Utilisez la formule explicite de $s_n$ avec $n=5$.
}
{
La valeur est \py{latex(s5_val)}.
}
{
En utilisant la formule :
\begin{equation*}
s_5 = 6\left(1 - \frac{1}{2^{6}}\right) = 6\left(1 - \frac{1}{64}\right) = 6 \times \frac{63}{64} = \frac{378}{64} = \frac{189}{32}
\end{equation*}

On peut aussi calculer directement la somme :
\begin{equation*}
3 + \frac{3}{2} + \frac{3}{4} + \frac{3}{8} + \frac{3}{16} + \frac{3}{32} = \frac{96}{32} + \frac{48}{32} + \frac{24}{32} + \frac{12}{32} + \frac{6}{32} + \frac{3}{32} = \frac{189}{32}
\end{equation*}
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