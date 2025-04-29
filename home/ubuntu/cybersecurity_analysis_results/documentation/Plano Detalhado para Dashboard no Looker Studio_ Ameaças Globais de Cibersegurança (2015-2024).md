## Plano Detalhado para Dashboard no Looker Studio: Ameaças Globais de Cibersegurança (2015-2024)

Este documento refina o plano original (`dashboard_plan.md`) com sugestões específicas para implementação no Looker Studio, utilizando o dataset `cybersecurity_data_for_looker.csv`.

**Fonte de Dados:** Conecte o Looker Studio ao arquivo `cybersecurity_data_for_looker.csv` (via upload de arquivo ou Google Sheets se carregado lá).

### 1. Configuração da Fonte de Dados no Looker Studio

*   Após conectar o CSV, verifique os tipos de dados:
    *   `Country`, `Attack Type`, `Target Industry`, `Attack Source`, `Security Vulnerability Type`, `Defense Mechanism Used`: Dimensão (Texto)
    *   `Year`: Dimensão (Número) - Pode ser convertido para Data (Ano) se preferir, mas Número funciona bem para filtros.
    *   `Financial Loss (in Million $)`, `Number of Affected Users`, `Incident Resolution Time (in Hours)`, `Loss_per_User`: Métrica (Número)
*   **Criar Campos Calculados (Opcional, mas recomendado):**
    *   `Count of Incidents`: `COUNT(Year)` ou qualquer outra coluna não nula. Renomeie para "Número de Incidentes". Isso simplifica o uso em scorecards e gráficos.

### 2. Implementação dos KPIs (Scorecards)

Use o componente "Scorecard" para cada KPI:

*   **Número Total de Incidentes:** Scorecard com Métrica = `Count of Incidents` (ou `COUNT_DISTINCT` de um ID de incidente, se houvesse).
*   **Prejuízo Financeiro Total (Milhões $):** Scorecard com Métrica = `SUM(Financial Loss (in Million $))`. Formate como Moeda (USD, por exemplo) com unidade compacta (Milhões).
*   **Total de Usuários Afetados:** Scorecard com Métrica = `SUM(Number of Affected Users)`. Formate como Número com unidade compacta.
*   **Tempo Médio de Resolução (Horas):** Scorecard com Métrica = `AVG(Incident Resolution Time (in Hours))`. Formate como Número (1 casa decimal).
*   **Tipo de Ataque Mais Frequente:** Use uma "Tabela" com Dimensão = `Attack Type`, Métrica = `Count of Incidents`. Ordene decrescente pela métrica e mostre apenas a primeira linha. Ou crie um campo calculado complexo (menos ideal).
*   **Indústria Mais Afetada (por Frequência):** Similar ao anterior, Tabela com Dimensão = `Target Industry`, Métrica = `Count of Incidents`, ordenada, mostrando Top 1.
*   **País Mais Afetado (por Frequência):** Similar, Tabela com Dimensão = `Country`, Métrica = `Count of Incidents`, ordenada, mostrando Top 1.

### 3. Implementação dos Filtros Interativos (Controles)

Use os componentes de "Controle":

*   **Ano (`Year`):** "Controle de Período" (se `Year` for convertido para Data) ou "Lista Suspensa" / "Controle Deslizante" (se `Year` for Número). Controle Deslizante pode ser bom para intervalo.
*   **País (`Country`):** "Lista Suspensa" (com opção de pesquisa).
*   **Tipo de Ataque (`Attack Type`):** "Lista Suspensa".
*   **Indústria Alvo (`Target Industry`):** "Lista Suspensa".
*   **Tipo de Vulnerabilidade (`Security Vulnerability Type`):** "Lista Suspensa".
*   **Fonte do Ataque (`Attack Source`):** "Lista Suspensa".

Configure os controles para filtrar todo o relatório ou grupos específicos de gráficos, conforme desejado.

### 4. Implementação dos Gráficos

*   **Tendências Temporais:**
    *   **Gráfico de Série Temporal:** Dimensão = `Year` (eixo X), Métrica = `Count of Incidents` (eixo Y).
    *   **Gráfico de Série Temporal:** Dimensão = `Year`, Métrica = `SUM(Financial Loss (in Million $))`.
    *   **Gráfico de Série Temporal:** Dimensão = `Year`, Métrica = `SUM(Number of Affected Users)`.
*   **Análise Categórica (Frequência e Impacto):**
    *   **Gráfico de Barras:** Dimensão = `Attack Type`, Métrica = `Count of Incidents`. Ordene pela métrica.
    *   **Gráfico de Barras:** Dimensão = `Attack Type`, Métrica = `AVG(Financial Loss (in Million $))`. Ordene pela métrica.
    *   **Gráfico de Barras:** Dimensão = `Attack Type`, Métrica = `AVG(Number of Affected Users)`. Ordene pela métrica.
    *   **Gráfico de Barras:** Dimensão = `Target Industry`, Métrica = `Count of Incidents`. Ordene e limite ao Top N (ex: 10) nas configurações do gráfico.
    *   **Gráfico de Barras:** Dimensão = `Target Industry`, Métrica = `AVG(Financial Loss (in Million $))`. Ordene e limite ao Top N.
    *   **Gráfico de Barras:** Dimensão = `Security Vulnerability Type`, Métrica = `Count of Incidents`. Ordene.
    *   **Gráfico de Barras:** Dimensão = `Attack Source`, Métrica = `Count of Incidents`. Ordene.
*   **Análise Geográfica:**
    *   **Mapa Geográfico (Google Maps):** Localização = `Country`, Métrica de Cor = `Count of Incidents` ou `SUM(Financial Loss (in Million $))`.
    *   **Gráfico de Barras:** Dimensão = `Country`, Métrica = `Count of Incidents`. Ordene e limite ao Top N (ex: 15).
    *   **Gráfico de Barras:** Dimensão = `Country`, Métrica = `SUM(Financial Loss (in Million $))`. Ordene e limite ao Top N.
*   **Distribuição:**
    *   **Gráfico de Barras (Histograma):** Use um gráfico de barras onde a Dimensão é `Financial Loss (in Million $)` agrupada em intervalos (bins) e a Métrica é `Count of Incidents`.
    *   **Gráfico de Barras (Histograma):** Dimensão = `Incident Resolution Time (in Hours)` agrupada em intervalos, Métrica = `Count of Incidents`.
    *   **Gráfico de Caixa (Box Plot) - *Nota: Looker Studio não tem Box Plot nativo.* Alternativa:** Use um Gráfico de Barras empilhadas ou Tabela para mostrar quartis/mediana calculados como campos separados, ou use um Gráfico de Dispersão se fizer sentido comparar duas métricas.

### 5. Layout Sugerido (Mantido do Plano Original)

*   **Topo:** Scorecards (KPIs) e Controles de Filtro globais (Ano, País).
*   **Corpo Principal:** Gráficos de Série Temporal, Mapa Geográfico, Gráficos de Barras (Tipos de Ataque, Indústrias).
*   **Seção Adicional/Lateral:** Controles de Filtro adicionais, Gráficos de Barras (Vulnerabilidades, Fontes).

Este plano detalhado deve fornecer um guia claro para a construção do dashboard no Looker Studio. Lembre-se de ajustar a formatação e os estilos para melhor clareza e apelo visual.

