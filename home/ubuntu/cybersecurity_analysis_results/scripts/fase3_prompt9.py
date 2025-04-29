import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# Configuração para melhor visualização
plt.style.use("seaborn-v0_8-darkgrid")
plt.rcParams["figure.figsize"] = (14, 8) # Ajustar tamanho para melhor visualização dos países
plt.rcParams["font.size"] = 12

# 1. Calcular a contagem total de incidentes para cada Country (Top 15)
country_counts = df["Country"].value_counts().nlargest(15).sort_values(ascending=False)

# Plotar gráfico de barras para contagem de incidentes por país
plt.figure(figsize=(14, 8))
ax1 = sns.barplot(x=country_counts.index, y=country_counts.values, palette="viridis")
plt.title("Top 15 Países por Frequência de Incidentes (2015-2024)", fontsize=16)
plt.xlabel("País", fontsize=14)
plt.ylabel("Número de Incidentes", fontsize=14)
plt.xticks(rotation=45, ha="right")

# Adicionar valores nas barras
for i, v in enumerate(country_counts.values):
    ax1.text(i, v + 5, str(v), ha="center", fontsize=11)

plt.tight_layout()
output_path_1 = "/home/ubuntu/country_frequency.png"
plt.savefig(output_path_1)
plt.close()
print(f"Gráfico de frequência de incidentes por país salvo em: {output_path_1}")

# 2. Calcular a soma total de Financial Loss para cada Country (Top 15)
country_loss = df.groupby("Country")["Financial Loss (in Million $)"].sum().nlargest(15).sort_values(ascending=False)

# Plotar gráfico de barras para prejuízo financeiro total por país
plt.figure(figsize=(14, 8))
ax2 = sns.barplot(x=country_loss.index, y=country_loss.values, palette="rocket")
plt.title("Top 15 Países por Prejuízo Financeiro Total (2015-2024)", fontsize=16)
plt.xlabel("País", fontsize=14)
plt.ylabel("Prejuízo Financeiro Total (Milhões $)", fontsize=14)
plt.xticks(rotation=45, ha="right")

# Adicionar valores nas barras
for i, v in enumerate(country_loss.values):
    ax2.text(i, v + 100, f"{v:.2f}", ha="center", fontsize=11)

plt.tight_layout()
output_path_2 = "/home/ubuntu/country_total_loss.png"
plt.savefig(output_path_2)
plt.close()
print(f"Gráfico de prejuízo financeiro total por país salvo em: {output_path_2}")

