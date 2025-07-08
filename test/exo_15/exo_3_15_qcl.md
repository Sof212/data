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
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
% Comment: % Commentaire de l'exercice (optionnel)
}
{
\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
from sympy import *
import sympy.stats as stats
import math as m
import random as rd

################################### VARIABLES MODIFIABLES
nmin,nmax=5,20                                     # bornes du paramètre n de la binomiale
prec=0.1
pmin,pmax=1,int(1/prec-1)                          # bornes du paramètre p de la binomiale (multiplié par 0.1)
prod=r"\times"                                     # choix du symbole de la multiplication
########################################################

# Initialisation de la binomiale
n=rd.randint(nmin,nmax)
p=round(rd.randint(pmin,pmax)*prec,1) # Arrondi à 1 décimale pour correspondre à prec=0.1
kmin,kmax=max(0,int(n*p)-5),min(int(n*p)+5,n)      # bornes de k pour le calcul de P(X=k)
k=rd.randint(kmin,kmax)

# Pour l'affichage LaTeX des nombres avec virgule
def pxs_nvirgzero(val):
    return str(val).replace('.', ',')

\end{python}
 
\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$.}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$.}


\qcl{\fr{Calculer $\fP(X=\py{k}).$}
 \en{Calculate $\fP(X=\py{k}).$}}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
\begin{python}
from sympy import *
import math as m
# Variables et calculs de la réponse exacte
n = \py{n}
p = \py{p}
k = \py{k}
bonne_valeur = m.comb(n,k)*(p**(k))*((1-p)**(n-k))
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice
\fr{Utilisez la formule de la probabilité d'une loi binomiale : $\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$.}
\en{Use the formula for the probability of a binomial distribution: $\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$.}
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
\fr{La probabilité est $\py{pxs_nvirgzero(bonne_valeur)}$.}
\en{The probability is $\py{pxs_nvirgzero(bonne_valeur)}$.}
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
 \fbox{$\fP(X=\py{k}) = \py{pxs_nvirgzero(bonne_valeur)}$.}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{\fr{Calculer l'espérance de $X$.}
\en{Calculate the expectation of $X$.}}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
n = \py{n}
p = \py{p}
bonne_valeur = n*p
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice
\fr{L'espérance d'une loi binomiale $\mathcal{B}(n,p)$ est donnée par la formule $E[X] = np$.}
\en{The expectation of a binomial distribution $\mathcal{B}(n,p)$ is given by the formula $E[X] = np$.}
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
\fr{L'espérance est $\py{pxs_nvirgzero(bonne_valeur)}$.}
\en{The expectation is $\py{pxs_nvirgzero(bonne_valeur)}$.}
}
{ % Solution détaillée
\en{If one can use the formulas given in the Lecture notes about $\fE[X]$  we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de l'espérance d'une loi binomiale}
\begin{equation*}
\begin{align*}
\fE[X] &= np\\
&= \py{n}\py{prod} \py{p}\\
&= \py{pxs_nvirgzero(bonne_valeur)}
\end{align*}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcl{\fr{Calculer la variance de $X$.}
\en{Calculate the variance of $X$.}}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
\begin{python}
from sympy import *
# Variables et calculs de la réponse exacte
n = \py{n}
p = \py{p}
bonne_valeur = n*p*(1-p)
\end{python}
[["CL","\py{bonne_valeur}"],["0"]]
}
{ % Indice
\fr{La variance d'une loi binomiale $\mathcal{B}(n,p)$ est donnée par la formule $Var(X) = np(1-p)$.}
\en{The variance of a binomial distribution $\mathcal{B}(n,p)$ is given by the formula $Var(X) = np(1-p)$.}
}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
\fr{La variance est $\py{pxs_nvirgzero(bonne_valeur)}$.}
\en{The variance is $\py{pxs_nvirgzero(bonne_valeur)}$.}
}
{ % Solution détaillée
\en{The variance of a binomial distribution $\mathcal{B}(n,p)$ is given by the formula:}
\fr{La variance d'une loi binomiale $\mathcal{B}(n,p)$ est donnée par la formule :}
\begin{equation*}
\begin{align*}
Var(X) &= np(1-p)\\
&= \py{n}\py{prod} \py{p}\py{prod} (1-\py{p})\\
&= \py{pxs_nvirgzero(bonne_valeur)}
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