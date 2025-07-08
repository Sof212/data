```latex
\begin{exercise}{
Title_exo: \fr{Calculs trigonométriques exacts}\en{Exact trigonometric calculations}
Modules: Trigonométrie 
Recommended_execution_time: 15
Ex_Level: Elementary
Chap: Fonctions trigonométriques
Involved_Concepts: Identités trigonométriques, Cercle unité
Original_source: 
Visibility: All
}
{
\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
cos_pi5 = (1 + sqrt(5))/4
sin_pi5 = sqrt(5 - sqrt(5))/(2*sqrt(2))

# === Propositions fausses calculées ===
fausse_sin1 = sqrt(5 + sqrt(5))/(2*sqrt(2))  # Erreur signe sous racine
fausse_sin2 = sqrt(5 - sqrt(5))/sqrt(8)      # Forme simplifiée incorrecte
fausse_sin3 = (sqrt(5) - 1)/4                # Confusion avec cos
\end{python}
\qcm{\fr{On donne $\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$. 

1. Quelle est la valeur exacte de $\sin\left(\frac{\pi}{5}\right)$ ?}\en{Given $\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$. 

1. What is the exact value of $\sin\left(\frac{\pi}{5}\right)$?}
}
{
\right{$\displaystyle \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle \frac{\sqrt{5 + \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle \frac{\sqrt{5 - \sqrt{5}}}{\sqrt{8}}$}
\wrong{$\displaystyle \frac{\sqrt{5} - 1}{4}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{On utilise l'identité trigonométrique fondamentale $\sin^2(x) + \cos^2(x) = 1$.
Pour $x = \frac{\pi}{5}$, on a :
$\sin^2\left(\frac{\pi}{5}\right) + \cos^2\left(\frac{\pi}{5}\right) = 1$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \cos^2\left(\frac{\pi}{5}\right)$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \left(\frac{1+\sqrt{5}}{4}\right)^2$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \frac{1 + 2\sqrt{5} + 5}{16}$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \frac{6 + 2\sqrt{5}}{16}$
$\sin^2\left(\frac{\pi}{5}\right) = \frac{16 - (6 + 2\sqrt{5})}{16}$
$\sin^2\left(\frac{\pi}{5}\right) = \frac{10 - 2\sqrt{5}}{16}$
Comme $\frac{\pi}{5}$ est dans le premier quadrant, $\sin\left(\frac{\pi}{5}\right) > 0$.
Donc, $\sin\left(\frac{\pi}{5}\right) = \sqrt{\frac{10 - 2\sqrt{5}}{16}} = \frac{\sqrt{10 - 2\sqrt{5}}}{4}$.
Pour obtenir la forme proposée, on peut multiplier le numérateur et le dénominateur par $\sqrt{2}$:
$\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{10 - 2\sqrt{5}} \times \sqrt{2}}{4 \times \sqrt{2}} = \frac{\sqrt{20 - 4\sqrt{5}}}{4\sqrt{2}}$.
Ceci n'est pas la forme attendue. Reprenons à partir de $\sin^2\left(\frac{\pi}{5}\right) = \frac{10 - 2\sqrt{5}}{16}$.
$\sin\left(\frac{\pi}{5}\right) = \sqrt{\frac{10 - 2\sqrt{5}}{16}} = \frac{\sqrt{10 - 2\sqrt{5}}}{4}$.
La bonne réponse est $\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$. Vérifions si $\frac{\sqrt{10 - 2\sqrt{5}}}{4} = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
Élevons au carré les deux expressions :
$\left(\frac{\sqrt{10 - 2\sqrt{5}}}{4}\right)^2 = \frac{10 - 2\sqrt{5}}{16}$
$\left(\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}\right)^2 = \frac{5 - \sqrt{5}}{4 \times 2} = \frac{5 - \sqrt{5}}{8}$.
Pour que les deux soient égales, il faut que $\frac{10 - 2\sqrt{5}}{16} = \frac{5 - \sqrt{5}}{8}$.
En multipliant le numérateur et le dénominateur de la deuxième fraction par 2, on obtient $\frac{2(5 - \sqrt{5})}{2 \times 8} = \frac{10 - 2\sqrt{5}}{16}$.
Les deux expressions sont bien égales.
Donc, $\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.}\en{We use the fundamental trigonometric identity $\sin^2(x) + \cos^2(x) = 1$.
For $x = \frac{\pi}{5}$, we have:
$\sin^2\left(\frac{\pi}{5}\right) + \cos^2\left(\frac{\pi}{5}\right) = 1$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \cos^2\left(\frac{\pi}{5}\right)$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \left(\frac{1+\sqrt{5}}{4}\right)^2$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \frac{1 + 2\sqrt{5} + 5}{16}$
$\sin^2\left(\frac{\pi}{5}\right) = 1 - \frac{6 + 2\sqrt{5}}{16}$
$\sin^2\left(\frac{\pi}{5}\right) = \frac{16 - (6 + 2\sqrt{5})}{16}$
$\sin^2\left(\frac{\pi}{5}\right) = \frac{10 - 2\sqrt{5}}{16}$
Since $\frac{\pi}{5}$ is in the first quadrant, $\sin\left(\frac{\pi}{5}\right) > 0$.
Therefore, $\sin\left(\frac{\pi}{5}\right) = \sqrt{\frac{10 - 2\sqrt{5}}{16}} = \frac{\sqrt{10 - 2\sqrt{5}}}{4}$.
To obtain the proposed form, we can multiply the numerator and denominator by $\sqrt{2}$:
$\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{10 - 2\sqrt{5}} \times \sqrt{2}}{4 \times \sqrt{2}} = \frac{\sqrt{20 - 4\sqrt{5}}}{4\sqrt{2}}$.
This is not the expected form. Let's restart from $\sin^2\left(\frac{\pi}{5}\right) = \frac{10 - 2\sqrt{5}}{16}$.
$\sin\left(\frac{\pi}{5}\right) = \sqrt{\frac{10 - 2\sqrt{5}}{16}} = \frac{\sqrt{10 - 2\sqrt{5}}}{4}$.
The correct answer is $\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$. Let's check if $\frac{\sqrt{10 - 2\sqrt{5}}}{4} = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
Square both expressions:
$\left(\frac{\sqrt{10 - 2\sqrt{5}}}{4}\right)^2 = \frac{10 - 2\sqrt{5}}{16}$
$\left(\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}\right)^2 = \frac{5 - \sqrt{5}}{4 \times 2} = \frac{5 - \sqrt{5}}{8}$.
For the two to be equal, we need $\frac{10 - 2\sqrt{5}}{16} = \frac{5 - \sqrt{5}}{8}$.
By multiplying the numerator and denominator of the second fraction by 2, we get $\frac{2(5 - \sqrt{5})}{2 \times 8} = \frac{10 - 2\sqrt{5}}{16}$.
The two expressions are indeed equal.
Therefore, $\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.}
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
sin_pi5 = sqrt(5 - sqrt(5))/(2*sqrt(2))
sin_4pi5 = sin_pi5

# === Propositions fausses calculées ===
fausse_sin4pi5_1 = -sin_pi5 # Erreur de signe
fausse_sin4pi5_2 = (1 + sqrt(5))/4 # Confusion avec cos
fausse_sin4pi5_3 = sqrt(5 + sqrt(5))/(2*sqrt(2)) # Erreur de signe sous racine
\end{python}
\qcm{\fr{2. En déduire la valeur exacte de $\sin\left(\frac{4\pi}{5}\right)$}\en{2. Deduce the exact value of $\sin\left(\frac{4\pi}{5}\right)$}
}
{
\right{$\displaystyle \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle \frac{1+\sqrt{5}}{4}$}
\wrong{$\displaystyle \frac{\sqrt{5 + \sqrt{5}}}{2\sqrt{2}}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{On remarque que $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$.
On utilise la propriété de symétrie du sinus : $\sin(\pi - x) = \sin(x)$.
Donc, $\sin\left(\frac{4\pi}{5}\right) = \sin\left(\pi - \frac{\pi}{5}\right) = \sin\left(\frac{\pi}{5}\right)$.
D'après la question précédente, $\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
Ainsi, $\sin\left(\frac{4\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.}\en{We notice that $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$.
We use the symmetry property of sine: $\sin(\pi - x) = \sin(x)$.
Therefore, $\sin\left(\frac{4\pi}{5}\right) = \sin\left(\pi - \frac{\pi}{5}\right) = \sin\left(\frac{\pi}{5}\right)$.
From the previous question, $\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
Thus, $\sin\left(\frac{4\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.}
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
cos_pi5 = (1 + sqrt(5))/4
cos_4pi5 = -cos_pi5

# === Propositions fausses calculées ===
fausse_cos4pi5_1 = cos_pi5 # Erreur de signe
fausse_cos4pi5_2 = sqrt(5 - sqrt(5))/(2*sqrt(2)) # Confusion avec sin
fausse_cos4pi5_3 = (1 - sqrt(5))/4 # Erreur de signe dans la formule
\end{python}
\qcm{\fr{3. Quelle est la valeur exacte de $\cos\left(\frac{4\pi}{5}\right)$ ?}\en{3. What is the exact value of $\cos\left(\frac{4\pi}{5}\right)$?}
}
{
\right{$\displaystyle -\frac{1+\sqrt{5}}{4}$}
\wrong{$\displaystyle \frac{1+\sqrt{5}}{4}$}
\wrong{$\displaystyle \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle \frac{1-\sqrt{5}}{4}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{On utilise la même remarque que précédemment : $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$.
On utilise la propriété de symétrie du cosinus : $\cos(\pi - x) = -\cos(x)$.
Donc, $\cos\left(\frac{4\pi}{5}\right) = \cos\left(\pi - \frac{\pi}{5}\right) = -\cos\left(\frac{\pi}{5}\right)$.
On nous donne $\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$.
Ainsi, $\cos\left(\frac{4\pi}{5}\right) = -\frac{1+\sqrt{5}}{4}$.}\en{We use the same observation as before: $\frac{4\pi}{5} = \pi - \frac{\pi}{5}$.
We use the symmetry property of cosine: $\cos(\pi - x) = -\cos(x)$.
Therefore, $\cos\left(\frac{4\pi}{5}\right) = \cos\left(\pi - \frac{\pi}{5}\right) = -\cos\left(\frac{\pi}{5}\right)$.
We are given $\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$.
Thus, $\cos\left(\frac{4\pi}{5}\right) = -\frac{1+\sqrt{5}}{4}$.}
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
sin_pi5 = sqrt(5 - sqrt(5))/(2*sqrt(2))
sin_9pi5 = -sin_pi5

# === Propositions fausses calculées ===
fausse_sin9pi5_1 = sin_pi5 # Erreur de signe
fausse_sin9pi5_2 = (1 + sqrt(5))/4 # Confusion avec cos
fausse_sin9pi5_3 = -(1 + sqrt(5))/4 # Confusion avec cos et erreur de signe
\end{python}
\qcm{\fr{4. Quelle est la valeur exacte de $\sin\left(\frac{9\pi}{5}\right)$ ?}\en{4. What is the exact value of $\sin\left(\frac{9\pi}{5}\right)$?}
}
{
\right{$\displaystyle -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle \frac{1+\sqrt{5}}{4}$}
\wrong{$\displaystyle -\frac{1+\sqrt{5}}{4}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{On remarque que $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$.
On utilise la propriété de périodicité et de symétrie du sinus : $\sin(2\pi - x) = -\sin(x)$.
Donc, $\sin\left(\frac{9\pi}{5}\right) = \sin\left(2\pi - \frac{\pi}{5}\right) = -\sin\left(\frac{\pi}{5}\right)$.
D'après la première question, $\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
Ainsi, $\sin\left(\frac{9\pi}{5}\right) = -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.}\en{We notice that $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$.
We use the periodicity and symmetry property of sine: $\sin(2\pi - x) = -\sin(x)$.
Therefore, $\sin\left(\frac{9\pi}{5}\right) = \sin\left(2\pi - \frac{\pi}{5}\right) = -\sin\left(\frac{\pi}{5}\right)$.
From the first question, $\sin\left(\frac{\pi}{5}\right) = \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.
Thus, $\sin\left(\frac{9\pi}{5}\right) = -\frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$.}
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
cos_pi5 = (1 + sqrt(5))/4
cos_9pi5 = cos_pi5

# === Propositions fausses calculées ===
fausse_cos9pi5_1 = -cos_pi5 # Erreur de signe
fausse_cos9pi5_2 = sqrt(5 - sqrt(5))/(2*sqrt(2)) # Confusion avec sin
fausse_cos9pi5_3 = sqrt(5 + sqrt(5))/4 # Erreur de signe sous racine et confusion
\end{python}
\qcm{\fr{5. Quelle est la valeur exacte de $\cos\left(\frac{9\pi}{5}\right)$ ?}\en{5. What is the exact value of $\cos\left(\frac{9\pi}{5}\right)$?}
}
{
\right{$\displaystyle \frac{1+\sqrt{5}}{4}$}
\wrong{$\displaystyle -\frac{1+\sqrt{5}}{4}$}
\wrong{$\displaystyle \frac{\sqrt{5 - \sqrt{5}}}{2\sqrt{2}}$}
\wrong{$\displaystyle \frac{\sqrt{5 + \sqrt{5}}}{4}$}
}
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{On remarque que $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$.
On utilise la propriété de périodicité et de symétrie du cosinus : $\cos(2\pi - x) = \cos(x)$.
Donc, $\cos\left(\frac{9\pi}{5}\right) = \cos\left(2\pi - \frac{\pi}{5}\right) = \cos\left(\frac{\pi}{5}\right)$.
On nous donne $\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$.
Ainsi, $\cos\left(\frac{9\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$.}\en{We notice that $\frac{9\pi}{5} = 2\pi - \frac{\pi}{5}$.
We use the periodicity and symmetry property of cosine: $\cos(2\pi - x) = \cos(x)$.
Therefore, $\cos\left(\frac{9\pi}{5}\right) = \cos\left(2\pi - \frac{\pi}{5}\right) = \cos\left(\frac{\pi}{5}\right)$.
We are given $\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$.
Thus, $\cos\left(\frac{9\pi}{5}\right) = \frac{1+\sqrt{5}}{4}$.}
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