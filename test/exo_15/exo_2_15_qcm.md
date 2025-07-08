```latex
\begin{exercise}{
Id: 7b9c5fda-fe94-4c85-a881-5ef3b77f7183
Title_exo: \en{Calculation of probabilities, expectation and variance of a binomial distribution}\fr{Calculs de probabilités, d'espérance et de variance d'une loi binomiale}
Modules: Proba_Stats_NYU
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Discrete_Probability_Distributions
Involved_Concepts: Binomial_Distribution, Expectation, Variance
Original_source: Ronan
Visibility: Teacher
}
{
\begin{python}
from sympy import *
import math as m
import random as rd

# Paramètres aléatoires pour l'exercice
nmin, nmax = 5, 20
prec = 0.1
pmin, pmax = 1, int(1 / prec - 1)
n = rd.randint(nmin, nmax)
p = round(rd.randint(pmin, pmax) * prec, 1) # p doit être un float avec une décimale
kmin, kmax = max(0, int(n * p) - 2), min(int(n * p) + 2, n) # Ajustement de k pour qu'il soit plus pertinent
k = rd.randint(kmin, kmax)

# --- QCM 1: Probabilité P(X=k) ---
# Bonne réponse
bonne_valeur_q1 = m.comb(n, k) * (p**k) * ((1 - p)**(n - k))

# Propositions fausses calculées
fausse_1_q1 = m.comb(n, k + 1) * (p**k) * ((1 - p)**(n - k)) if k + 1 <= n else m.comb(n, k - 1) * (p**k) * ((1 - p)**(n - k)) # Erreur sur k (k+1 ou k-1 si k+1 est hors limite)
fausse_2_q1 = m.comb(n, k) * (p**(k + 1)) * ((1 - p)**(n - k - 1)) if k + 1 <= n else m.comb(n, k) * (p**(k - 1)) * ((1 - p)**(n - k + 1)) # Erreur sur p (exposant de p ou 1-p)
fausse_3_q1 = m.comb(n - 1, k) * (p**k) * ((1 - p)**(n - 1 - k)) if n - 1 >= k else m.comb(n + 1, k) * (p**k) * ((1 - p)**(n + 1 - k)) # Erreur sur n (n-1 ou n+1)

# --- QCM 2: Espérance E[X] ---
# Bonne réponse
bonne_valeur_q2 = n * p

# Propositions fausses calculées
fausse_1_q2 = n * (1 - p)  # Erreur sur le paramètre p (utilise 1-p au lieu de p)
fausse_2_q2 = p  # Oubli de n
fausse_3_q2 = n * p * (1 - p) # Confusion avec la variance

# --- QCM 3: Variance V(X) ---
# Bonne réponse
bonne_valeur_q3 = n * p * (1 - p)

# Propositions fausses calculées
fausse_1_q3 = n * p  # Oubli du (1-p)
fausse_2_q3 = p * (1 - p)  # Oubli de n
fausse_3_q3 = n * (1 - p) # Erreur sur le paramètre p (utilise 1-p au lieu de p)
\end{python}

\fr{Soit $X$ une variable aléatoire obéissant à une loi binomiale $\mathcal{B}(\py{n};\py{p})$.}
\en{Let $X$ be a Binomial random variable, with parameters $n=\py{n}$ and $p=\py{p}$.}

\qcm{
\fr{Quelle est la probabilité $\fP(X=\py{k})$ ?}
\en{What is the probability $\fP(X=\py{k})$ ?}
}
{
\right{$\displaystyle \py{bonne_valeur_q1:.4f}$}
\wrong{$\displaystyle \py{fausse_1_q1:.4f}$}
\wrong{$\displaystyle \py{fausse_2_q1:.4f}$}
\wrong{$\displaystyle \py{fausse_3_q1:.4f}$}
}
{
\fr{Rappel de la formule de la loi binomiale : $\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$}
\en{Recall the binomial formula: $\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$}
}
{
\fr{Solution détaillée :
La probabilité $\fP(X=k)$ pour une loi binomiale $\mathcal{B}(n;p)$ est donnée par la formule :
$\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$.
En substituant les valeurs $n=\py{n}$, $p=\py{p}$ et $k=\py{k}$ :
\begin{equation*}
\fP(X=\py{k}) = \binom{\py{n}}{\py{k}} \py{p}^{\py{k}} (1-\py{p})^{\py{n}-\py{k}} = \py{m.comb(n,k)} \times \py{p**k:.4f} \times \py{(1-p)**(n-k):.4f} = \py{bonne_valeur_q1:.4f}
\end{equation*}}
\en{Detailed solution:
The probability $\fP(X=k)$ for a binomial distribution $\mathcal{B}(n;p)$ is given by the formula:
$\fP(X=k)=\binom{n}{k} p^{k} (1-p)^{n-k}$.
Substituting the values $n=\py{n}$, $p=\py{p}$ and $k=\py{k}$:
\begin{equation*}
\fP(X=\py{k}) = \binom{\py{n}}{\py{k}} \py{p}^{\py{k}} (1-\py{p})^{\py{n}-\py{k}} = \py{m.comb(n,k)} \times \py{p**k:.4f} \times \py{(1-p)**(n-k):.4f} = \py{bonne_valeur_q1:.4f}
\end{equation*}}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcm{
\fr{Quelle est l'espérance de $X$ ?}
\en{What is the expectation of $X$ ?}
}
{
\right{$\displaystyle \py{bonne_valeur_q2:.2f}$}
\wrong{$\displaystyle \py{fausse_1_q2:.2f}$}
\wrong{$\displaystyle \py{fausse_2_q2:.2f}$}
\wrong{$\displaystyle \py{fausse_3_q2:.2f}$}
}
{
\fr{Rappel : Pour une loi binomiale $\mathcal{B}(n;p)$, $\fE[X] = np$}
\en{Recall: For a binomial distribution $\mathcal{B}(n;p)$, $\fE[X] = np$}
}
{
\fr{Solution détaillée :
L'espérance d'une variable aléatoire suivant une loi binomiale $\mathcal{B}(n;p)$ est donnée par la formule $\fE[X] = np$.
En substituant les valeurs $n=\py{n}$ et $p=\py{p}$ :
\begin{equation*}
\fE[X] = np = \py{n} \times \py{p} = \py{bonne_valeur_q2:.2f}
\end{equation*}}
\en{Detailed solution:
The expectation of a random variable following a binomial distribution $\mathcal{B}(n;p)$ is given by the formula $\fE[X] = np$.
Substituting the values $n=\py{n}$ and $p=\py{p}$:
\begin{equation*}
\fE[X] = np = \py{n} \times \py{p} = \py{bonne_valeur_q2:.2f}
\end{equation*}}
}
{
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

\qcm{
\fr{Quelle est la variance de $X$ ?}
\en{What is the variance of $X$ ?}
}
{
\right{$\displaystyle \py{bonne_valeur_q3:.2f}$}
\wrong{$\displaystyle \py{fausse_1_q3:.2f}$}
\wrong{$\displaystyle \py{fausse_2_q3:.2f}$}
\wrong{$\displaystyle \py{fausse_3_q3:.2f}$}
}
{
\fr{Rappel : Pour une loi binomiale $\mathcal{B}(n;p)$, $\fV(X) = np(1-p)$}
\en{Recall: For a binomial distribution $\mathcal{B}(n;p)$, $\fV(X) = np(1-p)$}
}
{
\fr{Solution détaillée :
La variance d'une variable aléatoire suivant une loi binomiale $\mathcal{B}(n;p)$ est donnée par la formule $\fV(X) = np(1-p)$.
En substituant les valeurs $n=\py{n}$ et $p=\py{p}$ :
\begin{equation*}
\fV(X) = np(1-p) = \py{n} \times \py{p} \times (1-\py{p}) = \py{bonne_valeur_q3:.2f}
\end{equation*}}
\en{Detailed solution:
The variance of a random variable following a binomial distribution $\mathcal{B}(n;p)$ is given by the formula $\fV(X) = np(1-p)$.
Substituting the values $n=\py{n}$ and $p=\py{p}$:
\begin{equation*}
\fV(X) = np(1-p) = \py{n} \times \py{p} \times (1-\py{p}) = \py{bonne_valeur_q3:.2f}
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