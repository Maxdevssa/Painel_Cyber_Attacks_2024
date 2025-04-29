import pandas as pd
import numpy as np

# Carregar o DataFrame
df = pd.read_csv("/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv")

# Calcular Loss_per_User
# Tratar divisão por zero: onde 'Number of Affected Users' é 0, Loss_per_User será 0
df["Loss_per_User"] = np.where(
    df["Number of Affected Users"] == 0,
    0,
    df["Financial Loss (in Million $)"] / df["Number of Affected Users"]
)

# Multiplicar por 1.000.000 para ter o valor real por usuário, não em milhões
df["Loss_per_User"] = df["Loss_per_User"] * 1000000

# Exibir as primeiras linhas com a nova coluna
print("--- Primeiras linhas com a nova coluna Loss_per_User ---")
print(df.head())

# Verificar se há valores infinitos ou NaN caso a divisão por zero não tenha sido tratada corretamente
print("\n--- Verificação de NaN/Inf em Loss_per_User ---")
print(f"Valores NaN: {df['Loss_per_User'].isnull().sum()}")
print(f"Valores Infinitos: {np.isinf(df['Loss_per_User']).sum()}")

