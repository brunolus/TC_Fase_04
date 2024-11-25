import streamlit as st

left, cent, right = st.columns(3)
with right:
    st.image('imagens/fiap_simbolo.png')

# Adiciona espaço vertical
st.write("")



st.title('Negócio')

st.write("")

st.markdown(
    '''
        <div style='text-align: justify;'>
            <p>
                O preço do petróleo é definido pela oferta e demanda no mercado internacional, sendo cotado em dólares por barril. O petróleo Brent, extraído do Mar do Norte e negociado na Bolsa de Londres, é uma das principais referências da commodity, assim como o West Texas Intermediate (WTI), oriundo dos EUA. A principal diferença entre ambos está nos locais de extração e nas dinâmicas de mercado. Historicamente, o WTI apresenta preços mais baixos devido ao excesso de oferta nos EUA.
            </p>
            <p>
                Tanto o Brent quanto o WTI são classificados como petróleo leve e doce, valorizados por seu baixo teor de enxofre e facilidade de refino. O Brent lidera as cotações globais devido à extração em alto-mar, mais acessível, enquanto o WTI depende de transporte terrestre. Mais de 50% do petróleo mundial é cotado com base no Brent.
            </p>
            <p>
                O petróleo é negociado no mercado à vista, com liquidação imediata, ou no mercado futuro, por meio de contratos que especulam os preços sem troca física do produto. Investidores utilizam o mercado futuro para lucrar ou proteger-se da volatilidade, enquanto refinarias travam custos e produtores garantem receitas.
            </p>
            <p>
                Os preços do petróleo são influenciados por fatores como o valor do dólar, decisões da OPEC, níveis de produção e estoques, acordos internacionais e a economia global. Soluções de IA, como as propostas neste projeto, trazem previsibilidade ao mercado, ajudando na tomada de decisão com insights de curto prazo.
            </p>
        </div>
    ''',
    unsafe_allow_html=True
)

left, cent, right = st.columns(3)
with cent:
   st.image('imagens/petroleo_mar.png', width=250)