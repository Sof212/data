```latex
\begin{exercise}{
Id: 7b9c5fda-fe94-4c85-a881-5ef3b77f7183
Title_exo: \en{Calculation of probabilities, expectation and variance of a binomial distribution}\fr{Calculs de probabilités, d'espérance et de variance d'une loi binomiale}
Modules:  
Recommended_execution_time: 10 
Ex_Level: Elementary 
Chap:  
Involved_Concepts:  
Original_source: Ronan 
Visibility: Teacher 
}
{
\begin{python}
from sympy import *
import sympy.stats as stats
import math as m
import random as rd
# from pyxiscience.Mes_fctions_probabilistes_bis import * # Cette ligne semble être un import local, à vérifier si nécessaire ou à remplacer par une fonction équivalente si elle est utilisée.
# Si pxs_nvirgzero et pxsl_res_num sont des fonctions personnalisées, elles doivent être définies ici ou importées d'un module accessible.
# Pour cet exercice, je vais les simuler pour que le code soit fonctionnel.
def pxs_nvirgzero(val):
    return round(val, 4) # Exemple de simulation, ajuster selon la logique réelle

def pxsl_res_num(val):
    return str(round(val, 4)) # Exemple de simulation, ajuster selon la logique réelle

# Paramètres
nmin, nmax = 5, 20
prec = 0.1
pmin, pmax = 1, int(1/prec-1)
prod = r"\times" # Utilisation directe de la chaîne LaTeX pour \times

# Initialisation
n = rd.randint(nmin, nmax)
p = round(rd.randint(pmin, pmax)*prec, int(1/prec))
kmin, kmax = max(0, int(n*p)-5), min(int(n*p)+5, n)
k = rd.randint(kmin, kmax)

# Calculs
proba = m.comb(n, k)*(p**(k))*((1-p)**(n-k))
esperance = n*p
variance = n*p*(1-p)
\end{python}

\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$.}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$.}

\qcl{
\fr{Calculer $\fP(X=\py{k})$.}
\en{Calculate $\fP(X=\py{k})$.}
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = proba
\end{python}
[["CL","\py{pxsl_res_num(bonne_valeur)}"],["0"]]
}
{
}
{
\fr{La probabilité est $\fP(X=\py{k}) = \py{pxsl_res_num(proba)}$.}
\en{The probability is $\fP(X=\py{k}) = \py{pxsl_res_num(proba)}$.}
}
{
\fr{Comme nous savons que pour tout $0 \leqslant k \leqslant n$:
\begin{equation*}
\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k},
\end{equation*}
avec ici $n=\py{n}$ et $p=\py{p}$, nous avons
\begin{equation*}
\fP(X=\py{k}) = \binom{\py{n}}{\py{k}} \py{prod} \py{p}^{\py{k}} \py{prod} (1-\py{p})^{\py{n}-\py{k}}
\end{equation*}
et donc
\begin{equation*}
\fbox{$\fP(X=\py{k}) = \py{pxsl_res_num(proba)}$.}
\end{equation*}}
\en{Since we know that for any $0 \leqslant k \leqslant n$:
\begin{equation*}
\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k},
\end{equation*}
where, here, $n=\py{n}$ and $p=\py{p}$, one easily gets:
\begin{equation*}
\fP(X=\py{k}) = \binom{\py{n}}{\py{k}} \py{prod} \py{p}^{\py{k}} \py{prod} (1-\py{p})^{\py{n}-\py{k}}
\end{equation*}
and then
\begin{equation*}
\fbox{$\fP(X=\py{k}) = \py{pxsl_res_num(proba)}$.}
\end{equation*}}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{
\fr{Calculer l'espérance de $X$.}
\en{Calculate the expectation of $X$.}
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = esperance
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
\fr{L'espérance est $\fE[X] = \py{esperance}$.}
\en{The expectation is $\fE[X] = \py{esperance}$.}
}
{
\fr{Nous pouvons obtenir directement par formule de l'espérance d'une loi binomiale
\begin{equation*}
\begin{align*}
\fE[X] &= np\\
&= \py{n}\py{prod} \py{p}\\
&= \py{esperance}
\end{align*}
\end{equation*}}
\en{Using the formula for the expectation of a binomial distribution:
\begin{equation*}
\begin{align*}
\fE[X] &= np\\
&= \py{n}\py{prod} \py{p}\\
&= \py{esperance}
\end{align*}
\end{equation*}}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{
\fr{Calculer la variance de $X$.}
\en{Calculate the variance of $X$.}
}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
bonne_valeur = variance
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{
}
{
\fr{La variance est $\fV[X] = \py{variance}$.}
\en{The variance is $\fV[X] = \py{variance}$.}
}
{
\fr{Par la formule de la variance d'une loi binomiale:
\begin{equation*}
\begin{align*}
\fV[X] &= np(1-p)\\
&= \py{n}\py{prod} \py{p} \py{prod} (1-\py{p})\\
&= \py{variance}
\end{align*}
\end{equation*}}
\en{Using the variance formula for a binomial distribution:
\begin{equation*}
\begin{align*}
\fV[X] &= np(1-p)\\
&= \py{n}\py{prod} \py{p} \py{prod} (1-\py{p})\\
&= \py{variance}
\end{align*}
\end{equation*}}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}
}
\end{exercise}
```