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


\begin{python}
# Code Python : Ecrivez ci-dessous votre code Python
import sympy as sp
x = sp.Symbol('x')
F = (x - 1) / (x + 1)
F2 = sp.sqrt(1 + x**2)
F3=sp.sin(x)
\end{python}

Les suites suivantes sont définies par des relations de récurrence 
$u_{n+1}=f\left(u_{n}\right)$. 
Donner la fonction $f$ correspondante dans chacun des cas.


\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
u_0 &= 4 \\
u_{n+1} &= 2u_n - 3
\end{cases}
$

  On a $f(x)=
$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{sp.latex(F)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{sp.latex(F)}$
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

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
   { u _ { 0 } = 0 } \\
   { u _ { n + 1 } = \sqrt { 1 + u _ { n } ^ { 2 } } }
\end{cases}
$

  On a $f(x)=$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement

 [["CL","$\py{sp.latex(F2)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{sp.latex(F2)}$
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

\qcl{%Enoncé de la question: écrivez ci-dessous l'énoncé de la question
$
\begin{cases}
   { u _ { 0 } = 2 } \\
   { u _ { n + 1 } = \operatorname { s i n } ( u _ { n } ) }
\end{cases}
$

  On a $f(x)=$
}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{sp.latex(F3)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{sp.latex(F3)}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

   $
      f(x) = \sin(x) 
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
$
\begin{cases}
   u_{0}=4 \\
   u_{n+1}=\frac{u_{n}-1}{u_{n}+1}
\end{cases}
$.

  On a $f(x)=$

}
{%Solution PyxiScience: cette solution est pour PyxiScience uniquement
[["CL","$\py{sp.latex(F)}$"],["0"]]
}
{%Indice: Vous pouvez écrire une indication ci-dessous.

}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\py{sp.latex(F)}$
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
