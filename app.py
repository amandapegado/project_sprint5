import streamlit as st
import pandas as pd
import plotly.express as px

# Cabeçalho da Aplicação
st.header('Vendas de Carros')

# Lendo os dados
car_data = pd.read_csv('vehicles.csv')

# Criar botão
hist_button = st.button('Criar histograma', key='hist_button')

scatter_button = st.button('Criar gráfico de dispersão', key='scatter_button')

# Ação ao clicar no botão de histograma
if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


# Ação ao clicar no botão de gráfico de dispersão
if scatter_button:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Dispersão de Preço vs Odômetro")
    st.plotly_chart(fig, use_container_width=True)

# Criar caixas de seleção
hist_checkbox = st.checkbox('Criar histograma', key='hist_checkbox')
scatter_checkbox = st.checkbox(
    'Criar gráfico de dispersão', key='scatter_checkbox')

# Ação ao selecionar a caixa de seleção do histograma
if hist_checkbox:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Ação ao selecionar a caixa de seleção do gráfico de dispersão
if scatter_checkbox:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Dispersão de Preço vs Odômetro")
    st.plotly_chart(fig, use_container_width=True)