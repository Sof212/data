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
Déterminer une primitive de chacune des fonctions définies ci-dessous.<!-- 
, sur ${\bfR}^{*}_+$, par
 les expressions suivantes: -->

\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Soit $f:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction $\ds f(x) := \frac{x^{2}-2 x+1}{3}$.
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%Si l'on a remarqué que l'on peut simplifier l'expression $ \frac{1}{3}(x^2 - 2x + 1)$ en $ \frac{1}{3}(x-1)^2 $, alors 
On peut écrire:
\begin{equation*}
\begin{align*}
\int f(x) \ dx 
&=
\int  \frac{x^{2}-2 x+1}{3} \ dx 
=
 \frac{1}{3} \int (x^{2}-2 x+1) \ dx \\
&=
 \frac{1}{3} \left[ \frac{x^{3}}{3}- 2\frac{x^2}{2} + x \right] + C,
=
\frac{x^{3}}{9} - \frac{x^{2}}{3} + \frac{x}{3} + C,
\end{align*}
\end{equation*}
\fr{où $C$ désigne un nombre réel}%
\en{where $C$ is any real number}.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


\qst{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Soit $g:{\bfR}^{*}_+ \rightarrow \bfR$ la fonction définie par:
$\ds g(x) := x^{4}-4 x^{3}+x^{2}-4 x+3$.
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Là encore nous allons intégrer terme à terme.
On peut écrire:
\begin{equation*}
\begin{align*}
\int g(x) \ dx 
&=
\int (x^{4}-4x^{3}+x^{2}-4x+3) \, dx \\
&=
\frac{x^{5}}{5} - x^{4} + \frac{x^{3}}{3} - 2x^2 + 3x + C,
\end{align*}
\end{equation*}
\fr{où $C$ désigne un nombre réel}%
\en{where $C$ is any real number}.




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
