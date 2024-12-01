import streamlit as st


left, cent, right = st.columns(3)
with right:
    st.image('imagens/fiap_simbolo.png')

st.write("")
  

st.title('Projeto')

# Texto explicativo geral
st.markdown(
    """
    <div style="text-align: justify;">
        Este projeto foi desenvolvido pelo Grupo 44 como parte do desafio Tech Challenge. O objetivo principal é analisar os dados históricos do preço do petróleo Brent, extrair insights relevantes e implementar um modelo de Machine Learning para previsão de preços. Além disso, foi criado um MVP utilizando o Streamlit, o qual está acessando nesse momento, para demonstrar os resultados de forma interativa.
    </div>
    """,
    unsafe_allow_html=True
)

# Criação de abas para explicar cada etapa macro
tab1, tab2, tab3, tab4 = st.tabs(["Introdução", "Análise de Dados", "Modelo de Previsão", "Implementação"])

# Aba 1: Introdução
with tab1:
    st.subheader("Introdução")
    st.markdown(
        """
        O petróleo Brent é amplamente utilizado como referência global para precificação de petróleo. 
        Compreender as variações de preço pode ajudar empresas a tomar decisões estratégicas.
        
        Este trabalho foi dividido em três etapas principais:
        - **Análise de Dados:** Exploração e visualização dos dados históricos do preço do petróleo.
        - **Modelo de Previsão:** Criação de um modelo de Machine Learning para prever os preços futuros.
        - **MVP:** Desenvolvimento de um protótipo funcional usando Streamlit para apresentar os resultados.
        """
    )

# Aba 2: Análise de Dados
with tab2:
    # Título da aba
    st.subheader("Análise de Dados")

    # Explicação detalhada
    st.markdown(
    """
    Esta seção apresenta as etapas realizadas na análise exploratória e preparação dos dados históricos do preço do petróleo Brent, bem como as visualizações geradas a partir dos dados.

    ### Etapas Realizadas
    #### 1. Coleta de Dados
    Os dados foram coletados diretamente do site do **IPEA** usando a função `pd.read_html()` da biblioteca `pandas`. Essa função permite extrair tabelas HTML diretamente de uma URL. Os parâmetros utilizados incluem:
    - `skiprows=1`: Ignora a primeira linha da tabela.
    - `thousands='.'`: Define o separador de milhar.
    - `decimal=','`: Define o separador decimal.

    #### 2. Limpeza e Preparação dos Dados
    Três funções foram definidas para preparar os dados após entender quais dados e como os mesmos são entregues pelo **IPEA**:
    - **Renomeação de Colunas (`renomearColunas`)**: Renomeia as colunas para `data` e `preco` para facilitar a manipulação.
    - **Conversão de Datas (`tipoData`)**: Converte as datas do formato string para o formato datetime, padronizando-as.
    - **Exclusão de Dados Nulos (`excluirDadosNulos`)**: Remove registros que contenham valores ausentes.

    #### 3. Análise Exploratória
    Após a preparação, os dados foram analisados utilizando técnicas exploratórias:
    - **Histograma**: Visualização das frequências dos preços para identificar a distribuição dos valores.
    """
    )
    
    st.image("imagens/Analise_exploratorio_histograma_001.png", caption="Histograma - Análise Exploratória dos Dados")

    st.markdown(
    """
    - **Boxplot**: Gráfico que destaca possíveis outliers e a dispersão dos dados.
    """
    )

    st.image("imagens/Analise_exploratorio_boxplot_001.png", caption="Boxplot - Análise Exploratória dos Dados")

    st.markdown(
    """
    #### 4. Decomposição da Série Temporal
    Foi utilizada a função `seasonal_decompose` da biblioteca `statsmodels` para decompor a série temporal em:
    - **Tendência**: Mostra a direção geral dos preços ao longo do tempo.
    """
    )

    st.image("imagens/Decomposicao_temporal_decomposicao_001.png", caption="Decomposição - Série de Preços do Petróleo Brent")

    st.markdown(
    """
    - **Sazonalidade**: Identifica padrões repetitivos (por exemplo, sazonalidade mensal ou anual).
    """
    )

    st.image("imagens/Decomposicao_temporal_sezonalidade_001.png", caption="Sazonalidade - Série de Preços do Petróleo Brent")

    st.markdown(
    """
    - **Resíduo**: Representa as variações inexplicadas.

    #### 5. Filtragem Temporal
    Para analisar os dados mais recentes, foi aplicado um filtro para incluir apenas registros a partir de 2023.

    ### Visualizações Geradas
    #### Histograma
    Um histograma foi criado para exibir a frequência dos preços:
    - Eixo X: Preços do petróleo.
    - Eixo Y: Frequência de ocorrência.
    - Visualização estilizada com o template `ggplot2`.

    #### Boxplot
    Gráfico que destaca outliers e fornece insights sobre a dispersão e o comportamento dos preços.

    #### Decomposição de Séries Temporais
    A série foi decomposta em quatro partes:
    - Série original.
    - Média móvel.
    - Sazonalidade.
    - Resíduos.

    #### Sazonalidade Recente
    Uma análise específica da sazonalidade foi realizada para dados a partir de 2023.

    ### Conclusões
    - As visualizações e a decomposição forneceram informações valiosas sobre os padrões históricos do preço do petróleo Brent.
    - A sazonalidade mostrou tendências repetitivas que podem ser úteis na modelagem de previsão.
    """
    )
    st.markdown(
        """
        #### Análise das Oscilações do Petróleo Brent
        O petróleo Brent apresentou oscilações significativas em três momentos marcantes da história recente:

        **2008: Crise Financeira Global**  
        Durante a crise financeira global desencadeada pelo colapso do mercado imobiliário nos EUA (crise do subprime), a demanda global por petróleo caiu drasticamente. Após a falência do Lehman Brothers, os investidores abandonaram ativos de risco, incluindo commodities como o petróleo, em busca de liquidez. Isso resultou em uma queda acentuada nos preços, agravada pela redução no consumo de combustíveis mundialmente.  
        *Fonte: [Banco Mundial](https://www.worldbank.org/ext/en/home)*

        **2014: Superprodução e Conflito na OPEP**  
        Em 2014, a produção de petróleo de xisto nos EUA atingiu níveis recordes, resultando em uma oferta abundante no mercado global. Ao mesmo tempo, a demanda por petróleo diminuiu na Europa e na Ásia. A Organização dos Países Exportadores de Petróleo (OPEP) decidiu não reduzir a produção, priorizando sua participação de mercado. Essa estratégia impactou negativamente economias altamente dependentes do petróleo, como Venezuela, Rússia e Irã.  
        *Fonte: [EIA - U.S. Energy Information Administration ](https://www.eia.gov/)*

        **2020: Pandemia de COVID-19 e Guerra de Preços**  
        A pandemia de COVID-19 gerou uma queda sem precedentes no consumo global de petróleo, com a implementação de medidas de isolamento social. Além disso, divergências entre a Arábia Saudita e a Rússia em relação aos cortes na produção desencadearam uma guerra de preços. A Arábia Saudita decidiu aumentar a oferta, o que contribuiu para a redução significativa dos preços no mercado internacional.  
        *Fonte: [International Energy Agency (IEA)](https://www.iea.org/)*

        Esses eventos demonstram como fatores econômicos, geopolíticos e crises globais têm impacto direto no mercado do petróleo Brent, tornando-o altamente volátil e sensível a mudanças no cenário mundial.
        """
    )

# Aba 3: Modelo de Previsão
with tab3:
   # Título da aba
    st.subheader("Modelo de Previsão")

    # Introdução ao modelo
    st.markdown(
        """
        Nesta seção, apresentamos o uso do modelo **ARIMA** para a previsão dos preços do petróleo Brent. 
        O modelo foi treinado com dados históricos e validado com um conjunto de teste recente.
        
        ### Principais Etapas
        1. **Seleção do Modelo:** Utilizamos o **AutoARIMA** da biblioteca `StatsForecast`, que automatiza a escolha dos parâmetros ideais para o modelo.
        2. **Treinamento:** O modelo foi treinado com dados históricos (de 2000 a 2024-11-18).
        3. **Previsão:** Os preços futuros foram previstos para um período de 5 dias, com intervalos de confiança de 90%.
        4. **Visualização:** Gráficos interativos apresentam os valores reais, as previsões e as bandas de confiança.
        """
    )

    # Treinamento e Previsão do Modelo
    st.markdown(
        """
        Após a preparação dos dados e a definição do modelo, os dados foram divididos em:
        - **Treino:** De 2000 a 2024-11-18.
        - **Teste:** Dados a partir de 2024-11-19.
        
        Abaixo, apresentamos os resultados do modelo:
        """
    )

    # Tabela de Resultados (Valores Reais e Previstos)
    st.write("### Resultados do Modelo ARIMA")

    st.image("imagens/Modelo_de_previsao_resultados_001.png", caption="Resultado ARIMA")

    # Avaliação do Modelo com WMAPE
    st.markdown(
        """
        ### Avaliação do Modelo
        
        Para avaliar a precisão do modelo ARIMA, utilizamos a métrica **WMAPE** (Weighted Mean Absolute Percentage Error).
        
        - **O que é o WMAPE?** É uma métrica robusta que calcula o erro absoluto médio ponderado pelos valores reais, evitando distorções em cenários onde os valores reais são pequenos.
        - **Interpretação:** Quanto menor o WMAPE, melhor o desempenho do modelo. Valores próximos de 0 indicam uma previsão mais precisa.
        """
    )

    # Exibição do valor WMAPE calculado
    wmape_arima = 0.0105487536907552  # Este é o valor calculado com base no modelo.
    st.markdown(f"**WMAPE do modelo ARIMA:** {wmape_arima:.15}")

    # Conclusões
    st.markdown(
        """
        ### Conclusões
        - O modelo ARIMA foi eficaz para capturar os padrões históricos e gerar previsões confiáveis em curto prazo.
        - O **WMAPE** calculado indica que o modelo apresenta um erro percentual absoluto ponderado muito baixo (aproximadamente 1%), demonstrando alta precisão.
        - A banda de confiança ajuda a compreender a margem de erro nas previsões.
        - Para períodos mais longos, recomenda-se o uso de modelos híbridos ou baseados em aprendizado profundo, como LSTM.
        """
    )


# Aba 4: Implementação
with tab4:
    st.subheader("Implementação")
    st.markdown(
        """
        Nesta seção, detalhamos as etapas realizadas para implementar este projeto no Streamlit, abrangendo desde a análise de dados até o deploy final.

        1. **Análise e Preparação de Dados**  
           Os dados históricos do preço do petróleo Brent e do dólar foram extraídos de fontes confiáveis e processados no ambiente Google Colab. Durante esta etapa:  
           - Foram realizados tratamentos para remoção de dados inconsistentes e preenchimento de valores nulos.  
           - Os dados foram formatados em arquivos CSV e carregados no repositório do projeto para facilitar o acesso e reutilização.  

        2. **Criação do Modelo de Machine Learning**  
           Utilizamos o modelo **AutoARIMA**, implementado com a biblioteca `StatsForecast`, para prever os preços do petróleo Brent. As etapas foram:  
           - O modelo foi treinado no ambiente Colab com dados históricos de 2000 a 2024.  
           - O arquivo resultante (`auto_arima_brent.joblib`) foi exportado para ser utilizado diretamente no projeto Streamlit.  

        3. **Desenvolvimento da Interface no Streamlit**  
           A aplicação foi desenvolvida no framework **Streamlit**, e a estrutura do menu foi organizada em quatro seções principais:  
           - **Home**: Apresentação geral do projeto e equipe.  
           - **Negócio**: Explicação sobre o mercado de petróleo e seus fatores de influência.  
           - **Projeto**: Detalhamento das etapas realizadas, incluindo a implementação.  
           - **MVP - Petróleo Brent**: Interface interativa com gráficos de análise histórica e previsão de preços.  

           No desenvolvimento:  
           - Gráficos gerados no Colab foram exportados como imagens e integrados ao projeto para enriquecer a experiência visual.  
           - O modelo treinado foi carregado para fazer previsões diretamente na aplicação.  

        4. **Deploy da Aplicação**  
           O código-fonte foi versionado e armazenado em um repositório no GitHub. Para o deploy, seguimos os passos:  
           - A aplicação foi vinculada ao **Streamlit Community Cloud**, permitindo deploy automático a partir do repositório GitHub.  
           - A aplicação pode ser acessada diretamente online, garantindo acessibilidade para visualização e interação.  

        5. **Integração com o Power BI**  
           Os dados processados no Colab foram exportados em formato CSV e integrados ao Power BI Cloud. Essa etapa permitiu a criação de um painel interativo, complementando a visualização no Streamlit com análises aprofundadas.

        Com essa implementação, o projeto fornece uma experiência completa, desde a análise de dados até a previsão interativa de preços, acessível para qualquer dispositivo conectado à internet.
        """
    )
