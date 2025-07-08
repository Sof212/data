```latex
\begin{exercise}{
Title_exo: \fr{Combinaisons de codes cadenas}\en{Combination Lock Codes}
Modules: Combinatoire % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Dénombrement % NameID des chapitres
Involved_Concepts: Principe multiplicatif, Permutations % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
Comment: Exercice sur le dénombrement des codes de cadenas. % Comment: % Commentaire de l'exercice (optionnel)
}
{
(quest1)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = 9**3
# === Propositions fausses calculées ===
fausse_1 = 9**2  # Erreur méthodologique typique: oubli du 3ème chiffre
fausse_2 = 10**3  # Variante calcul incorrecte: inclusion du chiffre 0
fausse_3 = 9*3    # Approximation erronée: multiplication au lieu de puissance
\end{python}
\qcm{ \fr{Un cadenas possède un code à 3 chiffres, chacun compris entre 1 et 9. Combien y a-t-il de codes possibles en tout ?}\en{A padlock has a 3-digit code, each digit between 1 and 9. How many possible codes are there in total?}
}
{
\right{$\py{bonne_valeur}$}
\wrong{$\py{fausse_1}$}
\wrong{$\py{fausse_2}$}
\wrong{$\py{fausse_3}$}
}
{%% Solution détaillée : \fr{Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, avec $9$ choix possibles par chiffre. Le nombre total est donc $9 \times 9 \times 9 = 729$.}\en{For a three-digit code, each digit can be chosen independently of the others, with $9$ possible choices for each digit. The total number is therefore $9 \times 9 \times 9 = 729$.}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

(quest2)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = 9
# === Propositions fausses calculées ===
fausse_1 = 8  # Erreur méthodologique typique: oubli d'une possibilité (ex: 0 inclus)
fausse_2 = 10 # Variante calcul incorrecte: inclusion du chiffre 0
fausse_3 = 9*2 # Approximation erronée: multiplication par 2 au lieu de 1
\end{python}
\qcm{ \fr{Même contexte. Combien de codes commencent et se terminent par le chiffre 2 ?}\en{Same context. How many codes start and end with the digit 2?}
}
{
\right{$\py{bonne_valeur}$}
\wrong{$\py{fausse_1}$}
\wrong{$\py{fausse_2}$}
\wrong{$\py{fausse_3}$}
}
{%% Solution détaillée : \fr{Le premier et dernier chiffre sont fixés à $2$ ($1$ choix chacun), le chiffre du milieu a $9$ possibilités (de $1$ à $9$). Le nombre total de codes est donc $1 \times 9 \times 1 = 9$.}\en{The first and last digits are fixed at $2$ ($1$ choice each), the middle digit has $9$ possibilities (from $1$ to $9$). The total number of codes is therefore $1 \times 9 \times 1 = 9$.}
}
{ % Répartition des poids (Total = 100)
reasoning: 25
logic: 25
abstraction: 25
calculation: 25
}

(quest3)=
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = 4 * 9 * 5
# === Propositions fausses calculées ===
fausse_1 = 5 * 9 * 4  # Erreur méthodologique typique: inversion pair/impair
fausse_2 = 4 * 8 * 5  # Variante calcul incorrecte: oubli d'une possibilité pour le chiffre du milieu
fausse_3 = 4 * 9 * 4  # Approximation erronée: erreur sur le nombre de chiffres impairs
\end{python}
\qcm{ \fr{Même contexte. Combien de codes commencent par un chiffre pair et finissent par un chiffre impair ?}\en{Same context. How many codes start with an even digit and end with an odd digit?}
}
{
\right{$\py{bonne_valeur}$}
\wrong{$\py{fausse_1}$}
\wrong{$\py{fausse_2}$}
\wrong{$\py{fausse_3}$}
}
{%% Solution détaillée : \fr{Les chiffres pairs entre $1$ et $9$ sont $\{2, 4, 6, 8\}$, soit $4$ possibilités. Les chiffres impairs entre $1$ et $9$ sont $\{1, 3, 5, 7, 9\}$, soit $5$ possibilités. Le chiffre du milieu a $9$ possibilités (de $1$ à $9$). Le nombre total de codes est donc $4 \times 9 \times 5 = 180$.}\en{The even digits between $1$ and $9$ are $\{2, 4, 6, 8\}$, which is $4$ possibilities. The odd digits between $1$ and $9$ are $\{1, 3, 5, 7, 9\}$, which is $5$ possibilities. The middle digit has $9$ possibilities (from $1$ to $9$). The total number of codes is therefore $4 \times 9 \times 5 = 180$.}
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