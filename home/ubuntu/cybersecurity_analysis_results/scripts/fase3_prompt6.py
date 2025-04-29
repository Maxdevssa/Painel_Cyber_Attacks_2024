import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# Agrupar por ano
df_grouped_year = df.groupby("Year").agg(
    total_financial_loss=("Financial Loss (in Million $)", "sum"),
    total_affected_users=("Number of Affected Users", "sum")
).reset_index()

# 1 & 2: Calcular e plotar o total de Financial Loss por Year
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_grouped_year, x="Year", y="total_financial_loss", marker="o")
plt.title("Prejuízo Financeiro Total (Milhões $) por Ano (2015-2024)")
plt.xlabel("Ano")
plt.ylabel("Prejuízo Financeiro Total (Milhões $)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Salvar o gráfico de prejuízo financeiro
output_path_loss = "/home/ubuntu/financial_loss_per_year.png"
plt.savefig(output_path_loss)
print(f"Gráfico de prejuízo financeiro salvo em: {output_path_loss}")
plt.close() # Fechar a figura para o próximo gráfico

# 3 & 4: Calcular e plotar o total de Number of Affected Users por Year
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_grouped_year, x="Year", y="total_affected_users", marker="o", color="orange")
plt.title("Número Total de Usuários Afetados por Ano (2015-2024)")
plt.xlabel("Ano")
plt.ylabel("Número Total de Usuários Afetados")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Salvar o gráfico de usuários afetados
output_path_users = "/home/ubuntu/affected_users_per_year.png"
plt.savefig(output_path_users)
print(f"Gráfico de usuários afetados salvo em: {output_path_users}")
plt.close()

