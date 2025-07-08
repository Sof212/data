\begin{exercise}{
Title_exo: Sinus et cosinus exacts % Nom de l'exercice
Modules: Trigonométrie % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Trigonométrie % NameID des chapitres
Involved_Concepts: Identités_trigonométriques % ID ou NameID des notions
Original_source: % Source de l'exercice
}
{
% Contenu de l'exercice

(ques1)=
\qcl{%Enoncé de la première question: 
En utilisant l'égalité
$\cos \left(\frac{\pi}{5}\right)=\frac{1+\sqrt{5}}{4}$, donner la valeur exacte de $\sin \left(\frac{\pi}{5}\right)$.
\
On a $\sin \left(\frac{\pi}{5}\right) = $

}
{%Solution PyxiScience: pour PyxiScience uniquement
[["CL","$\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$"],["0"]]
}
{%Indice: 
Utilisez l'identité trigonométrique $\sin^2\left(\theta\right) + \cos^2\left(\theta\right) = 1$ pour calculer $\sin\left(\frac{\pi}{5}\right)$.
}
{%Solution brève fournie à l'utilisateur: 
On a $\sin \left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
}
{%Solution détaillée: 

Nous savons que, pour n'importe quel angle réel $\theta$, nous avons:  
\begin{equation}
\label{eq1}
\sin^2(\theta) + \cos^2(\theta) = 1.
\end{equation}
Dans notre cas, nous avons $\theta = \frac{\pi}{5}$. 
De l'égalité [](#eq1), avec $\theta = \frac{\pi}{5}$, nous déduisons que:
\begin{equation*}
\begin{align*}
%\label{eq2}
\sin^2\left(\frac{\pi}{5}\right) = 1 - \cos^2\left(\frac{\pi}{5}\right)
\end{align*}
\end{equation*}
et donc:
\begin{equation}
\label{Eq2}
\begin{align*}
\left|\sin\left(\frac{\pi}{5}\right)\right| = \sqrt{1 - \cos^2\left(\frac{\pi}{5}\right)}.
\end{align*}
\end{equation}
Comme par ailleurs le réel $\frac{\pi}{5}$ appartient à l'intervalle $[-\pi/2,\pi/2]$, on sait que 
$\sin\left(\frac{\pi}{5}\right) > 0$ et donc que $\sin\left(\frac{\pi}{5}\right) = \sin\left(\frac{\pi}{5}\right)$. On peut donc simplifier [](#Eq2) en écrivant:
\begin{equation}
\label{Eq3}
\begin{align*}
\sin\left(\frac{\pi}{5}\right)
= 
\sqrt{1 - \cos^2\left(\frac{\pi}{5}\right)}.
\end{align*}
\end{equation}

Calculons à présent $\cos^2\left(\frac{\pi}{5}\right)$. D'après l'égalité donnée en début 
d'exercice, on a:

\begin{equation}
\label{Eq4}
\begin{align*}
\cos^2\left(\frac{\pi}{5}\right) 
&=
 \left(\frac{1 + \sqrt{5}}{4}\right)^2 
=
 \frac{(1 + \sqrt{5})^2}{16} 
=
 \frac{1 + 2\sqrt{5} + 5}{16} 
=
 \frac{6 + 2\sqrt{5}}{16} \\
&=
 \frac{3 + \sqrt{5}}{8}.
\end{align*}
\end{equation}


En remplaçant $\cos^2\left(\frac{\pi}{5}\right) $ dans [](#Eq3), 
par la quantité obtenue en [](#Eq4), nous obtenons:
\begin{equation*}
\begin{align*}
\sin\left(\frac{\pi}{5}\right)
&= 
\sqrt{1 - \cos^2\left(\frac{\pi}{5}\right)}\\
&=\sqrt{1- \frac{3 + \sqrt{5}}{8}}
= \sqrt{ \frac{8-3 - \sqrt{5}}{8}} =  \sqrt{ \frac{5- \sqrt{5}}{8}}\\
&= \frac{ \sqrt{5- \sqrt{5}} }{2\sqrt{2}}.
\end{align*}
\end{equation*}

}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


% Deuxième question
(ques2)=
\qcl{%Enoncé de la première question: 
En utilisant la réponse donnée à la question précédente, on déduit 
la valeur exacte du cosinus de $\frac{4 \pi}{5}$. On a 
\
$\cos\left(\frac{4 \pi}{5}\right) = $
}
{%Solution PyxiScience: pour PyxiScience uniquement

[["CL","$-\frac{1 + \sqrt{5}}{4}$"],["0"]]
}
{%Indice: 
Utilisez la relation trigonométrique pour un angle dans le deuxième quadrant : $\cos\left(\pi - \theta\right) = -\cos(\theta)$.
}
{%Solution brève fournie à l'utilisateur: 
$\cos\left(\frac{4\pi}{5}\right) = -\frac{1 + \sqrt{5}}{4}$.
}
{%Solution détaillée: 

\begin{equation*}
\begin{align*}
&\fbox{$\cos\left(\frac{4\pi}{5}\right)  = - \frac{1-\sqrt{5}}{4}$}.&
\end{align*}
\end{equation*}

}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la deuxième question: 
En utilisant la réponse donnée à la  [question $1$](#ques1), on déduit  la valeur exacte 
du sinus de $\frac{4 \pi}{5}$. On a 
\
$\sin(\frac{4 \pi}{5}) = $
}
{%Solution PyxiScience: pour PyxiScience uniquement


[["CL","$\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$"],["0"]]
}
{%Indice: 
Utilisez la relation trigonométrique pour un angle dans le deuxième quadrant : $\sin\left(\pi - \theta\right) = \sin(\theta)$.
}
{%Solution brève fournie à l'utilisateur: 
$\sin\left(\frac{4\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
}
{%Solution détaillée: 




\begin{equation*}
\begin{align*}
&\fbox{$\sin\left(\frac{4\pi}{5}\right)  =  \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}} $}.&
\end{align*}
\end{equation*}

}
{
% Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}


\qcl{%Enoncé de la deuxième question:
On peut aussi calculer la valeur exacte du sinus de $\frac{9 \pi}{5}$. On a 
\
$\sin\left(\frac{9 \pi}{5}\right) = $
}
{%Solution PyxiScience: pour PyxiScience uniquement
[["CL","$-\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$"],["0"]]
}
{%Indice: 
Utilisez la relation trigonométrique pour un angle dans le quatrième quadrant : $\sin\left(2\pi - \theta\right) = -\sin(\theta)$.
}
{%Solution brève fournie à l'utilisateur: 
$\sin\left(\frac{9\pi}{5}\right) = -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
}
{%Solution détaillée: 


\begin{equation*}
\begin{align*}
&\fbox{$\sin\left(\frac{9\pi}{5}\right)  =  +\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}. $}.&
\end{align*}
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
On peut aussi calculer la valeur exacte du cosinus de $\frac{9 \pi}{5}$. On a 
\
$\cos\left(\frac{9 \pi}{5}\right) = $
}
{%Solution PyxiScience: pour PyxiScience uniquement
[["CL","$\frac{1+\sqrt{5}}{4}$"],["0"]]
}
{%Indice: 
Utilisez la relation trigonométrique pour un angle dans le quatrième quadrant : $\cos\left(2\pi - \theta\right) = \cos(\theta)$.
}
{%Solution brève fournie à l'utilisateur: Ecrivez ci-dessous une solution brève qui sera affichée à l'utilisateur. Idéalement "On a chp libre = ...".  
$\frac{1+\sqrt{5}}{4}$
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.



\begin{equation*}
\begin{align*}
&\fbox{$\cos\left(\frac{9\pi}{5}\right)  =  \frac{1+\sqrt{5}}{4}$}.&

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
