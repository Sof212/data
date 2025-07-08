```latex
\begin{exercise}{
Id: 001
Title_exo: Calcul de limites
Modules: M1_1_Analyse
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Limites
Involved_Concepts: Limite_fonction, Limite_infinie
}
{
Déterminer les limites suivantes.

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
bonne_valeur = -oo
\end{python}
$\lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x+4}\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Analysez le signe du dénominateur lorsque $x$ approche $2$ par la droite.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{bonne_valeur}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 Tout d'abord, nous remarquons que : $-2x + 4$ en $4 - 2x$.  Par ailleurs, lorsque $x$ tend vers $2^{+}$
 (valeurs légèrement supérieures à $2$), on a :
\begin{equation*}
   4 - 2(2^{+}) = 4 - 4^{+} = 0^{-}.
\end{equation*}
   En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la droite, nous avons : 
\begin{equation*}
   4 - 2x < 0 \quad \text{(pour } x > 2 \text{)} 
\end{equation*}
   Ce qui implique que $-2x + 4 < 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $-\infty$, lorsque $x$ tend vers $2$ par valeurs supérieures (\ie par la droite). Donc : 
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x + 4}\right) = -\infty.
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
\begin{python}
from sympy import *
bonne_valeur = oo
\end{python}
$\lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x+4}\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Analysez le signe du dénominateur lorsque $x$ approche $2$ par la gauche.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{bonne_valeur}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
  Lorsque $x$ tend vers $2^{-}$
 (valeurs légèrement inférieures à $2$), on a :
\begin{equation*}
   - 2(2^{-}) + 4 = 4 - 2(2^{-}) = 4 - 4^{-} = 0^{+}.
\end{equation*}
   En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la gauche, nous avons : 
\begin{equation*}
   - 2x + 4 > 0 \quad \text{(pour } x < 2 \text{)} 
\end{equation*}
   Ce qui implique que $-2x + 4 > 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $+\infty$, lorsque $x$ tend vers $2$ par valeurs inférieures (\ie par la gauche). Donc : 
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x + 4}\right) = +\infty.
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
\begin{python}
from sympy import *
bonne_valeur = oo
\end{python}
$\lim\limits_{x \rightarrow 0^{+}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Évaluez chaque facteur séparément lorsque $x$ approche $0$ par la droite.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{bonne_valeur}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 Analysons l'expression $  \left(2+\frac{1}{\sqrt{x}}\right)(2x+1) $ à mesure que $x$
 tend vers $0^{+}$.
Lorsque $x \rightarrow 0^{+}$, on a :
\begin{itemize}
    \item $\frac{1}{\sqrt{x}} \rightarrow +\infty$, donc $2+\frac{1}{\sqrt{x}} \rightarrow +\infty$.
    \item $2x+1 \rightarrow 2(0)+1 = 1$.
\end{itemize}
Le produit d'une quantité qui tend vers $+\infty$ et d'une quantité qui tend vers $1$ est $+\infty$.
Donc : 
\begin{equation*}
   \lim\limits_{x \rightarrow 0^{+}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right) = +\infty.
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
\begin{python}
from sympy import *
bonne_valeur = "La limite n'existe pas"
\end{python}
$\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Considérez le domaine de définition de $\sqrt{x}$.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{bonne_valeur}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour que l'expression $\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)$ soit définie, il faut que $\sqrt{x}$ soit défini, ce qui implique $x \ge 0$.
Lorsque $x \rightarrow 0^{-}$, $x$ prend des valeurs négatives. Dans ce cas, $\sqrt{x}$ n'est pas défini dans l'ensemble des nombres réels.
Par conséquent, la limite $\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$ n'existe pas.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
bonne_valeur = -oo
\end{python}
$\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x-4}{x-3}\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Analysez le signe du numérateur et du dénominateur lorsque $x$ approche $3$ par la droite.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{bonne_valeur}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
   En regardant l'expression : 
$
   \frac{x - 4}{x - 3}. 
$
   Lorsque $x \rightarrow 3^{+}$, on a :
\begin{itemize}
    \item $x - 4 \rightarrow 3 - 4 = -1$.
    \item $x - 3 \rightarrow 0^{+}$. (car $x$ est légèrement supérieur à $3$)
\end{itemize}
   Ceci donne : 
\begin{equation*}
\lim\limits_{x \rightarrow 3^{+}} \frac{x-4}{x-3}
=
   \frac{-1}{0^{+}} = -\infty. 
\end{equation*}
   Donc : 
$
   \lim\limits_{x \rightarrow 3^{+}}\left(\frac{x - 4}{x - 3}\right) = -\infty. 
$
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\begin{python}
from sympy import *
bonne_valeur = oo
\end{python}
$\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x-4}{x-3}\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{bonne_valeur}"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Analysez le signe du numérateur et du dénominateur lorsque $x$ approche $3$ par la gauche.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{bonne_valeur}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
   En regardant l'expression : 
$
   \frac{x - 4}{x - 3}. 
$
   Lorsque $x \rightarrow 3^{-}$, on a :
\begin{itemize}
    \item $x - 4 \rightarrow 3 - 4 = -1$.
    \item $x - 3 \rightarrow 0^{-}$. (car $x$ est légèrement inférieur à $3$)
\end{itemize}
   Ceci donne : 
\begin{equation*}
\lim\limits_{x \rightarrow 3^{-}} \frac{x-4}{x-3}
=
   \frac{-1}{0^{-}} = +\infty. 
\end{equation*}
   Donc : 
$
   \lim\limits_{x \rightarrow 3^{-}}\left(\frac{x - 4}{x - 3}\right) = +\infty. 
$
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