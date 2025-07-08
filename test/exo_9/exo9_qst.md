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
 Exprimer chacun des expressions suivantes sous la forme $\ln (a)$, où $a>0$.

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$A:= \ln (7)+\ln (8)$.
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement 
positifs.% et pour tout entier $k\geq 1$.

\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
%
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
%[](#fer1) et aussi [](#fer2)
\end{equation}


En utilisant [](#fer1), on peut écrire:  
\begin{equation*}
\begin{align*}
\ln(7) + \ln(8) = \ln(7 \cdot 8) = \ln(56).
\end{align*}
\end{equation*}
   Ainsi, nous avons $A = \ln(56)$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$B:=\ln(20) - \ln(4)$.
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 En utilisant [](#fer2), on peut écrire:  
\begin{equation*}
\begin{align*}
\ln(20) - \ln(4) = \ln\left(\frac{20}{4}\right) = \ln(5).
\end{align*}
\end{equation*}
   Ainsi, nous avons $B = \ln(56)$.


}

{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$C := -\ln (4)+\ln (28)$
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 On peut reformuler l'expression $C$ en écrivant:
$C =  -\ln (4) + \ln (28) =\ln (28)-\ln (4) $.
En utilisant [](#fer2), on peut écrire:   
\begin{equation*}
\begin{align*}
C =  \ln (28)-\ln (4) 
= 
 \ln\left(\frac{28}{4}\right) = \ln 7.
\end{align*}
\end{equation*}
Ainsi, nous avons $C = \ln 7$.

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
