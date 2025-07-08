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

from pyxiscience.Mes_fctions_probabilistes_bis import *

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


\qst{\fr{Calculer $\fP(X=\py{k}).$}
 \en{Calculate $\fP(X=\py{k}).$}}
{ % Indice

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
 \fbox{$\fP(X=\py{k})  \py{pxsl_res_num(proba)}$.}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qst{\fr{Déterminer l'espérance  de $X$.}
\en{Determine the expectation  of $X$.}}
{ % Indice

}
{ % Solution détaillée
\en{If one can use the formulas given in the Lecture notes about $\fE[X]$  we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de l'espérance  d'une loi binomiale}
\begin{equation*}
\begin{align*}
\fE[X] &= np\\
&= \py{n}\py{prod} \py{p}\\
&= \py{latex(esperance)}
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