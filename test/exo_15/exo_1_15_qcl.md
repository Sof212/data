```latex
\begin{exercise}{
Id: 7b9c5fda-fe94-4c85-a881-5ef3b77f7183
Title_exo: \en{Calculation of probabilities, expectation and variance of a binomial distribution}\fr{Calculs de probabilités, d'espérance et de variance d'une loi binomiale} % Nom de l'exercice
Modules:  % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap:  % NameID des chapitres
Involved_Concepts:  % ID ou NameID des notions 
Original_source: Ronan % Source de l'exercice
Visibility: Teacher % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel)
% Comment: % Commentaire de l'exercice (optionnel)
}
{
\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
from sympy import *
import sympy.stats as stats
import math as m
import random as rd

# from pyxiscience.Mes_fctions_probabilistes_bis import * # Cette ligne semble être un import local, à commenter ou remplacer si non disponible

# Fonction pxs_nvirgzero (à définir si elle n'est pas dans sympy ou math)
def pxs_nvirgzero(val):
    return val # Placeholder, à adapter si la fonction a un comportement spécifique

# Fonction myst (à définir si elle n'est pas dans sympy ou math)
def myst(val):
    return val # Placeholder, à adapter si la fonction a un comportement spécifique

################################### VARIABLES MODIFIABLES
nmin,nmax=5,20                                     # bornes du paramètre n de la binomiale
prec=0.1
pmin,pmax=1,int(1/prec-1)                          # bornes du paramètre p de la binomiale (multiplié par 0.1)
prod=myst(r"""\times""")                           # choix du symbole de la multiplication
########################################################

# Initialisation de la binomiale
n=rd.randint(nmin,nmax)
p=round(rd.randint(pmin,pmax)*prec,int(1/prec))
kmin,kmax=max(0,int(n*p)-5),min(int(n*p)+5,n)      # bornes de k pour le calcul de P(X=k)
k=rd.randint(kmin,kmax)

# Question 1
proba=m.comb(n,k)*(p**(k))*((1-p)**(n-k))

# Question 2
esperance=pxs_nvirgzero(n*p)
variance=pxs_nvirgzero(n*p*(1-p))
\end{python}
 
\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$.}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$.}


\qcl{\fr{Calculer $\fP(X=\py{k}).$}
 \en{Calculate $\fP(X=\py{k}).$}}
{
\begin{python}
from sympy import *
import math as m
# Variables et calculs de la réponse exacte
n_q1 = n
p_q1 = p
k_q1 = k
bonne_valeur = m.comb(n_q1,k_q1)*(p_q1**(k_q1))*((1-p_q1)**(n_q1-k_q1))
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice

}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
\fr{$\fP(X=\py{k}) = \py{proba}$}
\en{$\fP(X=\py{k}) = \py{proba}$}
}
{ % Solution détaillée
\en{Since we know that for any $0 \leqslant k \leqslant n$:}
\fr{Comme nous savons que pour tout $0 \leqslant k \leqslant n$}
\begin{equation*}
\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k},
\end{equation*}
\en{where, here, $n=\py{n}$ and $p=\py{p}$, one easily gets:}
\fr{avec ici $n=\py{n}$ et $p=\py{p}$, nous avons}
\begin{equation*}
 \fP(X=\py{k}) = \binom{\py{n}}{\py{k}} \py{prod} \py{p}^{\py{k}} \py{prod} (1-\py{p})^{\py{n}-\py{k}}
\end{equation*}
\fr{et donc}
\en{and then}
\begin{equation*}
 \fbox{$\fP(X=\py{k})  = \py{bonne_valeur}$.}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{\fr{Déterminer l'espérance  de $X$.}
\en{Determine the expectation  of $X$.}}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
n_q2 = n
p_q2 = p
bonne_valeur = n_q2 * p_q2
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice

}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
\fr{$\fE[X] = \py{esperance}$}
\en{$\fE[X] = \py{esperance}$}
}
{ % Solution détaillée
\en{If one can use the formulas given in the Lecture notes about $\fE[X]$  we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de l'espérance  d'une loi binomiale}
\begin{equation*}
\begin{align*}
\fE[X] &= np\\
&= \py{n}\py{prod} \py{p}\\
&= \py{bonne_valeur}
\end{align*}
\end{equation*}

}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{\fr{Déterminer la variance de $X$.}
\en{Determine the variance of $X$.}}
{
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
n_q3 = n
p_q3 = p
bonne_valeur = n_q3 * p_q3 * (1 - p_q3)
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice

}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
\fr{$\fVar[X] = \py{variance}$}
\en{$\fVar[X] = \py{variance}$}
}
{ % Solution détaillée
\en{If one can use the formulas given in the Lecture notes about $\fVar[X]$  we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de la variance d'une loi binomiale}
\begin{equation*}
\begin{align*}
\fVar[X] &= np(1-p)\\
&= \py{n}\py{prod} \py{p} \py{prod} (1 - \py{p})\\
&= \py{bonne_valeur}
\end{align*}
\end{equation*}

}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

}
\end{exercise}
```