import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('E:\\Visual\\Jupyter\\Sprint 5\\Proyecto final\\Final-proyect-5\\vehicles_us.csv')
hist_button = st.button('Construir histograma') # crear un botón
graph_button = st.button('Construir gráfico de dispersión') # crear un botón

#Button 1
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#Button 2
if graph_button: #al hacer click en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    #crear el gráfico
    fig = px.scatter(car_data, x="odometer", y="price")

    #mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

#Checkbox 1
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    
    # escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')
     # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#Checkbox 2
build_histogram = st.checkbox('Construir un gráfico')

if build_histogram: # si la casilla de verificación está seleccionada
    
    # escribir un mensaje
    st.write('Construir un gráfico para la columna odómetro')
    
    #crear el gráfico
    fig = px.scatter(car_data, x="odometer", y="price")

    #mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)
    