
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
Les suites suivantes sont définies par des relations de récurrence $u_{n+1}=f\left(u_{n}\right)$. 
Donner la fonction $f$ correspondante dans chacun des cas.

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question

Soit la suite ${(u_n)}_{n\in\fN}$ définie par:
$
\begin{cases}
u _ { 0 }  & { = 4 } \\
   { u _ { n + 1 } } & { = 2 u _ { n } - 3 }
\end{cases}
$.
%\end{equation*}


}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour les suites définies par les relations de récurrence données, 
notre objectif est d'extraire la fonction $ f $ correspondante selon la forme générale 
$ u_{n+1} = f(u_n) $. 
   
Ici, la relation de récurrence étant $ u_{n+1} = 2 u_n - 3 $, on identifie aisément
la fonction $f$ qui est donnée par : 
 $f(x) = 2x - 3$.

}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
    u _ { 0 } &{=} 0  \\
    {u _ { n + 1 }} &{= \sqrt { 1 + u _ { n } ^ { 2 }}}
\end{cases}
$

}

{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour cette suite, la relation de récurrence est $ u_{n+1} = \sqrt{1 + u_n^2} $. 
On identifie aisément
la fonction $f$ qui est donnée par : 
   $
      f(x) = \sqrt{1 + x^2}.
   $
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
   { u _ { 0 }} &{= } 2  \\
   { u _ { n + 1 }} &{= \operatorname { s i n } ( u _ { n } ) }
\end{cases}
$
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 
    Dans ce cas, la relation de récurrence est  $ u_{n+1} = \sqrt{1 + u_n^2} $. 
On identifie aisément
la fonction $f$ qui est donnée par : 
   $
      f(x) = \sin(x).
   $
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
   u_{0}&{=}4 \\
   u_{n+1}&=\frac{u_{n}-1}{u_{n}+1}
\end{cases}
$
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
      Enfin, pour cette suite, la relation de récurrence est $ u_{n+1} = \frac{u_n - 1}{u_n + 1} $. 
Nous pouvons identifier la fonction $ f $ comme : 
   $
      f(x) = \frac{x - 1}{x + 1}.
   $
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
