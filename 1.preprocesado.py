# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Pre-procesamiento
# Extracción y procesamiento de señales del laboratorio del 28/03/2026 generadas en el osciloscopio Rigol. La correspondiencia de cada archivo con su configuración es la siguiente:
#

# %% [markdown]
#  Archivo | Señal         | Config
# ---------|---------------|---------------------
#  11.csv  | Onda cuadrada | 25 MHz
#  2.csv   | Sinsoidal     | 25MHz
#  3.csv   | Sinusoidal    | 25MHz, span 0->1GHz
#  4.csv   | Sinusoidal    | 5MHz
#  5.csv   | Rampa         | 5MHz, simetría 100%
#  6.csv   | Rampa         | 5MHz, simetría 50%
#

# %% [markdown]
# Inicialmente importo y pruebo uno a ver cómo queda

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Process 11.csv
filename = "mediciones/3.csv"
output_name = "processed_11.csv"  # Change this name as needed

# Read CSV, skip first 2 rows (headers)
data = pd.read_csv(filename, skiprows=2, header=None)

# Extract frequency (col 0) and amplitude (col 2)
freq_hz = data.iloc[:, 0].values.astype(float)
amp_dbm = data.iloc[:, 2].values.astype(float)

# Convert frequency to GHz
freq_ghz = freq_hz / 1e6

# Create numpy array with two columns
processed_data = np.column_stack((freq_ghz, amp_dbm))

# %%
# Plot
plt.figure(figsize=(10, 6))
plt.plot(freq_ghz, amp_dbm)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Amplitude (dBm)')
plt.title('Frequency Spectrum')
plt.grid(True)
plt.show()

# %%
# Save to CSV
np.savetxt(output_name, processed_data, delimiter=',', header='Frequency_GHz,Amplitude_dBm', comments='')
print(f"Data saved to {output_name}")

# %% [markdown]
# Perect, vamos con todo segun la tabla

# %%
mediciones = ['11.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv']
salida = ['cuadrada_25MHz.csv', 'sin_25MHz.csv', 'sin_25MHz_span_0-1GHz.csv', 'sin_5MHz.csv', 'ramp_symm_100.csv', 'ramp_symm_50.csv']

# Process all files
for input_file, output_file in zip(mediciones, salida):
    # Read CSV, skip first 2 rows (headers)
    data = pd.read_csv(f"mediciones/{input_file}", skiprows=2, header=None)
    freq_hz = data.iloc[:, 0].values.astype(float)
    amp_dbm = data.iloc[:, 2].values.astype(float)
    freq_ghz = freq_hz / 1e6
    processed_data = np.column_stack((freq_ghz, amp_dbm))
    np.savetxt(output_file, processed_data, delimiter=',', header='Frequency_GHz,Amplitude_dBm', comments='')
    print(f"Processed {input_file} -> {output_file}")
