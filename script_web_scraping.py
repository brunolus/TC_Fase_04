import requests  # Realiza requisições HTTP para acessar dados de páginas web
from bs4 import BeautifulSoup  # Biblioteca para fazer parsing de conteúdo HTML
import pandas as pd
import numpy as np
import psycopg2 as ps
import pandas.io.sql as sqlio
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
import warnings


# Função que atualiza o DataFrame com dados mais recentes do IPEA
def atualizar_dataframe(dados_atuais, dados_novos, tabela):
    # Obtém a data mais recente no DataFrame atual
    ultima_data = dados_atuais['data'].max()
    # Filtra os dados mais recentes do DataFrame atualizado
    dados_novos_filtrados = dados_novos[dados_novos['data'] > ultima_data]
    dados_novos_filtrados['data'] = dados_novos_filtrados['data'].astype(str).replace(' 00:00:00', '')

    # Concatena os novos dados ao DataFrame atual, se houver registros novos
    if not dados_novos_filtrados.empty:
        # Atualiza o DataFrame com os novos dados
        dados_atualizados = pd.concat([dados_novos_filtrados, dados_atuais], ignore_index=True)
        # Realiza a atualização no banco de dados
        print(f'Foram encontrados {dados_novos_filtrados.shape[0]} novos registros.')
        #update_database(dados_novos_filtrados, tabela)
    else:
        # Caso não haja novos dados, mantém o DataFrame atual
        dados_atualizados = dados_atuais
        print('Não há novos registros ou a base local já está atualizada.')
        #update_database(dados_atualizados, tabela)
    
    return dados_atualizados


# Função para calcular o erro percentual absoluto médio ponderado (W-MAPE)
def wmape(valor_real, valor_previsto):
    erro_percentual = np.abs(valor_real - valor_previsto).sum() / np.abs(valor_real).sum()
    return erro_percentual


# Realizando Web Scraping

# PARTE 1 - EXTRAÇÃO DA SÉRIE HISTÓRICA DO PREÇO DO PETRÓLEO BRENT

# URL do IPEA para a série de preços do petróleo Brent
url_preco_brent = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
# Requisição dos dados
resposta_brent = requests.get(url_preco_brent)

# Verifica se a requisição foi bem-sucedida
if resposta_brent.status_code == 200:
    # Cria objeto BeautifulSoup para manipular o HTML da página
    soup = BeautifulSoup(resposta_brent.text, 'html.parser')
    # Localiza a tabela na página HTML
    tabela = soup.find('table', {'id': 'grd_DXMainTable'})
    # Converte a tabela em um DataFrame
    dados_brent_novos = pd.read_html(str(tabela), skiprows=0)[0]
    # Renomeia as colunas e trata dados
    dados_brent_novos.columns = dados_brent_novos.iloc[0]
    dados_brent_novos = dados_brent_novos.drop(0)
    dados_brent_novos['Data'] = dados_brent_novos['Data'].str.replace('/','-')
    dados_brent_novos['Data'] = pd.to_datetime(dados_brent_novos['Data'], format='%d-%m-%Y')
    dados_brent_novos['Preço - petróleo bruto - Brent (FOB)'] = dados_brent_novos['Preço - petróleo bruto - Brent (FOB)'].astype(int) / 100
    dados_brent_novos.rename(columns={'Data': 'data', 'Preço - petróleo bruto - Brent (FOB)': 'preco'}, inplace=True)

    # Verifica se o arquivo CSV existe, e o carrega se necessário
    caminho_arquivo_brent = 'dados/preco_brent.csv'
    try:
        dados_brent_existente = pd.read_csv(caminho_arquivo_brent)
    except FileNotFoundError:
        dados_brent_existente = dados_brent_novos
    
    # Atualiza o DataFrame com os dados novos
    tabela_brent = 'ipea.preco_brent'  # Nome da tabela no banco de dados
    dados_atualizados_brent = atualizar_dataframe(dados_brent_existente, dados_brent_novos, tabela_brent)
    # Exporta os dados atualizados para o CSV
    dados_atualizados_brent.to_csv(caminho_arquivo_brent, index=False)
else:
    # Exibe erro caso a requisição falhe
    print(f'Falha ao acessar a página. Código de status: {resposta_brent.status_code}')


# PARTE 2 - EXTRAÇÃO DA SÉRIE HISTÓRICA DO PREÇO DO DÓLAR

# URL do IPEA para a série de preços do dólar
url_preco_dolar = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M'
# Requisição dos dados
resposta_dolar = requests.get(url_preco_dolar)

# Verifica se a requisição foi bem-sucedida
if resposta_dolar.status_code == 200:
    # Cria objeto BeautifulSoup para manipular o HTML da página
    soup = BeautifulSoup(resposta_dolar.text, 'html.parser')
    # Localiza a tabela na página HTML
    tabela = soup.find('table', {'id': 'grd_DXMainTable'})
    # Converte a tabela em um DataFrame
    dados_dolar_novos = pd.read_html(str(tabela), skiprows=0, thousands='.', decimal=',')[0]
    # Renomeia as colunas e trata dados
    dados_dolar_novos.columns = dados_dolar_novos.iloc[0]
    dados_dolar_novos = dados_dolar_novos.drop(0)
    dados_dolar_novos['Data'] = dados_dolar_novos['Data'].str.replace('/','-')
    dados_dolar_novos['Data'] = pd.to_datetime(dados_dolar_novos['Data'], format='%d-%m-%Y')
    dados_dolar_novos['Taxa de câmbio - R$ / US$ - comercial - compra - média'] = dados_dolar_novos['Taxa de câmbio - R$ / US$ - comercial - compra - média'].astype(float)
    dados_dolar_novos.rename(columns={'Data': 'data', 'Taxa de câmbio - R$ / US$ - comercial - compra - média': 'preco'}, inplace=True)
    dados_dolar_novos = dados_dolar_novos[dados_dolar_novos['data'] >= '1987-05-20']

    # Verifica se o arquivo CSV existe, e o carrega se necessário
    caminho_arquivo_dolar = 'dados/preco_dolar.csv'
    try:
        dados_dolar_existente = pd.read_csv(caminho_arquivo_dolar)
    except FileNotFoundError:
        dados_dolar_existente = dados_dolar_novos
    
    # Atualiza o DataFrame com os dados novos
    tabela_dolar = 'ipea.preco_dolar'  # Nome da tabela no banco de dados
    dados_atualizados_dolar = atualizar_dataframe(dados_dolar_existente, dados_dolar_novos, tabela_dolar)
    # Exporta os dados atualizados para o CSV
    dados_atualizados_dolar.to_csv(caminho_arquivo_dolar, index=False)
else:
    # Exibe erro caso a requisição falhe
    print(f'Falha ao acessar a página. Código de status: {resposta_dolar.status_code}')


# PARTE 3 - EXTRAÇÃO DA PREVISÃO (FORECAST)

# Calculando o erro do modelo (W-MAPE)
try:
    # Verifica se já existe um arquivo de previsões anteriores para comparar
    ultima_previsao = pd.read_csv('dados/last_forecast.csv')
    erro_wmape = wmape(dados_atualizados_brent['preco'].head().values, ultima_previsao['preco_previsto'].values)
    #update_database_wmape(erro_wmape)
except FileNotFoundError:
    print('Não há dados suficientes para calcular o erro do modelo.')

# Realizando previsões com o modelo ARIMA

# Prepara os dados para o modelo StatsForecast
dados_forecast = dados_atualizados_brent[['data', 'preco']].rename(columns={'data': 'ds', 'preco': 'y'})
dados_forecast['unique_id'] = 'Preco'
dados_forecast.dropna(inplace=True)

# Define os dados de treinamento
dados_treinamento = dados_forecast.loc[dados_forecast['ds'] >= '2000-01-01']
horizonte_previsao = 5

# Implementação do modelo ARIMA
modelo_arima = StatsForecast(models=[AutoARIMA(season_length=5)], freq='B', n_jobs=-1)
modelo_arima.fit(dados_treinamento)
previsao = modelo_arima.predict(h=horizonte_previsao, level=[90])
previsao = previsao[['ds', 'AutoARIMA']].reset_index(drop=True).rename(columns={'ds': 'data', 'AutoARIMA': 'preco_previsto'})
previsao['preco_previsto'] = [int(n * 100) / 100 for n in previsao['preco_previsto']]
previsao = previsao.sort_values('data', ascending=False)

# Salvando as previsões no arquivo CSV
caminho_previsao = 'dados/last_forecast.csv'
previsao.to_csv(caminho_previsao, index=False)
