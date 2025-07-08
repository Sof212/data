```latex
\begin{exercise}{
Title_exo: \fr{Codes de cadenas}\en{Padlock Codes}
Modules: Probabilities_and_Statistics % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Combinatorics % NameID des chapitres
Involved_Concepts: Permutations, Combinations % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
}
{
% Contenu de l'exercice
\fr{Un cadenas possède un code a 3 chiffres, chacun de ces chiffres est compris entre 
$1$ et $9$.}\en{A padlock has a 3-digit code, each digit being between $1$ and $9$.}

\qcm{\fr{Combien y a-t-il de codes possibles en tout?}\en{How many possible codes are there in total?}
}
\begin{python}
from sympy import *
# === Calcul bonne réponse ===
bonne_valeur = 9**3
# === Propositions fausses calculées ===
fausse_1 = 9 * 8 * 7
fausse_2 = 10**3
fausse_3 = 9 * 9 * 8
fausse_4 = 9 * 10 * 10
\end{python}
{
\right{$\displaystyle 9^3 = \sympy{bonne_valeur}$}
\wrong{$\displaystyle 9 \times 8 \times 7 = \sympy{fausse_1}$}
\wrong{$\displaystyle 10^3 = \sympy{fausse_2}$}
\wrong{$\displaystyle 9 \times 9 \times 8 = \sympy{fausse_3}$}
\wrong{$\displaystyle 9 \times 10 \times 10 = \sympy{fausse_4}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
\fr{Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, 
et il y a $9$ choix possibles pour chaque chiffre (puisque l'on choisit un chiffre 
entre $1$ et $9$ inclus). 
Donc, le nombre total de codes possibles est :}\en{For a three-digit code, each digit can be chosen independently of the others, and there are $9$ possible choices for each digit (since we choose a digit between $1$ and $9$ inclusive). Therefore, the total number of possible codes is:}

\begin{equation*}
9 \times 9 \times 9 = 9^3 = \sympy{bonne_valeur}.
\end{equation*}
\fr{Il y a donc $ \sympy{bonne_valeur}$ choix distincts possibles de codes à trois chiffres.}\en{Thus, there are $\sympy{bonne_valeur}$ distinct possible choices for three-digit codes.}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{\fr{Combien y a-t-il de codes possibles qui commence et se termine par le chiffre $2$?}\en{How many possible codes start and end with the digit $2$?}
}
\begin{python}
from sympy import *
# === Calcul bonne réponse ===
bonne_valeur = 9
# === Propositions fausses calculées ===
fausse_1 = 1
fausse_2 = 8
fausse_3 = 10
fausse_4 = 81
\end{python}
{
\right{$\displaystyle \sympy{bonne_valeur}$}
\wrong{$\displaystyle \sympy{fausse_1}$}
\wrong{$\displaystyle \sympy{fausse_2}$}
\wrong{$\displaystyle \sympy{fausse_3}$}
\wrong{$\displaystyle \sympy{fausse_4}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
\fr{Pour résoudre ce problème, nous divisons la solution en deux parties distinctes, chacune utilisant des principes de combinatoire. 

Un code de $3$ chiffres est de la forme $XYZ$, où chaque
 lettre représente un chiffre compris entre $1$ et $9$. Pour ce cas particulier:}\en{To solve this problem, we divide the solution into two distinct parts, each using combinatorial principles.

A 3-digit code is of the form $XYZ$, where each letter represents a digit between $1$ and $9$. For this particular case:}
\begin{itemize}
    \item \fr{$X$ est le premier chiffre et doit être $2$.}\en{$X$ is the first digit and must be $2$.}
    \item \fr{$Y$ est le deuxième chiffre et peut être n'importe quel chiffre entre $1$ et $9$.}\en{$Y$ is the second digit and can be any digit between $1$ and $9$.}
    \item \fr{$Z$ est le troisième chiffre et doit également être $2$.}\en{$Z$ is the third digit and must also be $2$.}
\end{itemize}
\fr{Donc, nous avons :}\en{So, we have:}
\begin{itemize}
    \item \fr{$1$ possibilité pour le premier chiffre}\en{$1$ possibility for the first digit}
    \item \fr{$9$ possibilités pour le deuxième chiffre (de $1$ à $9$).}\en{$9$ possibilities for the second digit (from $1$ to $9$).}
    \item \fr{$1$ possibilité pour le dernier chiffre}\en{$1$ possibility for the last digit}
\end{itemize}
\fr{Le nombre total de codes possibles dans ce cas est donc :}\en{The total number of possible codes in this case is therefore:}
\begin{equation*}
1 \times 9 \times 1 = 9.
\end{equation*}
\fr{Autrement dit, il existe $9$ façons distinctes de créer un code à $3$ chiffres, dont 
les premier et dernier chiffres sont un $2$.}\en{In other words, there are $9$ distinct ways to create a 3-digit code where the first and last digits are $2$.}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{\fr{Combien y a-t-il de codes possibles commençant par un chiffre pair et finissant par un chiffre impair?}\en{How many possible codes start with an even digit and end with an odd digit?}
}
\begin{python}
from sympy import *
# === Calcul bonne réponse ===
bonne_valeur = 4 * 9 * 5
# === Propositions fausses calculées ===
fausse_1 = 4 * 9 * 4
fausse_2 = 5 * 9 * 5
fausse_3 = 4 * 10 * 5
fausse_4 = 5 * 9 * 4
\end{python}
{
\right{$\displaystyle 4 \times 9 \times 5 = \sympy{bonne_valeur}$}
\wrong{$\displaystyle 4 \times 9 \times 4 = \sympy{fausse_1}$}
\wrong{$\displaystyle 5 \times 9 \times 5 = \sympy{fausse_2}$}
\wrong{$\displaystyle 4 \times 10 \times 5 = \sympy{fausse_3}$}
\wrong{$\displaystyle 5 \times 9 \times 4 = \sympy{fausse_4}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
\fr{Il y a $4$ chiffres pairs compris entre $1$ et $9$ (les chiffres $2, 4, 6$ et $8$) et cinq 
chiffres impairs $1, 3, 5, 7$ et $9$. Nous avons donc:}\en{There are $4$ even digits between $1$ and $9$ (digits $2, 4, 6,$ and $8$) and five odd digits $1, 3, 5, 7,$ and $9$. So we have:}
\begin{itemize}
    \item \fr{$4$ possibilités pour le premier chiffre (pair).}\en{$4$ possibilities for the first digit (even).}
    \item \fr{$9$ possibilités pour le deuxième chiffre (de $1$ à $9$).}\en{$9$ possibilities for the second digit (from $1$ to $9$).}
    \item \fr{$5$ possibilités pour le dernier chiffre (impair).}\en{$5$ possibilities for the last digit (odd).}
\end{itemize}
\fr{Le nombre total de codes possibles dans ce cas est donc :}\en{The total number of possible codes in this case is therefore:}
\begin{equation*}
4 \times 9 \times 5 = \sympy{bonne_valeur}.
\end{equation*}
\fr{Autrement dit, il existe $\sympy{bonne_valeur}$ façons distinctes de créer un code à $3$ chiffres, dont 
le premier chiffre est pair et le troisième impair.}\en{In other words, there are $\sympy{bonne_valeur}$ distinct ways to create a 3-digit code where the first digit is even and the third is odd.}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}
}
\end{exercise}
```