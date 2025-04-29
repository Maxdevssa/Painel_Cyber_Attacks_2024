## Sugestões para Dashboard de Ameaças Globais de Cibersegurança (2015-2024)

Este documento descreve sugestões de KPIs, filtros interativos e tipos de gráficos para um dashboard eficaz baseado no dataset `Global_Cybersecurity_Threats_2015-2024.csv`.

**Ferramenta Sugerida:** Power BI / Tableau / Looker Studio (ou outra ferramenta de BI de sua preferência)

### 1. Principais KPIs (Indicadores Chave de Performance)

*   **Número Total de Incidentes:** Contagem geral de incidentes no período selecionado.
*   **Prejuízo Financeiro Total (Milhões $):** Soma total das perdas financeiras no período selecionado.
*   **Total de Usuários Afetados:** Soma total de usuários afetados no período selecionado.
*   **Tempo Médio de Resolução (Horas):** Média do tempo de resolução dos incidentes.
*   **Tipo de Ataque Mais Frequente:** O `Attack Type` com a maior contagem no período.
*   **Indústria Mais Afetada (por Frequência):** A `Target Industry` com a maior contagem de incidentes.
*   **País Mais Afetado (por Frequência):** O `Country` com a maior contagem de incidentes.

### 2. Filtros Interativos

Permitir que o usuário filtre os dados do dashboard pelos seguintes critérios:

*   **Ano (`Year`):** Seleção única ou múltipla de anos (slider ou lista).
*   **País (`Country`):** Seleção única ou múltipla de países (lista suspensa ou mapa clicável).
*   **Tipo de Ataque (`Attack Type`):** Seleção única ou múltipla (lista suspensa ou botões).
*   **Indústria Alvo (`Target Industry`):** Seleção única ou múltipla (lista suspensa).
*   **Tipo de Vulnerabilidade (`Security Vulnerability Type`):** Seleção única ou múltipla (lista suspensa).
*   **Fonte do Ataque (`Attack Source`):** Seleção única ou múltipla (lista suspensa).

### 3. Tipos de Gráficos Sugeridos

*   **Tendências Temporais:**
    *   **Gráfico de Linhas:** Número de Incidentes vs. Ano.
    *   **Gráfico de Linhas:** Prejuízo Financeiro Total vs. Ano.
    *   **Gráfico de Linhas:** Número Total de Usuários Afetados vs. Ano.
*   **Análise Categórica (Frequência e Impacto):**
    *   **Gráfico de Barras (Ordenado):** Contagem de Incidentes por `Attack Type`.
    *   **Gráfico de Barras (Ordenado):** Prejuízo Financeiro Médio (ou Total) por `Attack Type`.
    *   **Gráfico de Barras (Ordenado):** Média (ou Total) de Usuários Afetados por `Attack Type`.
    *   **Gráfico de Barras (Ordenado):** Contagem de Incidentes por `Target Industry` (Top N).
    *   **Gráfico de Barras (Ordenado):** Prejuízo Financeiro Médio (ou Total) por `Target Industry` (Top N).
    *   **Gráfico de Barras (Ordenado):** Contagem de Incidentes por `Security Vulnerability Type`.
    *   **Gráfico de Barras (Ordenado):** Contagem de Incidentes por `Attack Source`.
*   **Análise Geográfica:**
    *   **Mapa de Coroplético (Choropleth Map):** Intensidade de incidentes (contagem ou prejuízo total) por `Country`.
    *   **Gráfico de Barras (Ordenado):** Contagem de Incidentes por `Country` (Top N).
    *   **Gráfico de Barras (Ordenado):** Prejuízo Financeiro Total por `Country` (Top N).
*   **Distribuição:**
    *   **Histograma:** Distribuição do `Financial Loss (in Million $)`.
    *   **Histograma:** Distribuição do `Incident Resolution Time (in Hours)`.
    *   **Box Plot:** `Financial Loss (in Million $)` por `Attack Type` ou `Target Industry`.

### 4. Layout Sugerido

*   **Topo:** KPIs principais e filtros globais (Ano, País).
*   **Corpo Principal:**
    *   Gráficos de tendências temporais.
    *   Mapa geográfico.
    *   Gráficos de barras para análise de Tipos de Ataque e Indústrias.
*   **Seção Adicional/Lateral:** Filtros adicionais (Tipo de Ataque, Indústria, Vulnerabilidade, Fonte) e gráficos de barras para Vulnerabilidades e Fontes.

Estas são sugestões iniciais. O dashboard pode ser refinado com base nas necessidades específicas e nos insights mais relevantes descobertos durante a construção.

