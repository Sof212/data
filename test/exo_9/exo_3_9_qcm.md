```latex
\begin{exercise}{
Title_exo: \fr{Expressions logarithmiques}\en{Logarithmic expressions}
Modules: % NameID des modules
Recommended_execution_time: 10 % Temps conseillé pour l'exercice (en minutes)
Ex_Level: Elementary % Niveau de difficulté de l'exercice (Elementary, Intermediary, Advanced)
Chap: Logarithms % NameID des chapitres
Involved_Concepts: Logarithm_properties % ID ou NameID des notions
Original_source: % Source de l'exercice
Visibility: All % Visibilité de l'exercice : Teacher, Lecture, All (Teacher/Enseignant, Lecture/Cours, All/Tous)
Comment: Conversion d'un exercice QST en QCM, décliné en plusieurs questions.
}
{ % Contenu de l'exercice

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = 7 * 8
# === Propositions fausses calculées ===
fausse_1 = 7 + 8  # Erreur méthodologique typique
fausse_2 = abs(7 - 8)  # Variante calcul incorrecte  
fausse_3 = 7 * 8 + 3 # Approximation erronée (valeur aléatoire ajoutée)
\end{python}
\qcm{ %% [Énoncé original intégralement conservé]
\fr{Exprimer l'expression $A:= \ln (7)+\ln (8)$ sous la forme $\ln (a)$, où $a>0$.}
\en{Express the expression $A:= \ln (7)+\ln (8)$ in the form $\ln (a)$, where $a>0$.}
}
\right{$\ln (56)$}
\wrong{$\ln (15)$}
\wrong{$\ln (1)$}
\wrong{$\ln (59)$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement positifs.
\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
\end{equation}
Pour l'expression $A:= \ln (7)+\ln (8)$:
\begin{equation*}
\begin{align*}
\ln (7)+\ln (8) = \ln(7 \cdot 8) = \ln(56).
\end{align*}
\end{equation*}
Ainsi, nous avons $A = \ln(56)$.}
\en{We will use the following properties of logarithms, valid for all strictly positive $a,b$.
\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
\end{equation}
For the expression $A:= \ln (7)+\ln (8)$:
\begin{equation*}
\begin{align*}
\ln (7)+\ln (8) = \ln(7 \cdot 8) = \ln(56).
\end{align*}
\end{equation*}
Thus, we have $A = \ln(56)$.}
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Rational(20, 4)
# === Propositions fausses calculées ===
fausse_1 = 20 - 4  # Erreur méthodologique typique
fausse_2 = 20 * 4  # Variante calcul incorrecte  
fausse_3 = Rational(20, 4) + 2 # Approximation erronée (valeur aléatoire ajoutée)
\end{python}
\qcm{ %% [Énoncé original intégralement conservé]
\fr{Exprimer l'expression $A:= \ln (20) - \ln (4)$ sous la forme $\ln (a)$, où $a>0$.}
\en{Express the expression $A:= \ln (20) - \ln (4)$ in the form $\ln (a)$, where $a>0$.}
}
\right{$\ln (5)$}
\wrong{$\ln (16)$}
\wrong{$\ln (80)$}
\wrong{$\ln (7)$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement positifs.
\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
\end{equation}
Pour l'expression $A:= \ln (20) - \ln (4)$:
\begin{equation*}
\begin{align*}
\ln (20) - \ln (4) = \ln\left(\frac{20}{4}\right) = \ln(5).
\end{align*}
\end{equation*}
Ainsi, nous avons $A = \ln(5)$.}
\en{We will use the following properties of logarithms, valid for all strictly positive $a,b$.
\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
\end{equation}
For the expression $A:= \ln (20) - \ln (4)$:
\begin{equation*}
\begin{align*}
\ln (20) - \ln (4) = \ln\left(\frac{20}{4}\right) = \ln(5).
\end{align*}
\end{equation*}
Thus, we have $A = \ln(5)$.}
}

\begin{python}
from sympy import *
# === Calcul bonne réponse (extraite corrigé original) ===
bonne_valeur = Rational(28, 4)
# === Propositions fausses calculées ===
fausse_1 = 28 - 4  # Erreur méthodologique typique
fausse_2 = Rational(4, 28)  # Variante calcul incorrecte (division inversée)
fausse_3 = Rational(28, 4) + 1 # Approximation erronée (valeur aléatoire ajoutée)
\end{python}
\qcm{ %% [Énoncé original intégralement conservé]
\fr{Exprimer l'expression $A:= -\ln (4)+\ln (28)$ sous la forme $\ln (a)$, où $a>0$.}
\en{Express the expression $A:= -\ln (4)+\ln (28)$ in the form $\ln (a)$, where $a>0$.}
}
\right{$\ln (7)$}
\wrong{$\ln (24)$}
\wrong{$\ln (\frac{1}{7})$}
\wrong{$\ln (8)$}
\wronger  % (aucune proposition correcte)
\righter  % (toutes propositions correctes)
{%% Solution détaillée : [Corrigé \qst original préservé intégralement mettre les expression marhémathique entre $...$ et les phrases entre $\text{...}$]
\fr{Nous allons utiliser les propriétés suivantes des logarithmes, valables pour tous $a,b$ strictement positifs.
\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
\end{equation}
Pour l'expression $A:= -\ln (4)+\ln (28)$:
\begin{equation*}
\begin{align*}
-\ln (4)+\ln (28) = \ln(28) - \ln(4) = \ln\left(\frac{28}{4}\right) = \ln(7).
\end{align*}
\end{equation*}
Ainsi, nous avons $A = \ln(7)$.}
\en{We will use the following properties of logarithms, valid for all strictly positive $a,b$.
\begin{equation}
\begin{align}
\label{fer1}
&\ln(a) + \ln(b) = \ln(ab)&
\end{align}
\end{equation}
\begin{equation}
\begin{align}
\label{fer2}
&\ln(a) - \ln(b) = \ln\left(\frac{a}{b}\right)&
\end{align}
\end{equation}
For the expression $A:= -\ln (4)+\ln (28)$:
\begin{equation*}
\begin{align*}
-\ln (4)+\ln (28) = \ln(28) - \ln(4) = \ln\left(\frac{28}{4}\right) = \ln(7).
\end{align*}
\end{equation*}
Thus, we have $A = \ln(7)$.}
}

}
\end{exercise}
```