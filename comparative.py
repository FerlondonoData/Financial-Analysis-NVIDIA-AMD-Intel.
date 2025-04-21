import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Función para agregar el logo
def agregar_logo(ax, path_logo, zoom=0.15, xy=(0.9, 0.9)):
    logo_img = plt.imread(path_logo)
    imagebox = OffsetImage(logo_img, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, xycoords='axes fraction', frameon=False)
    ax.add_artist(ab)

# Ruta absoluta del logo
ruta_logo = '/Users/festroot/Downloads/logo.jpeg'

# Leer el archivo Excel
archivo = 'analisis_financiero_nvidia_vs_comp_limpio.xlsx'
ratios_df = pd.read_excel(archivo, sheet_name='Ratios_Claves')

# Filtrar únicamente las columnas necesarias para el gráfico comparativo de P/S
df_ps = ratios_df[['Ticker', 'P/S']].dropna(subset=['P/S'])

# Verificar que las tres empresas están presentes
print(df_ps)

# Estilo
sns.set(style="whitegrid")

# Gráfico comparativo de P/S Ratio para las tres empresas
plt.figure(figsize=(8, 5))
ax = sns.barplot(data=df_ps, x='Ticker', y='P/S', palette='Purples_d')

# Título y etiquetas
plt.title('Comparación de P/S Ratio (Price to Sales)')
plt.ylabel('P/S')
plt.xlabel('')

# Línea de referencia (promedio de la industria)
plt.axhline(5, color='gray', linestyle='--', label='Promedio industria (~5)')

# Mostrar la leyenda
plt.legend()

# Agregar logo
agregar_logo(ax, ruta_logo)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()
