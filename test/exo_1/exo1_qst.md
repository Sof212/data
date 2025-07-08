## Exercice


\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts: % ID ou NameID des notions
Original_source: % Source de l'exercice
}
{
% Contenu de l'exercice
Un cadenas possède un code a 3 chiffres, chacun de ces chiffres est compris entre 
$1$ et $9$. 

Combien y a-t-il de codes possibles:



\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
en tout?
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, 
et il y a $9$ choix possibles pour chaque chiffre (puisque l'on choisit un chiffre 
entre $1$ et $9$ inclus). 
Donc, le nombre total de codes possibles est :

\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
a = 9**3
\end{python}
\begin{equation*}
9 \times 9 \times 9 = 9^3 = \py{a}.
\end{equation*}
Il y a donc $ \py{a}$ choix distincts possibles de codes à trois chiffres.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}



\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
qui commence et se termine par le chiffre $2$?
}

{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour résoudre ce problème, nous divisons la solution en deux parties distinctes, chacune utilisant des principes de combinatoire. 

Un code de $3$ chiffres est de la forme $XYZ$, où chaque
 lettre représente un chiffre compris entre $1$ et $9$. Pour ce cas particulier:  

- $X$ est le premier chiffre et doit être $2$.
- $Y$ est le deuxième chiffre et peut être n'importe quel chiffre entre $1$ et $9$.
- $Z$ est le troisième chiffre et doit également être $2$.

Donc, nous avons :  
- $1$ possibilité pour le premier chiffre
- $9$ possibilités pour le deuxième chiffre (de $1$ à $9$). 
- $1$ possibilité pour le dernier chiffre

Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
1 \times 9 \times 1 = 9.
\end{equation*}
Autrement dit, il existe $9$ façons distinctes de créer un code à $3$ chiffres, dont 
les premier et dernier chiffres sont un $2$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
commençant par un chiffre pair et finissant par un chiffre impair?
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
b = 4*9*5
\end{python}

Il y a $4$ chiffres  pairs compris entre $1$ et $9$ (les chiffres $2, 4, 6$ et $8$ et cinq 
chiffres impairs $1, 3, 5, 7$ et  $9$. Nous avons donc:
- $4$ possibilités pour le premier chiffre
- $9$ possibilités pour le deuxième chiffre (de $1$ à $9$). 
- $5$ possibilités pour le dernier chiffre

Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
4 \times 9 \times 5 = \py{b}.
\end{equation*}

Autrement dit, il existe $\py{b}$ façons distinctes de créer un code à $3$ chiffres, dont 
le premier chiffre est pair et le troisième impair.


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
