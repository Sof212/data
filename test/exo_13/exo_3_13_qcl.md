```latex
\begin{exercise}{
Id: 0a1b2c3d-4e5f-6789-abcd-ef0123456789
Title_exo: Déterminer les primitives d'une fonction rationnelle
Modules: Analyse
Recommended_execution_time: 10
Ex_Level: Elementary
Chap: Intégration
Involved_Concepts: Décomposition en éléments simples, Primitives
Original_source: null
Visibility: All
}
{
% Contenu de l'exercice
Le but de l'exercice est de trouver les primitives de la fonction $f$ définie
sur ${\bfR}^{*}_{+}$ par
\begin{equation*}
f(x)
=
\frac{x^{2}+2 x+2}{x^{2}+x}.
\end{equation*}

\begin{python}
from sympy import *
# Définition des symboles
x, a, b, c = symbols('x a b c')

# Expression de f(x)
f_x = (x**2 + 2*x + 2) / (x**2 + x)

# Expression de la décomposition en éléments simples
# f_decomp = a + b/x + c/(x+1) # Non utilisé directement pour le calcul des coefficients

# Mettre au même dénominateur pour l'identification des coefficients
# On sait que f(x) = a + b/x + c/(x+1) = (a*x*(x+1) + b*(x+1) + c*x) / (x*(x+1))
# Donc, x^2 + 2x + 2 = a*x*(x+1) + b*(x+1) + c*x
# x^2 + 2x + 2 = ax^2 + ax + bx + b + cx
# x^2 + 2x + 2 = ax^2 + (a+b+c)x + b

# Coefficients du numérateur de f(x)
coeff_x2_f_x_num = 1
coeff_x_f_x_num = 2
coeff_const_f_x_num = 2

# Coefficients du numérateur de la forme décomposée
# ax^2 + (a+b+c)x + b
coeff_x2_decomp_num = a
coeff_x_decomp_num = a + b + c
coeff_const_decomp_num = b

# Résolution du système d'équations
# Equation 1: coeff_x2_f_x_num = coeff_x2_decomp_num  => 1 = a
# Equation 2: coeff_x_f_x_num = coeff_x_decomp_num    => 2 = a + b + c
# Equation 3: coeff_const_f_x_num = coeff_const_decomp_num => 2 = b

solutions = solve([Eq(coeff_x2_f_x_num, coeff_x2_decomp_num),
                    Eq(coeff_x_f_x_num, coeff_x_decomp_num),
                    Eq(coeff_const_f_x_num, coeff_const_decomp_num)], (a, b, c))

a_val = solutions[a]
b_val = solutions[b]
c_val = solutions[c]

# Pour la question sur la primitive
# Primitive de a
primitive_a = a_val * x
# Primitive de b/x (pour x > 0, abs(x) = x)
primitive_b_x = b_val * log(x)
# Primitive de c/(x+1) (pour x > 0, abs(x+1) = x+1)
primitive_c_x_plus_1 = c_val * log(x+1)

# La primitive F(x)
F_x = primitive_a + primitive_b_x + primitive_c_x_plus_1
F_x_latex = latex(F_x)

# Vérification des valeurs pour s'assurer qu'elles sont numériques
a_val_num = float(a_val)
b_val_num = float(b_val)
c_val_num = float(c_val)

\end{python}

\qcl{%Enoncé de la question:
Calculer la valeur du réel $a$ tel que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
}
{ % Solution PyxiScience:
[["CL","\py{a_val_num}"],["0"]]
}
{ % Indice:
Commencez par mettre l'expression $a+\frac{b}{x}+\frac{c}{x+1}$ au même dénominateur.
}
{ % Solution brève fournie à l'utilisateur:
La valeur de $a$ est $\py{a_val_num}$.
}
{ % Solution détaillée:
Nous pouvons procéder par équivalences et écrire, pour tout réel strictement positif $x$,
\begin{equation*}
\begin{align*}
f(x) = a + \frac{b}{x} + \frac{c}{x+1}
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
a + \frac{b}{x} + \frac{c}{x+1}\\
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
 \frac{a x(x+1)}{x(x+1)} + \frac{b(x+1)}{x(x+1)} + \frac{cx}{x(x+1)}\\
&\Longleftrightarrow
\frac{x^{2}+2 x+2}{x^{2}+x}
=
 \frac{a x(x+1) + b(x+1) + cx}{x(x+1)}\\
&\Longleftrightarrow
x^{2}+2 x+2
=
a x(x+1) + b(x+1) + cx\\
&\Longleftrightarrow
x^{2}+2 x+2
=
ax^2 + ax + bx + b + cx\\
&\Longleftrightarrow
x^{2}+2 x+2
=
ax^2 + (a+b+c)x + b.
\end{align*}
\end{equation*}
En identifiant les coefficients des polynômes des deux côtés de l'égalité, nous obtenons le système d'équations suivant :
\begin{align*}
\text{Coefficient de } x^2: & \quad 1 = a \\
\text{Coefficient de } x:  & \quad 2 = a+b+c \\
\text{Terme constant: }   & \quad 2 = b
\end{align*}
De la première équation, nous obtenons directement $a = \py{a_val_num}$.
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Calculer la valeur du réel $b$ tel que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
}
{ % Solution PyxiScience:
[["CL","\py{b_val_num}"],["0"]]
}
{ % Indice:
Utilisez l'identification des coefficients après avoir mis au même dénominateur.
}
{ % Solution brève fournie à l'utilisateur:
La valeur de $b$ est $\py{b_val_num}$.
}
{ % Solution détaillée:
Nous avons établi l'égalité des polynômes :
$x^{2}+2 x+2 = ax^2 + (a+b+c)x + b$.
En identifiant les coefficients des termes constants, nous obtenons :
$2 = b$.
Donc, $b = \py{b_val_num}$.
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Calculer la valeur du réel $c$ tel que $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$.
}
{ % Solution PyxiScience:
[["CL","\py{c_val_num}"],["0"]]
}
{ % Indice:
Une fois $a$ et $b$ trouvés, utilisez la relation entre les coefficients de $x$.
}
{ % Solution brève fournie à l'utilisateur:
La valeur de $c$ est $\py{c_val_num}$.
}
{ % Solution détaillée:
Nous avons établi l'égalité des polynômes :
$x^{2}+2 x+2 = ax^2 + (a+b+c)x + b$.
En identifiant les coefficients de $x$, nous obtenons :
$2 = a+b+c$.
Nous avons déjà trouvé $a=\py{a_val_num}$ et $b=\py{b_val_num}$. En substituant ces valeurs dans l'équation :
$2 = \py{a_val_num}+\py{b_val_num}+c$
$2 = \py{a_val_num+b_val_num}+c$
$c = 2-\py{a_val_num+b_val_num}$
$c = \py{c_val_num}$.
}
{ % Répartition des poids (Total = 100)
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\qcl{%Enoncé de la question:
Donner une primitive $F(x)$ de la fonction $f(x) = \frac{x^{2}+2 x+2}{x^{2}+x}$ sur ${\bfR}^{*}_{+}$ sous la forme $F(x) = ax + b\ln|x| + c\ln|x+1|$.
}
{ % Solution PyxiScience:
[["CL","\py{F_x_latex}"],["0"]]
}
{ % Indice:
Utilisez la décomposition en éléments simples $f(x)=a+\frac{b}{x}+\frac{c}{x+1}$ et intégrez chaque terme. N'oubliez pas que $x > 0$.
}
{ % Solution brève fournie à l'utilisateur:
Une primitive est $F(x) = \py{F_x_latex}$.
}
{ % Solution détaillée:
Nous avons trouvé la décomposition en éléments simples de $f(x)$ :
$f(x) = \py{a_val_num} + \frac{\py{b_val_num}}{x} + \frac{\py{c_val_num}}{x+1}$.
Pour trouver une primitive $F(x)$, nous intégrons chaque terme :
$\int \py{a_val_num} \, dx = \py{a_val_num}x$
$\int \frac{\py{b_val_num}}{x} \, dx = \py{b_val_num} \int \frac{1}{x} \, dx = \py{b_val_num} \ln|x|$
$\int \frac{\py{c_val_num}}{x+1} \, dx = \py{c_val_num} \int \frac{1}{x+1} \, dx = \py{c_val_num} \ln|x+1|$
Puisque la fonction est définie sur ${\bfR}^{*}_{+}$, $x > 0$, donc $|x| = x$ et $|x+1| = x+1$.
Ainsi, une primitive $F(x)$ est :
$F(x) = \py{a_val_num}x + \py{b_val_num}\ln(x) + \py{c_val_num}\ln(x+1)$.
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