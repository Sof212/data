```latex
\begin{exercise}{
Title_exo: \fr{Suites géométriques et sommes}\en{Geometric sequences and sums}
Modules: Suites_Numeriques % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Suites_Geometriques % NameID des chapitres
Involved_Concepts: Suite_Geometrique, Somme_Suite_Geometrique, Limite_Suite % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
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
# === Calcul bonne réponse (extraite corrigé original) ===
n = symbols('n')
bonne_valeur = 6 * (1 - Rational(1, 2)**(n + 1))
bonne_valeur_latex = latex(bonne_valeur)

# === Propositions fausses calculées ===
fausse_1 = 3 * (1 - Rational(1, 2)**(n + 1)) # Erreur sur le premier terme
fausse_1_latex = latex(fausse_1)

fausse_2 = 6 * (1 - Rational(1, 2)**n) # Erreur sur l'exposant (n au lieu de n+1)
fausse_2_latex = latex(fausse_2)

fausse_3 = 3 * (1 - Rational(1, 2)**n) # Combinaison des deux erreurs précédentes
fausse_3_latex = latex(fausse_3)

fausse_4 = 6 * (1 + Rational(1, 2)**(n + 1)) # Erreur de signe
fausse_4_latex = latex(fausse_4)

fausse_5 = 3 * (1 + Rational(1, 2)**(n + 1)) # Erreur de signe et de premier terme
fausse_5_latex = latex(fausse_5)
\end{python}
\qcm{
\fr{Mettre $\left(s_{n}\right)_{n}$ sous forme explicite.}
\en{Express $\left(s_{n}\right)_{n}$ in explicit form.}
}
{
\right{$\displaystyle \mathbf{s_n = \sympy{bonne_valeur_latex}}$}
\wrong{$\displaystyle \mathbf{s_n = \sympy{fausse_1_latex}}$}
\wrong{$\displaystyle \mathbf{s_n = \sympy{fausse_2_latex}}$}
\wrong{$\displaystyle \mathbf{s_n = \sympy{fausse_3_latex}}$}
\wrong{$\displaystyle \mathbf{s_n = \sympy{fausse_4_latex}}$}
\wrong{$\displaystyle \mathbf{s_n = \sympy{fausse_5_latex}}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
\fr{Rappelez-vous la formule de la somme des termes d'une suite géométrique.}
\en{Recall the formula for the sum of terms in a geometric sequence.}
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
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
u_n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n}.
\end{equation*}

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
Soit $(a_k)_{k\geq 0}$ une suite géométrique de raison $q\neq 1$. La somme des $N$ premiers termes de la suite $(a_k)_{k\geq 0}$, notée 
$A_{N-1} = a_0 + \dots + a_{N-1}$ est donnée par la formule:
\begin{equation*}
A_{N-1}
=
a_0 \cdot \frac{1-q^{N}}{1-q}.
\end{equation*}
```
````

En utilisant le rappel précédent avec $a_0 = 1$, $q= \frac{1}{2} $,  $N = n+1$ (car il y a $n+1$ termes de $u_0$ à $u_n$), on peut écrire:

\begin{equation*}
w_n = 1 \cdot \frac{1\left(1 - \left(\frac{1}{2}\right)^{n+1}\right)}{1 - \frac{1}{2}} 
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
\en{Let's start by analyzing the given geometric sequence $ (u_n)_{n \geqslant 0} $.

#### Step 1: Find the explicit expression for $ u_n $

Since $ (u_n)_{n \geqslant 0} $ is a geometric sequence, we can express the $n^{\text{th}}$ term of the sequence in terms of $n$ and its first term, here $u_0$:
\begin{equation*}
u_n = u_0 \cdot q^n, 
\end{equation*}
where $q$ denotes the common ratio of the sequence $ (u_n)_{n \geqslant 0} $.
So here we have:
\begin{equation*}
u_n = 3 \cdot \left(\frac{1}{2}\right)^n = \frac{3}{2^n}.
\end{equation*}

**Step 2: Calculate $ s_n $**

Now let's calculate the sum $ s_n $ of the first $ n+1 $ terms of the sequence $ (u_n) $. We have: 
\begin{equation*}
\begin{align*}
s_n &= u_0 + u_1 + u_2 + \cdots + u_n \\
&= 3 + \frac{3}{2} + \frac{3}{4} + \cdots + \frac{3}{2^n}.
\end{align*}
\end{equation*}

By factoring out $3$ from the previous quantity, we get: 
\begin{equation*}
\begin{align*}
s_n = 3\left(1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}\right) 
\end{align*}
\end{equation*}

Let $w_n := 1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}$. It is clear that:
\begin{equation}
\label{djdjdoij_en}
s_n = 3\cdot w_n
\end{equation}
and that
\begin{equation*}
w_n
=
\frac{1}{2^0} +\frac{1}{2^1} + \frac{1}{2^2}  + \cdots + \frac{1}{2^n}.
\end{equation*}

This shows that $w_n$ is the sum of the first $n+1$ terms of a geometric series with first term $1$ and common ratio $r = \frac{1}{2}$. 

````{prfe:observ*}
```{color:black}
Let $(a_k)_{k\geq 0}$ be a geometric sequence with common ratio $q\neq 1$, and $N$ a positive integer. The sum of the first $N$ terms of the sequence $(a_k)_{k\geq 0}$, denoted 
$A_{N-1} = a_0 + \dots + a_{N-1}$ is given by the formula:
\begin{equation*}
A_{N-1}
=
a_0 \cdot \frac{1-q^{N}}{1-q}.
\end{equation*}
```
````

Using the previous reminder with $a_0 = 1$, $q= \frac{1}{2} $,  $N = n+1$ (because there are $n+1$ terms from $u_0$ to $u_n$), we can write:

\begin{equation*}
w_n = 1 \cdot \frac{1\left(1 - \left(\frac{1}{2}\right)^{n+1}\right)}{1 - \frac{1}{2}} 
=
 \frac{1 - \frac{1}{2^{n+1}}}{\frac{1}{2}} = 2\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

Substituting this expression into \eqref{djdjdoij_en}, we get: 
\begin{equation*}
s_n = 3 \cdot 2\left(1 - \frac{1}{2^{n+1}}\right) = 6\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

In other words, we have:
\begin{equation}
\label{oijfoij_en}
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

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur_lim = 6
bonne_valeur_lim_latex = latex(bonne_valeur_lim)

# === Propositions fausses calculées ===
fausse_lim_1 = 3 # Erreur sur le premier terme
fausse_lim_1_latex = latex(fausse_lim_1)

fausse_lim_2 = 0 # Erreur de calcul (limite de la fraction)
fausse_lim_2_latex = latex(fausse_lim_2)

fausse_lim_3 = oo # Erreur conceptuelle (suite divergente)
fausse_lim_3_latex = latex(fausse_lim_3)

fausse_lim_4 = -oo # Erreur conceptuelle (suite divergente)
fausse_lim_4_latex = latex(fausse_lim_4)

fausse_lim_5 = 12 # Erreur de calcul (multiplication par 2 au lieu de 1/2)
fausse_lim_5_latex = latex(fausse_lim_5)
\end{python}
\qcm{
\fr{Déterminer la limite de la suite $\left(s_{n}\right)_{n}$.}
\en{Determine the limit of the sequence $\left(s_{n}\right)_{n}$.}
}
{
\right{$\displaystyle \mathbf{\sympy{bonne_valeur_lim_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{fausse_lim_1_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{fausse_lim_2_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{fausse_lim_3_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{fausse_lim_4_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{fausse_lim_5_latex}}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
\fr{Utilisez l'expression explicite de $s_n$ trouvée précédemment et la limite d'une suite géométrique de raison $q$ avec $|q|<1$.}
\en{Use the explicit expression for $s_n$ found previously and the limit of a geometric sequence with common ratio $q$ where $|q|<1$.}
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
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
\end{equation*}
}
\en{We want to determine the limit of $ (s_n)_{n} $ as $ n $ approaches infinity. 

Let's start from equation \eqref{oijfoij_en}. We have:
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