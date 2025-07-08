```latex
\begin{exercise}{
Title_exo: \fr{Identification de fonctions de récurrence}\en{Identification of recurrence functions}
Modules: Suites récurrentes % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Suites_numériques % NameID des chapitres
Involved_Concepts: Relation_de_récurrence, Fonction_associée % ID ou NameID des notions
Original_source:  % Source de l'exercice
Visibility: Teacher % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
% Variations: % Liste des variations de l'exercice (optionnel) : ["variation1", "variation2"]
Comment: % Comment: % Commentaire de l'exercice (optionnel)
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = "f(x) = 2x - 3"
# === Propositions fausses calculées ===
fausse_1 = "f(x) = 2x + 3"  # Erreur de signe
fausse_2 = "f(x) = -2x - 3"  # Erreur de signe
fausse_3 = "f(x) = 3x - 2"  # Erreur de coefficients
fausse_4 = "f(x) = \\frac{x - 3}{2}" # Erreur de transformation
\end{python}
\qcm{ \fr{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par :
$
\begin{cases}
u_0 = 4 \\
u_{n+1} = 2 u_n - 3
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}\en{
Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
u_0 = 4 \\
u_{n+1} = 2 u_n - 3
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$?
}
}
{
\right{$\displaystyle \mathbf{f(x) = 2x - 3}$}
\wrong{$\displaystyle \mathbf{f(x) = 2x + 3}$}
\wrong{$\displaystyle \mathbf{f(x) = -2x - 3}$}
\wrong{$\displaystyle \mathbf{f(x) = 3x - 2}$}
\wrong{$\displaystyle \mathbf{f(x) = \frac{x - 3}{2}}$}
}
{
\fr{Indice: Identifiez l'opération appliquée à $u_n$ pour obtenir $u_{n+1}$}\en{Hint: Identify the operation applied to $u_n$ to obtain $u_{n+1}$}
}
{
\fr{Solution: La relation $u_{n+1} = 2 u_n - 3$ montre que $f$ est la fonction affine $x \mapsto 2x - 3$.}\en{Solution: The relation $u_{n+1} = 2 u_n - 3$ shows that $f$ is the affine function $x \mapsto 2x - 3$.}
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = "f(x) = \\sqrt{1 + x^2}"
# === Propositions fausses calculées ===
fausse_1 = "f(x) = \\sqrt{x^2 - 1}"  # Erreur de signe
fausse_2 = "f(x) = 1 + x^2"  # Oubli de la racine
fausse_3 = "f(x) = (1 + x)^2"  # Erreur de parenthèses
fausse_4 = "f(x) = \\sqrt{x} + 1" # Erreur de variable
\end{python}
\qcm{ \fr{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par :
$
\begin{cases}
u_0 = 0 \\
u_{n+1} = \sqrt{1 + u_n^2}
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}\en{
Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
u_0 = 0 \\
u_{n+1} = \sqrt{1 + u_n^2}
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$?
}
}
{
\right{$\displaystyle \mathbf{f(x) = \sqrt{1 + x^2}}$}
\wrong{$\displaystyle \mathbf{f(x) = \sqrt{x^2 - 1}}$}
\wrong{$\displaystyle \mathbf{f(x) = 1 + x^2}$}
\wrong{$\displaystyle \mathbf{f(x) = (1 + x)^2}$}
\wrong{$\displaystyle \mathbf{f(x) = \sqrt{x} + 1}$}
}
{
\fr{Indice: Observez l'expression sous la racine carrée}\en{Hint: Observe the expression under the square root}
}
{
\fr{Solution: La relation montre que $f$ applique la racine carrée de (1 + le carré du terme précédent), donc $f(x) = \sqrt{1 + x^2}$.}\en{Solution: The relation shows that $f$ applies the square root of (1 + the square of the previous term), so $f(x) = \sqrt{1 + x^2}$.}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = "f(x) = \\sin(x)"
# === Propositions fausses calculées ===
fausse_1 = "f(x) = \\cos(x)"  # Erreur de fonction trigonométrique
fausse_2 = "f(x) = \\sin(x^2)"  # Erreur de variable
fausse_3 = "f(x) = \\sin(1 + x)"  # Erreur de constante
fausse_4 = "f(x) = \\arcsin(x)" # Erreur de fonction inverse
\end{python}
\qcm{ \fr{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par :
$
\begin{cases}
u_0 = 2 \\
u_{n+1} = \sin(u_n)
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}\en{
Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
u_0 = 2 \\
u_{n+1} = \sin(u_n)
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$?
}
}
{
\right{$\displaystyle \mathbf{f(x) = \sin(x)}$}
\wrong{$\displaystyle \mathbf{f(x) = \cos(x)}$}
\wrong{$\displaystyle \mathbf{f(x) = \sin(x^2)}$}
\wrong{$\displaystyle \mathbf{f(x) = \sin(1 + x)}$}
\wrong{$\displaystyle \mathbf{f(x) = \arcsin(x)}$}
}
{
\fr{Indice: Identifiez la fonction trigonométrique appliquée}\en{Hint: Identify the trigonometric function applied}
}
{
\fr{Solution: La relation montre directement que $f$ est la fonction sinus : $f(x) = \sin(x)$.}\en{Solution: The relation directly shows that $f$ is the sine function: $f(x) = \sin(x)$.}
}
{
logic: 30
abstraction: 20
reasoning: 30
calculation: 20
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = "f(x) = \\frac{x - 1}{x + 1}"
# === Propositions fausses calculées ===
fausse_1 = "f(x) = \\frac{x + 1}{x - 1}"  # Inversion numérateur/dénominateur
fausse_2 = "f(x) = \\frac{1 - x}{1 + x}"  # Erreur de signe
fausse_3 = "f(x) = \\frac{1}{x + 1} - 1"  # Erreur de transformation
fausse_4 = "f(x) = \\frac{2x}{x + 1}" # Erreur de coefficients
\end{python}
\qcm{ \fr{
Soit la suite ${(u_n)}_{n\in\fN}$ définie par :
$
\begin{cases}
u_0 = 4 \\
u_{n+1} = \frac{u_n - 1}{u_n + 1}
\end{cases}
$
Quelle est la fonction $f$ telle que $u_{n+1} = f(u_n)$ ?
}\en{
Let the sequence ${(u_n)}_{n\in\fN}$ be defined by:
$
\begin{cases}
u_0 = 4 \\
u_{n+1} = \frac{u_n - 1}{u_n + 1}
\end{cases}
$
What is the function $f$ such that $u_{n+1} = f(u_n)$?
}
}
{
\right{$\displaystyle \mathbf{f(x) = \frac{x - 1}{x + 1}}$}
\wrong{$\displaystyle \mathbf{f(x) = \frac{x + 1}{x - 1}}$}
\wrong{$\displaystyle \mathbf{f(x) = \frac{1 - x}{1 + x}}$}
\wrong{$\displaystyle \mathbf{f(x) = \frac{1}{x + 1} - 1}$}
\wrong{$\displaystyle \mathbf{f(x) = \frac{2x}{x + 1}}$}
}
{
\fr{Indice: Observez la structure fractionnaire de la relation}\en{Hint: Observe the fractional structure of the relation}
}
{
\fr{Solution: La relation montre que $f$ est la fonction homographique $x \mapsto \frac{x - 1}{x + 1}$.}\en{Solution: The relation shows that $f$ is the homographic function $x \mapsto \frac{x - 1}{x + 1}$.}
}
{
logic: 25
abstraction: 25
reasoning: 25
calculation: 25
}
}
\end{exercise}
```