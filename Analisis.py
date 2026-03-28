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

# %%
