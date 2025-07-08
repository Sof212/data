

\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts : % ID ou NameID des notions
}
{
% Contenu de l'exercice
Déterminer les limites suivantes.

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 2^{+}}\left(\frac{1}{-2 x+4}\right)$
}
{
\right{$-\infty$}
\wrong{$+\infty$}
\wrong{$1$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

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

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x+4}\right)$
}
{
\wrong{$-\infty$}
\right{$+\infty$}
\wrong{$1$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
  Lorsque $x$ tend vers $2^{-}$
 (valeurs légèrement inférieures à $2$), on a :
\begin{equation*}
   - 2(2^{-}) + 4 = 4 - 2(2^{-}) = 4 - 4^{-} = 0^{+}.
\end{equation*}
   En examinant le signe de $-2x + 4$ lorsque $x$ approche $2$ par la gauche, nous avons : 
\begin{equation*}
   - 2x + 4 > 0 \quad \text{(pour } x < 2 \text{)} 
\end{equation*}
   Ce qui implique que $-2x + 4 > 0$. Ainsi, $\frac{1}{-2x + 4}$ tend vers $+\infty$, lorsque $x$ tend vers $2$ par valeurs inférieures (\ie par la gauche). Donc : 
\begin{equation*}
   \lim\limits_{x \rightarrow 2^{-}}\left(\frac{1}{-2 x + 4}\right) = +\infty.
\end{equation*}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 0^{+}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{
\right{$-\infty$}
\wrong{$0$}
\wrong{$+\infty$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%**Limite $\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x-4}{x-3}\right)$** :
 
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
\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{
\wrong{$-\infty$}
\right{$+\infty$}
\wrong{$0$}


% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

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




\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 3^{+}}\left(\frac{x-4}{x-3}\right)$
}
{
\wrong{$-3$}
\wrong{$-4$}
\right{$+\infty$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%**Limite $\lim\limits_{x \rightarrow 0^{+}}\left(2+\frac{1}{\sqrt{x}}(2x+1)\right)$** : 

 Analysons l'expression $  \left(2+\frac{1}{\sqrt{x}}\right)(2x+1) $ à mesure que $x$
 tend vers $0^{+}$. On a :
\begin{equation*}
\bigg(2+\frac{1}{\sqrt{x}}\bigg)(2x+1) = 2(2x+1) + \frac{1}{\sqrt{x}}(2x+1) = 4x + 2 + \frac{2x}{\sqrt{x}} + \frac{1}{\sqrt{x}}. 
\end{equation*}
   Lorsque $x$ approche $0^{+}$, $\sqrt{x} $ tend vers $0$ et $\frac{1}{\sqrt{x}} \rightarrow$ tend vers  $+\infty$. Par conséquent, 
$
   \lim\limits_{x \rightarrow 0^{+}}\left(4x + 2 + \frac{1}{\sqrt{x}}\right) = +\infty. 
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
$\lim\limits_{x \rightarrow 3^{-}}\left(\frac{x-4}{x-3}\right)$
}
{
\wrong{$-3$}
\wrong{$+\infty$}
\right{$-\infty$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%**Limite $\lim\limits_{x \rightarrow 0^{-}}\left(2+\frac{1}{\sqrt{x}}(2x+1)\right)$** : 
 Analysons l'expression $  \left(2+\frac{1}{\sqrt{x}}\right)(2x+1) $ à mesure que $x$
 tend vers $0^{-}$. On a :
\begin{equation*}
   \left(2+\frac{1}{\sqrt{x}}\right)(2x+1) = 2(2x+1) + \frac{1}{\sqrt{x}}(2x+1) = 4x + 2 + \frac{2x}{\sqrt{x}} + \frac{1}{\sqrt{x}}. 
\end{equation*}

   Lorsque $x$ approche $0^{-}$, on a $\sqrt{x}$ tend vers $0$ et $\frac{1}{\sqrt{x}}$ tend vers
$-\infty$. Par conséquent, 
\begin{equation*}
   \lim\limits_{x \rightarrow 0^{-}}\left(4x + 2 + \frac{1}{\sqrt{x}}\right) = -\infty. 
\end{equation*}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}




\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$\lim\limits_{x \rightarrow 0^{-}}\left(\left(2+\frac{1}{\sqrt{x}}\right)(2 x+1)\right)$
}
{
\wrong{$0$}
\wrong{$+\infty$}
\wrong{$-\infty$}
\right{Aucune des réponses proposées}
% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
$\sqrt{x}$ n'étant pas défini lorsque $x$ est négatif, on
ne peut pas considérer $4x + 2 + \frac{1}{\sqrt{x}}$ lorsque $x$ approche $0$ par valeurs. négatives.
La quantité $\lim\limits_{x \rightarrow 0^{-}}\left(4x + 2 + \frac{1}{\sqrt{x}}\right)$
n'a donc aucun sens.

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



