```latex
\begin{exercise}{
Title_exo: \fr{Résolution d'équation quadratique}\en{Solving Quadratic Equation}
Modules: Algebra
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Equations
Involved_Concepts: Quadratic_equations, Discriminant, Roots_of_polynomials
Original_source:
Visibility: All
}
{ % Contenu de l'exercice

\begin{python}
from sympy import *

# Coefficients de l'équation quadratique ax^2 + bx + c = 0
a_val = 1
b_val = -2
c_val = -15

# Calcul du discriminant
delta_val = b_val**2 - 4*a_val*c_val

# Calcul des solutions
bonne_valeur_s1 = Rational(-b_val - sqrt(delta_val), 2*a_val)
bonne_valeur_s2 = Rational(-b_val + sqrt(delta_val), 2*a_val)

# Génération de propositions fausses intelligentes

# Erreur 1: Inversion des signes des solutions
fausse_s1_inverse = -bonne_valeur_s1
fausse_s2_inverse = -bonne_valeur_s2

# Erreur 2: Erreur de signe sur -b dans la formule quadratique
fausse_s1_err_signe_b = Rational(b_val - sqrt(delta_val), 2*a_val)
fausse_s2_err_signe_b = Rational(b_val + sqrt(delta_val), 2*a_val)

# Erreur 3: Erreur de calcul du dénominateur (oubli du 2)
fausse_s1_err_denom = Rational(-b_val - sqrt(delta_val), a_val)
fausse_s2_err_denom = Rational(-b_val + sqrt(delta_val), a_val)

# Erreur 4: Une solution correcte, l'autre avec une petite erreur (ex: +2)
fausse_s1_mix = bonne_valeur_s1
fausse_s2_mix = bonne_valeur_s2 + 2 # Ex: -3 et 7

# Formatage LaTeX des paires de solutions
correct_pair = f"${latex(bonne_valeur_s1)}$ et ${latex(bonne_valeur_s2)}$"
wrong_pair_1 = f"${latex(fausse_s1_inverse)}$ et ${latex(fausse_s2_inverse)}$"
wrong_pair_2 = f"${latex(fausse_s1_err_signe_b)}$ et ${latex(fausse_s2_err_signe_b)}$"
wrong_pair_3 = f"${latex(fausse_s1_err_denom)}$ et ${latex(fausse_s2_err_denom)}$"
wrong_pair_4 = f"${latex(fausse_s1_mix)}$ et ${latex(fausse_s2_mix)}$"
\end{python}
\qcm{
\fr{Quelles sont les solutions de l'équation $X^{2}-2 X-15=0$ ?}
\en{What are the solutions to the equation $X^{2}-2 X-15=0$?}
}
{
\right{\py{correct_pair}}
\wrong{\py{wrong_pair_1}}
\wrong{\py{wrong_pair_2}}
\wrong{\py{wrong_pair_3}}
\wrong{\py{wrong_pair_4}}
\wronger
}
{ % Indice
\fr{Pensez à utiliser la formule du discriminant $\Delta = b^2 - 4ac$ pour une équation de la forme $aX^2 + bX + c = 0$.}
\en{Consider using the discriminant formula $\Delta = b^2 - 4ac$ for an equation of the form $aX^2 + bX + c = 0$.}
}
{ % Solution détaillée
\fr{Commençons par calculer le discriminant, noté $\Delta$, de l'équation $X^{2}-2 X-15=0$. Les coefficients sont $a=1$, $b=-2$, $c=-15$.
On a :
\begin{equation*}
\Delta 
=
(-2)^{2}-4 \cdot (1) \cdot (-15)
=
4+60
=
64
=
8^2.
\end{equation*}
Puisque $\Delta > 0$, l'équation admet deux solutions réelles distinctes, notées $s_1$ et $s_2$. On a:
\begin{equation*}
\begin{align*}
&s_1 
=
 \frac{-(-2)-8}{2\cdot 1}
=
 \frac{2-8}{2}
=
 \frac{-6}{2}
=-3&
&\text{et}&
&s_2 
=
 \frac{-(-2)+8}{2\cdot 1}
=
 \frac{2+8}{2}
=
 \frac{10}{2}
=5&
\end{align*}
\end{equation*}
Ainsi, les solutions de l'équation sont : $-3$ et $5$.}
\en{Let's start by calculating the discriminant, denoted $\Delta$, of the equation $X^{2}-2 X-15=0$. The coefficients are $a=1$, $b=-2$, $c=-15$.
We have:
\begin{equation*}
\Delta 
=
(-2)^{2}-4 \cdot (1) \cdot (-15)
=
4+60
=
64
=
8^2.
\end{equation*}
Since $\Delta > 0$, the equation has two distinct real solutions, denoted $s_1$ and $s_2$. We have:
\begin{equation*}
\begin{align*}
&s_1 
=
 \frac{-(-2)-8}{2\cdot 1}
=
 \frac{2-8}{2}
=
 \frac{-6}{2}
=-3&
&\text{and}&
&s_2 
=
 \frac{-(-2)+8}{2\cdot 1}
=
 \frac{2+8}{2}
=
 \frac{10}{2}
=5&
\end{align*}
\end{equation*}
Thus, the solutions to the equation are: $-3$ and $5$.}
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

}
\end{exercise}
```