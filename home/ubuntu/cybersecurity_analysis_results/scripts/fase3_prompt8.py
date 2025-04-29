import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# Configuração para melhor visualização
plt.style.use("seaborn-v0_8-darkgrid")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 12

# 1. Calcular a contagem total de incidentes para cada Target Industry (Top 10)
industry_counts = df["Target Industry"].value_counts().nlargest(10).sort_values(ascending=False)

# Plotar gráfico de barras para contagem de incidentes por indústria
plt.figure(figsize=(12, 8))
ax1 = sns.barplot(x=industry_counts.index, y=industry_counts.values, palette="viridis")
plt.title("Top 10 Indústrias Mais Visadas por Incidentes (2015-2024)", fontsize=16)
plt.xlabel("Indústria Alvo", fontsize=14)
plt.ylabel("Número de Incidentes", fontsize=14)
plt.xticks(rotation=45, ha="right")

# Adicionar valores nas barras
for i, v in enumerate(industry_counts.values):
    ax1.text(i, v + 5, str(v), ha="center", fontsize=11)

plt.tight_layout()
output_path_1 = "/home/ubuntu/industry_frequency.png"
plt.savefig(output_path_1)
plt.close()
print(f"Gráfico de frequência de incidentes por indústria salvo em: {output_path_1}")

# 2. Calcular a média de Financial Loss para cada Target Industry (Top 10)
industry_loss = df.groupby("Target Industry")["Financial Loss (in Million $)"].mean().nlargest(10).sort_values(ascending=False)

# Plotar gráfico de barras para prejuízo financeiro médio por indústria
plt.figure(figsize=(12, 8))
ax2 = sns.barplot(x=industry_loss.index, y=industry_loss.values, palette="rocket")
plt.title("Top 10 Indústrias por Prejuízo Financeiro Médio (2015-2024)", fontsize=16)
plt.xlabel("Indústria Alvo", fontsize=14)
plt.ylabel("Prejuízo Financeiro Médio (Milhões $)", fontsize=14)
plt.xticks(rotation=45, ha="right")

# Adicionar valores nas barras
for i, v in enumerate(industry_loss.values):
    ax2.text(i, v + 0.5, f"{v:.2f}", ha="center", fontsize=11)

plt.tight_layout()
output_path_2 = "/home/ubuntu/industry_avg_loss.png"
plt.savefig(output_path_2)
plt.close()
print(f"Gráfico de prejuízo financeiro médio por indústria salvo em: {output_path_2}")

