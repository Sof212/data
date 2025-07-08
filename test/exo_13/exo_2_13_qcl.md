```latex
\begin{exercise}{
Id: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f
Title_exo: Primitives d'une fonction rationnelle
Modules: R1_11_Calcul_Integral
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Integration
Involved_Concepts: Rational_Functions, Primitives
Original_source: null
Visibility: All
}
{
\qcl{
\begin{python}
from sympy import symbols, Rational, log

# Variables et calculs de la réponse exacte
# Pour la question sur le coefficient 'a'
a_val = 1
\end{python}
Pour la fonction $f(x) = \frac{x^{2}+2x+2}{x^{2}+x}$ définie sur $\mathbb{R}^{*}_{+}$, 
calculer le coefficient $a$ dans la décomposition $f(x) = a + \frac{b}{x} + \frac{c}{x+1}$.
}
{
[["CL","\py{a_val}"],["0"]]
}
{
Indice: Écrivez $f(x)$ sous forme réduite et identifiez les coefficients.
}
{
Le coefficient $a$ vaut \py{a_val}.
}
{
Nous procédons par identification des coefficients :

\begin{equation*}
\begin{align*}
f(x) = a + \frac{b}{x} + \frac{c}{x+1}
&\Longleftrightarrow \frac{x^{2}+2x+2}{x^{2}+x} = \frac{a x(x+1) + b(x+1) + cx}{x(x+1)}\\
&\Longleftrightarrow x^{2}+2x+2 = ax^2 + x(a+b+c) + b\\
&\Longleftrightarrow (1-a)x^{2}+(2-(a+b+c))x+2-b = 0
\end{align*}
\end{equation*}

En identifiant les coefficients, on obtient le système :
\begin{equation*}
\begin{cases}
1-a = 0 \\
2-(a+b+c) = 0 \\
2-b = 0
\end{cases}
\end{equation*}

La première équation donne directement $a = 1$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import symbols, Rational, log

# Variables et calculs de la réponse exacte
# Pour la question sur le coefficient 'b'
b_val = 2
\end{python}
Pour la fonction $f(x) = \frac{x^{2}+2x+2}{x^{2}+x}$ définie sur $\mathbb{R}^{*}_{+}$, 
calculer le coefficient $b$ dans la décomposition $f(x) = a + \frac{b}{x} + \frac{c}{x+1}$.
}
{
[["CL","\py{b_val}"],["0"]]
}
{
Indice: Utilisez le système d'équations obtenu par identification.
}
{
Le coefficient $b$ vaut \py{b_val}.
}
{
En résolvant le système obtenu par identification :
\begin{equation*}
\begin{cases}
1-a = 0 \\
2-(a+b+c) = 0 \\
2-b = 0
\end{cases}
\end{equation*}

La troisième équation donne directement $b = 2$.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{
\begin{python}
from sympy import symbols, Rational, log

# Variables et calculs de la réponse exacte
# Pour la question sur le coefficient 'c'
c_val = -1
\end{python}
Pour la fonction $f(x) = \frac{x^{2}+2x+2}{x^{2}+x}$ définie sur $\mathbb{R}^{*}_{+}$, 
calculer le coefficient $c$ dans la décomposition $f(x) = a + \frac{b}{x} + \frac{c}{x+1}$.
}
{
[["CL","\py{c_val}"],["0"]]
}
{
Indice: Après avoir trouvé a et b, déduisez c du système.
}
{
Le coefficient $c$ vaut \py{c_val}.
}
{
Avec $a = 1$ et $b = 2$, la deuxième équation du système :
\begin{equation*}
2-(1+2+c) = 0 \Rightarrow c = -1
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
from sympy import symbols, Rational, log

# Variables et calculs de la réponse exacte
# Pour la question sur la constante K
K_val = -1 + log(2)
K_val_latex = latex(K_val)
\end{python}
Pour la fonction $f(x) = \frac{x^{2}+2x+2}{x^{2}+x}$, donner la valeur de la primitive $F$ qui s'annule en 1, 
sous la forme $F(x) = x + 2\ln x - \ln(x+1) + K$. Calculer la constante $K$.
}
{
[["CL","\py{K_val_latex}"],["0"]]
}
{
Indice: Utilisez la décomposition en éléments simples trouvée précédemment.
}
{
La constante $K$ vaut $\py{K_val_latex}$.
}
{
En intégrant la décomposition $f(x) = 1 + \frac{2}{x} - \frac{1}{x+1}$, on obtient :
\begin{equation*}
F(x) = x + 2\ln x - \ln(x+1) + K
\end{equation*}

La condition $F(1) = 0$ donne :
\begin{equation*}
1 + 2\ln 1 - \ln 2 + K = 0 \Rightarrow 1 - \ln 2 + K = 0 \Rightarrow K = -1 + \ln 2
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