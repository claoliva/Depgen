import streamlit as st
import pandas as pd
import requests as rq
url= 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
response=rq.get(url).json()
response.keys()
dfMulheres=pd.DataFrame(response['dados'])
dfMulheres['sexo']='F'
url= 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
dfHomens=pd.DataFrame()
response=rq.get(url).json()
dfHomens=pd.DataFrame(response['dados'])
dfHomens['sexo']='M'
dftotal=pd.concat([dfMulheres, dfHomens], axis='index')
opcao=st.selectbox('Qual o sexo?', df['sexo'].unique())
dfFiltrado=df[df['sexo']==opcao]
st.title('Deputados do sexo' + opcao)
ocorrencias=dfFiltrado['siglaUf'].value_counts()
dfEstados=pd.DataFrame({'siglaUf': ocorrencias.index, 'quantidade': ocorrencias.values})
totalHomens=dfHomens['nome'].count()
st.metric('Total de homens', totalHomens)
totalMulheres=dfMulheres['nome'].count()
st.metric('Total de mulheres', totalMulheres)
st.bar_chart(dfEstados, x='siglaUf', y='quantidade', x_label='Siglas dos Estados', y_label='Quantidade de Deputados')
st.dataframe(dfFiltrado)
