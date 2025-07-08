\begin{exercise}{
Title_exo: Résolution d'équations exponentielles et logarithmiques % Nom de l'exercice
Modules: Logarithmes_et_exponentielles % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Logarithmes_et_exponentielles % NameID des chapitres
Involved_Concepts: Équations_exponentielles_et_logarithmiques % ID ou NameID des notions
Original_source: % Source de l'exercice
}
{
% Contenu de l'exercice

\qcl{%Enoncé de la première question: 
Résoudre l'équation suivante :
\begin{equation}
\label{Eq1}
\mathrm{e}^{x} = 2
\end{equation}


}
{%Solution PyxiScience: pour PyxiScience uniquement
[["CL","\ln{2}"],["0"]]
}
{%Indice: 
Utilisez les propriétés des logarithmes et des exponentielles pour résoudre chaque équation.
}
{%Solution brève fournie à l'utilisateur: 
$x = \ln 2$.
}
{%Solution détaillée: 
Pour résoudre [](#Eq1), et puisqu'on peut prendre le logarithme de $2$, il suffit de prendre 
le logarithme népérien de chaque côté de  [](#Eq1). On a donc: 
\begin{equation*}
\label{Eq1}
\mathrm{e}^{x} = 2
\Longleftrightarrow
x = \ln 2.
\end{equation*}
On a donc montré que l'unique solution de l'équation [](#Eq1) est $x = \ln 2$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}





\qcl{%Enoncé de la deuxième question: 
Résoudre l'équation suivante :
\begin{equation}
\label{Eq2}
\mathrm{e}^{x} = \frac{1}{4}
\end{equation}


}
{%Solution PyxiScience: pour PyxiScience uniquement
[["CL","\ln{-4}"],["0"]]
}
{%Indice:
 Utilisez les propriétés des logarithmes et des exponentielles pour résoudre chaque équation.
}
{%Solution brève fournie à l'utilisateur: 
$x = - \ln 4$.
}
{%Solution détaillée: 
Pour résoudre [](#Eq2), et puisqu'on peut prendre le logarithme de $\frac{1}{4}$, il suffit de prendre 
le logarithme népérien de chaque côté de  [](#Eq2). On a donc: 
\begin{equation*}
\label{Eq1}
\mathrm{e}^{x} = \frac{1}{4}
\Longleftrightarrow
x = \ln\left(\frac{1}{4}\right)
\Longleftrightarrow
x = \ln 1 -  \ln4
\Longleftrightarrow
x = -  \ln4.
\end{equation*}
On a donc montré que l'unique solution de l'équation [](#Eq2) est $x = -  \ln4$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}





\qcl{%Enoncé de la troisième question: 
Résoudre l'équation suivante :
\begin{equation}
\label{Eq3}
\ln(x) = \frac{\ln(5)}{2}
\end{equation}


}
{%Solution PyxiScience: pour PyxiScience uniquement
[["CL","\sqrt{5}"],["0"]]
}
{%Indice: 
Utilisez les propriétés des logarithmes et des exponentielles pour résoudre chaque équation.
}
{%Solution brève fournie à l'utilisateur: 
$x =  \sqrt{5}$.
}
{%Solution détaillée: 
Pour résoudre [](#Eq3), il suffit de prendre l'exponentielle de chaque côté de  [](#Eq3).
On a donc: 
\begin{equation*}
\ln(x) = \frac{\ln(5)}{2}
&\Longleftrightarrow
x = e^{\large\frac{\ln(5)}{2}}
\Longleftrightarrow
x = {\left(e^{\ln 5}\right)}^{\frac{1}{2}}
\Longleftrightarrow
x = {5}^{\frac{1}{2}}\\
&\Longleftrightarrow
x = \sqrt{5}.
\end{equation*}
On a donc montré que l'unique solution de l'équation [](#Eq3) est $x =  \sqrt{5}$.
}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}




\qcl{%Enoncé de la quatrième question: 
Résoudre l'équation suivante :
\begin{equation}
\label{Eq4}
\ln(x) = -\ln(9).
\end{equation}


}
{%Solution PyxiScience: pour PyxiScience uniquement
[["CL","\frac{1}{9}"],["0"]]
}
{%Indice: Utilisez les propriétés des logarithmes et des exponentielles pour résoudre chaque équation.
}
{%Solution brève fournie à l'utilisateur: 
$x =  \frac{1}{9}$.
}
{%Solution détaillée: 
Pour résoudre [](#Eq4), il suffit, là encore, de prendre l'exponentielle de chaque côté de
  [](#Eq4). On a donc: 
\begin{equation*}
\ln(x) = -\ln9
&\Longleftrightarrow
x = e^{-\ln9}
\Longleftrightarrow
x = e^{\ln(9^{-1})}
\Longleftrightarrow
x =9^{-1}\\
&\Longleftrightarrow
x = \frac{1}{9}.
\end{equation*}
On a donc montré que l'unique solution de l'équation   [](#Eq4) est $x = \frac{1}{9}.$
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
