import numpy as np
import Shogi_Acoes
import os

timeA = [] #Lista que guardará as peças capturadas
timeB = []
contadorA = 0  #Contador de Pontos
contadorB = 0

estado = "Inicio"  #Estado atual do jogo
vez = True  #Se é minha vez de jogar

tabuleiro = np.array([["2B", "3B", "4B", "5B", "8B", "5B", "4B", "3B", "2B"],
                      ["00", "7B", "00", "00", "00", "00", "00", "6B", "00"],
                      ["1B", "1B", "1B", "1B", "1B", "1B", "1B", "1B", "1B"],
                      ["00", "00", "00", "00", "00", "00", "00", "00", "00"],
                      ["00", "6A", "00", "00", "6B", "00", "00", "00", "00"],
                      ["00", "00", "00", "00", "00", "00", "00", "00", "00"],
                      ["1A", "1A", "1A", "1A", "1A", "1A", "1A", "1A", "1A"],
                      ["00", "6A", "00", "00", "00", "00", "00", "7A", "00"],
                      ["2A", "3A", "4A", "5A", "8A", "5A", "4A", "3A", "2A"]])

os.system("clear")
print("**Bem vindo ao SHOGI**")
Shogi_Acoes.jogo(tabuleiro, estado, vez, timeA, timeB)


