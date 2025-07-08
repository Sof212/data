```latex
\begin{exercise}{
Title_exo: \fr{Codes de cadenas}\en{Padlock Codes}
Modules: Combinatorics
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Probability_and_Combinatorics
Involved_Concepts: Counting_principles, Permutations
Original_source: Adapted
Visibility: All
Comment: Exercice sur les principes de comptage appliqués aux codes de cadenas.
}
{
\fr{Un cadenas possède un code à 3 chiffres, chacun de ces chiffres est compris entre $1$ et $9$.}\en{A padlock has a 3-digit code, each digit being between $1$ and $9$.}

\begin{python}
from sympy import *

# Q1
bonne_valeur_q1 = 9**3
fausse_q1_1 = 3**9 # Erreur d'inversion
fausse_q1_2 = 9*3  # Erreur de multiplication au lieu de puissance
fausse_q1_3 = 10**3 # Chiffres de 0 à 9 (si 0 était inclus)
\end{python}

\qcm{ \fr{Combien y a-t-il de codes possibles en tout ?}\en{How many possible codes are there in total?}
}
{
\right{$\py{bonne_valeur_q1}$}
\wrong{$\py{fausse_q1_1}$}
\wrong{$\py{fausse_q1_2}$}
\wrong{$\py{fausse_q1_3}$}
}
{ % Indice
\fr{Pensez au nombre de choix pour chaque position du code.}\en{Think about the number of choices for each position of the code.}
}
{ % Solution détaillée
\fr{Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, et il y a $9$ choix possibles pour chaque chiffre (puisque l'on choisit un chiffre entre $1$ et $9$ inclus).
Donc, le nombre total de codes possibles est :}\en{For a three-digit code, each digit can be chosen independently of the others, and there are $9$ possible choices for each digit (since we choose a digit between $1$ and $9$ inclusive).
Thus, the total number of possible codes is:}
\begin{equation*}
9 \times 9 \times 9 = 9^3 = \py{bonne_valeur_q1}.
\end{equation*}
\fr{Il y a donc $\py{bonne_valeur_q1}$ choix distincts possibles de codes à trois chiffres.}\en{There are therefore $\py{bonne_valeur_q1}$ distinct possible choices for three-digit codes.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *

# Q2
bonne_valeur_q2 = 9
fausse_q2_1 = 1*1*1 # Oubli du chiffre du milieu
fausse_q2_2 = 9*9*9 # Erreur de compréhension des contraintes
fausse_q2_3 = 2*9*2 # Erreur sur les chiffres fixes
\end{python}

\qcm{ \fr{Combien y a-t-il de codes possibles qui commencent et se terminent par le chiffre $2$?}\en{How many possible codes start and end with the digit $2$?}
}
{
\right{$\py{bonne_valeur_q2}$}
\wrong{$\py{fausse_q2_1}$}
\wrong{$\py{fausse_q2_2}$}
\wrong{$\py{fausse_q2_3}$}
}
{ % Indice
\fr{Fixez les chiffres imposés et comptez les possibilités pour les autres.}\en{Fix the imposed digits and count the possibilities for the others.}
}
{ % Solution détaillée
\fr{Pour résoudre ce problème, nous divisons la solution en deux parties distinctes, chacune utilisant des principes de combinatoire.

Un code de $3$ chiffres est de la forme $XYZ$, où chaque lettre représente un chiffre compris entre $1$ et $9$. Pour ce cas particulier:

\begin{itemize}
    \item $X$ est le premier chiffre et doit être $2$. Il y a $1$ possibilité.
    \item $Y$ est le deuxième chiffre et peut être n'importe quel chiffre entre $1$ et $9$. Il y a $9$ possibilités.
    \item $Z$ est le troisième chiffre et doit également être $2$. Il y a $1$ possibilité.
\end{itemize}

Le nombre total de codes possibles dans ce cas est donc :}\en{To solve this problem, we divide the solution into two distinct parts, each using combinatorial principles.

A 3-digit code is of the form $XYZ$, where each letter represents a digit between $1$ and $9$. For this particular case:

\begin{itemize}
    \item $X$ is the first digit and must be $2$. There is $1$ possibility.
    \item $Y$ is the second digit and can be any digit between $1$ and $9$. There are $9$ possibilities.
    \item $Z$ is the third digit and must also be $2$. There is $1$ possibility.
\end{itemize}

The total number of possible codes in this case is therefore:}
\begin{equation*}
1 \times 9 \times 1 = \py{bonne_valeur_q2}.
\end{equation*}
\fr{Autrement dit, il existe $\py{bonne_valeur_q2}$ façons distinctes de créer un code à $3$ chiffres, dont les premier et dernier chiffres sont un $2$.}\en{In other words, there are $\py{bonne_valeur_q2}$ distinct ways to create a 3-digit code, where the first and last digits are $2$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *

# Q3
bonne_valeur_q3 = 4*9*5
fausse_q3_1 = 5*9*4 # Inversion pair/impair
fausse_q3_2 = 4*9*4 # Erreur sur le nombre de chiffres impairs
fausse_q3_3 = 5*9*5 # Erreur sur le nombre de chiffres pairs
\end{python}

\qcm{ \fr{Combien y a-t-il de codes possibles commençant par un chiffre pair et finissant par un chiffre impair?}\en{How many possible codes start with an even digit and end with an odd digit?}
}
{
\right{$\py{bonne_valeur_q3}$}
\wrong{$\py{fausse_q3_1}$}
\wrong{$\py{fausse_q3_2}$}
\wrong{$\py{fausse_q3_3}$}
}
{ % Indice
\fr{Identifiez les chiffres pairs et impairs entre $1$ et $9$.}\en{Identify the even and odd digits between $1$ and $9$.}
}
{ % Solution détaillée
\fr{Il y a $4$ chiffres pairs compris entre $1$ et $9$ (les chiffres $2, 4, 6$ et $8$) et $5$ chiffres impairs ($1, 3, 5, 7$ et $9$). Nous avons donc:
\begin{itemize}
    \item $4$ possibilités pour le premier chiffre (pair).
    \item $9$ possibilités pour le deuxième chiffre (de $1$ à $9$, sans contrainte).
    \item $5$ possibilités pour le dernier chiffre (impair).
\end{itemize}

Le nombre total de codes possibles dans ce cas est donc :}\en{There are $4$ even digits between $1$ and $9$ (digits $2, 4, 6,$ and $8$) and $5$ odd digits ($1, 3, 5, 7,$ and $9$). We therefore have:
\begin{itemize}
    \item $4$ possibilities for the first digit (even).
    \item $9$ possibilities for the second digit (from $1$ to $9$, no constraint).
    \item $5$ possibilities for the last digit (odd).
\end{itemize}

The total number of possible codes in this case is therefore:}
\begin{equation*}
4 \times 9 \times 5 = \py{bonne_valeur_q3}.
\end{equation*}
\fr{Autrement dit, il existe $\py{bonne_valeur_q3}$ façons distinctes de créer un code à $3$ chiffres, dont le premier chiffre est pair et le troisième impair.}\en{In other words, there are $\py{bonne_valeur_q3}$ distinct ways to create a 3-digit code, where the first digit is even and the third is odd.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}
}
\end{exercise}
```