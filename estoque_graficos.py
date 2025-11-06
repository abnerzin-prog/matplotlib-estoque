import matplotlib.pyplot as plt

# 1️⃣ Tendência de Estoque Diário (Gráfico de Linha)
dias = [1, 2, 3, 4, 5, 6, 7]
estoque = [100, 95, 110, 105, 120, 115, 130]

plt.figure(figsize=(6,4))
plt.plot(dias, estoque, marker='o', color='blue', label='Estoque diário')
plt.title('Tendência de Estoque Diário')
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade em Estoque')
plt.legend()
plt.grid(True)
plt.show()

# 2️⃣ Comparação de Produtos (Gráfico de Barras)
produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
quantidades = [50, 75, 30, 60]

plt.figure(figsize=(6,4))
plt.bar(produtos, quantidades, color='orange')
plt.title('Comparação de Produtos em Estoque')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.show()

# 3️⃣ Proporção de Categorias (Gráfico de Pizza)
categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
valores = [15000, 8000, 5000]

plt.figure(figsize=(6,4))
plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90)
plt.title('Proporção do Valor Total de Estoque por Categoria')
plt.show()

# 4️⃣ Preço vs. Quantidade (Gráfico de Dispersão)
precos = [50, 120, 300, 80, 20]
estoque = [80, 25, 10, 70, 150]

plt.figure(figsize=(6,4))
plt.scatter(precos, estoque, color='green')
plt.title('Relação entre Preço e Quantidade em Estoque')
plt.xlabel('Preço Unitário (R$)')
plt.ylabel('Quantidade em Estoque')
plt.show()
