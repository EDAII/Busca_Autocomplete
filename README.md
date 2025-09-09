
# Dicionário Inteligente 

## Alunos  
| Matrícula | Nome |  
|:----------:|:---------------------------:|  
| 20/2046229 | Kallyne Macêdo Passos |  
| 20/0022199 | Leonardo Sobrinho de Aguiar |  

## Descrição do projeto

Este projeto objetiva explorar o tema de Algoritmos de Busca através da implementação de um "Dicionário Inteligente", uma aplicação web com uma funcionalidade de autocomplete que sugere palavras em tempo real à medida que o usuário digita e, após a seleção da palavra desejada, apresenta o significado dela. Assim, a aplicação recebe as palavras de um arquivo .csv e as insere em uma Árvore AVL, que, a partir da ordenação alfabética, atua como um índice otimizado para encontrar rapidamente todas as palavras que começam com um determinado prefixo.

## Guia de instalação

**Linguagem**: Python, HTML, CSS e JavaScript<br>
**Framework**: Flask<br>
**Pré-requisitos**: Navegador instalado, Python, Flask, Flask_CORS e Pandas presentes no computador; clonar o repositório localmente.

### Passo a Passo

### 1. Clonar repositório:
```bash
git clone https://github.com/EDAII/Busca_Autocomplete.git
```
### 2. Instale as Dependências:
Abra um terminal ou prompt de comando na pasta do projeto e execute:
```bash
pip install Flask Flask-CORS pandas
```
### 3. Inicie o Servidor:
Digite no mesmo terminal:
```bash
python app.py
```
### 4. Acesse a Aplicação:
Abra seu navegador web e acesse o seguinte endereço: http://127.0.0.1:5000

## Capturas de tela

<div align="center">
Página inicial
<img width="1912" height="832" alt="image" src="https://github.com/user-attachments/assets/95955c84-4df5-4f6c-9472-0e53b0c98347" /></div>
<br>
<div align="center">
Busca pela letra 'A'
<img width="1917" height="712" alt="image" src="https://github.com/user-attachments/assets/d5081e8a-cb90-4e56-b79a-379380f4956f" /></div>
<br>
<div align="center">
Resultado ao clicar em 'algebra'
<img width="1920" height="801" alt="image" src="https://github.com/user-attachments/assets/edf57114-aca8-455e-8d91-59610e2c97ab" /></div>


## Conclusões
Para desenvolver o projeto, foi escolhida a Árvore AVL como a estrutura de dados principal, implementada em Python. Por ser uma árvore de busca binária autobalanceada, após cada inserção de novas palavras do dicionário, a árvore realiza rotações para garantir que a diferença de altura entre as subárvores de qualquer nó seja no máximo um, impedindo, dessa forma, a degeneração da árvore para uma forma de lista ligada e garantindo que a complexidade de tempo para as operações realizadas seja sempre logarítmica, O(log n). Dessa forma, a Árvore AVL se mostrou uma boa escolha em relação às alternativas. 

## Outros
Para adicionar novos itens ao dicionário, é necessário atualizar os dados que servem como a fonte de informação para a análise. Assim, é possível cadastrar um novo termo e seu significado adicionando-os no arquivo ``dicionario.csv`` para que o sistema possa reconhecer, analisar e exibir o novo termo na interface.

## Gravação 

[Link da gravação](https://www.youtube.com/watch?v=ztO6GAjfO_s)
