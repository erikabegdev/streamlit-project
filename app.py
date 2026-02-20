import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de Anúncios de Carros")

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando histograma da quilometragem')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando gráfico de dispersão preço vs quilometragem')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
