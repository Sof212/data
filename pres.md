Voici un texte clair pour présenter le processus à l’oral ou dans un rapport :

L’objectif de ce système est de normaliser automatiquement les noms d’écoles et d’universités. À partir d’un nom saisi de manière libre, comme « univ paris saclay », le système doit retrouver le nom de référence correspondant, ici « Université Paris-Saclay ».

Le processus repose sur une architecture hybride en deux étapes : une recherche lexicale rapide, appelée *retrieve*, suivie d’un reclassement neuronal plus précis, appelé *rerank*.

Tout d’abord, nous disposons d’un dictionnaire de référence. Chaque clé correspond au nom normalisé d’un établissement, tandis que la valeur associée contient la liste de ses alias. Ces alias peuvent être des abréviations, des variantes orthographiques, d’anciens noms ou des formulations couramment utilisées.

Lorsqu’un nom brut est reçu, RapidFuzz le compare aux alias présents dans le dictionnaire. Cette comparaison lexicale permet de sélectionner rapidement les 15 établissements les plus proches. Cette étape ne produit pas encore la réponse définitive : elle sert uniquement à réduire le nombre de candidats à analyser.

Ensuite, pour chacun des 15 candidats, le système construit une paire composée de la requête initiale et des informations de l’établissement candidat, notamment son nom normalisé et ses alias.

Ces paires sont transmises à un cross-encoder BERT. Le modèle analyse simultanément la requête et chaque candidat afin de mesurer leur correspondance sémantique. Contrairement à la comparaison lexicale, il peut prendre en compte le contexte et des relations plus fines entre les termes.

Enfin, les candidats sont classés selon le score attribué par le modèle. Celui qui obtient le score le plus élevé est sélectionné, et sa clé dans le dictionnaire devient le résultat final. La sortie du système est donc directement le nom normalisé de l’établissement, et non un identifiant technique.

Cette approche combine ainsi la rapidité de RapidFuzz avec la précision du cross-encoder BERT : le premier filtre efficacement un grand nombre d’établissements, tandis que le second effectue la décision finale sur un ensemble réduit de candidats.
