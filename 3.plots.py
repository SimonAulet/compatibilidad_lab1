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
# Ploteo todas las señales
#
# %%
import matplotlib.pyplot as plt
import pandas as pd

# %%
# Cargar el archivo CSV
x1 = pd.read_csv('signals/ramp_symm_50_M.csv')

# Mostrar las primeras filas para verificar
print("Primeras filas del archivo:")
print(x1.head())
print("\nInformación del DataFrame:")
print(x1.info())

# %%
plt.figure(figsize=(24, 16))
plt.plot(x1['Frequency_MHz'], x1['Amplitude_dBm'], 'b-', linewidth=1.5)
plt.title('Espectro rampa con simetría del 50%', fontsize=24)
plt.xlabel('Frecuencia (MHz)', fontsize=20)
plt.ylabel('Amplitud (dBm)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Añadir anotaciones para puntos importantes
# Encontrar el valor máximo
max_idx = x1['Amplitude_dBm'].idxmax()
max_freq = x1.loc[max_idx, 'Frequency_MHz']
max_amp = x1.loc[max_idx, 'Amplitude_dBm']
max_idx2 = int(x1['Amplitude_dBm'][int(max_idx)+1 : ].idxmax()) # type: ignore
max_freq2 = x1.loc[max_idx2, 'Frequency_MHz']
max_amp2 = x1.loc[max_idx2, 'Amplitude_dBm']
max_idx3 = int(x1['Amplitude_dBm'][int(max_idx2)+1 : ].idxmax()) # type: ignore
max_freq3 = x1.loc[max_idx3, 'Frequency_MHz']
max_amp3 = x1.loc[max_idx3, 'Amplitude_dBm']

plt.annotate(f'Máximo 1: {max_amp:.2f} dBm\n@ {max_freq:.3f} MHz',
             xy=(max_freq, max_amp),
             xytext=(max_freq + 20, max_amp),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 2: {max_amp2:.2f} dBm\n@ {max_freq2:.3f} MHz',
             xy=(max_freq2, max_amp2),
             xytext=(max_freq2 + 20, max_amp2 + 5),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 3: {max_amp3:.2f} dBm\n@ {max_freq3:.3f} MHz',
             xy=(max_freq3, max_amp3),
             xytext=(max_freq3 + 20, max_amp3 + 5),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.savefig('plots/ramp_symm_50_M_plot.png')
plt.show()


# %%
