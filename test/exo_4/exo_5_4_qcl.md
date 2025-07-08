

\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts : % ID ou NameID des notions
}
{


\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python

import sympy as sp
import numpy as np

n = sp.Symbol('n', integer=True, positive=True)


s_n = 6 * (1 - 1/(2**(n+1)))

\end{python}

% Contenu de l'exercice
Soit $\left(u_{n}\right)_{n \geqslant 0}$ la suite géométrique de terme initial 3 et de raison $1 / 2$. Soit $\left(s_{n}\right)_{n \geqslant 0}$ la suite définie pour tout $n$ par

\begin{equation*}
s_{n}=u_{0}+u_{1}+\cdots+u_{n}
\end{equation*}
\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Mettre $\left(s_{n}\right)_{n}$ sous forme explicite (\ie exprimez $u_n$ en fonction de $n$, pour tout $n$).
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{sp.latex(s_n)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
Pour tout $n\geq 0$, $s_n = 6\left(1 - \frac{1}{2^{n+1}}\right)$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Commençons par analyser la suite géométrique $ (u_n)_{n \geqslant 0} $ donnée.

#### Étape 1 : Trouver l'expression explicite de $ u_n $.

La suite  $ (u_n)_{n \geqslant 0} $ étant géométrique, on peut exprimer le $n^{\text{ième}}$
terme de la suite en fonction de $n$ et de son premier terme, ici $u_0$:
\begin{equation*}
u_n = u_0 \cdot q^n, 
\end{equation*}
où $q$ désigne la raison de la suite   $ (u_n)_{n \geqslant 0} $.
 On a donc ici:
\begin{equation*}
u_n = u_0 \cdot q^n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n}.
\end{equation*}

**Étape 2 : Calculer $ s_n $**

Calculons à présent la somme $ s_n $ des $ n $ premiers termes de la suite $ (u_n) $. On a  : 
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
%On peut écrire:
\begin{equation*}
w_n
=
\frac{1}{2^0} +\frac{1}{2^1} + \frac{1}{2^2}  + \cdots + \frac{1}{2^n}.
\end{equation*}

Ceci montre que $w_n$ est la somme des $n+1$ premiers termes d'une série 
géométrique de premier terme $1$ et de raison $r = \frac{1}{2}$. 

%ceci est une observation
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

En utilisant le rappel précédent avec $u_0 = 3$, $q= \frac{1}{2} $,  $N = n+1$, on peut écrire:

\begin{equation*}
w_n = 3\cdot \frac{1\left(1 - \left(\frac{1}{2}\right)^{n+1}\right)}{1 - \frac{1}{2}} 
=
 \frac{1 - \frac{1}{2^{n+1}}}{\frac{1}{2}} = 2\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

En substituant cette expression dans [](djdjdoij),  on obtient : 
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
Déterminer la limite de $\left(s_{n}\right)_{n}$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","6"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$6$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%Nous cherchons à déterminer la limite de $ (s_n)_{n} $ quand $ n $ tend vers l'infini. 

Repartons de l'égalité [](oijfoij). On a :%Puisque 
\begin{equation*}
\lim\limits_{n \rightarrow \infty} \frac{1}{2^{n+1}}
=
\lim\limits_{n \rightarrow \infty} {\left(\frac{1}{2}\right)}^{n+1}
=
0
%s_n = 6\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}
puisque $0<\frac{1}{2}<1$. On voit donc que que 
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
