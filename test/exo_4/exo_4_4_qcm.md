
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
Soit $\left(u_{n}\right)_{n \geqslant 0}$ la suite géométrique de terme initial 3 et de raison $1 / 2$. Soit $\left(s_{n}\right)_{n \geqslant 0}$ la suite définie pour tout $n$ par

\begin{equation*}
s_{n}=u_{0}+u_{1}+\cdots+u_{n}
\end{equation*}
\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
On souhaite mettre $\left(s_{n}\right)_{n}$ sous forme explicite. On a :
$s_n= $
}
{

\right{$6\left(1 + \frac{1}{2^{n+1}}\right) $}
\wrong{$6\left(1 - \frac{1}{2^{n+1}}\right) $}
\wrong{$2\left(1 + \frac{1}{2^{n-1}}\right) $}
\wrong{$2\left(1 - \frac{1}{2^{n-1}}\right) $}




% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.


En utilisant le rappel précédent avec $u_0 = 3$, $q= \frac{1}{2} $,  $N = n+1$, on peut écrire:

\begin{equation*}
w_n = 3\cdot \frac{1\left(1 - \left(\frac{1}{2}\right)^{n+1}\right)}{1 - \frac{1}{2}} 
=
 \frac{1 - \frac{1}{2^{n+1}}}{\frac{1}{2}} = 2\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation*}

En substituant cette expression dans [](djdjdoij),  on obtient : 
\begin{equation*}
s_n = 3 \cdot 2\left(1 - \frac{1}{2^{n+1}}\right) = 6\left(1 + \frac{1}{2^{n+1}}\right).
\end{equation*}

Autrement dit, on a:
\begin{equation}
\label{oijfoij}
s_n = 6\left(1 + \frac{1}{2^{n+1}}\right).
\end{equation}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcm{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
On souhaite déterminer la limite de la suite $\left(s_{n}\right)_{n}$. 

On a $\lim\limits_{n\to\infty}s_n= $

}
{
\right{$6$}
\wrong{$+\infty$}
\wrong{$0$}
\wrong{-$\infty$}


% Ajoutez autant de réponses que nécessaire

}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.


\begin{equation*}
 \lim\limits_{n \rightarrow \infty} s_n
=
6.
\end{equation*}


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
