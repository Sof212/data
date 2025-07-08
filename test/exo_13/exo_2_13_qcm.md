```latex
\begin{exercise}{
Title_exo: \fr{Décomposition en éléments simples et primitives}\en{Partial fraction decomposition and antiderivatives}
Modules: Calcul Intégral
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Intégration, Fractions rationnelles
Involved_Concepts: Primitives, Décomposition en éléments simples
Original_source: 
Visibility: All
}
{
\begin{python}
from sympy import *

# Question 1: Décomposition en éléments simples
# Bonne réponse
a_correct = 1
b_correct = 2
c_correct = -1

# Fausses propositions
# Erreur de signe sur b
a_false1 = 1
b_false1 = -2
c_false1 = 1

# Erreur de coefficient sur a
a_false2 = 2
b_false2 = 1
c_false2 = -1

# Tous les coefficients à 1
a_false3 = 1
b_false3 = 1
c_false3 = 1

# Oubli de a et c
a_false4 = 0
b_false4 = 2
c_false4 = 0
\end{python}
\qcm{\fr{On considère la fonction $f$ définie sur $\mathbf{R}^{*}_{+}$ par :
$$f(x) = \frac{x^{2}+2x+2}{x^{2}+x}$$

Quelle est la décomposition correcte de $f(x)$ sous la forme $a + \frac{b}{x} + \frac{c}{x+1}$ ?}\en{Consider the function $f$ defined on $\mathbf{R}^{*}_{+}$ by:
$$f(x) = \frac{x^{2}+2x+2}{x^{2}+x}$$

What is the correct partial fraction decomposition of $f(x)$ in the form $a + \frac{b}{x} + \frac{c}{x+1}$?
}}
{
\right{\fr{$a=\sympy{a_correct}$, $b=\sympy{b_correct}$, $c=\sympy{c_correct}$}\en{$a=\sympy{a_correct}$, $b=\sympy{b_correct}$, $c=\sympy{c_correct}$}}
\wrong{\fr{$a=\sympy{a_false1}$, $b=\sympy{b_false1}$, $c=\sympy{c_false1}$}\en{$a=\sympy{a_false1}$, $b=\sympy{b_false1}$, $c=\sympy{c_false1}$}}
\wrong{\fr{$a=\sympy{a_false2}$, $b=\sympy{b_false2}$, $c=\sympy{c_false2}$}\en{$a=\sympy{a_false2}$, $b=\sympy{b_false2}$, $c=\sympy{c_false2}$}}
\wrong{\fr{$a=\sympy{a_false3}$, $b=\sympy{b_false3}$, $c=\sympy{c_false3}$}\en{$a=\sympy{a_false3}$, $b=\sympy{b_false3}$, $c=\sympy{c_false3}$}}
\wrong{\fr{$a=\sympy{a_false4}$, $b=\sympy{b_false4}$, $c=\sympy{c_false4}$}\en{$a=\sympy{a_false4}$, $b=\sympy{b_false4}$, $c=\sympy{c_false4}$}}
}
{
\fr{Indication : Effectuer la division polynomiale puis la décomposition en éléments simples.}\en{Hint: Perform polynomial division then partial fraction decomposition.}
}
{
\fr{Solution détaillée :

Nous procédons par identification :
\begin{align*}
\frac{x^{2}+2x+2}{x^{2}+x} &= a + \frac{b}{x} + \frac{c}{x+1} \\
&= \frac{ax(x+1) + b(x+1) + cx}{x(x+1)}
\end{align*}

En identifiant les numérateurs :
\begin{align*}
x^2 + 2x + 2 &= ax^2 + (a+b+c)x + b
\end{align*}

Ce qui donne le système :
\begin{equation*}
\begin{cases}
1 = a \\
2 = a + b + c \\
2 = b
\end{cases}
\end{equation*}

La solution est $(a,b,c) = (\sympy{a_correct},\sympy{b_correct},\sympy{c_correct})$.}\en{Detailed solution:

We proceed by identification:
\begin{align*}
\frac{x^{2}+2x+2}{x^{2}+x} &= a + \frac{b}{x} + \frac{c}{x+1} \\
&= \frac{ax(x+1) + b(x+1) + cx}{x(x+1)}
\end{align*}

By identifying the numerators:
\begin{align*}
x^2 + 2x + 2 &= ax^2 + (a+b+c)x + b
\end{align*}

Which gives the system:
\begin{equation*}
\begin{cases}
1 = a \\
2 = a + b + c \\
2 = b
\end{cases}
\end{equation*}

The solution is $(a,b,c) = (\sympy{a_correct},\sympy{b_correct},\sympy{c_correct})$.}
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\begin{python}
from sympy import *

# Question 2: Primitive
# Bonne réponse
primitive_correct_latex = r"x + 2\ln|x| - \ln|x+1| + C"

# Fausses propositions
# Erreur de signe sur le dernier terme
primitive_false1_latex = r"x + \ln|x| + \ln|x+1| + C"

# Erreur de coefficient sur le premier terme
primitive_false2_latex = r"2x + \ln|x| - \ln|x+1| + C"

# Erreur de signe sur le deuxième terme
primitive_false3_latex = r"x + 2\ln|x| + \ln|x+1| + C"

# Erreur de puissance sur le premier terme
primitive_false4_latex = r"x^2 + 2\ln|x| - \ln|x+1| + C"
\end{python}
\qcm{\fr{En utilisant la décomposition précédente, quelle est une primitive de $f$ ?}\en{Using the previous decomposition, what is an antiderivative of $f$?}
}
{
\right{$\displaystyle \mathbf{\sympy{primitive_correct_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{primitive_false1_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{primitive_false2_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{primitive_false3_latex}}$}
\wrong{$\displaystyle \mathbf{\sympy{primitive_false4_latex}}$}
}
{
\fr{Indication : Intégrer terme à terme la décomposition obtenue.}\en{Hint: Integrate term by term the obtained decomposition.}
}
{
\fr{Solution détaillée :

Avec $f(x) = 1 + \frac{2}{x} - \frac{1}{x+1}$, on intègre :
\begin{align*}
\int f(x)dx &= \int 1 dx + 2\int \frac{1}{x}dx - \int \frac{1}{x+1}dx \\
&= x + 2\ln|x| - \ln|x+1| + C
\end{align*}
}\en{Detailed solution:

With $f(x) = 1 + \frac{2}{x} - \frac{1}{x+1}$, we integrate:
\begin{align*}
\int f(x)dx &= \int 1 dx + 2\int \frac{1}{x}dx - \int \frac{1}{x+1}dx \\
&= x + 2\ln|x| - \ln|x+1| + C
\end{align*}
}
}
{
logic: 20
abstraction: 20
reasoning: 20
calculation: 40
}
\end{exercise}
```