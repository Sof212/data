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
Le but de l'exercice est de trouver les primitives de la fonction $f$, définie sur $\mathbb{R}_{*}^{+}$,
 par:
\begin{equation}
\label{dizduhzeiduheziduzehi}
f(x)=\frac{x^{2}+2 x+2}{x^{2}+x}.
\end{equation}

\qcm{%Enoncé de la question: 
Déterminer les réels $a$, $b$ et $c$ tels que 
\begin{equation}
\label{dizduhzeiduheziduzehiUYGUYGUYG}
f(x)=a+\frac{b}{x}+\frac{c}{x+1}.
\end{equation}

}
{
\right{$a = 1, \ b = 2, \ c = 1$}
\wrong{$a = 2, \ b = 1, \ c = -1$}
\wrong{$a = 1, \ b = -2, \ c = 1$}
\wrong{$a = 0, \ b = 2, \ c = 1$}

% Ajoutez autant de réponses que nécessaire

}
{%Indice:
 Effectuez une division polynomiale entre le numérateur et le dénominateur de $f(x)$, puis décomposez le résultat en fractions simples.
}
{%Solution détaillée:Ecrivez ci-dessous la solution détaillée qui sera affichée à l'utilisateur.
Pour exprimer la fonction $f$ en termes des réels $a$, $b$, et $c$, nous allons identifier ces coefficients
en comparant les deux expressions connues de $f$ qui sont [](#dizduhzeiduheziduzehi) 
et [](#dizduhzeiduheziduzehiUYGUYGUYG)
Nous avons, pour tout réel $x$ différent de $0$ et $1$,
\begin{equation*}
\begin{align*}
&\frac{x^{2}+2 x+2}{x^{2}+x}
=
a+\frac{b}{x}+\frac{c}{x+1}&\\
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
\frac{ax(x+1)}{x(x+1)}+\frac{b(x+1)}{x(x+1)}+\frac{cx}{x(x+1)}\\
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
\frac{ax^2 + ax + bx +b + cx}{x(x+1)}\\
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
\frac{ax^2 + (a + b+c)x +b }{x^2 + x}\\
&\Longleftrightarrow
x^{2}+2 x+2
=
ax^2 + (a + b+c)x +b \\
&\Longleftrightarrow
(a-1)x^{2}+(2-(a+b+c)) x+2-b
=
0
\end{align*} 
\end{equation*} 
Ceci ne laisse d'autre possibilités que:
\begin{equation*} 
(\cS): \ \begin{cases}
			a-1 = 0 \\
            2-(a+b+c) = 0 \\
            2-b = 0 
		 \end{cases}
\end{equation*} 
Ce système a unique solution qui est $a = 1$, $b =2$ et $c =-1$. On a donc
\begin{equation*} 
\begin{align*} 
\text{Pour tout $x$ de $\bfR\backslash\{0,1\}$},  \hspace{2ex}
f(x) = 1+\frac{2}{x}+\frac{-1}{x+1}.
\end{align*} 
\end{equation*} 




Ainsi, les valeurs de $a$, $b$, et $c$ que nous avons déterminées sont :  
$
\boxed{(1, 2, -1)}. 
$

Nous pouvons vérifier que ces valeurs satisfont l'équation initiale de $f$, c'est-à-dire 
 [](#dizduhzeiduheziduzehi).
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
