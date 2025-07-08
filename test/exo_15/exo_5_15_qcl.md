\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts: % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: % Commentaire de l'exercice (optionnel)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
}
{ % Contenu de l'exercice
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

\qcl{ % Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\fr{Calculer $\fP(X=\py{k}).$}
 \en{Calculate $\fP(X=\py{k}).$}
}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{pxsl_res_num(proba)}$"],["0"]]
}
{ % Indice: Vous pouvez écrire une indication ci-dessous.

}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{pxsl_res_num(proba)}$
}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
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
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{ % Enoncé de la question: écrivez ci-dessous l'énoncé de la question
\fr{Déterminer l'espérance  de $X$.}
\en{Determine the expectation  of $X$.}
}
{ % Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{latex(esperance)}$"],["0"]]
}
{ % Indice: Vous pouvez écrire une indication ci-dessous.

}
{ % Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{latex(esperance)}$
}
{ % Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
\en{If one can use the formulas given in the Lecture notes about $\fE[X]$ , we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de l'espérance d'une loi binomiale}
\begin{equation*}
\begin{align*}
\fE[X] &= np\\
&= \py{n}\py{prod} \py{p}\\
&= \py{latex(esperance)}
\end{align*}
\end{equation*}



}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}





}
\end{exercise}