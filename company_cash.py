import yfinance as yf
import pandas as pd

# Definir las empresas a analizar
companies = ['NVDA', 'AMD', 'INTC']

# Crear diccionario para almacenar los datos
income_data = {}
fcf_data = {}

# Recuperar datos de las tres empresas
for ticker in companies:
    # Obtener los datos financieros de la empresa
    company = yf.Ticker(ticker)

    # Datos de ingresos
    income_statement = company.financials.T  # Transponer para que las fechas estén como índices
    income_data[ticker] = income_statement['Total Revenue']  # Recuperamos los ingresos

    # Datos de flujo de caja libre (Free Cash Flow)
    cashflow_statement = company.cashflow.T  # Transponer para que las fechas estén como índices
    # Verificamos si la columna 'Free Cash Flow' existe en los datos
    if 'Free Cash Flow' in cashflow_statement.columns:
        fcf_data[ticker] = cashflow_statement['Free Cash Flow']
    else:
        fcf_data[ticker] = pd.Series([None] * len(income_statement))  # Si no existe, colocar None

# Crear DataFrame de ingresos
income_df = pd.DataFrame(income_data)

# Crear DataFrame de Free Cash Flow
fcf_df = pd.DataFrame(fcf_data)

# Mostrar los DataFrames resultantes
print("Income (Revenues) Data:")
print(income_df)

print("\nFree Cash Flow Data:")
print(fcf_df)

# Guardar los datos en un archivo Excel para revisar mejor
income_df.to_excel("income_data.xlsx")
fcf_df.to_excel("fcf_data.xlsx")
