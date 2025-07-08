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


\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
from sympy import *
a_1=Matrix([[5,-3]])
a_2=Matrix([[-3,5]])
a_1_latex=latex(a_1, mat_delim='', mat_str='pmatrix')
a_2_latex=latex(a_2, mat_delim='', mat_str='pmatrix')



\end{python}


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
Résoudre l'équation suivante :
\begin{equation}
\label{eq}
x^{2}-2 x-15 
=
 0.
\end{equation}
Si les solutions de [](#eq) sont $s_1$ et $s_2$, on donnera les solutions sous
 la forme suivante: $(s_1, s_2)$. (vecteur ligne)

}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","\py{a_1_latex}","\py{a_2_latex}"],["0","0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
 Utilisez le discriminant pour résoudre l'équation quadratique.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$(5, -3)$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Commençons par calculer le discriminant, noté $\Delta$, de l'équation [](#eq). On a :
\begin{equation*}
\Delta 
=
(-2)^{2}-4 \cdot (-15)
=
4+60
=
64
=
8^2.

:
\begin{equation*}
\begin{align*}
&s_1 
=
 \frac{-(-2)-8}{2\cdot 1}
=
 \frac{-6}{2}
=-3&
&\&&
&s_2 
=
 \frac{-(-2)+8}{2\cdot 1}
=
 \frac{10}{2}
=5&
\end{align*}
\end{equation*}
Ainsi, les solutions de l'équation  [](#eq) sont :  $\boxed{5 \quad \text{et} \quad -3}.
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

