```latex
\begin{exercise}{
Id: 8a7b3c2d-4e5f-6g7h-8i9j-0k1l2m3n4o5p
Title_exo: Suites géométriques et sommes
Modules: M1_10_Suites
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Suites_Numeriques
Involved_Concepts: Suites_Geometriques, Somme_Suites, Limite_Suites
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
Soit $\left(u_{n}\right)_{n \geqslant 0}$ la suite géométrique de terme initial $3$ et 
de raison $1/2$. Soit $\left(s_{n}\right)_{n \geqslant 0}$ la suite définie pour tout $n$ par

\begin{equation*}
s_{n}=u_{0}+u_{1}+\cdots+u_{n}
\end{equation*}

\begin{python}
from sympy import *
n = symbols('n')
# Calcul de l'expression explicite de u_n
u0 = 3
q = Rational(1, 2)
un_expr = u0 * q**n

# Calcul de l'expression explicite de s_n
# La formule de la somme des n+1 premiers termes d'une suite géométrique est u0 * (1 - q^(n+1)) / (1 - q)
sn_expr = u0 * (1 - q**(n + 1)) / (1 - q)
sn_simplified = simplify(sn_expr)

# Calcul de la limite de s_n
limit_sn = limit(sn_simplified, n, oo)

# Formatage pour la sortie LaTeX
un_latex = latex(un_expr)
sn_latex = latex(sn_simplified)
limit_sn_latex = latex(limit_sn)
\end{python}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Donnez l'expression explicite de $u_n$ en fonction de $n$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{un_latex}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Rappelez-vous la formule générale du $n$-ième terme d'une suite géométrique.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
L'expression explicite de $u_n$ est $\py{un_latex}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Commençons par analyser la suite géométrique $ (u_n)_{n \geqslant 0} $ donnée.

#### Étape 1 : Trouver l'expression explicite pour $ u_n $

La suite  $ (u_n)_{n \geqslant 0} $ étant géométrique, on peut exprimer le $n^{\text{ième}}$
terme de la suite en fonction de $n$ et de son premier terme, ici $u_0$:
\begin{equation*}
u_n = u_0 \cdot q^n, 
\end{equation*}
où $q$ désigne la raison de la suite   $ (u_n)_{n \geqslant 0} $.
 On a donc ici:
\begin{equation*}
u_n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n}.
\end{equation*}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Donnez l'expression explicite de $s_n$ en fonction de $n$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{sn_latex}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez la formule de la somme des termes d'une suite géométrique.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
L'expression explicite de $s_n$ est $\py{sn_latex}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
**Étape 2 : Calculer $ s_n $**

Calculons à présent la somme $ s_n $ des $ n+1 $ premiers termes de la suite $ (u_n) $. On a  : 
\begin{equation*}
\begin{align*}
s_n &= u_0 + u_1 + u_2 + \cdots + u_n \\
&= 3 + \frac{3}{2} + \frac{3}{4} + \cdots + \frac{3}{2^n}.
\end{align*}
\end{equation*}

En factorisant par $3$ la quantité précédente, nous obtenons : 
\begin{equation*}
\begin{align*}
s_n = 3\left(1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}\right) 
\end{align*}
\end{equation*}

Notons $w_n := 1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}$. Il est clair que:
\begin{equation}
\label{djdjdoij}
s_n = 3\cdot w_n
\end{equation}
et que
\begin{equation*}
w_n
=
\frac{1}{2^0} +\frac{1}{2^1} + \frac{1}{2^2}  + \cdots + \frac{1}{2^n}.
\end{equation*}

Ceci montre que $w_n$ est la somme des $n+1$ premiers termes d'une série 
géométrique de premier terme $1$ et de raison $r = \frac{1}{2}$. 

````{prfe:observ*}
```{color:black}
Soit $(a_n)_{n\geq 0}$ une suite géométrique de raison $q\neq 1$, et $N$ un entier
 strictement positif. La somme des $N$ premiers termes de la suite $(a_n)_{n\geq 0}$, notée 
$A_N$ est donnée par par la formule:
\begin{equation*}
A_N
=
u_0 \cdot \frac{1-q^{N}}{1-q}.
\end{equation*}
```
````

En utilisant le rappel précédent avec $u_0 = 1$, $q= \frac{1}{2} $,  $N = n+1$, on peut écrire:

\begin{equation*}
w_n = 1\cdot \frac{1\left(1 - \left(\frac{1}{2}\right)^{n+1}\right)}{1 - \frac{1}{2}} 
=
 \frac{1 - \frac{1}{2^{n+1}}}{\frac{1}{2}} = 2\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

En substituant cette expression dans \eqref{djdjdoij},  on obtient : 
\begin{equation*}
s_n = 3 \cdot 2\left(1 - \frac{1}{2^{n+1}}\right) = 6\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

Autrement dit, on a:
\begin{equation}
\label{oijfoij}
s_n = 6\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Déterminer la limite de la suite $\left(s_{n}\right)_{n}$ lorsque $n \rightarrow \infty$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{limit_sn_latex}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Analysez le comportement du terme $\left(\frac{1}{2}\right)^{n+1}$ lorsque $n$ tend vers l'infini.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
La limite de la suite $\left(s_{n}\right)_{n}$ est $\py{limit_sn_latex}$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Nous cherchons à déterminer la limite de $ (s_n)_{n} $ quand $ n $ tend vers l'infini. 

Repartons de l'égalité \eqref{oijfoij}. On a :
\begin{equation*}
\lim\limits_{n \rightarrow \infty} \frac{1}{2^{n+1}}
=
\lim\limits_{n \rightarrow \infty} {\left(\frac{1}{2}\right)}^{n+1}
=
0
\end{equation*}
puisque $0<\frac{1}{2}<1$. On voit donc que 
$\lim\limits_{n \rightarrow \infty} \left(1 - \frac{1}{2^{n+1}} \right)= 1$ et donc que:
\begin{equation*}
 \lim\limits_{n \rightarrow \infty} 6\left(1 - \frac{1}{2^{n+1}}\right) 
=
6.
\end{equation*}

En d'autres termes, on a montré que:
\begin{equation*}
 \lim\limits_{n \rightarrow \infty} s_n
=
6.
\end{equation*}
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