import json

json_data = '''
[
    { "id": 1, "nome": "Arroz", "quantidade": 50, "preco": 20.99 },
    { "id": 2, "nome": "Feijão", "quantidade": 30, "preco": 8.50 },
    { "id": 3, "nome": "Macarrão", "quantidade": 40, "preco": 5.90 },
    { "id": 4, "nome": "Açúcar", "quantidade": 25, "preco": 4.20 },
    { "id": 5, "nome": "Café", "quantidade": 60, "preco": 14.70 },
    { "id": 6, "nome": "Leite", "quantidade": 100, "preco": 4.80 },
    { "id": 7, "nome": "Óleo de Soja", "quantidade": 70, "preco": 9.50 },
    { "id": 8, "nome": "Sabonete", "quantidade": 200, "preco": 1.50 },
    { "id": 9, "nome": "Detergente", "quantidade": 150, "preco": 2.30 },
    { "id": 10, "nome": "Papel Higiênico", "quantidade": 80, "preco": 12.00 }
]
'''
produtos = json.loads(json_data)

valor_total = 0

for produto in produtos:
    subtotal = produto['quantidade'] * produto['preco']
    valor_total = valor_total + subtotal

    print(f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}, Valor Total: R$ {subtotal:.2f}")

print(f"\nValor total em produtos no mercado: R$ {valor_total:.2f}")