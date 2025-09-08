from flask import Flask, render_template, request, jsonify
from AutoComplete import AVLTree
import pandas as pd 

app = Flask(__name__)

# Construção da árvore AVL a partir do dicionário
print("Carregando dicionário e construindo a árvore AVL...")
caminho_do_arquivo = 'dicionario.csv'
dicionario_avl = AVLTree()

try:
    dados = pd.read_csv(caminho_do_arquivo, sep=';', low_memory=False)

    # Inserindo não nulos
    for indice, linha in dados.iterrows():
        if pd.notna(linha['palavra']) and pd.notna(linha['significado']):
            dicionario_avl.insert(linha['palavra'], linha['significado'])

    print("Árvore AVL pronta e servidor rodando.")

except Exception as e:
    print(f"Ocorreu um erro ao carregar ou processar o arquivo: {e}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggest')
def suggest():
    prefixo = request.args.get('prefix', '').lower()
    
    if not prefixo:
        return jsonify([]) 

    sugestoes = dicionario_avl.sugerir(prefixo, limite=10) 
    return jsonify(sugestoes)


if __name__ == '__main__':
    app.run(debug=True)

