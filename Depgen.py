import requests as req
import pandas as pd
import streamlit as st
urlMulheres = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome"
resposta = req.get(urlMulheres)
dadosJSON = resposta.json()
dfMulheres = pd.DataFrame(dadosJSON['dados'])
dfMulheres['sexo'] = 'F'
urlHomens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta = req.get(urlHomens)
dadosJSON = resposta.json()
dfHomens = pd.DataFrame(dadosJSON['dados'])
dfHomens['sexo'] = 'M'
df = pd.concat([dfMulheres, dfHomens])

opcao = st.selectbox(
    'Qual o sexo?',
    df['sexo'].unique()
)
dfFiltrado = df[df['sexo'] == opcao]
st.title('Deputados do sexo' + opcao)

ocorrencias = dfFiltrado['siglaUf'].value_counts()
dfEstados = pd.DataFrame({
    'siglaUf':ocorrencias.index,
    'quantidade':ocorrencias.values}
)

totalHomens = dfHomens['id'].count()
st.metric('Total de homens', totalHomens)
totalMulheres = dfMulheres['id'].count()
st.metric('Total de mulheres', totalMulheres)
st.bar_chart(dfEstados,
            x = 'siglaUf',
            y = 'quantidade',
            x_label = 'Siglas dos estados',
            y_label = 'Quantidade de deputados'
      )
st.dataframe(dfFiltrado)
