import pandas as pd

# 1. Carregar o CSV em um DataFrame chamado df
df = pd.read_csv('/home/ubuntu/upload/Global_Cybersecurity_Threats_2015-2024.csv')

# 2. Exibir as primeiras 5 linhas (df.head())
print('--- Primeiras 5 linhas (df.head()) ---')
print(df.head())
print('\n' + '-'*50 + '\n')

# 3. Exibir as informações do DataFrame (df.info())
print('--- Informações do DataFrame (df.info()) ---')
df.info()
print('\n' + '-'*50 + '\n')

# 4. Exibir estatísticas descritivas básicas (df.describe(include='all'))
print('--- Estatísticas Descritivas (df.describe(include=\'all\')) ---')
print(df.describe(include='all'))

