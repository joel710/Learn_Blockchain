# Implémentation d'une Blockchain en Python

Ce projet est une implémentation simple d'une blockchain en Python, démontrant les concepts fondamentaux de la technologie blockchain, notamment les blocs, le hachage et le minage par preuve de travail.

## Table des matières
- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Fichiers du projet](#fichiers-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnement](#fonctionnement)
- [Documentation du projet](#documentation-du-projet)
- [Achèvement du devoir](#achèvement-du-devoir)

## Aperçu

Cette implémentation démontre les concepts fondamentaux de la technologie blockchain :
- Blocs avec index, horodatage, données, hachage précédent et hachage actuel
- Hachage SHA-256 pour l'identification des blocs
- Mécanisme de consensus par preuve de travail
- Liaison en chaîne par références de hachage
- Minage de blocs avec difficulté ajustable

## Fonctionnalités

- ✅ Création de blocs avec tous les attributs requis
- ✅ Hachage SHA-256 utilisant le module hashlib de Python
- ✅ Création du bloc genesis
- ✅ Minage par preuve de travail avec difficulté ajustable
- ✅ Validation de la blockchain par chaînage de hachage
- ✅ Affichage visuel de la blockchain
- ✅ Visualisation améliorée dans la V2

## Fichiers du projet

- [main.py](file:///c:/Users/MSI/Desktop/Blockchain/main.py) - Implémentation originale de la blockchain
- [V2.py](file:///c:/Users/MSI/Desktop/Blockchain/V2.py) - Version améliorée avec visualisation améliorée
- [DOCUMENTATION_BLOCKCHAIN.md](file:///c:/Users/MSI/Desktop/Blockchain/DOCUMENTATION_BLOCKCHAIN.md) - Documentation du parcours d'apprentissage (en français)
- [DEVOIR_BLOCKCHAIN.md](file:///c:/Users/MSI/Desktop/Blockchain/DEVOIR_BLOCKCHAIN.md) - Réponses aux questions du devoir et explications

## Installation

Aucune installation spéciale n'est requise. Le projet utilise uniquement les bibliothèques standard de Python :
- `hashlib` pour le hachage SHA-256
- `datetime` pour la génération d'horodatage

Python 3.6 ou supérieur est recommandé.

## Utilisation

Pour exécuter l'implémentation de la blockchain :

```bash
python main.py
```

ou

```bash
python V2.py
```

Les deux commandes vont :
1. Créer une blockchain avec un bloc genesis
2. Miner 4 blocs supplémentaires avec preuve de travail
3. Afficher la blockchain complète

## Fonctionnement

### Structure d'un bloc
Chaque bloc contient :
- `index` : Position dans la blockchain
- `timestamp` : Heure de création
- `data` : Informations stockées dans le bloc
- `previous_hash` : Hachage du bloc précédent (mécanisme de liaison)
- `nonce` : Nombre utilisé pour la preuve de travail
- `hash` : Hachage SHA-256 du contenu du bloc

### Processus de minage
Le minage consiste à trouver un nonce qui produit un hachage répondant aux exigences de difficulté :
1. Créer un nouveau bloc avec les données fournies
2. Incrémenter le nonce jusqu'à ce que le hachage commence par le nombre spécifié de zéros
3. Ajouter le bloc miné à la chaîne

### Difficulté
La difficulté détermine combien de zéros initiaux le hachage doit avoir :
- Difficulté 1 : Le hachage commence par "0"
- Difficulté 3 : Le hachage commence par "000"
- Une difficulté plus élevée nécessite plus de travail computationnel

## Documentation du projet

Pour une explication détaillée du processus d'apprentissage et de l'implémentation du code, voir :
- [DOCUMENTATION_BLOCKCHAIN.md](file:///c:/Users/MSI/Desktop/Blockchain/DOCUMENTATION_BLOCKCHAIN.md) (en français)
- [DEVOIR_BLOCKCHAIN.md](file:///c:/Users/MSI/Desktop/Blockchain/DEVOIR_BLOCKCHAIN.md) (réponses au devoir)

## Achèvement du devoir

Ce projet remplit toutes les exigences du devoir sur la blockchain :
1. ✅ Classe Block avec tous les attributs requis
2. ✅ Méthode calculate_hash() implémentant SHA-256
3. ✅ Classe Blockchain avec chaîne, create_genesis_block() et get_latest_block()
4. ✅ Méthode mine_block() avec implémentation de la preuve de travail
5. ✅ Fonction utilitaire hash_starts_with_zeros()
6. ✅ Création de 4 blocs avec une difficulté de 3
7. ✅ Fonctionnalité d'affichage

L'implémentation démontre la compréhension de :
- Structure et création de blocs
- Mécanismes de hachage
- Liaison de la blockchain
- Consensus par preuve de travail
- Sécurité par difficulté computationnelle