import streamlit as st

left, cent, right = st.columns(3)
with right:
    st.image('imagens/fiap_simbolo.png')

# Adiciona espaço vertical
st.write("")


st.title('TC 04 - Análise de Projeção Petróleo')

st.write("")


st.markdown(
    '''
        <div style="text-align: justify;">
            <p>
                Este projeto visa desenvolver um dashboard interativo para gerar insights relevantes sobre o mercado de petróleo Brent, incluindo a aplicação de um modelo de Machine Learning para previsão de preços.
            </p>
            <p>
                O projeto completo pode ser acessado no <b><a style='text-decoration:none;' href='https://github.com/brunolus/TC_Fase_04'>repositório</a></b> no GitHub.
            </p>
    ''',
    unsafe_allow_html=True
)


left, cent, right = st.columns(3)
with cent:
   st.image('imagens/barril_petroleo.png', width=250)