```latex
\begin{exercise}{
Id: 001
Title_exo: Limites de fonctions 
Modules: Analyse 
Recommended_execution_time: 10 
Ex_Level: Elementary 
Chap: Limites 
Involved_Concepts : Limites latérales, formes indéterminées
Visibility: All
}
{
Déterminer les valeurs des limites suivantes.

\qcl{
\begin{python}
from sympy import *
x = symbols('x')
bonne_valeur = -oo
\end{python}
Calculer la limite suivante : $\lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x+4}\right)$
}
{
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{
Examinez le signe du dénominateur lorsque x tend vers 2 par valeurs supérieures.
}
{
La réponse est $\py{latex(bonne_valeur)}$
}
{
Tout d'abord, nous remarquons que : $-2x + 4$ en $4 - 2x$. Par ailleurs, lorsque $x$ tend vers $2^{+}$ (valeurs légèrement supérieures à $2$), on a :
\begin{equation*}
   4 - 2(2^{+}) = 4 - 4^{+} = 0^{-}.
\end{equation*}
En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la droite, nous avons : 
\begin{equation*}
   4 - 2x < 0 \quad \text{(pour } x > 2 \text{)} 
\end{equation*}
Ce qui implique que $-2x + 4 < 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $-\infty$, lorsque $x$ tend vers $2$ par valeurs supérieures. Donc : 
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x + 4}\right) = -\infty.
\end{equation*}
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
x = symbols('x')
bonne_valeur = oo
\end{python}
Calculer la limite suivante : $\lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x+4}\right)$
}
{
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{
Examinez le signe du dénominateur lorsque x tend vers 2 par valeurs inférieures.
}
{
La réponse est $\py{latex(bonne_valeur)}$
}
{
Lorsque $x$ tend vers $2^{-}$ (valeurs légèrement inférieures à $2$), on a :
\begin{equation*}
   - 2(2^{-}) + 4 = 4 - 2(2^{-}) = 4 - 4^{-} = 0^{+}.
\end{equation*}
En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la gauche, nous avons : 
\begin{equation*}
   - 2x + 4 > 0 \quad \text{(pour } x < 2 \text{)} 
\end{equation*}
Ce qui implique que $-2x + 4 > 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $+\infty$, lorsque $x$ tend vers $2$ par valeurs inférieures. Donc : 
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x + 4}\right) = +\infty.
\end{equation*}
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
x = symbols('x')
bonne_valeur = -oo
\end{python}
Calculer la limite suivante : $\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x-4}{x-3}\right)$
}
{
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{
Analysez séparément le numérateur et le dénominateur.
}
{
La réponse est $\py{latex(bonne_valeur)}$
}
{
En regardant l'expression : $\frac{x - 4}{x - 3}$. Lorsque $x \rightarrow 3^{+}$, on a $x - 4 \rightarrow -1$ et $x - 3 \rightarrow 0^{+}$. Ceci donne : 
\begin{equation*}
\lim\limits_{x \rightarrow 3^{+}} \frac{x-4}{x-3} = \frac{-1}{0^{+}} = -\infty. 
\end{equation*}
Donc : $\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x - 4}{x - 3}\right) = -\infty$.
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
x = symbols('x')
bonne_valeur = oo
\end{python}
Calculer la limite suivante : $\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x-4}{x-3}\right)$
}
{
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{
Analysez séparément le numérateur et le dénominateur.
}
{
La réponse est $\py{latex(bonne_valeur)}$
}
{
En regardant l'expression : $\frac{x - 4}{x - 3}$. Lorsque $x \rightarrow 3^{-}$, on a $x - 4 \rightarrow -1$ et $x - 3 \rightarrow 0^{-}$. Ceci donne : 
\begin{equation*}
\lim\limits_{x \rightarrow 3^{-}} \frac{x-4}{x-3} = \frac{-1}{0^{-}} = +\infty. 
\end{equation*}
Donc : $\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x - 4}{x - 3}\right) = +\infty$.
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
x = symbols('x')
bonne_valeur = oo
\end{python}
Calculer la limite suivante : $\lim\limits_{x \rightarrow 0^{+}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{
Développez l'expression et analysez chaque terme.
}
{
La réponse est $\py{latex(bonne_valeur)}$
}
{
Analysons l'expression $\left(2+\frac{1}{\sqrt{x}}\right)(2x+1)$ à mesure que $x$ tend vers $0^{+}$. On a :
\begin{equation*}
\bigg(2+\frac{1}{\sqrt{x}}\bigg)(2x+1) = 4x + 2 + \frac{2x}{\sqrt{x}} + \frac{1}{\sqrt{x}}. 
\end{equation*}
Lorsque $x$ approche $0^{+}$, $\frac{1}{\sqrt{x}} \rightarrow +\infty$. Par conséquent, 
\begin{equation*}
\lim\limits_{x \rightarrow 0^{+}}\left(4x + 2 + \frac{1}{\sqrt{x}}\right) = +\infty. 
\end{equation*}
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
x = symbols('x')
# La limite n'existe pas dans les réels pour x -> 0- car sqrt(x) n'est pas définie.
# Cependant, si on considère le domaine des nombres complexes, la limite peut être calculée.
# Pour cet exercice, on suppose qu'on reste dans les réels, donc la limite n'est pas définie.
# Si on force une réponse pour un QCM, on pourrait mettre "n'existe pas" ou "indéfini".
# Mais pour un champ libre, il est plus précis de dire que la fonction n'est pas définie.
# Si l'exercice attend une valeur numérique, il y a une ambiguïté.
# Si on interprète "Calculer la limite" comme "si elle existe", alors elle n'existe pas.
# Si on doit donner une valeur, il faut revoir l'énoncé.
# Pour l'instant, je vais mettre une valeur qui reflète l'idée d'une "non-existence" ou d'une erreur.
# Cependant, l'énoncé original donne une réponse de "-oo", ce qui implique une interprétation
# où sqrt(x) est traitée comme une fonction qui peut tendre vers -i*oo pour x < 0.
# C'est une interprétation mathématiquement discutable dans le contexte des limites réelles.
# Si l'exercice est destiné à des étudiants en analyse réelle, cette question est mal posée.
# Si l'exercice est pour des étudiants en analyse complexe, alors il faut le préciser.
# Étant donné la réponse originale "-oo", je vais la reproduire, mais avec une note.
# Cela implique que l'on considère une extension où sqrt(x) pour x<0 est traitée de manière à donner un résultat réel négatif infini.
# C'est une simplification abusive ou une erreur dans l'énoncé original si le contexte est réel.
# Pour rester fidèle à la réponse originale, je vais la reproduire.
bonne_valeur = -oo
\end{python}
Calculer la limite suivante : $\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{
[["CL","\py{latex(bonne_valeur)}"],["0"]]
}
{
Attention à la définition de la racine carrée pour x négatif. La fonction $\sqrt{x}$ n'est pas définie pour $x < 0$ dans l'ensemble des nombres réels.
}
{
La réponse est $\py{latex(bonne_valeur)}$ (Note : Dans le cadre des nombres réels, cette limite n'est pas définie car $\sqrt{x}$ n'est pas définie pour $x < 0$. La réponse $-\infty$ implique une interprétation dans un contexte plus large ou une simplification.)
}
{
Analysons l'expression $\left(2+\frac{1}{\sqrt{x}}\right)(2x+1)$ à mesure que $x$ tend vers $0^{-}$.
Dans l'ensemble des nombres réels, la fonction $\sqrt{x}$ n'est pas définie pour $x < 0$. Par conséquent, l'expression $\left(2+\frac{1}{\sqrt{x}}\right)(2x+1)$ n'est pas définie pour $x < 0$.
Strictement parlant, la limite $\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$ n'existe pas dans l'ensemble des nombres réels.

Cependant, si l'on considère une extension où $\frac{1}{\sqrt{x}}$ pour $x \rightarrow 0^{-}$ est interprétée de manière à produire un résultat réel (ce qui est mathématiquement incorrect sans contexte supplémentaire, comme l'analyse complexe où $\sqrt{x} = i\sqrt{|x|}$), et si l'on suit la réponse originale fournie, on pourrait imaginer une situation où :
Lorsque $x$ approche $0^{-}$, si on force une interprétation où $\frac{1}{\sqrt{x}}$ tend vers $-\infty$ (ce qui est une simplification abusive ou une erreur conceptuelle dans le cadre réel standard), alors :
\begin{equation*}
\left(2+\frac{1}{\sqrt{x}}\right)(2x+1) \approx \left(2 + (-\infty)\right)(0+1) = (-\infty)(1) = -\infty.
\end{equation*}
**Conclusion rigoureuse (dans les réels) :** La limite n'existe pas car la fonction n'est pas définie pour $x < 0$.
**Conclusion basée sur la réponse attendue de l'exercice :** Si l'on doit donner une valeur, et en supposant une interprétation non standard ou un contexte implicite (par exemple, une erreur dans l'énoncé original ou une simplification pédagogique), la réponse attendue est $-\infty$.
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