import random

valores = [0, 1, 2, 3, 4]
probabilidades = [0.20, 0.35, 0.25, 0.15, 0.05]

simulacoes = random.choices(valores, weights=probabilidades, k=30)

print(f"Resultados das 30 simulações: {simulacoes}")
print(f"Média simulada: {sum(simulacoes)/30}")