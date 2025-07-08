
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

Les suites ci-dessous sont définies par des relations de récurrence $u_{n+1}=f\left(u_{n}\right)$. 
Donner la fonction $f$ correspondante dans chacun des cas.


\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
u _ { 0 }  &=& 4  \\
 u _ { n + 1 }  & =&  2 u _ { n } - 3 
\end{cases}
$.
}
{

\wrong{$f(x)=3-2x$}
\right{ $f(x)=2x - 3$ }
\wrong{$f(x)=\sqrt{1 + x^2}$}
\right{ $f(x)=\frac{4}{2x - 3}$ }



% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

 $f(x) = 2x - 3$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
u _ { 0 }  &=& 0  \\
 u _ { n + 1 }  & =&  \sqrt { 1 + u _ { n } ^ { 2 } }
\end{cases}
$
}
{


\wrong{$f(x) = \sqrt{1 - x^2}$}
\right{$f(x) = \sqrt{1 + x^2}$}
\wrong{$f(x) = -\sqrt{1 + x^2}$}
\wrong{$f(x) = -\sqrt{1 - x^2}$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

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

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
u _ { 0 }  &=& 2  \\
 u _ { n + 1 }  & =&   \sin( u _ { n } ) 
\end{cases}
$
}
{
\wrong{$f(x) = 1 - \sin(x^2)$}
\wrong{$f(x) = \sqrt{1 - \sin(x^2)}$}
\wrong{$f(x) = |1 - \cos(x^2)|$}
\right{$f(x) = \sin(x)$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

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

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
   u_{0}=4 \\
   u_{n+1}=\frac{u_{n}-1}{u_{n}+1}
 \end{cases}
$
}
{

\wrong{$f(x) =\frac{\sqrt{x + 1}}{\sqrt{x - 1}}$}
\right{$f(x) =\frac{x - 1}{x + 1}$}
\wrong{$f(x) = \sin(x)$}
\wrong{$f(x) =\frac{x + 1}{x - 1}$}


% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 
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
