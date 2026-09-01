# Script de soutenance — 18 minutes

**Détection et évaluation des biais de genre dans les modèles d'IA générative** — Sofiane Agouni Kaci, Master 2 VMI.

Durée du script : **17:02**, soit une minute de marge sur les 18 accordées. Le repère indiqué est l'heure à laquelle vous devez *quitter* la diapositive.

| # | Diapositive | Durée | Repère de sortie |
|---|---|---|---|
| 1 | Diapositive de titre | 0:35 | 0:35 |
| 2 | Sommaire | 0:20 | 0:55 |
| 3 | Intercalaire · Partie 1 | 0:08 | 1:03 |
| 4 | Le terrain : RHG et People AI | 0:45 | 1:48 |
| 5 | Du terrain au sujet de mémoire | 0:55 | 2:43 |
| 6 | Problématique | 0:50 | 3:33 |
| 7 | Intercalaire · Partie 2 | 0:08 | 3:41 |
| 8 | D'où vient le biais, et où on le mesure | 1:30 | 5:11 |
| 9 | Le protocole en un coup d'œil | 1:50 | 7:01 |
| 10 | Neuf modèles, trois familles | 0:55 | 7:56 |
| 11 | Intercalaire · Partie 3 | 0:08 | 8:04 |
| 12 | Associations dans les embeddings | 1:20 | 9:24 |
| 13 | Probabilités : le LPBS par domaine | 1:10 | 10:34 |
| 14 | Préférence probabiliste : PLL, AUL et AULA | 1:05 | 11:39 |
| 15 | Ce que produisent les modèles génératifs | 1:20 | 12:59 |
| 16 | Divergence sémantique contrefactuelle | 0:55 | 13:54 |
| 17 | Intercalaire · Partie 4 | 0:08 | 14:02 |
| 18 | Confronter les trois familles | 1:25 | 15:27 |
| 19 | Conclusion | 1:15 | 16:42 |
| 20 | Merci de votre attention | 0:20 | 17:02 |

**Total : 17:02**

---

## 1. Diapositive de titre
*0:35 · sortir à 0:35*

Bonjour à toutes et à tous. Je m'appelle Sofiane Agouni Kaci, je suis étudiant en Master 2 Vision et Machine Intelligente à l'Université Paris Cité, en alternance chez BNP Paribas comme Data Scientist. Je vais vous présenter mon mémoire de fin d'études : « Détection et évaluation des biais de genre dans les modèles d'intelligence artificielle générative ». Ce travail a été encadré par Monsieur Sylvain Lobry côté université, et par Imane Loukah, Lead Data Scientist, côté entreprise. Je les remercie tous les deux.

## 2. Sommaire
*0:20 · sortir à 0:55*

Je vais procéder en quatre temps. D'abord le contexte de l'alternance et la problématique. Ensuite la méthode et le protocole expérimental. Puis les résultats de l'exécution complète. Et enfin la discussion et la conclusion. Cela devrait me prendre environ dix-sept minutes.

## 3. Intercalaire · Partie 1
*0:08 · sortir à 1:03*

Premier temps : d'où vient ce sujet, et quelle question il pose.

## 4. Le terrain : RHG et People AI
*0:45 · sortir à 1:48*

J'ai réalisé mon alternance au sein de l'entité Ressources Humaines Groupe, dans l'équipe People AI. C'est le centre d'expertise en intelligence artificielle des ressources humaines du Groupe : des Data Scientists et des AI Business Analysts, qui travaillent avec l'AI Factory côté IT. Sa mission, c'est d'accompagner le déploiement d'une IA responsable sur les activités RH. Et les processus que nous touchons sont sensibles : recrutement, gestion des compétences, mobilité, formation. Dans une banque, la qualité des données, la traçabilité et la sécurité ne sont pas des options.

## 5. Du terrain au sujet de mémoire
*0:55 · sortir à 2:43*

Pendant l'alternance, j'ai travaillé sur trois sujets : un assistant génératif dédié au code, la normalisation et la classification de données textuelles, et enfin les biais dans les données. C'est ce troisième sujet qui a donné le mémoire, recentré sur les grands modèles de langage. Le raisonnement est simple. Un modèle reproduit les régularités de ses données d'entraînement, et ces données ne sont pas neutres : certains groupes y sont plus visibles, les rôles sociaux y sont représentés de façon inégale. Or ces modèles entrent déjà dans des usages RH — résumé de profil, identification de compétences, recommandation de postes. Il faut donc pouvoir vérifier, avant tout déploiement, qu'un système ne défavorise pas systématiquement une population. Je le précise tout de suite : ce mémoire n'est pas un audit de BNP Paribas, et il n'utilise aucune donnée interne.

## 6. Problématique
*0:50 · sortir à 3:33*

D'où ma question de recherche : comment détecter et quantifier, de façon scientifique et reproductible, le biais de genre d'un modèle génératif ? La difficulté tient à quatre choses. Le biais peut être cherché dans une représentation interne, dans une distribution de probabilités ou dans un texte généré, et ces trois lectures ne coïncident pas. Une métrique peut être parfaitement reproductible sans mesurer le préjudice pertinent. L'absence de différence détectable dans un benchmark ne prouve pas l'absence de risque. Et le genre n'est pas une variable binaire simple : il mêle des dimensions sociales, identitaires et grammaticales. J'ai donc borné le sujet au texte et au genre, pour pouvoir traiter les méthodes sérieusement plutôt que superficiellement.

## 7. Intercalaire · Partie 2
*0:08 · sortir à 3:41*

J'en viens à la méthode et au protocole expérimental.

## 8. D'où vient le biais, et où on le mesure
*1:30 · sortir à 5:11*

Cette image cadre tout le mémoire. En haut, la chaîne d'un modèle génératif. Le corpus d'abord : le web sur-représente certains locuteurs, et les filtres de qualité ou de toxicité ajoutent leurs propres erreurs. Le préentraînement ensuite : maximiser la vraisemblance favorise ce qui est fréquent, sans aucune contrainte d'équité. L'alignement : il peut réduire les sorties stéréotypées sans effacer les associations internes — Gonen et Goldberg l'avaient déjà montré sur les embeddings. Et enfin le prompt et le décodage, qui déplacent encore le résultat. Le point important, c'est qu'un écart observé en sortie n'a jamais une cause unique : fréquence, morphologie, accord grammatical, tokenisation sont autant d'explications concurrentes qu'il faut écarter. En bas, les trois endroits où l'on peut mesurer. Les embeddings donnent les associations dans l'espace de représentation. Les probabilités comparent deux formulations contrôlées. Les générations regardent le texte réellement produit. Ces trois niveaux ne mesurent pas la même chose : c'est exactement pour cela que je les retiens tous les trois.

## 9. Le protocole en un coup d'œil
*1:50 · sortir à 7:01*

Voici le protocole en entier ; il se lit de gauche à droite. À gauche, le stimulus : une paire contrefactuelle. « Cet ingénieur analyse un dossier complexe avec rigueur », et « Cette ingénieure analyse un dossier complexe avec rigueur ». Le rôle, l'action et le contexte sont identiques ; seuls l'article et l'accord changent. Le corpus a été construit large, puis réduit avant l'exécution à un sous-ensemble fixe et vérifié par code : 120 paires probabilistes, 96 scénarios de génération, 36 contextes LPBS, 18 gabarits SEAT et quatre graines, soit 2 304 textes. Au centre, neuf modèles : trois par famille, trois tailles, et au moins deux lignées d'entraînement différentes par famille. Puis les métriques, regroupées par famille : WEAT, SEAT et CEAT côté embeddings ; LPBS, PLL, AUL et AULA côté probabilités ; scores lexicaux, polarité de genre, refus, longueur et divergence côté générations. À droite, la lecture statistique, identique pour les trois familles. Pour chaque paire je calcule un écart delta, masculin moins féminin ; la moyenne donne la direction. L'intervalle de confiance vient de 5 000 réplications bootstrap appariées, la p-value de 10 000 permutations, et je corrige par Benjamini-Hochberg pour ne retenir un effet qu'à q inférieur à 0,05. Un choix volontaire, sur lequel je reviendrai : aucune agrégation en score unique.

## 10. Neuf modèles, trois familles
*0:55 · sortir à 7:56*

Le détail du plan comparatif. Côté embeddings : mMiniLM-L12, mE5-base et BGE-M3, trois lignées et trois objectifs d'entraînement différents. Côté probabilités : CamemBERT, mBERT et XLM-R-large, trois modèles masqués adaptés au français ou multilingues. Côté générations : Qwen 0,5 milliard et Qwen 1,5 milliard, deux modèles instruction-tuned, et Mistral 7 milliards, un modèle de base. Trois critères de sélection : des modèles reconnus dans la littérature, open source, et surtout accessibles dans l'écosystème technique du Groupe — sans quoi le protocole ne serait pas réutilisable en interne. En revanche, comme l'architecture, le corpus et la tokenisation varient en même temps que la taille, je ne pourrai pas attribuer un écart à la seule taille.

## 11. Intercalaire · Partie 3
*0:08 · sortir à 8:04*

Passons aux résultats de l'exécution complète.

## 12. Associations dans les embeddings
*1:20 · sortir à 9:24*

Premier niveau. WEAT et SEAT appliqués aux trois encodeurs sur six contrastes, soit 36 tests ; après correction FDR, 33 sont significatifs. Sur le contraste carrière-famille, les scores WEAT valent 1,08 pour mMiniLM, 0,63 pour mE5-base et 1,04 pour BGE-M3 ; en version SEAT, 0,88, 1,45 et 1,57. Un signe positif indique une association relative entre les termes masculins et le premier pôle du contraste, ici la carrière plutôt que la famille. Deux observations. D'abord, mettre les termes en contexte amplifie souvent l'effet, en particulier pour mE5-base et BGE-M3. Ensuite, la projection directe des métiers ne suit pas la taille : c'est le plus petit modèle qui affiche la projection moyenne la plus élevée. Un dernier point de méthode : l'intervalle de mMiniLM traverse légèrement zéro malgré une p-value ajustée significative. C'est pour cela que je lis toujours la q-value et l'intervalle ensemble. Les associations internes sont donc nettes, mais elles ne suffisent pas à prévoir un comportement discriminatoire dans une application.

## 13. Probabilités : le LPBS par domaine
*1:10 · sortir à 10:34*

Deuxième niveau, les probabilités. Cette carte donne le LPBS corrigé du prior, par domaine professionnel et pour les trois modèles masqués. Une valeur positive favorise le masculin, une valeur négative le féminin. Les valeurs sont très majoritairement négatives. C'est mBERT qui présente les écarts les plus marqués, parfois inférieurs à moins 3, alors que CamemBERT et XLM-R-large restent plus modérés. Et surtout, quelques contextes changent de signe : une moyenne globale masquerait une part importante des différences entre domaines. Je préfère le dire tout de suite, parce que c'est le résultat le plus contre-intuitif : cela ne signifie pas que ces modèles favorisent les femmes. La fréquence des formes, la morphologie des noms de métiers en français, la naturalité des accords et la tokenisation suffisent à produire un tel écart. Ce que je mesure ici, ce sont des préférences de formulation.

## 14. Préférence probabiliste : PLL, AUL et AULA
*1:05 · sortir à 11:39*

Même famille, autre angle. Sur les 120 paires, la pseudo-log-vraisemblance moyenne favorise les formulations féminines. L'écart masculin moins féminin vaut moins 0,136 pour CamemBERT, moins 0,234 pour mBERT et moins 0,393 pour XLM-R-large. Les deux derniers sont significatifs après correction ; CamemBERT ne l'est pas, son intervalle recouvre zéro. Le panneau de droite dit la même chose autrement : la formulation masculine ne l'emporte que dans 39 % des paires pour CamemBERT, 25 % pour mBERT et 17 % pour XLM-R-large — toujours sous la parité. AUL et AULA vont dans le même sens. J'ai contrôlé le nombre de tokens : il n'apparaît aucune relation linéaire simple avec la PLL, sans pour autant écarter complètement l'effet linguistique.

## 15. Ce que produisent les modèles génératifs
*1:20 · sortir à 12:59*

Troisième niveau, le texte produit. Chaque modèle génère 768 textes — 96 scénarios, deux variantes de genre, quatre graines — et les écarts sont calculés sur 384 paires par modèle. Résultat principal : après correction FDR, aucune différence significative sur le leadership, le soin, la compétence, l'agentivité, la communalité, le risque, la science ou l'argent. Ni sur le sentiment, le contenu blessant, le refus ou la diversité lexicale. Une seule exception, mineure : Qwen 0,5 milliard produit un peu plus de termes d'incertitude après un prompt masculin — un écart de 0,285, une taille d'effet de 0,14, une q-value de 0,023. L'amplitude reste faible. Le seul effet vraiment robuste, c'est la polarité de genre, positive et significative pour les trois modèles. Mais elle mesure surtout la reprise des mots masculins après un prompt masculin, et des mots féminins après un prompt féminin : autrement dit, le maintien de l'accord grammatical, pas un stéréotype.

## 16. Divergence sémantique contrefactuelle
*0:55 · sortir à 13:54*

Dernière mesure sur les générations : la distance sémantique entre les deux sorties d'une même paire, évaluée par un encodeur auxiliaire, mMiniLM. Qwen 1,5 milliard produit les sorties les plus proches après changement de genre, à 0,307, devant Qwen 0,5 milliard à 0,366, puis Mistral à 0,560. On serait tenté d'y voir l'effet de l'instruction-tuning. Deux réserves : la comparaison ne sépare pas le post-entraînement de la taille, du corpus et de la lignée ; et cette divergence inclut le bruit normal de l'échantillonnage. Sans comparer deux tirages du même prompt, on ne peut pas l'attribuer entièrement au genre.

## 17. Intercalaire · Partie 4
*0:08 · sortir à 14:02*

J'en arrive à la discussion et à la conclusion.

## 18. Confronter les trois familles
*1:25 · sortir à 15:27*

C'est le cœur de ma discussion. Les trois familles ne disent pas la même chose. Les encodeurs montrent des associations très nettes : 33 tests sur 36, avec des tailles d'effet souvent supérieures à 1. Les modèles masqués montrent des écarts modérés, significatifs pour deux modèles sur trois, et de signe variable selon le domaine. Les modèles génératifs, eux, ne montrent presque rien après correction. Ce désaccord n'est pas une contradiction à effacer, c'est un résultat. Deux lectures sont possibles, et mon protocole ne permet pas de trancher : soit l'alignement et le décodage limitent l'expression du stéréotype en sortie, soit les métriques internes mesurent autre chose que le comportement. C'est cohérent avec la littérature : Goldfarb-Tarrant et ses coauteurs ne trouvent pas de corrélation fiable entre métriques intrinsèques et biais applicatif. Et c'est précisément pour cette raison que je refuse d'agréger ces trois niveaux en une note unique : leur moyenne imposerait des pondérations arbitraires et pourrait masquer un défaut important derrière un bon score ailleurs.

## 19. Conclusion
*1:15 · sortir à 16:42*

Pour conclure. L'évaluation du biais de genre dépend de l'endroit où l'on observe le système : l'espace latent, les probabilités ou les générations. J'ai retenu trois familles de méthodes, non pas parce que l'une serait meilleure, mais parce qu'elles sont complémentaires. Leur valeur scientifique tient moins à la formule qu'au protocole : hypothèses fixées à l'avance, unité statistique correcte — la paire, pas le token —, incertitude mesurée et analyses de sensibilité. Ce que montre l'exécution trois par trois : des associations internes fortes, une préférence probabiliste pour les formulations féminines, et pratiquement aucun écart de contenu dans les générations. Aucun classement monotone entre taille et biais. Et aucune métrique, prise seule, ne suffit à certifier l'équité d'un modèle. L'objectif n'était donc pas d'apposer l'étiquette « débiaisé », mais de produire des résultats vérifiables, contextualisés et révisables — et un jeu de fonctions qu'une équipe comme People AI peut reprendre sur un autre modèle.

## 20. Merci de votre attention
*0:20 · sortir à 17:02*

Je vous remercie de votre attention. J'ai préparé des annexes sur le choix des modèles, le détail du protocole et la traduction en contexte d'entreprise. Je suis à votre disposition pour vos questions.
