import streamlit as st
import pandas as pd
import plotly.express as px


dados = pd.read_csv('dados/preco_brent.csv')
dados = dados[dados['data'] >= '2000-01-01']
forecast = pd.read_csv('dados/last_forecast.csv')

#tipando coluna de data
dados['data'] = pd.to_datetime(dados['data'])

#configurando template do plotly
template = 'ggplot2'

#figuras

#série
fig = px.line(
    data_frame=dados, 
    x=dados.data,
    y=dados.preco,
    template=template,
    color_discrete_sequence=['#E6004C'],
    labels={
        'preco':'Preço (US$)',
        'data':'Data'
    }
    
)
fig.update_layout(
    title='Histórico de Preço do Petróleo Brent (US$)',
    xaxis_title='Período',
    yaxis_title='Preço (US$)'
)

#série prevista
fig_previsao = px.line(
    data_frame=forecast, 
    x=forecast.data,
    y=forecast.preco_previsto,
    template=template,
    color_discrete_sequence=['#E6004C'],
    labels={
        'preco_previsto':'Preço previsto (US$)',
        'data':'Data'
    }
)
fig_previsao.update_layout(
    title='Previsão de Preço do Petróleo Brent (US$)',
    xaxis_title='Período',
    yaxis_title='Preço Previsto (US$)'
)

#visualização no streamlit

#logo fiap
left, cent, right = st.columns(3)
with right:
    st.image('imagens/fiap_simbolo.png')

#título
st.title('Análise Petróleo Brent')

#layout do aplicativo
tab1, tab2 = st.tabs(['Previsão', 'Análise Histórica'])


with tab1:
    #série prevista
    st.plotly_chart(fig_previsao, use_container_width=True)
    st.markdown('O gráfico acima apresenta a previsão para as próximas 5 cotações do barril de petróleo Brent, gerada pelo modelo AutoARIMA')

with tab2:
    #série
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        '''
        <div style='text-align: justify;'>
            <p>
                O petróleo Brent sofreu oscilações significativas em três momentos recentes:
            </p>
            <ul>
                <li>2008: Durante a crise financeira global, desencadeada pela especulação imobiliária nos EUA (subprime), houve uma queda drástica na demanda e no preço do petróleo. Após o colapso do Lehman Brothers, os investidores abandonaram commodities como o petróleo, buscando liquidez, enquanto o consumo global de combustíveis despencava.</li>
                <li>2014: A superprodução, especialmente do petróleo de xisto dos EUA, combinada com a menor demanda na Europa e Ásia, derrubou os preços. A OPEP recusou reduzir a produção para preservar sua participação de mercado, prejudicando economias dependentes do petróleo, como Venezuela, Rússia e Irã.</li>
                <li>2020: A pandemia da COVID-19 provocou uma redução global no consumo de petróleo devido ao isolamento social, resultando em queda de preços. Divergências entre a Arábia Saudita e a Rússia sobre cortes na produção levaram a uma guerra de preços, com a Arábia Saudita aumentando a oferta e reduzindo drasticamente os valores.</li>
            </ul>
            <p>
                Esses eventos mostram como fatores econômicos, geopolíticos e crises globais afetam diretamente o mercado do petróleo Brent.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )