```latex
\begin{exercise}{
Id: 87654321-abcd-1234-efgh-1234567890ab
Title_exo: Calcul de limites
Modules: Analyse
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Limites de fonctions
Involved_Concepts : Limites, Formes indéterminées
Visibility: All
}
{
Déterminer les limites ci-dessous.

\qcl{%Enoncé de la question:
Calculer la limite suivante : $\lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x+4}\right)$
}
{ % Solution PyxiScience:
\begin{python}
from sympy import *
bonne_valeur = -oo
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice:
Analysez le signe du dénominateur lorsque $x$ approche $2$ par des valeurs supérieures.
}
{ % Solution brève fournie à l'utilisateur:
La limite est $-\infty$.
}
{ % Solution détaillée:
Tout d'abord, nous remarquons que : $-2x + 4$ peut s'écrire $4 - 2x$.
Lorsque $x$ tend vers $2^{+}$ (valeurs légèrement supérieures à $2$), on a :
\begin{equation*}
   4 - 2(2^{+}) = 4 - 4^{+} = 0^{-}.
\end{equation*}
En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la droite, nous avons :
\begin{equation*}
   4 - 2x < 0 \quad \text{(pour } x > 2 \text{)}
\end{equation*}
Ce qui implique que $-2x + 4 < 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $-\infty$, lorsque $x$ tend vers $2$ par valeurs supérieures (i.e. par la droite). Donc :
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x + 4}\right) = \py{bonne_valeur}.
\end{equation*}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Calculer la limite suivante : $\lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x+4}\right)$
}
{ % Solution PyxiScience:
\begin{python}
from sympy import *
bonne_valeur = oo
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice:
Analysez le signe du dénominateur lorsque $x$ approche $2$ par des valeurs inférieures.
}
{ % Solution brève fournie à l'utilisateur:
La limite est $+\infty$.
}
{ % Solution détaillée:
Lorsque $x$ tend vers $2^{-}$ (valeurs légèrement inférieures à $2$), on a :
\begin{equation*}
   - 2(2^{-}) + 4 = 4 - 2(2^{-}) = 4 - 4^{-} = 0^{+}.
\end{equation*}
En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la gauche, nous avons :
\begin{equation*}
   - 2x + 4 > 0 \quad \text{(pour } x < 2 \text{)}
\end{equation*}
Ce qui implique que $-2x + 4 > 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $+\infty$, lorsque $x$ tend vers $2$ par valeurs inférieures (i.e. par la gauche). Donc :
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x + 4}\right) = \py{bonne_valeur}.
\end{equation*}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Calculer la limite suivante : $\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x-4}{x-3}\right)$
}
{ % Solution PyxiScience:
\begin{python}
from sympy import *
bonne_valeur = -oo
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice:
Évaluez le numérateur et le dénominateur séparément lorsque $x$ approche $3$ par la droite.
}
{ % Solution brève fournie à l'utilisateur:
La limite est $-\infty$.
}
{ % Solution détaillée:
En regardant l'expression :
$
   \frac{x - 4}{x - 3}.
$
Lorsque $x \rightarrow 3^{+}$, on a :
$
   x - 4 \rightarrow 3^{+} - 4 = -1
$
et
$
   x - 3 \rightarrow 3^{+} - 3 = 0^{+}.
$
Ceci donne :
\begin{equation*}
\lim\limits_{x \rightarrow 3^{+}} \frac{x-4}{x-3}
=
   \frac{-1}{0^{+}} = \py{bonne_valeur}.
\end{equation*}
Donc :
$
   \lim\limits_{x \rightarrow 3^{+}}\left(\frac{x - 4}{x - 3}\right) = \py{bonne_valeur}.
$
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Calculer la limite suivante : $\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x-4}{x-3}\right)$
}
{ % Solution PyxiScience:
\begin{python}
from sympy import *
bonne_valeur = oo
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice:
Évaluez le numérateur et le dénominateur séparément lorsque $x$ approche $3$ par la gauche.
}
{ % Solution brève fournie à l'utilisateur:
La limite est $+\infty$.
}
{ % Solution détaillée:
En regardant l'expression :
$
   \frac{x - 4}{x - 3}.
$
Lorsque $x \rightarrow 3^{-}$, on a :
$
   x - 4 \rightarrow 3^{-} - 4 = -1
$
et
$
   x - 3 \rightarrow 3^{-} - 3 = 0^{-}.
$
Ceci donne :
\begin{equation*}
\lim\limits_{x \rightarrow 3^{-}} \frac{x-4}{x-3}
=
   \frac{-1}{0^{-}} = \py{bonne_valeur}.
\end{equation*}
Donc :
$
   \lim\limits_{x \rightarrow 3^{-}}\left(\frac{x - 4}{x - 3}\right) = \py{bonne_valeur}.
$
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Calculer la limite suivante : $\lim\limits_{x \rightarrow 0^{+}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{ % Solution PyxiScience:
\begin{python}
from sympy import *
bonne_valeur = oo
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice:
Analysez le comportement de chaque facteur de l'expression lorsque $x$ approche $0$ par la droite.
}
{ % Solution brève fournie à l'utilisateur:
La limite est $+\infty$.
}
{ % Solution détaillée:
Analysons l'expression $  \left(2+\frac{1}{\sqrt{x}}\right)(2x+1) $ à mesure que $x$ tend vers $0^{+}$.
Lorsque $x$ approche $0^{+}$, on a :
$\sqrt{x} \rightarrow 0^{+}$
donc $\frac{1}{\sqrt{x}} \rightarrow +\infty$.
Par conséquent, le premier facteur $(2+\frac{1}{\sqrt{x}})$ tend vers $2 + (+\infty) = +\infty$.

Pour le second facteur, lorsque $x \rightarrow 0^{+}$, on a :
$2x+1 \rightarrow 2(0) + 1 = 1$.

La limite de l'expression est donc le produit de ces deux limites :
$\lim\limits_{x \rightarrow 0^{+}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right) = (+\infty) \times 1 = \py{bonne_valeur}$.
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Calculer la limite suivante : $\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{ % Solution PyxiScience:
\begin{python}
from sympy import *
bonne_valeur = "Non définie"
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice:
Considérez le domaine de définition de la fonction $\sqrt{x}$.
}
{ % Solution brève fournie à l'utilisateur:
La limite n'est pas définie.
}
{ % Solution détaillée:
L'expression contient $\sqrt{x}$. Pour que $\sqrt{x}$ soit définie dans les nombres réels, il faut que $x \ge 0$.
Lorsque $x \rightarrow 0^{-}$, cela signifie que $x$ prend des valeurs légèrement inférieures à $0$ (par exemple, $-0.001$). Pour de telles valeurs, $\sqrt{x}$ n'est pas définie dans l'ensemble des nombres réels.
Par conséquent, la fonction $\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)$ n'est pas définie pour $x < 0$.
La limite $\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$ n'est donc \py{bonne_valeur}.
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

}
\end{exercise}
```