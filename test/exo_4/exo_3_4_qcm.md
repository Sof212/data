```latex
\begin{exercise}{
Title_exo: \fr{Suites géométriques et sommes}\en{Geometric sequences and sums}
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Sequences, Series % NameID des chapitres
Involved_Concepts: Geometric_sequence, Sum_of_series, Limit_of_sequence % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Conversion d'un exercice QST en QCM. L'exercice original a été divisé en deux questions pour une meilleure granularité.
}
{ % Contenu de l'exercice

Soit $\left(u_{n}\right)_{n \geqslant 0}$ la suite géométrique de terme initial $3$ et 
de raison $1/2$. Soit $\left(s_{n}\right)_{n \geqslant 0}$ la suite définie pour tout $n$ par

\begin{equation*}
s_{n}=u_{0}+u_{1}+\cdots+u_{n}
\end{equation*}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
u0 = 3
q = Rational(1, 2)
n_sym = symbols('n')
bonne_sn_expr = u0 * (1 - q**(n_sym + 1)) / (1 - q)
bonne_sn_expr = simplify(bonne_sn_expr)
# === Propositions fausses calculées ===
fausse_sn_1 = u0 * (1 + q**(n_sym + 1)) / (1 - q) # Erreur méthodologique typique (signe)
fausse_sn_1 = simplify(fausse_sn_1)
fausse_sn_2 = u0 * (1 - q**n_sym) / (1 - q) # Variante calcul incorrecte (nombre de termes)
fausse_sn_2 = simplify(fausse_sn_2)
fausse_sn_3 = u0 * q * (1 - q**(n_sym + 1)) / (1 - q) # Approximation erronée (premier terme)
fausse_sn_3 = simplify(fausse_sn_3)
fausse_sn_4 = (1 - q**(n_sym + 1)) / (1 - q) # Oubli du facteur u0
fausse_sn_4 = simplify(fausse_sn_4)
\end{python}
\qcm{ % Enoncé de la question
\fr{Mettre $\left(s_{n}\right)_{n}$ sous forme explicite.}
\en{Express $\left(s_{n}\right)_{n}$ in explicit form.}
}
{
\right{$s_n = \sympy{bonne_sn_expr}$}
\wrong{$s_n = \sympy{fausse_sn_1}$}
\wrong{$s_n = \sympy{fausse_sn_2}$}
\wrong{$s_n = \sympy{fausse_sn_3}$}
\wrong{$s_n = \sympy{fausse_sn_4}$}
}
{ % Indice
\fr{Rappelez-vous la formule de la somme des $n+1$ premiers termes d'une suite géométrique de premier terme $u_0$ et de raison $q$: $S_{n} = u_0 \frac{1-q^{n+1}}{1-q}$.}
\en{Recall the formula for the sum of the first $n+1$ terms of a geometric sequence with first term $u_0$ and common ratio $q$: $S_{n} = u_0 \frac{1-q^{n+1}}{1-q}$.}
}
{ % Solution détaillée
\fr{Commençons par analyser la suite géométrique $ (u_n)_{n \geqslant 0} $ donnée.

#### Étape 1 : Trouver l'expression explicite pour $ u_n $

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

En utilisant la formule de la somme des termes d'une suite géométrique avec $u_0 = 1$, $q= \frac{1}{2} $,  $N = n+1$, on peut écrire:

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
\end{equation}}
\en{Let's start by analyzing the given geometric sequence $ (u_n)_{n \geqslant 0} $.

#### Step 1: Find the explicit expression for $ u_n $

Since the sequence $ (u_n)_{n \geqslant 0} $ is geometric, we can express the $n^{\text{th}}$
term of the sequence in terms of $n$ and its first term, here $u_0$:
\begin{equation*}
u_n = u_0 \cdot q^n, 
\end{equation*}
where $q$ denotes the common ratio of the sequence $ (u_n)_{n \geqslant 0} $.
So we have:
\begin{equation*}
u_n = u_0 \cdot q^n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n}.
\end{equation*}

**Step 2: Calculate $ s_n $**

Now let's calculate the sum $ s_n $ of the first $ n $ terms of the sequence $ (u_n) $. We have: 
\begin{equation*}
\begin{align*}
s_n &= u_0 + u_1 + u_2 + \cdots + u_n \\
&= 3 + \frac{3}{2} + \frac{3}{4} + \cdots + \frac{3}{2^n}.
\end{align*}
\end{equation*}

Factoring out $3$ from the previous quantity, we get: 
\begin{equation*}
\begin{align*}
s_n = 3\left(1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}\right) 
\end{align*}
\end{equation*}

Let $w_n := 1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}$. It is clear that:
\begin{equation}
\label{djdjdoij}
s_n = 3\cdot w_n
\end{equation}
and that
\begin{equation*}
w_n
=
\frac{1}{2^0} +\frac{1}{2^1} + \frac{1}{2^2}  + \cdots + \frac{1}{2^n}.
\end{equation*}

This shows that $w_n$ is the sum of the first $n+1$ terms of a geometric series 
with first term $1$ and common ratio $r = \frac{1}{2}$. 

Using the formula for the sum of terms of a geometric sequence with $u_0 = 1$, $q= \frac{1}{2} $,  $N = n+1$, we can write:

\begin{equation*}
w_n = 1\cdot \frac{1\left(1 - \left(\frac{1}{2}\right)^{n+1}\right)}{1 - \frac{1}{2}} 
=
 \frac{1 - \frac{1}{2^{n+1}}}{\frac{1}{2}} = 2\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

Substituting this expression into \eqref{djdjdoij}, we get: 
\begin{equation*}
s_n = 3 \cdot 2\left(1 - \frac{1}{2^{n+1}}\right) = 6\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

In other words, we have:
\begin{equation}
\label{oijfoij}
s_n = 6\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation}}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
u0 = 3
q = Rational(1, 2)
n_sym = symbols('n')
bonne_sn_expr = u0 * (1 - q**(n_sym + 1)) / (1 - q)
bonne_sn_expr = simplify(bonne_sn_expr)
bonne_limite = limit(bonne_sn_expr, n_sym, oo)
# === Propositions fausses calculées ===
fausse_limite_1 = u0 # Erreur méthodologique typique (premier terme)
fausse_limite_2 = 0 # Variante calcul incorrecte (limite de q^n)
fausse_limite_3 = oo # Approximation erronée (divergence)
fausse_limite_4 = 1 # Autre erreur de calcul
\end{python}
\qcm{ % Enoncé de la question
\fr{Déterminer la limite de la suite $\left(s_{n}\right)_{n}$.}
\en{Determine the limit of the sequence $\left(s_{n}\right)_{n}$.}
}
{
\right{$\sympy{bonne_limite}$}
\wrong{$\sympy{fausse_limite_1}$}
\wrong{$\sympy{fausse_limite_2}$}
\wrong{$\sympy{fausse_limite_3}$}
\wrong{$\sympy{fausse_limite_4}$}
}
{ % Indice
\fr{Utilisez l'expression explicite de $s_n$ trouvée précédemment et rappelez-vous que $\lim_{n \to \infty} q^n = 0$ si $|q| < 1$.}
\en{Use the explicit expression for $s_n$ found previously and recall that $\lim_{n \to \infty} q^n = 0$ if $|q| < 1$.}
}
{ % Solution détaillée
\fr{Nous cherchons à déterminer la limite de $ (s_n)_{n} $ quand $ n $ tend vers l'infini. 

Repartons de l'égalité \eqref{oijfoij}. On a :
\begin{equation*}
\lim\limits_{n \rightarrow \infty} \frac{1}{2^{n+1}}
=
\lim\limits_{n \rightarrow \infty} {\left(\frac{1}{2}\right)}^{n+1}
=
0
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
\end{equation*}}
\en{We want to determine the limit of $ (s_n)_{n} $ as $ n $ approaches infinity. 

Let's start from equality \eqref{oijfoij}. We have:
\begin{equation*}
\lim\limits_{n \rightarrow \infty} \frac{1}{2^{n+1}}
=
\lim\limits_{n \rightarrow \infty} {\left(\frac{1}{2}\right)}^{n+1}
=
0
\end{equation*}
since $0<\frac{1}{2}<1$. We therefore see that 
$\lim\limits_{n \rightarrow \infty} \left(1 - \frac{1}{2^{n+1}} \right)= 1$ and thus:
\begin{equation*}
 \lim\limits_{n \rightarrow \infty} 6\left(1 - \frac{1}{2^{n+1}}\right) 
=
6.
\end{equation*}

In other words, we have shown that:
\begin{equation*}
 \lim\limits_{n \rightarrow \infty} s_n
=
6.
\end{equation*}}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

}
\end{exercise}
```