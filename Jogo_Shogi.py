from minimax import minimax, minimax_alfabeta
from Verificacao_Movimentacao import Shogi_Movimentacoes as movimentacoes
from Verificacao_Movimentacao import Shogi_Verificacoes as verificacoes
from Shogi_Jogadores import Shogi_Jogador
from Shogi_Jogadores import Shogi_Jogador_Agente

import numpy as np

class JogoShogi():
  def __init__(self, tabuleiro = None, jogador_turno = None):
    self.tabuleiro = tabuleiro
    self.jogador_turno = jogador_turno

  def inicializaJogadores(self):
    (humano, agente) = (Shogi_Jogador.Jogador("0", "min"), Shogi_Jogador_Agente.JogadorShogiAgente("1"))
    humano.define_proximo_turno(agente)
    agente.define_proximo_turno(humano)
    self.jogador_turno = humano
    return (humano, agente)

  def turno(self):
    return self.jogador_turno

  def jogar(self, tabuleiro, pos1, pos2, timeA, timeB, jogador_turno, humano, agente):
    novo_tabuleiro = tabuleiro
    movimentacoes.movimentacaoPeca(tabuleiro, pos1, pos2, timeA, timeB, jogador_turno, humano, agente)
    return JogoShogi(novo_tabuleiro, self.jogador_turno.proximo_turno())

  def gerarJogadasValidas(self, tabuleiro, timeA, timeB, jogador_turno, humano, agente):
    pecas_com_jogadas_validas = []
    if self.jogador_turno == agente:
      linha = []
      coluna = []
      for i in range(0, 9):
        for j in range(0, 9):
          if tabuleiro[i][j].__contains__("B"):
            pecas_agente.append((i, j))

      pecas_agente = np.array(pecas_agente)

      for peca in pecas_agente:
        for i in range(0, 9):
          for j in range(0, 9):
            jogada_valida = [i, j]
            if verificacoes.verificaJogadaValida(tabuleiro, peca, jogada_valida, jogador_turno, humano, agente, timeA, timeB):
              pecas_com_jogadas_validas.append({"peca": [peca[0], peca[1]], "jogada": jogada_valida})
    else: 
      pecas_humano = []
      for i in range(0, 9):
        for j in range(0, 9):
          if tabuleiro[i][j].__contains__("A"):
            pecas_humano.append((i, j))

      pecas_humano = np.array(pecas_humano)

      for peca in pecas_humano:
        for i in range(0, 9):
          for j in range(0, 9):
            jogada_valida = [i, j]
            if verificacoes.verificaJogadaValida(tabuleiro, peca, jogada_valida, jogador_turno, humano, agente, timeA, timeB):
              pecas_com_jogadas_validas.append({"peca": [peca[0], peca[1]], "jogada": jogada_valida})
    return pecas_com_jogadas_validas

  def venceu(self, timeA, timeB, humano, agente):
    if self.jogador_turno == humano:
      if timeA.__contains__("8B"):
        return true
    else:
      print(timeA)
      print(timeB)
      if timeB.__contains__("8A"):
        return true
    return False

  def empate(self):
    return (not self.venceu()) and (len(self.gerar_jogadas_validas()) == 0)

  def calcular_utilidade(self, timeA, timeB, humano, agente):
    if self.jogador_turno == agente:
      if self.venceu(timeA, timeB, humano, agente) and agente.e_min():
        return -1
      elif self.venceu(timeA, timeB, humano, agente) and agente.e_max():
        return 1
      else:
        return 0
    return 0

  def imprimir(self):
    return self.tabuleiro

  def imprimir_jogada(self, turno, jogada):
    raise NotImplementedError("Deve ser implementado")
