# Ignorar advertencias del módulo urllib3 por compatibilidad con OpenSSL
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

# ─── Imports del script original ───
import yfinance as yf
import pandas as pd

# Lista de compañías para analizar
tickers = ['NVDA', 'AMD', 'INTC']

# Diccionario para guardar la info
data = {}

for ticker in tickers:
    stock = yf.Ticker(ticker)
    
    data[ticker] = {
        'info': stock.info,
        'financials': stock.financials,
        'balance_sheet': stock.balance_sheet,
        'cashflow': stock.cashflow,
        'history': stock.history(period='1y'),
        'quarterly_financials': stock.quarterly_financials,
        'sustainability': stock.sustainability,
    }

# Convertir ratios importantes a tabla
summary = []

for ticker in tickers:
    info = data[ticker]['info']
    summary.append({
        'Ticker': ticker,
        'P/E': info.get('trailingPE'),
        'P/S': info.get('priceToSalesTrailing12Months'),
        'ROE': info.get('returnOnEquity'),
        'Deuda/Patrimonio': info.get('debtToEquity'),
        'Margen Neto': info.get('netMargins'),
        'Flujo de Caja Libre': info.get('freeCashflow'),
        'Crecimiento Ingresos (5y)': info.get('revenueGrowth'),
    })

ratios_df = pd.DataFrame(summary)
print(ratios_df)

# Guardar todo a Excel (compatible con Google Sheets)
with pd.ExcelWriter('analisis_financiero_nvidia_vs_comp.xlsx') as writer:
    for ticker in tickers:
        data[ticker]['financials'].to_excel(writer, sheet_name=f'{ticker}_fin')
        data[ticker]['balance_sheet'].to_excel(writer, sheet_name=f'{ticker}_bs')
        data[ticker]['cashflow'].to_excel(writer, sheet_name=f'{ticker}_cf')

        # Quitar zona horaria para evitar error con Excel
        hist_df = data[ticker]['history'].copy()
        hist_df.index = hist_df.index.tz_localize(None)
        hist_df.to_excel(writer, sheet_name=f'{ticker}_hist')

    # Ratios principales
    ratios_df.to_excel(writer, sheet_name='Ratios_Claves', index=False)

