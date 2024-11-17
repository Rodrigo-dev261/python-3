import sqlite3
from datetime import datetime

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT,
    quantidade INTEGER NOT NULL,
    marca TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS movimentacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    tipo TEXT,
    quantidade INTEGER,
    data TEXT,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
''')

def adicionar_produto(nome, categoria, quantidade, marca):
    cursor.execute('''
    INSERT INTO produtos (nome, categoria, quantidade, marca)
    VALUES (?, ?, ?, ?)
    ''', (nome, categoria, quantidade, marca))
    conn.commit()

def atualizar_estoque(produto_id, quantidade, tipo):
    cursor.execute('''
    UPDATE produtos
    SET quantidade = quantidade + ?
    WHERE id = ?
    ''', (quantidade if tipo == 'entrada' else -quantidade, produto_id))
    conn.commit()

    cursor.execute('''
    INSERT INTO movimentacoes (produto_id, tipo, quantidade, data)
    VALUES (?, ?, ?, ?)
    ''', (produto_id, tipo, quantidade, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()

def gerar_relatorio_estoque():
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    print('Relatório de Estoque:')
    for produto in produtos:
        print(f'ID: {produto[0]}, Nome: {produto[1]}, Categoria: {produto[2]}, Quantidade: {produto[3]}, Marca: {produto[4]}')

def gerar_relatorio_movimentacoes():
    cursor.execute('SELECT * FROM movimentacoes')
    movimentacoes = cursor.fetchall()
    print('Histórico de Movimentações:')
    for mov in movimentacoes:
        print(f'ID: {mov[0]}, Produto ID: {mov[1]}, Tipo: {mov[2]}, Quantidade: {mov[3]}, Data: {mov[4]}')

def listar_produtos():
    cursor.execute('SELECT id, nome FROM produtos')
    produtos = cursor.fetchall()
    print('Lista de Produtos:')
    for produto in produtos:
        print(f'ID: {produto[0]}, Nome: {produto[1]}')

def menu():
    while True:
        print('\nControle de Estoque')
        print('1. Adicionar Produto')
        print('2. Entrada no Estoque')
        print('3. Saída do Estoque')
        print('4. Gerar Relatório de Estoque')
        print('5. Gerar Relatório de Movimentações')
        print('6. Listar Produtos')
        print('7. Sair')

        escolha = input('Escolha uma Opção: ')

        if escolha == '1':
            nome = input('Nome do Produto: ')
            categoria = input('Categoria: ')
            quantidade = int(input('Quantidade: '))
            marca = input('Marca: ')
            adicionar_produto(nome, categoria, quantidade, marca)
        elif escolha == '2':
            listar_produtos()
            produto_id = int(input('ID do Produto: '))
            quantidade = int(input('Quantidade: '))
            atualizar_estoque(produto_id, quantidade, 'entrada')
        elif escolha == '3':
            listar_produtos()
            produto_id = int(input('ID do Produto: '))
            quantidade = int(input('Quantidade: '))
            atualizar_estoque(produto_id, quantidade, 'saida')
        elif escolha == '4':
            gerar_relatorio_estoque()
        elif escolha == '5':
            gerar_relatorio_movimentacoes()
        elif escolha == '6':
            listar_produtos()
        elif escolha == '7':
            break
        else:
            print('Opção inválida! Tente novamente.')

# Executar o menu
menu()

# Fechar conexão
conn.close()
