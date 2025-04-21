# Uso:
# python mostra_grafico.py arquivo1.txt arquivo2.txt

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

# le do arquivo (com colunas separadas por virgulas)
dados = dict()
D = dict()

N = dict()
t = dict()
freq = dict()

# para cada argumento
for name in sys.argv[1:]:
    # le arquivo
    df = pd.read_csv(name)

    # seleciona unica coluna
    mdados = df.iloc[:,0]
    mN = len(mdados)
    mt = np.arange(mN)

    mD = np.fft.fft(mdados)
    mfreq = np.fft.fftfreq(mN)*9600

    # pega so freq. positivas, pois dados sao reais
    mD = mD[:mN//2]
    mfreq = mfreq[:mN//2]

    # adiciona dados nos dicionarios acima
    dados[name] = mdados
    D[name] = mD

    N[name] = mN
    t[name] = mt
    freq[name] = mfreq

# faz um grafico
plt.figure(figsize=(10, 8))
for name in dados.keys():
    plt.plot(t[name], dados[name], lw=2, label=name)
plt.xlabel("Amostra")
plt.ylabel("Leitura")
plt.legend()
plt.show()

# faz um grafico
plt.figure(figsize=(10, 8))
for name in D.keys():
    plt.loglog(freq[name], np.abs(D[name])**2, lw=2, label=name)
plt.xlabel("Frequencia [Hz]")
plt.ylabel("Intensidade [a.u.]")
plt.legend()
plt.show()