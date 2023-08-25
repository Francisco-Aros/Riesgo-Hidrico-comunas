import geopandas as gpd
import folium
from folium import CustomIcon
from streamlit_folium import folium_static
import streamlit as st
from streamlit.components.v1 import html



st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

# Crea dos columnas en el sidebar
col1, col2 = st.sidebar.columns([1, 7])

css = '''
<style>
    [data-testid='stSidebarNav'] > ul {
        min-height: 54vh;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

st.title("Presentación web")

st.info(
    "La siguiente web presenta un total de 5 pestañas adicionales a ésta, en las cuales se pueden apreciar a través de diversos visualizadores web la situación actualizada de cada comuna que compone la Asociación Paisajes de Conservación para la Biodiversidad de la Región de Los Ríos."
)


st.write("Los invitamos a recorrer cada una de las pestañas de cada comuna y finalmente una última pestaña referente al Territorio de acción correspondiente a la asociación. ")

def main():
    # Estilo CSS para anclar en la parte inferior
    st.markdown(    
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #000000;
            padding: 2px;
            text-align: center;
        }
        .footer p {
            font-size: 12px; /* Ajusta el tamaño de la letra */
            line-height: 1.2; /* Ajusta el espacio entre líneas */
            margin: 0; /* Elimina el margen alrededor del párrafo */
            color: #ffffff; /* Cambia el color del texto a blanco */
        }
        .footer a {
            font-size: 15px; /* Ajusta el tamaño del hipervínculo */
            color: #1443E4; /* Cambia el color del hipervínculo a blanco */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Agrega una división con la clase 'footer'
    st.markdown(
        """
        <div class="footer">
            <p>Web diseñada y desarrollada por Francisco Javier Aros Muñoz. Geógrafo - Mg. en Planificación y Gestión Territorial</p>
            <a href="mailto:franciscoarosmunoz@gmail.com">franciscoarosmunoz@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()