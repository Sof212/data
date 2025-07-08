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
On donne $\cos \left(\frac{\pi}{5}\right)=\frac{1+\sqrt{5}}{4}$.

\qcm{%Enoncé de la question: Calculer la valeur exacte de $\sin \left(\frac{\pi}{5}\right)$.
La valeur exacte de $\sin \left(\frac{\pi}{5}\right)$ est:

}
{
\right{$\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\frac{1 + \sqrt{5}}{2\sqrt{2}}$}
\wrong{$\frac{\sqrt{5 + \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\frac{5}{8}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez l'identité trigonométrique $\sin^2\left(\theta\right) + \cos^2\left(\theta\right) = 1$ pour calculer $\sin\left(\frac{\pi}{5}\right)$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

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

\qcm{%Enoncé de la question: En déduire les valeurs exactes du sinus et du cosinus de $\frac{4 \pi}{5}$.
Du résultat obtenu à la question précédente, on peut déduire les valeurs
sinus et du cosinus de $\frac{4 \pi}{5}$. On a:
%En déduire les valeurs exactes du sinus et du cosinus de $\frac{4 \pi}{5}$

}
{
\right{$\cos\left(\frac{4\pi}{5}\right) = -\frac{1 + \sqrt{5}}{4}$ et $\sin\left(\frac{4\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\cos\left(\frac{4\pi}{5}\right) = \frac{1 + \sqrt{5}}{4}$ et $\sin\left(\frac{4\pi}{5}\right) = -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\cos\left(\frac{4\pi}{5}\right) = -\frac{\sqrt{5 + 1}}{4}$ et $\sin\left(\frac{4\pi}{5}\right) = \frac{\sqrt{5 + \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\cos\left(\frac{4\pi}{5}\right) = \frac{1}{2}$ et $\sin\left(\frac{4\pi}{5}\right) = \frac{\sqrt{3}}{2}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez les relations trigonométriques pour un angle dans le deuxième quadrant : $\cos\left(\pi - \theta\right) = -\cos(\theta)$ et $\sin\left(\pi - \theta\right) = \sin(\theta)$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

Puisque $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, et que $\sin(\pi - x) = \sin x$, pour tout réel $x$, on a:
\begin{equation*}
\begin{align*}
\sin\left(\frac{4\pi}{5}\right) 
=
 \sin\left(\pi - \frac{\pi}{5}\right) 
=
 \sin\left(\frac{\pi}{5}\right) 
=
 \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}} 
\end{align*}
\end{equation*}
D'autre part, puisque $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$, et que $\cos(\pi - x) = -\cos x$, pour tout réel $x$, on a:
\begin{equation*}
\begin{align*}
\cos\left(\frac{4\pi}{5}\right) 
=
 \cos\left(\pi - \frac{\pi}{5}\right) 
=
 -\cos\left(\frac{\pi}{5}\right) 
=
- \frac{1+\sqrt{5}}{4}. &
\end{align*}
\end{equation*}

On en déduit donc que:


\begin{equation*}
\begin{align*}
&\fbox{$\sin\left(\frac{4\pi}{5}\right)  =  \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}} $}&
&\&&
&\fbox{$\cos\left(\frac{4\pi}{5}\right)  = - \frac{1+\sqrt{5}}{4}$}.&
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

\qcm{%Enoncé de la question: En déduire les valeurs exactes du sinus et du cosinus de $\frac{9 \pi}{5}$.
On peut en déduire les valeurs exactes du sinus et du cosinus de  $\frac{9 \pi}{5}$. On a :

}
{
\right{$\cos\left(\frac{9\pi}{5}\right) = \frac{1 + \sqrt{5}}{4}$ et $\sin\left(\frac{9\pi}{5}\right) = -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\cos\left(\frac{9\pi}{5}\right) = -\frac{1 + \sqrt{5}}{4}$ et $\sin\left(\frac{9\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\cos\left(\frac{9\pi}{5}\right) = \frac{5}{4}$ et $\sin\left(\frac{9\pi}{5}\right) = -\frac{3}{2}$}
\wrong{$\cos\left(\frac{9\pi}{5}\right) = \frac{\sqrt{5 + 1}}{4}$ et $\sin\left(\frac{9\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2}$}
}
{%Indice: Vous pouvez écrire une indication ci-dessous.
Utilisez les relations trigonométriques pour un angle dans le quatrième quadrant : $\cos\left(2\pi - \theta\right) = \cos(\theta)$ et $\sin\left(2\pi - \theta\right) = -\sin(\theta)$.
}
{%Solution détaillée: Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.

Puisque $\frac{9\pi}{5} = \frac{4\pi}{5} + \pi$ et que l'on sait que  
\begin{equation*}
\begin{align*}
&\sin(\pi + x) = -\sin x, \  \text{pour tout réel $x$} &\\
&\&&\\
&\sin(\pi - x) = \sin x, \  \text{pour tout réel $x$, } &
\end{align*}
\end{equation*}



on a:

\begin{equation*}
\begin{align*}
\sin\left(\frac{9\pi}{5}\right) 
&=
 \sin\left(\pi + \frac{4\pi}{5}\right) 
=
 -\sin\left(\frac{4\pi}{5}\right) 
=
 -\sin\left(\pi-\frac{\pi}{5}\right) 
=
-\sin\left(\frac{\pi}{5}\right)\\
&=
-\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}.
\end{align*}
\end{equation*}


D'autre part, puisque $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$, et que $\cos(2\pi - x) = \cos (-x) = \cos x$, pour tout réel $x$, on a:
\begin{equation*}
\begin{align*}
\cos\left(\frac{9\pi}{5}\right) 
&=
\cos\left(2\pi - \frac{\pi}{5}\right) 
=
\cos\left(-\frac{\pi}{5}\right) 
=
 \cos\frac{\pi}{5}
=
\frac{1+\sqrt{5}}{4}. &
\end{align*}
\end{equation*}




On en déduit donc que:


\begin{equation*}
\begin{align*}
&\fbox{$\sin\left(\frac{9\pi}{5}\right)  =  \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}} $}&
&\&&
&\fbox{$\cos\left(\frac{9\pi}{5}\right)  =  \frac{1+\sqrt{5}}{4}$}.&
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

}
\end{exercise}
