import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")  # leer los datos
st.header('Visualizaciones de performance de anuncios de venta de coches')

build_graph = st.checkbox('Construir un gráfico de barras')
hist_button = st.button('Construir histograma') 
disp_button = st.button('Construir gráfico de dispersión')# crear un botón

if build_graph:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de barras para el conjunto de datos por cantidad de tipo de vehiculo')

    # crear un histograma
    type_counts = car_data['type'].value_counts().reset_index()
    type_counts.columns = ['type', 'count']

    fig = px.bar(type_counts, 
             x='count', 
             y='type', 
             orientation='h', 
             title='Número de Vehículos por Tipo',
             color='count',  # Colorear las barras según la cantidad
             color_continuous_scale=px.colors.sequential.Plasma)
    fig.update_layout(
        xaxis_title='Cantidad de Vehículos',
        yaxis_title='Tipo de Vehículo',
        title_font=dict(size=20),
        xaxis=dict(showgrid=True, gridcolor='LightGray'),
        yaxis=dict(showgrid=True, gridcolor='LightGray')
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)   
    
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
   

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
