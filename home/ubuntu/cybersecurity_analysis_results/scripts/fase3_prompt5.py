import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# 1. Contar o número de incidentes por Year
incident_counts_per_year = df['Year'].value_counts().sort_index()

# 2. Plotar um gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x=incident_counts_per_year.index, y=incident_counts_per_year.values, palette='viridis')
plt.title('Número de Incidentes de Cibersegurança por Ano (2015-2024)')
plt.xlabel('Ano')
plt.ylabel('Número de Incidentes')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar o gráfico
output_path = '/home/ubuntu/incident_frequency_per_year.png'
plt.savefig(output_path)

print(f"Gráfico salvo em: {output_path}")

