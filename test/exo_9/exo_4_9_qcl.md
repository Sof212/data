\begin{exercise}{
Title_exo: Logarithmes et simplification % Nom de l'exercice
Modules: Fonctions % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Logarithmes % NameID des chapitres
Involved_Concepts: Propriétés_des_logarithmes % ID ou NameID des notions
Original_source: % Source de l'exercice
}
{
% Contenu de l'exercice
Exprimer chacun des nombres suivants sous la forme $\ln(a)$, où $a>0$.



\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$A:=\ln(7) + \ln(8)$ : 
}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","$\ln(56)$"],["0"]]
}
{ % Ceci est mon indice
Utilisez la propriété $\ln(a) + \ln(b) = \ln(ab)$.
}
{ %La réponse correcte est:
$A=\ln(56)$.
}
{ % Ceci est la solution détaillée


 nous avons $A = \ln(56)$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$B:=\ln(20) - \ln(4)$: 

}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","$\ln(5)$"],["0"]]
}
{ % Ceci est mon indice
Utilisez la propriété $\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)$.

}
{ %Solution brève
$B =\ln(5)$.
}
{ % Ceci est la solution détaillée
En utilisant la deuxième propriété, donnée dans l'indication ci-dessus, on a :  
\begin{equation*}
\ln(20) - \ln(5) 
=
\ln\left(\frac{20}{4}\right) 
=
 \ln(5).
\end{equation*}
Ainsi, nous avons $B =\ln(4)$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$C:=-\ln(4) + \ln(28)$ :
}
{ % Solution PyxiScience: pour PyxiScience uniquement
[["CL","$\ln(7)$"],["0"]]
}
{ % Ceci est mon indice
Reformulez l'expression en utilisant la propriété 
$\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)$.
}
{ %La réponse correcte est:
$7$.
}
{ % Ceci est la solution détaillée
Reformulons l'expression. On a :
\begin{equation*}
C 
=
-\ln(4) + \ln(28) 
=
 \ln(28) - \ln(4) 
=
 \ln\left(\frac{28}{4}\right) 
=
 \ln(7).
\end{equation*}


Ainsi, nous avons $C = 7$.
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
