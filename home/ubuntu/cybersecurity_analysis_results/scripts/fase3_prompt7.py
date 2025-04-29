import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar o DataFrame
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# Configuração para melhor visualização
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# 1. Calcular a contagem total de cada Attack Type
attack_type_counts = df['Attack Type'].value_counts().sort_values(ascending=False)

# Plotar gráfico de barras para contagem de tipos de ataque
plt.figure(figsize=(12, 8))
ax1 = sns.barplot(x=attack_type_counts.index, y=attack_type_counts.values, palette='viridis')
plt.title('Frequência de Tipos de Ataque (2015-2024)', fontsize=16)
plt.xlabel('Tipo de Ataque', fontsize=14)
plt.ylabel('Número de Incidentes', fontsize=14)
plt.xticks(rotation=45)

# Adicionar valores nas barras
for i, v in enumerate(attack_type_counts.values):
    ax1.text(i, v + 20, str(v), ha='center', fontsize=11)

plt.tight_layout()
output_path_1 = "/home/ubuntu/attack_type_frequency.png"
plt.savefig(output_path_1)
plt.close()
print(f"Gráfico de frequência de tipos de ataque salvo em: {output_path_1}")

# 2. Calcular a média de Financial Loss para cada Attack Type
attack_type_loss = df.groupby('Attack Type')['Financial Loss (in Million $)'].mean().sort_values(ascending=False)

# Plotar gráfico de barras para prejuízo financeiro médio por tipo de ataque
plt.figure(figsize=(12, 8))
ax2 = sns.barplot(x=attack_type_loss.index, y=attack_type_loss.values, palette='rocket')
plt.title('Prejuízo Financeiro Médio por Tipo de Ataque (2015-2024)', fontsize=16)
plt.xlabel('Tipo de Ataque', fontsize=14)
plt.ylabel('Prejuízo Financeiro Médio (Milhões $)', fontsize=14)
plt.xticks(rotation=45)

# Adicionar valores nas barras
for i, v in enumerate(attack_type_loss.values):
    ax2.text(i, v + 1, f"{v:.2f}", ha='center', fontsize=11)

plt.tight_layout()
output_path_2 = "/home/ubuntu/attack_type_avg_loss.png"
plt.savefig(output_path_2)
plt.close()
print(f"Gráfico de prejuízo financeiro médio por tipo de ataque salvo em: {output_path_2}")

# 3. Calcular a média de Number of Affected Users para cada Attack Type
attack_type_users = df.groupby('Attack Type')['Number of Affected Users'].mean().sort_values(ascending=False)

# Plotar gráfico de barras para usuários afetados médio por tipo de ataque
plt.figure(figsize=(12, 8))
ax3 = sns.barplot(x=attack_type_users.index, y=attack_type_users.values, palette='mako')
plt.title('Média de Usuários Afetados por Tipo de Ataque (2015-2024)', fontsize=16)
plt.xlabel('Tipo de Ataque', fontsize=14)
plt.ylabel('Média de Usuários Afetados', fontsize=14)
plt.xticks(rotation=45)

# Adicionar valores nas barras
for i, v in enumerate(attack_type_users.values):
    ax3.text(i, v + 10000, f"{int(v):,}".replace(',', '.'), ha='center', fontsize=11)

plt.tight_layout()
output_path_3 = "/home/ubuntu/attack_type_avg_users.png"
plt.savefig(output_path_3)
plt.close()
print(f"Gráfico de média de usuários afetados por tipo de ataque salvo em: {output_path_3}")
