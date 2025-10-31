import hashlib
import datetime

# =========================
# Classe Block
# =========================
class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

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

# =========================
# Classe Blockchain
# =========================
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

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

    def hash_starts_with_zeros(self, hash_value, difficulty):
        """
        Vérifie si le hash commence par 'difficulty' zéros.
        """
        return hash_value.startswith("0" * difficulty)

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

        # Tant que le hash ne commence pas par 'difficulty' zéros, on incrémente le nonce
        while not self.hash_starts_with_zeros(new_block.hash, difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        print(f"✅ Bloc {new_block.index} miné avec succès ! Hash : {new_block.hash}")
        self.chain.append(new_block)

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

# =========================
# TEST DU PROGRAMME
# =========================
if __name__ == "__main__":
    difficulty = 3  # Le hash doit commencer par 3 zéros
    my_blockchain = Blockchain()  # Création de la blockchain avec bloc genesis

    # Ajout de 3 nouveaux blocs avec preuve de travail
    my_blockchain.mine_block("Premier bloc après Genesis", difficulty)
    my_blockchain.mine_block("Deuxième bloc ajouté", difficulty)
    my_blockchain.mine_block("Troisième bloc ajouté", difficulty)
    my_blockchain.mine_block("Quatrième bloc ajouté", difficulty)

    # Affichage complet de la blockchain
    my_blockchain.display_chain()
