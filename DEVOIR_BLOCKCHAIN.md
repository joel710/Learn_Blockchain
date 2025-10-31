# Devoir : Implémentation d'une Blockchain avec Preuve de Travail

## 1. Réponse aux questions de base

### 1.1. Implémentation de la classe Block

La classe [Block](file:///c:/Users/MSI/Desktop/Blockchain/main.py#L5-L22) a été implémentée avec tous les attributs requis :

```python
class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index           # Numéro du bloc
        self.timestamp = timestamp   # Date/heure de création
        self.data = data             # Données quelconques
        self.previous_hash = previous_hash  # Hachage du bloc précédent
        self.nonce = 0               # Entier initialisé à 0
        self.hash = self.calculate_hash()   # Hachage du bloc courant
```

### 1.2. Méthode calculate_hash()

La méthode [calculate_hash()](file:///c:/Users/MSI/Desktop/Blockchain/main.py#L14-L22) retourne le SHA-256 de la concaténation des attributs :

```python
def calculate_hash(self):
    """
    Calcule le hash SHA-256 du bloc à partir de ses attributs.
    """
    to_hash = (
        str(self.index)
        + str(self.timestamp)
        + str(self.data)
        + str(self.previous_hash)
        + str(self.nonce)
    )
    return hashlib.sha256(to_hash.encode()).hexdigest()
```

### 1.3. Implémentation de la classe Blockchain

La classe [Blockchain](file:///c:/Users/MSI/Desktop/Blockchain/main.py#L25-L79) a été implémentée avec les éléments requis :

```python
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Attribut chain (liste de blocs)

    def create_genesis_block(self):
        """
        Crée le premier bloc (Genesis Block) de la blockchain.
        """
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Retourne le dernier bloc de la blockchain.
        """
        return self.chain[-1]
```

### 1.4. Test avec un bloc genesis

Le test a été implémenté dans la section principale du programme :

```python
if __name__ == "__main__":
    difficulty = 3  # Le hash doit commencer par 3 zéros
    my_blockchain = Blockchain()  # Création de la blockchain avec bloc genesis
    # ... (ajout de blocs et affichage)
```

## 2. Réponse aux questions sur le minage avec preuve de travail

### 2.1. Méthode mine_block(data, difficulty)

La méthode [mine_block()](file:///c:/Users/MSI/Desktop/Blockchain/main.py#L53-L71) implémente le mécanisme de minage :

```python
def mine_block(self, data, difficulty):
    """
    Crée un nouveau bloc et le mine selon la difficulté donnée.
    """
    previous_block = self.get_latest_block()
    new_block = Block(
        index=previous_block.index + 1,
        timestamp=datetime.datetime.now(),
        data=data,
        previous_hash=previous_block.hash
    )

    print(f"\n⛏️  Minage du bloc {new_block.index} en cours...")

    # Incrémente le nonce jusqu'à ce que le hash commence par 'difficulty' zéros
    while not self.hash_starts_with_zeros(new_block.hash, difficulty):
        new_block.nonce += 1
        new_block.hash = new_block.calculate_hash()

    print(f"✅ Bloc {new_block.index} miné avec succès ! Hash : {new_block.hash}")
    self.chain.append(new_block)
```

### 2.2. Fonction utilitaire hash_starts_with_zeros()

La fonction [hash_starts_with_zeros()](file:///c:/Users/MSI/Desktop/Blockchain/main.py#L45-L51) vérifie si un hash commence par un certain nombre de zéros :

```python
def hash_starts_with_zeros(self, hash_value, difficulty):
    """
    Vérifie si le hash commence par 'difficulty' zéros.
    """
    return hash_value.startswith("0" * difficulty)
```

### 2.3. Ajout de 4 blocs avec difficulté de 3

Dans le programme principal, 4 blocs ont été ajoutés avec une difficulté de 3 :

```python
# Ajout de 4 nouveaux blocs avec preuve de travail
my_blockchain.mine_block("Premier bloc après Genesis", difficulty)
my_blockchain.mine_block("Deuxième bloc ajouté", difficulty)
my_blockchain.mine_block("Troisième bloc ajouté", difficulty)
my_blockchain.mine_block("Quatrième bloc ajouté", difficulty)
```

### 2.4. Affichage de la blockchain

La méthode [display_chain()](file:///c:/Users/MSI/Desktop/Blockchain/main.py#L73-L89) permet d'afficher tous les blocs :

```python
def display_chain(self):
    """
    Affiche les informations de chaque bloc de la chaîne.
    """
    print("\n===== BLOCKCHAIN =====")
    for block in self.chain:
        print(f"\nBloc n°{block.index}")
        print(f"Timestamp       : {block.timestamp}")
        print(f"Données         : {block.data}")
        print(f"Hash            : {block.hash}")
        print(f"Hash précédent  : {block.previous_hash}")
        print(f"Nonce           : {block.nonce}")
    print("=======================\n")
```

## 3. Explication du fonctionnement

### 3.1. Principe de la preuve de travail

La preuve de travail (Proof-of-Work) est un mécanisme qui rend le minage des blocs coûteux en ressources, ce qui sécurise la blockchain. Pour miner un bloc, l'algorithme doit trouver un nonce tel que le hash du bloc commence par un certain nombre de zéros (défini par la difficulté).

Plus la difficulté est élevée, plus il faut de tentatives pour trouver le bon nonce, ce qui rend le minage plus long et coûteux en calcul.

### 3.2. Sécurité de la blockchain

Cette approche rend la blockchain sécurisée car :
1. Modifier un bloc existant changerait son hash
2. Cela invaliderait tous les blocs suivants
3. Pour modifier un bloc, il faudrait recommencer tout le minage
4. Avec plusieurs participants, il faudrait contrôler plus de 50% de la puissance de calcul

## 4. Résultats obtenus

Lors de l'exécution du programme :
1. Un bloc genesis est créé automatiquement
2. 4 blocs supplémentaires sont minés avec une difficulté de 3
3. Chaque bloc nécessite de trouver un nonce tel que le hash commence par "000"
4. La blockchain finale contient 5 blocs au total
5. Chaque bloc est lié au précédent par son hash

## 5. Code complet

Le code complet est disponible dans le fichier [main.py](file:///c:/Users/MSI/Desktop/Blockchain/main.py) et [V2.py](file:///c:/Users/MSI/Desktop/Blockchain/V2.py) de ce projet.