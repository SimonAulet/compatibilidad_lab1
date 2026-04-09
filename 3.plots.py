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
x2 = pd.read_csv('signals/ramp_symm_100_M.csv')
x3 = pd.read_csv('signals/sin_5MHz_M.csv')
x4 = pd.read_csv('signals/sin_25MHz_M.csv')
x5 = pd.read_csv('signals/square_25MHz_span_0-1GHz_M.csv')
x6 = pd.read_csv('signals/square_25MHz_M.csv')

# %% [markdown]
# Ploteo de rampa con simetría del 50%. Se marcan los tres primeros picos

# %% jupyter={"source_hidden": true}
plt.figure(figsize=(24, 16))
plt.plot(x1['Frequency_MHz'], x1['Amplitude_dBm'], 'b-', linewidth=1.5)
plt.title('Espectro rampa con simetría del 50%', fontsize=24)
plt.xlabel('Frecuencia (MHz)', fontsize=20)
plt.ylabel('Amplitud (dBm)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()

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
plt.savefig('plots/ramp_symm_50_M.png')
plt.show()


# %% [markdown]
# Ploteo de rampa con simetría del 100%. Se marcan los tres primeros picos y la línea donde cae -20 dBm

# %% jupyter={"source_hidden": true}
plt.figure(figsize=(24, 16))
plt.plot(x2['Frequency_MHz'], x2['Amplitude_dBm'], 'b-', linewidth=1.5)
plt.title('Espectro rampa con simetría del 100%', fontsize=24)
plt.xlabel('Frecuencia (MHz)', fontsize=20)
plt.ylabel('Amplitud (dBm)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()

max_idx = x2['Amplitude_dBm'].idxmax()
max_freq = x2.loc[max_idx, 'Frequency_MHz']
max_amp = x2.loc[max_idx, 'Amplitude_dBm']
max_idx2 = int(x2['Amplitude_dBm'][int(max_idx)+1 : ].idxmax()) # type: ignore
max_freq2 = x2.loc[max_idx2, 'Frequency_MHz']
max_amp2 = x2.loc[max_idx2, 'Amplitude_dBm']
max_idx3 = int(x2['Amplitude_dBm'][int(max_idx2)+1 : ].idxmax()) # type: ignore
max_freq3 = x2.loc[max_idx3, 'Frequency_MHz']
max_amp3 = x2.loc[max_idx3, 'Amplitude_dBm']

plt.annotate(f'Máximo 1: {max_amp:.2f} dBm\n@ {max_freq:.3f} MHz',
             xy=(max_freq, max_amp),
             xytext=(max_freq+10, max_amp+0.2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 2: {max_amp2:.2f} dBm\n@ {max_freq2:.3f} MHz',
             xy=(max_freq2, max_amp2),
             xytext=(max_freq2+35, max_amp2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 3: {max_amp3:.2f} dBm\n@ {max_freq3:.3f} MHz',
             xy=(max_freq3, max_amp3),
             xytext=(max_freq3 + 55, max_amp3-1),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.hlines(-20, 0, 200, 'black')
plt.annotate('Corte de -20 dBm',
             xy=(max_freq3, max_amp3),
             xytext=(80, -19),
             fontsize=20)
plt.savefig('plots/ramp_symm_100_M.png')
plt.show()

# %% [markdown]
# Ploteo de seno generado a 5 MHz con línea de corte a -20 dBm y tres primeros máximos

# %% jupyter={"source_hidden": true}
plt.figure(figsize=(24, 16))
plt.plot(x3['Frequency_MHz'], x3['Amplitude_dBm'], 'b-', linewidth=1.5)
plt.title('Espectro seno con frecuencia de 5MHz', fontsize=24)
plt.xlabel('Frecuencia (MHz)', fontsize=20)
plt.ylabel('Amplitud (dBm)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()

max_idx = x3['Amplitude_dBm'].idxmax()
max_freq = x3.loc[max_idx, 'Frequency_MHz']
max_amp = x3.loc[max_idx, 'Amplitude_dBm']
max_idx2 = int(x3['Amplitude_dBm'][int(max_idx)+1 : ].idxmax()) # type: ignore
max_freq2 = x3.loc[max_idx2, 'Frequency_MHz']
max_amp2 = x3.loc[max_idx2, 'Amplitude_dBm']
max_idx3 = int(x3['Amplitude_dBm'][int(max_idx2)+1 : ].idxmax()) # type: ignore
max_freq3 = x3.loc[max_idx3, 'Frequency_MHz']
max_amp3 = x3.loc[max_idx3, 'Amplitude_dBm']

plt.annotate(f'Máximo 1: {max_amp:.2f} dBm\n@ {max_freq:.3f} MHz',
             xy=(max_freq, max_amp),
             xytext=(max_freq+10, max_amp+0.2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 2: {max_amp2:.2f} dBm\n@ {max_freq2:.3f} MHz',
             xy=(max_freq2, max_amp2),
             xytext=(max_freq2+35, max_amp2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 3: {max_amp3:.2f} dBm\n@ {max_freq3:.3f} MHz',
             xy=(max_freq3, max_amp3),
             xytext=(max_freq3 + 55, max_amp3-1),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.hlines(-20, 0, 200, 'black')
plt.annotate('Corte de -20 dBm',
             xy=(max_freq3, max_amp3),
             xytext=(80, -19),
             fontsize=20)
plt.savefig('plots/sin_5MHz.png')
plt.show()

# %% [markdown]
# Ploteo de seno generado a 25 MHz con línea de corte a -20 y el span de $0$ a $200 \text{MHz}$

# %%
plt.figure(figsize=(24, 16))
plt.plot(x4['Frequency_MHz'], x4['Amplitude_dBm'], 'b-', linewidth=1.5)
plt.title('Espectro seno con frecuencia de 25MHz y un span de 0-200 MHz', fontsize=24)
plt.xlabel('Frecuencia (MHz)', fontsize=20)
plt.ylabel('Amplitud (dBm)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()

max_idx = x4['Amplitude_dBm'].idxmax()
max_freq = x4.loc[max_idx, 'Frequency_MHz']
max_amp = x4.loc[max_idx, 'Amplitude_dBm']
max_idx2 = int(x4['Amplitude_dBm'][int(max_idx)+1 : ].idxmax()) # type: ignore
max_freq2 = x4.loc[max_idx2, 'Frequency_MHz']
max_amp2 = x4.loc[max_idx2, 'Amplitude_dBm']
max_idx3 = int(x4['Amplitude_dBm'][int(max_idx2)+1 : ].idxmax()) # type: ignore
max_freq3 = x4.loc[max_idx3, 'Frequency_MHz']
max_amp3 = x4.loc[max_idx3, 'Amplitude_dBm']

plt.annotate(f'Máximo: {max_amp:.2f} dBm\n@ {max_freq:.3f} MHz',
             xy=(max_freq, max_amp),
             xytext=(max_freq+10, max_amp-8.2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 2: {max_amp2:.2f} dBm\n@ {max_freq2:.3f} MHz',
             xy=(max_freq2, max_amp2),
             xytext=(max_freq2+10, max_amp2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 3: {max_amp3:.2f} dBm\n@ {max_freq3:.3f} MHz',
             xy=(max_freq3, max_amp3),
             xytext=(max_freq3 + 10, max_amp3+1),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.hlines(-20, 0, 200, 'black')
plt.annotate('Corte de -20 dBm',
             xy=(max_freq, max_amp),
             xytext=(80, -19),
             fontsize=20)
plt.savefig('plots/sin_25MHz.png')
plt.show()

# %% [markdown]
# Ploteo de seno generado a 25 MHz con línea de corte a -20 y el span de $0$ a $1 \text{GHz}$ recortado para mostrar hasta 200MHz

# %% jupyter={"source_hidden": true}
#x5 = x5[x5['Frequency_MHz'] <= 200]
plt.figure(figsize=(24, 16))
plt.plot(x5['Frequency_MHz'], x5['Amplitude_dBm'], 'b-', linewidth=1.5)
plt.title('Espectro onda cuadrada con frecuencia de 25MHz y un span de 0-1 GHz', fontsize=24)
plt.xlabel('Frecuencia (MHz)', fontsize=20)
plt.ylabel('Amplitud (dBm)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()

max_idx = x5['Amplitude_dBm'].idxmax()
max_freq = x5.loc[max_idx, 'Frequency_MHz']
max_amp = x5.loc[max_idx, 'Amplitude_dBm']
max_idx2 = int(x5['Amplitude_dBm'][int(max_idx)+1 : ].idxmax()) # type: ignore
max_freq2 = x5.loc[max_idx2, 'Frequency_MHz']
max_amp2 = x5.loc[max_idx2, 'Amplitude_dBm']
max_idx3 = int(x5['Amplitude_dBm'][int(max_idx2)+1 : ].idxmax()) # type: ignore
max_freq3 = x5.loc[max_idx3, 'Frequency_MHz']
max_amp3 = x5.loc[max_idx3, 'Amplitude_dBm']

plt.annotate(f'Máximo 1: {max_amp:.2f} dBm\n@ {max_freq:.3f} MHz',
             xy=(max_freq, max_amp),
             xytext=(max_freq+10, max_amp+0.2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 2: {max_amp2:.2f} dBm\n@ {max_freq2:.3f} MHz',
             xy=(max_freq2, max_amp2),
             xytext=(max_freq2+35, max_amp2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 3: {max_amp3:.2f} dBm\n@ {max_freq3:.3f} MHz',
             xy=(max_freq3, max_amp3),
             xytext=(max_freq3 + 125, max_amp3+1),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.hlines(-20, 0, 1000, 'black')
plt.annotate('Corte de -20 dBm',
             xy=(max_freq3, max_amp3),
             xytext=(80, -19),
             fontsize=20)
plt.savefig('plots/square_25MHz_span_0-1GHz.png')
plt.show()


# %% [markdown]
# Ploteo de seno generado a 25 MHz con línea de corte a -20 y el span de $0$ a $1 \text{GHz}$

# %% jupyter={"source_hidden": true}
plt.figure(figsize=(24, 16))
plt.plot(x6['Frequency_MHz'], x6['Amplitude_dBm'], 'b-', linewidth=1.5)
plt.title('Espectro onda cuadrada a 25MHz', fontsize=24)
plt.xlabel('Frecuencia (MHz)', fontsize=20)
plt.ylabel('Amplitud (dBm)', fontsize=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()

max_idx = x6['Amplitude_dBm'].idxmax()
max_freq = x6.loc[max_idx, 'Frequency_MHz']
max_amp = x6.loc[max_idx, 'Amplitude_dBm']
max_idx2 = int(x6['Amplitude_dBm'][int(max_idx)+1 : ].idxmax()) # type: ignore
max_freq2 = x6.loc[max_idx2, 'Frequency_MHz']
max_amp2 = x6.loc[max_idx2, 'Amplitude_dBm']
max_idx3 = int(x6['Amplitude_dBm'][int(max_idx2)+1 : ].idxmax()) # type: ignore
max_freq3 = x6.loc[max_idx3, 'Frequency_MHz']
max_amp3 = x6.loc[max_idx3, 'Amplitude_dBm']

plt.annotate(f'Máximo 1: {max_amp:.2f} dBm\n@ {max_freq:.3f} MHz',
             xy=(max_freq, max_amp),
             xytext=(max_freq+10, max_amp+0.2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 2: {max_amp2:.2f} dBm\n@ {max_freq2:.3f} MHz',
             xy=(max_freq2, max_amp2),
             xytext=(max_freq2+15, max_amp2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.annotate(f'Máximo 3: {max_amp3:.2f} dBm\n@ {max_freq3:.3f} MHz',
             xy=(max_freq3, max_amp3),
             xytext=(max_freq3 + 15, max_amp3+2),
             arrowprops=dict(arrowstyle='->', color='darkred'),
             fontsize=20,
             color='darkred')
plt.hlines(-20, 0, 200, 'black')
plt.annotate('Corte de -20 dBm',
             xy=(max_freq3, max_amp3),
             xytext=(80, -19),
             fontsize=20)
plt.savefig('plots/square_25MHz.png')
plt.show()

# %%
