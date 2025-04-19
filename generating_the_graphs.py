import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Función para agregar el logo a cada gráfico
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

# Estilo de los gráficos
sns.set(style="whitegrid")  # Corregí el paréntesis que te faltaba

# Gráfico 1: P/E Ratio
plt.figure(figsize=(8, 5))
ax1 = sns.barplot(data=ratios_df, x='Ticker', y='P/E', palette='Blues_d')
plt.title('Comparación del P/E Ratio')
plt.ylabel('P/E Ratio')
plt.xlabel('')
plt.axhline(y=20, color='red', linestyle='--', label='Límite saludable (~20)')
plt.legend()
agregar_logo(ax1, ruta_logo)
plt.tight_layout()

# Gráfico 2: ROE (Return on Equity)
plt.figure(figsize=(8, 5))
ax2 = sns.barplot(data=ratios_df, x='Ticker', y='ROE', palette='Greens_d')
plt.title('Comparación de ROE (Return on Equity)')
plt.ylabel('ROE')
plt.xlabel('')
plt.axhline(y=0.15, color='orange', linestyle='--', label='Buen nivel > 15%')
plt.legend()
agregar_logo(ax2, ruta_logo)
plt.tight_layout()

# Gráfico 3: P/S Ratio
plt.figure(figsize=(8, 5))
ax3 = sns.barplot(data=ratios_df, x='Ticker', y='P/S', palette='Purples_d')
plt.title('Comparación de P/S (Price to Sales)')
plt.ylabel('P/S')
plt.xlabel('')
plt.axhline(y=5, color='gray', linestyle='--', label='Promedio industria ~5')
plt.legend()
agregar_logo(ax3, ruta_logo)
plt.tight_layout()

# Mostrar todos los gráficos juntos
plt.show()
