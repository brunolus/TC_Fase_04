import streamlit as st
import pandas as pd
import plotly.express as px



dados = pd.read_csv('dados/preco_hist_brent.csv')
dados = dados[dados['data'] >= '2000-01-01']
forecast = pd.read_csv('dados/previsao_atual.csv')

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

st.write("")
    

#título
st.title('Análise Petróleo Brent')

#layout do aplicativo
tab1, tab2 = st.tabs(['Análise Histórica', 'Previsão'])


with tab1:
    #série
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    #série prevista
    st.plotly_chart(fig_previsao, use_container_width=True)
    st.markdown('O gráfico acima apresenta a previsão para as próximas 5 cotações do barril de petróleo Brent, gerada pelo modelo AutoARIMA')
