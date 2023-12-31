import geopandas as gpd
import folium
from folium import CustomIcon
from streamlit_folium import folium_static
import streamlit as st
from streamlit.components.v1 import html



st.sidebar.write("En la comuna de Valdivia existen 17 localidades que reciben ayuda de agua potable en caminones aljibes a través del municipio, entregandose un total de 133.200 litros")
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

st.title("Ejemplo de capas de información en visualizador web")

st.info(
    "En el siguiente mapa cuenta con un selector de capas para poder activar/desactivar las que desee. En este ejemplo se cuenta con los sectores de la comuna de Valdivia y en cuales de ellos existe entrega de agua potable a través de camiones aljibes, ya sean estos por parte de un camión municipal o de la gobernación regional."
)

@st.cache_data()
def get_data():
    # Cargar el archivo SHP en un objeto GeoDataFrame
    shp_path = "Localidades_Valdivia_CamionesAljibe.shp"
    gdf = gpd.read_file(shp_path)
    # Cargar el segundo archivo SHP en otro objeto GeoDataFrame
    shp2_path = "APRValdivia.shp"
    gdf_points = gpd.read_file(shp2_path)  # Corregir nombre de la variable
    #cargar tercer sho
    shp3_path = "Derechos_comuna_Valdivia.shp"
    gdf_points2 = gpd.read_file(shp3_path)
    return gdf, gdf_points, gdf_points2  # Corregir nombre de la variable


# Obtener los datos de los polígonos y puntos
gdf, gdf_points, gdf_points2 = get_data()  # Corregir nombre de la variable

unique_values = gdf['Fam_afecta'].unique()
print(unique_values)

# Crear un objeto Folium Map centrado en los datos de los polígonos
m = folium.Map(location=[-39.85, -73.06], zoom_start=10, tiles='Stamen Terrain')

# Definir la paleta de colores para asignar un color único a cada valor único en 'Fam_afecta'
color_palette = {
    1.0: '#ffb4b4', #rosado
    2.0: '#ffa5a5',   
    3.0: '#ff9696',   
    5.0: '#ff8787',   
    4.0: '#ff7878',  
    7.0: '#ff6969',   
    6.0: '#ff5a5a',  
    13.0: '#ff4b4b',
    10.0: '#ff3c3c',
    12.0: '#ff2d2d', 
    14.0: '#ff1e1e', 
    42.0: '#ff0f0f', 
    32.0: '#ff0000',  # Rojo muy intenso
}

# Función para asignar colores diferentes a cada atributo
def style_function(feature):
    attribute = feature['properties']['Fam_afecta']
    return {'fillColor': color_palette.get(attribute, '#808081'), 'fillOpacity': 0.7, 'color': 'none'}

# Obtener los datos de los polígonos y puntos
gdf, gdf_points, gdf_points2 = get_data()

# Crear un objeto FeatureGroup de Folium para los polígonos
#poligonos_group = folium.FeatureGroup(name='Zonas de entrega de agua potable mediante camiones aljibes')
folium.GeoJson(gdf,
               tooltip=folium.GeoJsonTooltip(fields=['NOM_LOCALI', 'Fam_afecta', 'Lt_entrega'], aliases=['Nombre de localidad', 'Familias Personas afectadas','Litros entregados']),
               style_function=style_function,
               name='Zonas de entrega de agua potable mediante camiones aljibes',
               show= True
               ).add_to(m)

# Crear un objeto FeatureGroup de Folium para los puntos
#puntos_group = folium.FeatureGroup(name='APR Los Lagos')
folium.GeoJson(gdf_points,
               tooltip=folium.GeoJsonTooltip(fields=['Nombre__of', 'Beneficiar'], aliases=['Nombre', 'Beneficiarios']),
               name='APR Valdivia',
               show= False
               ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
folium.GeoJson(gdf_points2,
               tooltip=folium.GeoJsonTooltip(fields=['TipoDerech', 'Naturaleza', 'UsodelAgua', 'Clasificac'], aliases=['Tipo de derecho', 'Naturaleza de derecho', 'Uso del agua', 'Clasificación']),
               name= 'Derechos de aprovechamiento de aguas, comuna de Valdivia',
               show= False
               ).add_to(m)




# Agregar los FeatureGroup al mapa
#m.add_child(poligonos_group)
#m.add_child(puntos_group)

# Crear el control de capas agrupadas

control = folium.LayerControl()

control.add_to(m)

# Mostrar el mapa en Streamlit utilizando folium_static
folium_static(m, width=700, height=450)


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
            <p>Web diseñada y desarrollada por Francisco Javier Aros Muñoz.. Geógrafo - Mg. en Planificación y Gestión Territorial</p>
            <a href="mailto:franciscoarosmunoz@gmail.com">franciscoarosmunoz@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
