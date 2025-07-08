

\begin{exercise}{
Title_exo: % Nom de l'exercice
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: % NameID des chapitres
Involved_Concepts : % ID ou NameID des notions
}
{


\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python

import sympy as sp
import numpy as np

n = sp.Symbol('n', integer=True, positive=True)


s_n = 6 * (1 - 1/(2**(n+1)))

\end{python}

% Contenu de l'exercice
Soit $\left(u_{n}\right)_{n \geqslant 0}$ la suite géométrique de terme initial 3 et de raison $1 / 2$. Soit $\left(s_{n}\right)_{n \geqslant 0}$ la suite définie pour tout $n$ par

\begin{equation*}
s_{n}=u_{0}+u_{1}+\cdots+u_{n}
\end{equation*}
\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Mettre $\left(s_{n}\right)_{n}$ sous forme explicite (\ie exprimez $u_n$ en fonction de $n$, pour tout $n$).
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{sp.latex(s_n)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
Pour tout $n\geq 0$, $s_n = 6\left(1 - \frac{1}{2^{n+1}}\right)$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

\begin{equation}
\label{oijfoij}
s_n = 6\left(1 - \frac{1}{2^{n+1}}\right).
\end{equation}
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Déterminer la limite de $\left(s_{n}\right)_{n}$.
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","6"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$6$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
%Nous cherchons à déterminer la limite de $ (s_n)_{n} $ quand $ n $ tend vers l'infini. 

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
