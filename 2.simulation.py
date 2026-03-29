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

# %%
# %% [markdown]
# Simulation of the signals, first in time domain
#
# %%

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

# %% [markdown]
# Define attenuator

# %%
def coupler(X, attenuation_db=-20):
    H = 10**(attenuation_db / 20)
    return X * H
# %%

fs = 100e6
t = np.arange(0, 1e-3, 1/fs)

f0 = 5e6 #ramp freq =5MHz
duty = 1          # symmetry

x = signal.sawtooth(2*np.pi*f0*t, width=duty)

# %%
plt.plot(t, x)
plt.xlim(0, 0.001e-3)
plt.show()

# %% [markdown]
# Simulación del analizador de espectro. Falta la resolución del ancho del filtro que movimos en el laboratorio
#
# %%

def spectrum_fft(x, fs):
    N = len(x)
    window = np.hanning(N)
    xw = x * window

    X = np.fft.fft(xw)
    freqs = np.fft.fftfreq(N, 1/fs)

    mask = freqs > 0
    return freqs[mask], X[mask]
def fft_to_power(X, R=50):
    mag = np.abs(X)
    mag = mag / len(X)
    P = (mag**2) / R

    return P
def power_to_dBm(P):
    return 10 * np.log10(P / 1e-3)
def spectrum_analyzer(x, fs, R=50):
    freqs, X = spectrum_fft(x, fs)
    P = fft_to_power(X, R)
    P_dBm = power_to_dBm(P)
    return freqs, P_dBm

# %% [markdown]
# Ahora paso la señal por el analizador de espectro
#
# %%
ramp_sym_50 = spectrum_analyzer(coupler(x), fs)

# %%
ramp_sym_50
