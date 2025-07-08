\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts : % ID ou NameID des notions
}
{
Déterminer les limites suivantes.

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x+4}\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$-\infty$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$-\infty$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
 Tout d'abord, nous remarquons que : $-2x + 4$ en $4 - 2x$.  Par ailleurs, lorsque $x$ tend vers $2^{+}$
 (valeurs légèrement supérieures à $2$), on a :
\begin{equation*}
   4 - 2(2^{+}) = 4 - 4^{+} = 0^{-}.
\end{equation*}
   En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la droite, nous avons : 
\begin{equation*}
   4 - 2x < 0 \quad \text{(pour } x > 2 \text{)} 
\end{equation*}
   Ce qui implique que $-2x + 4 < 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $-\infty$, lorsque $x$ tend vers $2$ par valeurs supérieures (\ie par la droite). Donc : 
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x + 4}\right) = -\infty.
\end{equation*}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}



\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$+\infty$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$+\infty$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%**Limite $\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x-4}{x-3}\right)$** :
 
   En regardant l'expression : 
$
   \frac{x - 4}{x - 3}. 
$
   Lorsque $x \rightarrow 3^{+}$, on a $
   x - 4 \rightarrow -1 \quad \text{et} \quad x - 3 \rightarrow 0^{-}. 
$
   Ceci donne : 

\begin{equation*}
\lim\limits_{x \rightarrow 3^{-}} \frac{x-4}{x-3}
=
   \frac{-1}{0^{-}} = +\infty. 
\end{equation*}

   Donc : 
$
   \lim\limits_{x \rightarrow 3^{+}}\left(\frac{x - 4}{x - 3}\right) = +\infty. 
$
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x-4}{x-3}\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$-\infty$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$-\infty$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%**Limite $\lim\limits_{x \rightarrow 0^{+}}\left(2+\frac{1}{\sqrt{x}}(2x+1)\right)$** : 

   En regardant l'expression : 
$
   \frac{x - 4}{x - 3}. 
$
   Lorsque $x \rightarrow 3^{+}$, on a $
   x - 4 \rightarrow -1 \quad \text{et} \quad x - 3 \rightarrow 0^{+}. 
$
   Ceci donne : 

\begin{equation*}
\lim\limits_{x \rightarrow 3^{-}} \frac{x-4}{x-3}
=
   \frac{-1}{0^{+}} = -\infty. 
\end{equation*}

   Donc : 
$
   \lim\limits_{x \rightarrow 3^{+}}\left(\frac{x - 4}{x - 3}\right) = -\infty. 
$
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x-4}{x-3}\right)$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$-\infty$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$-\infty$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%**Limite $\lim\limits_{x \rightarrow 0^{-}}\left(2+\frac{1}{\sqrt{x}}(2x+1)\right)$** : 
   En regardant l'expression : 
$
   \frac{x - 4}{x - 3}. 
$
   Lorsque $x \rightarrow 3^{-}$, on a $
   x - 4 \rightarrow -1 \quad \text{et} \quad x - 3 \rightarrow 0^{-}. 
$
   Ceci donne : 

\begin{equation*}
\lim\limits_{x \rightarrow 3^{-}} \frac{x-4}{x-3}
=
   \frac{-1}{0^{-}} = +\infty. 
\end{equation*}

   Donc : 
$
   \lim\limits_{x \rightarrow 3^{-}}\left(\frac{x - 4}{x - 3}\right) = +\infty. 
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
