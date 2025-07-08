```latex
\begin{exercise}{
Title_exo: Limites unilatérales
Modules: Analyse
Recommended_execution_time: 15
Ex_Level: Elementary
Chap: Limites
Involved_Concepts: Limite unilatérale, Forme indéterminée
}
{
\begin{python}
from sympy import *
\end{python}

\qcm{
$\lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x+4}\right)$ est :
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = -oo
# === Propositions fausses calculées ===
fausse_1 = oo  # Erreur de signe
fausse_2 = 0   # Confusion avec une limite finie
fausse_3 = Rational(1,2) # Valeur numérique sans rapport
\end{python}
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : Lorsque $x \rightarrow 2^+$, $-2x+4 \rightarrow 0^-$ donc $\frac{1}{-2x+4} \rightarrow -\infty$.
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\qcm{
$\lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x+4}\right)$ est :
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = oo
# === Propositions fausses calculées ===
fausse_1 = -oo  # Erreur de signe
fausse_2 = 0    # Confusion avec une limite finie
fausse_3 = Rational(1,2) # Valeur numérique sans rapport
\end{python}
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : Lorsque $x \rightarrow 2^-$, $-2x+4 \rightarrow 0^+$ donc $\frac{1}{-2x+4} \rightarrow +\infty$.
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\qcm{
$\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x-4}{x-3}\right)$ est :
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = -oo
# === Propositions fausses calculées ===
fausse_1 = oo   # Erreur de signe
fausse_2 = -1   # Limite du numérateur
fausse_3 = Rational(1,3) # Valeur numérique sans rapport
\end{python}
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : Quand $x \rightarrow 3^+$, $x-4 \rightarrow -1$ et $x-3 \rightarrow 0^+$, donc $\frac{x-4}{x-3} \rightarrow -\infty$.
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\qcm{
$\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x-4}{x-3}\right)$ est :
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = oo
# === Propositions fausses calculées ===
fausse_1 = -oo  # Erreur de signe
fausse_2 = -1   # Limite du numérateur
fausse_3 = Rational(1,3) # Valeur numérique sans rapport
\end{python}
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : Quand $x \rightarrow 3^-$, $x-4 \rightarrow -1$ et $x-3 \rightarrow 0^-$, donc $\frac{x-4}{x-3} \rightarrow +\infty$.
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\qcm{
$\lim\limits_{x \rightarrow 0^{+}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$ est :
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = oo
# === Propositions fausses calculées ===
fausse_1 = -oo  # Erreur de signe
fausse_2 = 2    # Limite du second facteur
fausse_3 = 0    # Confusion avec une limite nulle
\end{python}
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : L'expression se développe en $4x + 2 + \frac{2x}{\sqrt{x}} + \frac{1}{\sqrt{x}}$. Quand $x \rightarrow 0^+$, $\frac{1}{\sqrt{x}} \rightarrow +\infty$ domine.
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{
$\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$ est :
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = "N'existe pas" # La fonction n'est pas définie
# === Propositions fausses calculées ===
fausse_1 = oo   # Ignorance du domaine de définition
fausse_2 = -oo  # Ignorance du domaine de définition
fausse_3 = 2    # Valeur numérique sans rapport
\end{python}
\right{$\sympy{bonne_valeur}$}
\wrong{$\sympy{fausse_1}$}
\wrong{$\sympy{fausse_2}$}
\wrong{$\sympy{fausse_3}$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
}
{%% Solution détaillée : La fonction $\sqrt{x}$ n'est pas définie pour $x < 0$ dans les réels, donc la limite n'existe pas.
}
{
logic: 30
abstraction: 30
reasoning: 20
calculation: 20
}
}
\end{exercise}
```