```latex
\begin{exercise}{
Id: 7b9c5fda-fe94-4c85-a881-5ef3b77f7183
Title_exo: \en{Calculation of probabilities, expectation and variance of a binomial distribution}\fr{Calculs de probabilités, d'espérance et de variance d'une loi binomiale} % Nom de l'exercice
Modules: Proba_Stats_NYU % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Binomial_Distribution % NameID des chapitres
Involved_Concepts: Binomial_Prob, Expectation, Variance % ID ou NameID des notions 
Original_source: Ronan % Source de l'exercice
Visibility: Teacher % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
% Comment: % Commentaire de l'exercice (optionnel)
}
{
\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$.}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$.}

\begin{python}
from sympy import *
import sympy.stats as stats
import math as m
import random as rd

# from pyxiscience.Mes_fctions_probabilistes_bis import * # Cette ligne semble être une dépendance externe, non fournie. Je la commente.

################################### VARIABLES MODIFIABLES
nmin,nmax=5,20                                     # bornes du paramètre n de la binomiale
prec=0.1
pmin,pmax=1,int(1/prec-1)                          # bornes du paramètre p de la binomiale (multiplié par 0.1)
# prod=myst(r"""\times""")                           # choix du symbole de la multiplication - myst n'est pas défini. Utilisation directe de \times en LaTeX.
########################################################

# Initialisation de la binomiale
n=rd.randint(nmin,nmax)
p=round(rd.randint(pmin,pmax)*prec,int(1/prec))
kmin,kmax=max(0,int(n*p)-5),min(int(n*p)+5,n)      # bornes de k pour le calcul de P(X=k)
k=rd.randint(kmin,kmax)

# Question 1
# Calcul bonne réponse
bonne_proba = m.comb(n,k)*(p**(k))*((1-p)**(n-k))

# Propositions fausses calculées
fausse_proba_1 = bonne_proba + 0.1 # Erreur d'approximation ou de calcul simple
fausse_proba_2 = bonne_proba - 0.1 # Erreur d'approximation ou de calcul simple
fausse_proba_3 = bonne_proba * 2   # Erreur de facteur
fausse_proba_4 = bonne_proba / 2   # Erreur de facteur

# Fonction pour formater les nombres avec une précision raisonnable pour les probabilités
def pxsl_res_num(val):
    return f"{val:.4f}" # Formatage à 4 décimales pour les probabilités

# Question 2
# Calcul bonne réponse
bonne_esperance = n * p
# Propositions fausses calculées
fausse_esperance_1 = n + p # Erreur de formule (addition au lieu de multiplication)
fausse_esperance_2 = n * (1-p) # Erreur de formule (1-p au lieu de p)
fausse_esperance_3 = n * p * (1-p) # Erreur de formule (variance au lieu d'espérance)

# Question 3 (ajoutée pour la variance)
# Calcul bonne réponse
bonne_variance = n * p * (1-p)
# Propositions fausses calculées
fausse_variance_1 = n * p # Erreur de formule (espérance au lieu de variance)
fausse_variance_2 = n * p * p # Erreur de formule (p^2 au lieu de p(1-p))
fausse_variance_3 = n * (1-p) # Erreur de formule (manque p)
\end{python}
 
\qcm{\fr{Calculer $\fP(X=\py{k}).$}
 \en{Calculate $\fP(X=\py{k}).$}}
{
\right{$\py{pxsl_res_num(bonne_proba)}$}
\wrong{$\py{pxsl_res_num(fausse_proba_1)}$}
\wrong{$\py{pxsl_res_num(fausse_proba_2)}$}
\wrong{$\py{pxsl_res_num(fausse_proba_3)}$}
\wrong{$\py{pxsl_res_num(fausse_proba_4)}$}
}
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
 \fP(X=\py{k}) = \binom{\py{n}}{\py{k}} \times \py{p}^{\py{k}} \times (1-\py{p})^{\py{n}-\py{k}}
\end{equation*}
\fr{et donc}
\en{and then}
\begin{equation*}
 \fbox{$\fP(X=\py{k}) = \py{pxsl_res_num(bonne_proba)}$.}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcm{\fr{Déterminer l'espérance de $X$.}
\en{Determine the expectation of $X$.}}
{
\right{$\py{latex(bonne_esperance)}$}
\wrong{$\py{latex(fausse_esperance_1)}$}
\wrong{$\py{latex(fausse_esperance_2)}$}
\wrong{$\py{latex(fausse_esperance_3)}$}
}
{ % Indice

}
{ % Solution détaillée
\en{If one can use the formulas given in the Lecture notes about $\fE[X]$  we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de l'espérance d'une loi binomiale}
\begin{equation*}
\begin{align*}
\fE[X] &= np\\
&= \py{n} \times \py{p}\\
&= \py{latex(bonne_esperance)}
\end{align*}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcm{\fr{Déterminer la variance de $X$.}
\en{Determine the variance of $X$.}}
{
\right{$\py{latex(bonne_variance)}$}
\wrong{$\py{latex(fausse_variance_1)}$}
\wrong{$\py{latex(fausse_variance_2)}$}
\wrong{$\py{latex(fausse_variance_3)}$}
}
{ % Indice

}
{ % Solution détaillée
\en{If one can use the formulas given in the Lecture notes about $\text{Var}(X)$  we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de la variance d'une loi binomiale}
\begin{equation*}
\begin{align*}
\text{Var}(X) &= np(1-p)\\
&= \py{n} \times \py{p} \times (1-\py{p})\\
&= \py{latex(bonne_variance)}
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