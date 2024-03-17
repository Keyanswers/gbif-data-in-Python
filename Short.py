# Import libraries
# Importar bibliotecas
import numpy as np  # Para operaciones numéricas
import pandas as pd  # Para trabajar con datos tabulares
import geopandas as gpd  # Para trabajar con datos geoespaciales
import matplotlib.pyplot as plt  # Para trazar gráficos

# Import function from pygbif
# Importar función de pygbif
from pygbif import occurrences

# Define species name
# Definir nombre de la especie
sp = 'Neosmilaster georgianus'

# Search occurrences for the species
# Buscar ocurrencias de la especie
ngd = occurrences.search(scientificName=sp, limit=500)

# Normalize the JSON data and create a DataFrame
# Normalizar los datos JSON y crear un DataFrame
ngdDF = pd.json_normalize(ngd['results'])

# Select specific columns
# Seleccionar columnas específicas
cols = ['decimalLongitude', 'decimalLatitude', 'occurrenceStatus', 'datasetName', 'individualCount']
ngdDF2 = ngdDF[cols]

# Drop missing values
# Eliminar valores faltantes
ngdDF2 = ngdDF2.dropna()

# Load natural earth data
# Cargar datos de naturalearth
nl = gpd.read_file(
    gpd.datasets.get_path(
        'naturalearth_lowres'
    )
)

# Create subplot and plot the natural earth data
# Crear un subplot y trazar los datos de naturalearth
fig, ax = plt.subplots(figsize=(4, 3))
nl.plot(ax=ax, color='lightgray', edgecolor='black')

# Set axis limits
# Establecer límites de los ejes
ax.set_xlim([-66, 39])
ax.set_ylim([-68, 0.5])

# Extract coordinates for scatter plot
# Extraer coordenadas para el gráfico de dispersión
XX = ngdDF2['decimalLongitude']
YY = ngdDF2['decimalLatitude']

# Scatter plot of occurrences
# Gráfico de dispersión de las ocurrencias
plt.scatter(x=XX, y=YY, color='black', s=50)

# Add legend
# Agregar leyenda
plt.legend(['individualCount'], loc='lower right', bbox_to_anchor=(1, 0))

# Set axis labels and ticks
# Establecer etiquetas y marcas de los ejes
ax.set_xlabel('Longitude', color='black', size=15)
ax.set_ylabel('Latitude', color='black', size=15)
ax.tick_params(axis='x', color='black', labelsize=15)
ax.tick_params(axis='y', color='black', labelsize=15)

# Import necessary function from matplotlib
# Importar la función necesaria de matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Create subplot and plot natural earth data again
# Crear un subplot y trazar los datos de naturalearth nuevamente
fig, ax = plt.subplots(figsize=(4, 3))
nl.plot(ax=ax, color='lightgray', edgecolor='black')

# Set axis limits
# Establecer límites de los ejes
ax.set_xlim([-66, 39])
ax.set_ylim([-68, 0.5])

# Extract coordinates for scatter plot
# Extraer coordenadas para el gráfico de dispersión
XX = ngdDF2['decimalLongitude']
YY = ngdDF2['decimalLatitude']

# Scatter plot of occurrences with color and size based on individualCount
# Gráfico de dispersión de las ocurrencias con color y tamaño basados en individualCount
sca = ax.scatter(x=XX, y=YY, c=ngdDF2['individualCount'], s=50, cmap='RdYlBu_r', alpha=0.5)

# Add colorbar
# Agregar barra de color
Div = make_axes_locatable(ax)
cax = Div.append_axes('right', size='5%', pad=0.1)
plt.colorbar(sca, cax=cax)

# Set axis labels and ticks
# Establecer etiquetas y marcas de los ejes
ax.set_xlabel('Longitude', color='black', size=15)
ax.set_ylabel('Latitude', color='black', size=15)
ax.tick_params(axis='x', color='black', labelsize=15)
ax.tick_params(axis='y', color='black', labelsize=15)
