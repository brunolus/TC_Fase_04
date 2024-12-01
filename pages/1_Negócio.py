import streamlit as st

# Layout para o símbolo da FIAP no topo
left, cent, right = st.columns(3)
with right:
    st.image('imagens/fiap_simbolo.png')

# Adiciona espaço vertical
st.write("")

# Título da seção
st.title('Negócio')

# Espaçamento vertical
st.write("")

# Texto descritivo mais elaborado e contextualizado
st.markdown(
    """
    <div style='text-align: justify; font-size: 16px;'>
        <p>
            O petróleo desempenha um papel essencial na economia global, sendo considerado um dos principais recursos estratégicos do mundo. É uma commodity que movimenta trilhões de dólares anualmente, influenciando diretamente preços de energia, transporte e bens de consumo. O <strong>Brent</strong>, extraído do Mar do Norte, é a principal referência para a precificação no mercado europeu, africano e asiático, enquanto o <strong>West Texas Intermediate (WTI)</strong>, proveniente dos Estados Unidos, reflete a dinâmica do mercado norte-americano.
        </p>
        <p>
            O Brent e o WTI possuem características que os tornam altamente desejados pela indústria. Ambos são classificados como petróleos leves e doces devido ao baixo teor de enxofre, o que facilita o processo de refino para produção de combustíveis como gasolina e diesel. Entretanto, o Brent se destaca pela acessibilidade logística, devido à extração em plataformas marítimas, enquanto o WTI enfrenta desafios relacionados ao transporte terrestre.
        </p>
        <p>
            O mercado de petróleo opera em duas modalidades principais:
        </p>
        <ul>
            <li>
                <strong>Mercado à Vista:</strong> Onde o petróleo é comercializado com liquidação imediata, refletindo o preço atual do barril.
            </li>
            <li>
                <strong>Mercado Futuro:</strong> Baseado em contratos que permitem aos investidores e produtores especular sobre preços ou se proteger contra oscilações de mercado. Esses contratos desempenham um papel estratégico, pois garantem estabilidade para refinarias e previsibilidade de receitas para os produtores.
            </li>
        </ul>
        <p>
            A formação do preço do petróleo é uma equação complexa influenciada por diversos fatores. Entre eles:
        </p>
        <ul>
            <li>
                <strong>Decisões da OPEP:</strong> A Organização dos Países Exportadores de Petróleo regula a produção global para controlar a oferta e estabilizar os preços.
            </li>
            <li>
                <strong>Cotação do Dólar:</strong> Como o petróleo é precificado globalmente em dólares, a valorização ou desvalorização da moeda impacta diretamente os custos para países importadores.
            </li>
            <li>
                <strong>Conflitos Geopolíticos:</strong> Regiões produtoras como Oriente Médio frequentemente enfrentam tensões políticas que afetam a estabilidade do fornecimento.
            </li>
            <li>
                <strong>Avanços Tecnológicos:</strong> A extração de petróleo de xisto nos EUA e a automação de plataformas offshore têm moldado o equilíbrio de oferta e demanda global.
            </li>
            <li>
                <strong>Eventos Globais:</strong> Crises financeiras, pandemias e mudanças climáticas também têm um impacto significativo no consumo e na produção.
            </li>
        </ul>
        <p>
            Nos últimos anos, o avanço da <strong>Inteligência Artificial (IA)</strong> tem transformado o setor energético. Soluções baseadas em algoritmos preditivos estão ajudando empresas e governos a analisarem padrões históricos, preverem flutuações de preços e tomarem decisões estratégicas com maior precisão. Este projeto explora exatamente esse potencial, aplicando técnicas de <strong>Machine Learning</strong> para prever preços do petróleo Brent e gerar insights valiosos para um mercado altamente volátil.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

left, cent, right = st.columns(3)
with cent:
   st.image('imagens/petroleo_mar.png', width=250)