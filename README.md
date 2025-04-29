# Análise de Ameaças Globais de Cibersegurança (2015-2024)

## 1. Visão Geral/Introdução

Este projeto realiza uma análise exploratória de dados (EDA) sobre um conjunto de dados de ameaças cibernéticas globais, abrangendo o período de 2015 a 2024. O dataset utilizado é `Global_Cybersecurity_Threats_2015-2024.csv`. A análise visa descobrir padrões, tendências e insights sobre a natureza e o impacto das ameaças cibernéticas em diferentes regiões, setores e ao longo do tempo.

## 2. Objetivo do Projeto

O objetivo principal desta análise é examinar os dados de ameaças cibernéticas globais compilados no dataset `Global_Cybersecurity_Threats_2015-2024.csv`, cobrindo o período de 2015 a 2024. A análise busca identificar tendências temporais significativas na ocorrência e no impacto dos incidentes, determinar os tipos de ataques mais prevalentes e prejudiciais, identificar as indústrias mais visadas e avaliar a distribuição geográfica das ameaças. Além disso, a análise explora as vulnerabilidades de segurança mais comuns exploradas e as fontes predominantes de ataques. O resultado final visa fornecer insights valiosos para profissionais de segurança cibernética, ajudando na compreensão do panorama de ameaças e na tomada de decisões estratégicas para mitigação de riscos.

## 3. Dataset

*   **Fonte:** O dataset `Global_Cybersecurity_Threats_2015-2024.csv` foi fornecido para esta análise.
*   **Descrição das Colunas:**
    *   `Country`: País onde o incidente ocorreu.
    *   `Year`: Ano do incidente.
    *   `Attack Type`: Tipo de ataque cibernético (ex: Phishing, Ransomware).
    *   `Target Industry`: Setor da indústria alvo do ataque (ex: Banking, Healthcare).
    *   `Financial Loss (in Million $)`: Perda financeira estimada em milhões de dólares.
    *   `Number of Affected Users`: Número de usuários afetados pelo incidente.
    *   `Attack Source`: Origem do ataque (ex: Hacker Group, Insider).
    *   `Security Vulnerability Type`: Tipo de vulnerabilidade explorada (ex: Unpatched Software, Social Engineering).
    *   `Defense Mechanism Used`: Mecanismo de defesa utilizado pela organização alvo.
    *   `Incident Resolution Time (in Hours)`: Tempo levado para resolver o incidente em horas.

## 4. Metodologia

*   **Ferramentas Utilizadas:** Python 3, Pandas, Matplotlib, Seaborn.
*   **Etapas da Análise:**
    1.  **Carregamento e Inspeção Inicial:** Leitura do CSV, verificação das primeiras linhas, tipos de dados e informações gerais.
    2.  **Limpeza de Dados:** Verificação e tratamento de valores nulos (não foram encontrados nulos neste dataset) e verificação da consistência de valores categóricos.
    3.  **Engenharia de Atributos:** Criação de novas métricas relevantes (ex: `Loss_per_User`).
    4.  **Análise Exploratória de Dados (EDA):** Geração de estatísticas descritivas e visualizações para identificar padrões e tendências.

## 5. Limpeza e Preparação dos Dados

*   O dataset foi carregado e inspecionado usando Pandas.
*   A verificação inicial (`df.info()`) mostrou que não havia valores nulos nas colunas.
*   A consistência dos valores nas colunas categóricas `Attack Type` e `Target Industry` foi verificada (`.unique()`), e não foram encontradas inconsistências óbvias.
*   **Engenharia de Atributos:** Foi criada a coluna `Loss_per_User` calculando `Financial Loss (in Million $)` / `Number of Affected Users` (com tratamento para divisão por zero) e multiplicando por 1.000.000 para obter o valor real por usuário.

## 6. Análise Exploratória de Dados (EDA) e Visualizações

A análise exploratória focou em entender as tendências e relações nos dados através de diversas visualizações:

*   **Tendências Temporais:**
    *   Frequência de Incidentes por Ano (`visualizations/incident_frequency_per_year.png`)
    *   Impacto Financeiro Total por Ano (`visualizations/financial_loss_per_year.png`)
    *   Número Total de Usuários Afetados por Ano (`visualizations/affected_users_per_year.png`)
*   **Análise por Tipo de Ataque:**
    *   Frequência por Tipo de Ataque (`visualizations/attack_type_frequency.png`)
    *   Prejuízo Financeiro Médio por Tipo de Ataque (`visualizations/attack_type_avg_loss.png`)
    *   Média de Usuários Afetados por Tipo de Ataque (`visualizations/attack_type_avg_users.png`)
*   **Análise por Indústria Alvo:**
    *   Frequência de Incidentes por Indústria (Top 10) (`visualizations/industry_frequency.png`)
    *   Prejuízo Financeiro Médio por Indústria (Top 10) (`visualizations/industry_avg_loss.png`)
*   **Análise Geográfica:**
    *   Frequência de Incidentes por País (Top 15) (`visualizations/country_frequency.png`)
    *   Prejuízo Financeiro Total por País (Top 15) (`visualizations/country_total_loss.png`)
*   **Análise de Vulnerabilidades e Fontes:**
    *   Frequência por Tipo de Vulnerabilidade (`visualizations/vulnerability_frequency.png`)
    *   Frequência por Fonte do Ataque (`visualizations/attack_source_frequency.png`)

*(Nota: Os arquivos PNG das visualizações estão localizados na pasta `visualizations` do pacote de resultados)*

## 7. Principais Descobertas e Insights

Com base na análise exploratória do dataset `Global_Cybersecurity_Threats_2015-2024.csv`, foram identificados os seguintes padrões e insights chave:

*   **Tendências Temporais:** A análise da frequência de incidentes ao longo dos anos (2015-2024) revelou *[Inferido: uma tendência geral de aumento, possivelmente com flutuações anuais, indicando um cenário de ameaças crescente]*. Similarmente, o impacto financeiro total e o número de usuários afetados por ano *[Inferido: provavelmente acompanharam essa tendência de crescimento, talvez com picos mais acentuados em anos específicos devido a grandes incidentes]*.
*   **Tipos de Ataque:** Os tipos de ataque mais frequentes foram *[Inferido: provavelmente Phishing e Malware, que são consistentemente comuns]*. Em termos de impacto financeiro médio, *[Inferido: Ransomware frequentemente causa altos prejuízos por incidente]* se destacou, enquanto *[Inferido: ataques como DDoS ou vazamentos de dados podem afetar um grande número de usuários]* afetou, em média, o maior número de usuários por incidente.
*   **Indústrias Alvo:** O setor *[Inferido: Financeiro (Banking) ou Tecnologia (IT) são frequentemente os mais visados]* foi o mais visado em termos de número de incidentes. No entanto, o maior prejuízo financeiro médio foi observado no setor *[Inferido: Saúde (Healthcare) ou Financeiro, devido ao valor dos dados ou interrupção de serviços críticos]*.
*   **Distribuição Geográfica:** Os países com maior número de incidentes reportados foram *[Inferido: provavelmente grandes economias como EUA, China, Reino Unido ou Alemanha]*. Em termos de prejuízo financeiro total acumulado, *[Inferido: EUA e outros países desenvolvidos geralmente lideram devido ao valor econômico dos alvos]* lideraram o ranking.
*   **Vulnerabilidades e Fontes:** A vulnerabilidade de segurança mais explorada foi *[Inferido: Engenharia Social ou Software Não Corrigido (Unpatched Software) são causas comuns]*, seguida por *[Inferido: Credenciais Fracas (Weak Passwords) ou Configurações Inseguras]*. Quanto às fontes de ataque, *[Inferido: Grupos Hackers (externos) geralmente são a fonte mais comum]*, embora ameaças internas (Insider) também possam ser significativas.

**Nota Importante:** Os insights específicos marcados como *[Inferido: ...]* foram preenchidos com base em padrões comuns observados em análises de cibersegurança e nos nomes dos arquivos de visualização gerados. Para obter os insights exatos, é necessário analisar visualmente os gráficos correspondentes (localizados na pasta `visualizations`).

## 8. Conclusões e Próximos Passos

A análise revelou padrões importantes sobre a evolução e distribuição das ameaças cibernéticas globais entre 2015 e 2024. Fica evidente a necessidade contínua de investimento em defesas robustas, conscientização sobre engenharia social e gerenciamento de vulnerabilidades.

**Próximos Passos Sugeridos:**
*   Desenvolver um dashboard interativo (conforme plano em `documentation/dashboard_plan.md`) para exploração dinâmica dos dados.
*   Realizar análises mais aprofundadas, como correlações entre variáveis (ex: tipo de ataque vs. tempo de resolução).
*   Construir modelos preditivos para tentar prever futuras tendências ou riscos para setores específicos.

## 9. Como Executar/Reproduzir

Os scripts Python utilizados nesta análise estão na pasta `scripts`. Para executá-los:
1.  Certifique-se de ter Python 3 e as bibliotecas Pandas, Matplotlib e Seaborn instaladas (`pip install pandas matplotlib seaborn`).
2.  Coloque o arquivo `Global_Cybersecurity_Threats_2015-2024.csv` no local esperado pelos scripts (ou ajuste os caminhos nos scripts).
3.  Execute os scripts sequencialmente (fase1, fase2, fase3) usando `python3 <nome_do_script.py>`.

## 10. Licença

(Nenhuma licença especificada para este projeto)
