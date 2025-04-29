import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# Configuração para melhor visualização
plt.style.use("seaborn-v0_8-darkgrid")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 12

# 1. Calcular a contagem total de cada Security Vulnerability Type
vulnerability_counts = df["Security Vulnerability Type"].value_counts().sort_values(ascending=False)

# Plotar gráfico de barras para contagem de tipos de vulnerabilidade
plt.figure(figsize=(12, 8))
ax1 = sns.barplot(x=vulnerability_counts.index, y=vulnerability_counts.values, palette="viridis")
plt.title("Frequência de Tipos de Vulnerabilidade de Segurança (2015-2024)", fontsize=16)
plt.xlabel("Tipo de Vulnerabilidade", fontsize=14)
plt.ylabel("Número de Incidentes", fontsize=14)
plt.xticks(rotation=45, ha="right")

# Adicionar valores nas barras
for i, v in enumerate(vulnerability_counts.values):
    ax1.text(i, v + 10, str(v), ha="center", fontsize=11)

plt.tight_layout()
output_path_1 = "/home/ubuntu/vulnerability_frequency.png"
plt.savefig(output_path_1)
plt.close()
print(f"Gráfico de frequência de tipos de vulnerabilidade salvo em: {output_path_1}")

# 2. Calcular a contagem total de cada Attack Source
source_counts = df["Attack Source"].value_counts().sort_values(ascending=False)

# Plotar gráfico de barras para contagem de fontes de ataque
plt.figure(figsize=(12, 8))
ax2 = sns.barplot(x=source_counts.index, y=source_counts.values, palette="rocket")
plt.title("Frequência de Fontes de Ataque (2015-2024)", fontsize=16)
plt.xlabel("Fonte do Ataque", fontsize=14)
plt.ylabel("Número de Incidentes", fontsize=14)
plt.xticks(rotation=45, ha="right")

# Adicionar valores nas barras
for i, v in enumerate(source_counts.values):
    ax2.text(i, v + 10, str(v), ha="center", fontsize=11)

plt.tight_layout()
output_path_2 = "/home/ubuntu/attack_source_frequency.png"
plt.savefig(output_path_2)
plt.close()
print(f"Gráfico de frequência de fontes de ataque salvo em: {output_path_2}")

