# Financial Analysis of NVIDIA, AMD, and Intel

This repository contains a detailed financial analysis of three major tech companies: NVIDIA, AMD, and Intel. The analysis includes downloading financial data, processing it, and generating visual comparisons using key financial ratios like P/E, ROE, and P/S. Additionally, it compares their stock performance over the past year.

## Key Questions Answered

1. **Is NVIDIA overvalued?**
   - We analyze NVIDIA's current valuation using financial ratios and compare it to its competitors (AMD and Intel).
   
2. **Is it a good idea to invest in NVIDIA now, or should you wait?**
   - The analysis provides insights into NVIDIA's financial position and growth potential, helping you decide if it's an attractive investment.
   
3. **How does NVIDIA compare with AMD and Intel?**
   - A comparative analysis is conducted based on the following financial ratios:
     - **P/E (Price-to-Earnings) Ratio**
     - **ROE (Return on Equity)**
     - **P/S (Price-to-Sales) Ratio**
     - Other financial metrics like debt-to-equity and net margins are also analyzed.

## Files Included

1. **`descargar_datos.py`**: Downloads the financial data of NVIDIA, AMD, and Intel from Yahoo Finance using `yfinance`.
2. **`limpiar_datos.py`**: Cleans the downloaded financial data and prepares it for analysis.
3. **`graficas.py`**: Generates visualizations (bar charts) comparing the key financial ratios of the companies and includes their logos in the graphs.
4. **`analisis_financiero_nvidia_vs_comp.xlsx`**: Excel file containing the raw and cleaned data of the financial analysis.
5. **`analisis_financiero_nvidia_vs_comp_limpio.xlsx`**: Cleaned Excel file for analysis, with unnecessary data removed.

## How to Run the Code

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Financial-Analysis-NVIDIA-AMD-Intel.git
