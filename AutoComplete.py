import pandas as pd
class Node:

    # nó na Árvore AVL
    def __init__(self, key, meaning):
        self.key = key
        self.meaning = meaning # Significado da palavra
        self.left = None
        self.right = None
        self.height = 1 # altura de um novo nó

# Implementação da Árvore AVL
class AVLTree:

    def __init__(self):
        self.root = None
    
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        # Fator de balanceamento = Altura da subárvore esquerda - Altura da direita
        return self.getHeight(node.left) - self.getHeight(node.right)

    # Rotações
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        # Atualiza as alturas
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        # Atualiza as alturas
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def insert(self, key, meaning):
        self.root = self._insert_recursive(self.root, key, meaning)

    def _insert_recursive(self, root, key, meaning):
        if not root:
            return Node(key, meaning)
        elif key < root.key:
            root.left = self._insert_recursive(root.left, key, meaning)
        else:
            root.right = self._insert_recursive(root.right, key, meaning)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Caso desbalanceado aplica uma das rotações
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Lógica do Autocompletar
    def sugerir(self, prefixo, limite=10):

        # Retorna uma lista de palavras que começam com o prefixo
        sugestoes = []
        if not self.root or not prefixo:
            return sugestoes
            
        self._coletar_sugestoes(self.root, prefixo, sugestoes, limite)
        return sugestoes
    
    # Navega na árvore e coleta as sugestões.
    def _coletar_sugestoes(self, node, prefixo, sugestoes, limite):

        if not node or len(sugestoes) >= limite:
            return

        # Compara o prefixo com o início da palavra atual no nó
        if prefixo < node.key[:len(prefixo)]:
            self._coletar_sugestoes(node.left, prefixo, sugestoes, limite)
        
        elif prefixo > node.key[:len(prefixo)]:
            self._coletar_sugestoes(node.right, prefixo, sugestoes, limite)
            
        else: 
            self._coletar_sugestoes(node.left, prefixo, sugestoes, limite)

            if len(sugestoes) < limite and node.key.startswith(prefixo):
                sugestoes.append({'palavra':node.key, 'significado':node.meaning})

            self._coletar_sugestoes(node.right, prefixo, sugestoes, limite)

if __name__ == "__main__":
    dicionario_avl = AVLTree()

    caminho_do_arquivo = 'dicionario.csv'
    palavras = pd.read_csv(caminho_do_arquivo, sep=';')

    print("Construindo dicionário AVL...")
    for indice, linha in palavras.iterrows():
        if pd.notna(linha['palavra']):
           dicionario_avl.insert(linha['palavra'], linha['significado'])
    print("Dicionário construído com sucesso!")
    print("-" * 30)

    while True:
        prefixo_usuario = input("Digite um prefixo (ou 'sair' para terminar): ").lower()
        if prefixo_usuario == 'sair':
            break
        if not prefixo_usuario:
            continue
            
        sugestoes_encontradas = dicionario_avl.sugerir(prefixo_usuario)
        
        if sugestoes_encontradas:
            print("Sugestões encontradas:")
            for s in sugestoes_encontradas:
                print(f"  - {s}")
        else:
            print("Nenhuma sugestão encontrada.")
        print("-" * 30)

