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
from scipy.ndimage import gaussian_filter1d


# %% [markdown]
# Define attenuator

# %%
def coupler(X, attenuation_db=-20):
    H = 10**(attenuation_db / 20)
    return X * H
# %% [markdown]
# Time domain signals simulation

# %%

fs = 100e6
t = np.arange(0, 1e-3, 1/fs)

f0 = 5e6          # ramp freq =5MHz
duty = 1          # symmetry = 100%

x_1 = signal.sawtooth(2*np.pi*f0*t, width=duty)
#x_1 = x_1 * 10**1.6
# %%
plt.plot(t, x)
plt.xlim(0.001e-3, 0.002e-3)
plt.title('100% symmetry sawtooth Sample from 1 to 2 ms')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage')
plt.show()

# %% [markdown]
# Simulación del analizador de espectro. Falta la resolución del ancho del filtro que movimos en el laboratorio
#
# %%


# %% [markdown]
# Ahora paso la señal por el analizador de espectro
#
# %%

def spectrum_analyzer(
    x, fs,
    f_start, f_stop,
    n_points,
    R=50,
    rbw_hz=100e3   # default: 100 kHz RBW (reasonable for ~200 MHz span)
):
    """
    Simulates a spectrum analyzer.

    Parameters:
    - x: time-domain signal
    - fs: sampling frequency [Hz]
    - f_start, f_stop: frequency span [Hz]
    - n_points: number of output points
    - R: system impedance (default 50 ohm)
    - rbw_hz: resolution bandwidth [Hz]

    Returns:
    processed_data = [freq_GHz, amp_dBm]
    """

    N = len(x)

    # --- 1. Apply window to reduce spectral leakage ---
    window = np.hanning(N)
    xw = x * window

    # --- 2. Compute FFT ---
    X = np.fft.fft(xw)
    freqs = np.fft.fftfreq(N, 1/fs)

    # Keep only positive frequencies
    mask = freqs > 0
    freqs = freqs[mask]
    X = X[mask]

    # --- 3. Convert magnitude to power ---
    mag = np.abs(X) / N
    P = (mag**2) / R

    # Avoid log of zero
    P[P <= 0] = 1e-20

    P_dbm = 10 * np.log10(P / 1e-3)

    # --- 4. Simulate RBW (frequency-domain smoothing) ---
    df = fs / N
    rbw_bins = rbw_hz / df

    P_dbm = gaussian_filter1d(P_dbm, sigma=rbw_bins)

    # --- 5. Select analyzer span ---
    mask_span = (freqs >= f_start) & (freqs <= f_stop)
    freqs_span = freqs[mask_span]
    P_span = P_dbm[mask_span]

    # --- 6. Resample to match analyzer points ---
    freqs_target = np.linspace(f_start, f_stop, n_points)
    P_interp = np.interp(freqs_target, freqs_span, P_span)

    # --- 7. Output format ---
    freq_ghz = freqs_target / 1e9
    processed_data = np.column_stack((freq_ghz, P_interp))

    return processed_data

# %%
ramp_sym_50_S = spectrum_analyzer(coupler(x), fs, 0, 200e6, 100000)

# %%
plt.plot(ramp_sym_50_S[:, 0], ramp_sym_50_S[:, 1])
