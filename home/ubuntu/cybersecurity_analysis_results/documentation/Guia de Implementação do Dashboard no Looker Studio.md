# Guia de Implementação do Dashboard no Looker Studio

Este guia fornece um passo a passo resumido para implementar o dashboard de Ameaças Globais de Cibersegurança no Looker Studio, utilizando o arquivo `cybersecurity_data_for_looker.csv` e o plano detalhado `dashboard_plan_looker_studio.md`.

## 1. Conectar a Fonte de Dados

1.  Abra o Looker Studio (studio.google.com).
2.  Crie um novo "Relatório em branco".
3.  Na janela "Adicionar dados ao relatório", escolha o conector "Upload de arquivo".
4.  Faça o upload do arquivo `cybersecurity_data_for_looker.csv`.
5.  Clique em "Adicionar" e confirme a adição ao relatório.

## 2. Configurar Campos na Fonte de Dados

1.  No menu "Recurso", selecione "Gerenciar fontes de dados adicionadas".
2.  Clique em "Editar" na fonte de dados recém-adicionada (`cybersecurity_data_for_looker.csv`).
3.  **Verifique os Tipos de Dados:** Confirme se os tipos estão corretos conforme descrito no `dashboard_plan_looker_studio.md` (Dimensões de Texto, Métricas Numéricas, etc.). Ajuste se necessário.
4.  **Crie Campos Calculados:**
    *   Clique em "Adicionar um Campo".
    *   Nome do Campo: `Count of Incidents`
    *   Fórmula: `COUNT(Year)` (ou outra coluna garantidamente não nula)
    *   Salve o campo.
5.  **Renomeie Campos (Opcional):** Renomeie colunas como `Financial Loss (in Million $)` para nomes mais amigáveis, se desejar (ex: "Prejuízo Financeiro (Milhões $)").
6.  Clique em "Concluído" no canto superior direito.

## 3. Adicionar Controles de Filtro

1.  No menu "Inserir", selecione os controles desejados ("Lista Suspensa", "Controle Deslizante", "Controle de Período", etc.).
2.  Para cada controle, configure o "Campo de Controle" para a dimensão correspondente (`Year`, `Country`, `Attack Type`, etc.).
3.  Posicione os controles na parte superior do relatório, conforme o layout sugerido.
4.  Ajuste as opções de cada controle (ex: permitir seleção múltipla, definir intervalo para slider).

## 4. Criar KPIs (Scorecards)

1.  No menu "Inserir", selecione "Scorecard".
2.  Para cada KPI listado no plano:
    *   Arraste a métrica correspondente para o campo "Métrica" do scorecard (ex: `Count of Incidents`, `SUM(Financial Loss (in Million $))`).
    *   Ajuste a formatação (número, moeda, unidades compactas) na aba "Estilo".
3.  Posicione os scorecards na parte superior do relatório.

## 5. Construir os Gráficos

1.  No menu "Inserir", selecione o tipo de gráfico apropriado ("Gráfico de Série Temporal", "Gráfico de Barras", "Mapa Geográfico", etc.) conforme o plano detalhado.
2.  Para cada gráfico:
    *   Configure a "Dimensão" e a "Métrica" conforme especificado no `dashboard_plan_looker_studio.md`.
    *   Aplique ordenação (na seção "Classificar") e limites (ex: "Mostrar Top 10") quando necessário.
    *   Ajuste a aparência (cores, eixos, títulos) na aba "Estilo".
3.  Organize os gráficos no corpo principal e nas seções laterais do relatório, seguindo o layout sugerido.

## 6. Revisar e Refinar

1.  Teste a interatividade dos filtros.
2.  Verifique se todos os gráficos e KPIs estão exibindo os dados corretamente.
3.  Ajuste o layout, cores e fontes para garantir clareza e boa apresentação visual.
4.  Dê um nome ao seu relatório e salve-o.

Seguindo estes passos e consultando o `dashboard_plan_looker_studio.md` para detalhes específicos de cada componente, você poderá construir o dashboard interativo no Looker Studio.

