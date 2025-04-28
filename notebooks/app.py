import pandas as pd
import streamlit as st
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    st.header ('Histograma de odómetro')

if st.button('Creación de un Gráfico de Dispersión'):
    st.write('Precio vs Año')
    fig2 = px.scatter(car_data, x="model_year", y="price", title="Precio según Año del Modelo")
    st.plotly_chart(fig2)