
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
[["CL","6561"],["0"]]
}
{ % Ceci est mon indice
Combien de choix avez-vous pour chaque chiffre du code ?
 Pensez à ce que cela signifie lorsque les chiffres sont choisis indépendamment les uns des autres.
}
{ %La réponse correcte est:
6561
}
{ % Ceci est la solution détaillée




\begin{equation*}
9^4 = 6561.
\end{equation*}
Il y a donc $6561$ choix distincts possibles de codes à trois chiffres.
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


}
{ %La réponse correcte est:
9
}
{ % Ceci est la solution détaillée



\begin{equation*}
1 \times 9 \times 1 = 9.
\end{equation*}

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
[["CL","216"],["0"]]
}
{ % Ceci est mon indice


}
{ %La réponse correcte est:
216
}
{ % Ceci est la solution détaillée

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

