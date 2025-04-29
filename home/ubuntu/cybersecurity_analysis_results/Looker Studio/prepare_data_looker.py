import pandas as pd
import numpy as np

# Carregar o DataFrame original
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# Recalcular Loss_per_User (como feito na análise anterior)
# Tratar divisão por zero: onde 'Number of Affected Users' é 0, Loss_per_User será 0
df["Loss_per_User"] = np.where(
    df["Number of Affected Users"] == 0,
    0,
    df["Financial Loss (in Million $)"] / df["Number of Affected Users"]
)

# Multiplicar por 1.000.000 para ter o valor real por usuário, não em milhões
df["Loss_per_User"] = df["Loss_per_User"] * 1000000

# Arredondar para 2 casas decimais para melhor apresentação
df["Loss_per_User"] = df["Loss_per_User"].round(2)

# Salvar o DataFrame modificado em um novo arquivo CSV
output_csv_path = "/home/ubuntu/cybersecurity_data_for_looker.csv"
df.to_csv(output_csv_path, index=False)

print(f"Arquivo CSV preparado para Looker Studio salvo em: {output_csv_path}")

# Verificar as primeiras linhas do novo CSV
print("\n--- Primeiras 5 linhas do CSV preparado ---")
print(df.head())

