import pandas as pd

# Carregar o DataFrame (assumindo que já foi carregado e limpo, se necessário)
df = pd.read_csv('/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv')

# 1. Listar todos os valores únicos da coluna Attack Type
print('--- Valores Únicos em Attack Type ---')
print(df['Attack Type'].unique())
print('\n' + '-'*50 + '\n')

# 2. Listar todos os valores únicos da coluna Target Industry
print('--- Valores Únicos em Target Industry ---')
print(df['Target Industry'].unique())

