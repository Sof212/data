
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
Un cadenas possède un code a $3$ chiffres, chacun de ces chiffres est compris entre 
$1$ et $9$. 

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Au total, combien de codes peut-on former? 

}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","729"],["0"]]
}
{ % Ceci est mon indice
Combien de choix avez-vous pour chaque chiffre du code ?
 Pensez à ce que cela signifie lorsque les chiffres sont choisis indépendamment les uns des autres.
}
{ %La réponse correcte est:
729
}
{ % Ceci est la solution détaillée
Pour un code à trois chiffres, chaque chiffre peut être choisi indépendamment des autres, 
et il y a $9$ choix possibles pour chaque chiffre (puisque l'on choisit un chiffre 
entre $1$ et $9$ inclus). 
Donc, le nombre total de codes possibles est :



\begin{equation*}
9 \times 9 \times 9 = 9^3 = 729.
\end{equation*}
Il y a donc $ 729$ choix distincts possibles de codes à trois chiffres.
}
{
% Répartition des poids (Total = 100)
logic: 30
abstraction: 25
reasoning: 30
calculation: 15
}


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Combien de codes commencent et se terminent par le chiffre $2 ?$ 
}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","9"],["0"]]
}
{ % Ceci est mon indice
 Si les premier et dernier chiffres sont fixés, combien de choix reste-t-il pour le chiffre du milieu ?

}
{ %La réponse correcte est:
9
}
{ % Ceci est la solution détaillée
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
logic: 35
abstraction: 25
reasoning: 35
calculation: 5
}


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
 Combien de codes commencent par un chiffre pair et se terminent par un chiffre impair?

}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","180"],["0"]]
}
{ % Ceci est mon indice
Recherchez le nombre de chiffres pairs entre $1$ et $9$

}
{ %La réponse correcte est:
180
}
{ % Ceci est la solution détaillée
Il y a $4$ chiffres  pairs compris entre $1$ et $9$ (les chiffres $2, 4, 6$ et $8$ et cinq 
chiffres impairs $1, 3, 5, 7$ et  $9$. Nous avons donc:
- $4$ possibilités pour le premier chiffre
- $9$ possibilités pour le deuxième chiffre (de $1$ à $9$). 
- $5$ possibilités pour le dernier chiffre


Le nombre total de codes possibles dans ce cas est donc : 
\begin{equation*}
4 \times 9 \times 5 = 180.
\end{equation*}


Autrement dit, il existe $180$ façons distinctes de créer un code à $3$ chiffres, dont 
le premier chiffre est pair et le troisième impair.
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

