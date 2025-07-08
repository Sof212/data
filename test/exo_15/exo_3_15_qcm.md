```latex
\begin{exercise}{
Id: 7b9c5fda-fe94-4c85-a881-5ef3b77f7183
Title_exo: \en{Calculation of probabilities, expectation and variance of a binomial distribution}\fr{Calculs de probabilités, d'espérance et de variance d'une loi binomiale}
Modules: Probability_and_Statistics
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Probability_and_Statistics
Involved_Concepts: Binomial_distribution, Probability, Expectation, Variance
Original_source: Ronan
Visibility: All
Comment: This exercise has been converted from a QST format to QCM, splitting the original questions into individual QCMs for clarity and automated grading.
}
{ % Contenu de l'exercice

\begin{python}
from sympy import *
import sympy.stats as stats
import math as m
import random as rd

# Define a placeholder for the custom function if it's essential for calculations
def pxs_nvirgzero(val):
    return round(val, 2) # Assuming it rounds to 2 decimal places for numerical results

################################### VARIABLES MODIFIABLES
nmin,nmax=5,20
prec=0.1
pmin,pmax=1,int(1/prec-1)
prod=r"\times"
########################################################

# Initialisation de la binomiale
n=rd.randint(nmin,nmax)
p=round(rd.randint(pmin,pmax)*prec,int(1/prec))
kmin,kmax=max(0,int(n*p)-5),min(int(n*p)+5,n)
k=rd.randint(kmin,kmax)

# Question 1
bonne_valeur=m.comb(n,k)*(p**(k))*((1-p)**(n-k))

# Generate false propositions for proba
fausse_1 = round(bonne_valeur * 0.9, 4)
fausse_2 = round(bonne_valeur * 1.1, 4)
fausse_3 = round(m.comb(n,k)*(p**(k+1))*((1-p)**(n-k-1)), 4) if k < n else round(bonne_valeur * 0.5, 4)
\end{python}

\qcm{
\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$. Calculer $\fP(X=\py{k}).$}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$. Calculate $\fP(X=\py{k}).$}
}
{
\right{$\py{round(bonne_valeur, 4)}$}
\wrong{$\py{fausse_1}$}
\wrong{$\py{fausse_2}$}
\wrong{$\py{fausse_3}$}
}
{ % Indice
\fr{Rappelez-vous la formule de la probabilité d'une loi binomiale : $\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$.}
\en{Recall the formula for the probability of a binomial distribution: $\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$.}
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
 \fbox{$\fP(X=\py{k})  = \py{round(bonne_valeur, 4)}$.}
\end{equation*}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\begin{python}
from sympy import *
import sympy.stats as stats
import math as m
import random as rd

# Define a placeholder for the custom function if it's essential for calculations
def pxs_nvirgzero(val):
    return round(val, 2) # Assuming it rounds to 2 decimal places for numerical results

################################### VARIABLES MODIFIABLES
nmin,nmax=5,20
prec=0.1
pmin,pmax=1,int(1/prec-1)
prod=r"\times"
########################################################

# Initialisation de la binomiale
n=rd.randint(nmin,nmax)
p=round(rd.randint(pmin,pmax)*prec,int(1/prec))
kmin,kmax=max(0,int(n*p)-5),min(int(n*p)+5,n)
k=rd.randint(kmin,kmax)

# Question 2
bonne_valeur=pxs_nvirgzero(n*p)

# Generate false propositions for esperance
fausse_1 = pxs_nvirgzero(n * (1-p))
fausse_2 = pxs_nvirgzero(n + p)
fausse_3 = pxs_nvirgzero(n * p * p)
\end{python}

\qcm{
\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$. Déterminer l'espérance de $X$.}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$. Determine the expectation of $X$.}
}
{
\right{$\py{bonne_valeur}$}
\wrong{$\py{fausse_1}$}
\wrong{$\py{fausse_2}$}
\wrong{$\py{fausse_3}$}
}
{ % Indice
\fr{L'espérance d'une loi binomiale $\mathcal{B}(n,p)$ est donnée par la formule $E[X] = np$.}
\en{The expectation of a binomial distribution $\mathcal{B}(n,p)$ is given by the formula $E[X] = np$.}
}
{ % Solution détaillée
\en{If one can use the formulas given in the Lecture notes about $\fE[X]$ we immediately can write:}
\fr{Nous pouvons obtenir directement par formule de l'espérance d'une loi binomiale}
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

\begin{python}
from sympy import *
import sympy.stats as stats
import math as m
import random as rd

# Define a placeholder for the custom function if it's essential for calculations
def pxs_nvirgzero(val):
    return round(val, 2) # Assuming it rounds to 2 decimal places for numerical results

################################### VARIABLES MODIFIABLES
nmin,nmax=5,20
prec=0.1
pmin,pmax=1,int(1/prec-1)
prod=r"\times"
########################################################

# Initialisation de la binomiale
n=rd.randint(nmin,nmax)
p=round(rd.randint(pmin,pmax)*prec,int(1/prec))
kmin,kmax=max(0,int(n*p)-5),min(int(n*p)+5,n)
k=rd.randint(kmin,kmax)

# Question 3 (Variance, derived from original Python code)
bonne_valeur=pxs_nvirgzero(n*p*(1-p))

# Generate false propositions for variance
fausse_1 = pxs_nvirgzero(n * p)
fausse_2 = pxs_nvirgzero(n * p * (1-p) * (1-p))
fausse_3 = pxs_nvirgzero(n * p * p * (1-p))
\end{python}

\qcm{
\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$. Déterminer la variance de $X$.}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$. Determine the variance of $X$.}
}
{
\right{$\py{bonne_valeur}$}
\wrong{$\py{fausse_1}$}
\wrong{$\py{fausse_2}$}
\wrong{$\py{fausse_3}$}
}
{ % Indice
\fr{La variance d'une loi binomiale $\mathcal{B}(n,p)$ est donnée par la formule $Var(X) = np(1-p)$.}
\en{The variance of a binomial distribution $\mathcal{B}(n,p)$ is given by the formula $Var(X) = np(1-p)$.}
}
{ % Solution détaillée
\fr{La variance d'une loi binomiale $\mathcal{B}(n,p)$ est donnée par la formule :}
\en{The variance of a binomial distribution $\mathcal{B}(n,p)$ is given by the formula:}
\begin{equation*}
Var(X) = np(1-p)
\end{equation*}
\fr{Avec $n=\py{n}$ et $p=\py{p}$, nous avons :}
\en{With $n=\py{n}$ and $p=\py{p}$, we have:}
\begin{equation*}
Var(X) = \py{n} \py{prod} \py{p} \py{prod} (1-\py{p}) = \py{bonne_valeur}
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