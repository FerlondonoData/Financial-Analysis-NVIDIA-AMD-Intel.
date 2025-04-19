import pandas as pd

# Leer el archivo original
archivo_original = 'analisis_financiero_nvidia_vs_comp.xlsx'
excel_data = pd.read_excel(archivo_original, sheet_name=None)

# Nuevo diccionario para guardar los datos limpios
datos_limpios = {}

# Limpiar hoja de ratios clave
ratios_df = excel_data['Ratios_Claves'].copy()

# Eliminar filas con valores nulos en los ratios importantes
ratios_df.dropna(subset=[
    'P/E', 'P/S', 'ROE', 'Deuda/Patrimonio',
    'Margen Neto', 'Flujo de Caja Libre', 'Crecimiento Ingresos (5y)'
], inplace=True)

# Guardar en el diccionario limpio
datos_limpios['Ratios_Claves'] = ratios_df

# Limpiar las hojas históricas (precios)
for hoja in excel_data:
    if hoja.endswith('_hist'):
        df = excel_data[hoja].dropna()
        datos_limpios[hoja] = df

# Las otras hojas las dejamos igual (puedes limpiarlas si es necesario)
for hoja in excel_data:
    if hoja not in datos_limpios:
        datos_limpios[hoja] = excel_data[hoja]

# Guardar todo en un nuevo archivo limpio
archivo_limpio = 'analisis_financiero_nvidia_vs_comp_limpio.xlsx'
with pd.ExcelWriter(archivo_limpio) as writer:
    for nombre_hoja, df in datos_limpios.items():
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)

print(f"✔ Datos limpios guardados como '{archivo_limpio}'")
