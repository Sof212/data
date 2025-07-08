
\begin{exercise}{
Title_exo:  (Benoit Rittaud) % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts: % ID ou NameID des notions
Original_source: % Source de l'exercice
}
{
% Contenu de l'exercice
Un cadenas possède un code a $3$ chiffres, chacun de ces chiffres est compris entre 
$1$ et $9$. 

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Parmi les choix donnés ci-dessous lequel ou lesquels corresponds au nombre total 
de combinaisons de codes possibles:
}
{
\right{729}
\wrong{300}
\wrong{27}
\right{81}
\wrong{504}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.


\begin{equation*}
9 \times 9 \times 9 = 9^3 = 729.
\end{equation*}

}
{
% Répartition des poids (Total = 100)
logic: 30
abstraction: 25
reasoning: 30
calculation: 15
}

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Combien de codes commencent et se terminent par le chiffre $2$?

Choisissez la ou les bonnes réponses.

}
{
\wrong{11}
\wrong{10}
\right{81}
\wrong{8}
% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.
 Si les premier et dernier chiffres sont fixés, combien de choix reste-t-il pour le chiffre du milieu ?
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
- $9$ possibilité pour le dernier chiffre


Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
1 \times 9 \times 9 = 81.
\end{equation*}
Autrement dit, il existe $9$ façons distinctes de créer un code à $3$ chiffres, dont 
les premier et dernier chiffres sont un $2$.
}
{
% Répartition des poids (Total = 100)
logic: 35
abstraction: 25
reasoning: 35
calculation: 5
}

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Combien de codes commencent par un chiffre pair et se terminent par un chiffre impair?

Choisissez la ou les bonnes réponses.
}
{
\wrong{150}
\wrong{175}
\wrong{178}
\wrong{é&§}
\wrong{220}
\wrong{225}
\righter
% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Recherchez le nombre de chiffres pairs entre $1$ et $9$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Il y a $4$ chiffres  pairs compris entre $1$ et $9$ (les chiffres $2, 4, 6$ et $8$ et cinq 
chiffres impairs $1, 3, 5, 7$ et  $9$. Nous avons donc:
- $4$ possibilités pour le premier chiffre
- $9$ possibilités pour le deuxième chiffre (de $1$ à $9$). 
- $§$ possibilités pour le dernier chiffre


Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
4 \times 9 \times 6 = 216.
\end{equation*}





}
{
% Répartition des poids (Total = 100)
logic: 35
abstraction: 20
reasoning: 35
calculation: 10
}

}
\end{exercise}
