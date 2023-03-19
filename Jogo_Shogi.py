from minimax import minimax, minimax_alfabeta
from Verificacao_Movimentacao import Shogi_Movimentacoes as movimentacoes
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

  def gerarJogadasValidas(self, tabuleiro, agente):
    if self.jogador_turno == agente:
      pecas_agente = []
      for i in range(0, 9):
        for j in range(0, 9):
          if tabuleiro[i][j].__contains__("B"):
            print(str(i) + " " + str(j))
            pecas_agente.append((i, j))

      pecas_agente = np.array(pecas_agente)
      print(pecas_agente)

      # Fazer um for percorrendo todos itens do time B e pegar todas jogadas possíveis de cada um
      # No fim será criado uma tupla contendo a posicao da peca e todas suas jogadas possiveis

      return 0

  def venceu(self):
    raise NotImplementedError("Deve ser implementado")

  def empate(self):
    return (not self.venceu()) and (len(self.gerar_jogadas_validas()) == 0)

  def calcular_utilidade(self, jogador):
    raise NotImplementedError("Deve ser implementado")

  def imprimir(self):
    return self.tabuleiro

  def imprimir_jogada(self, turno, jogada):
    raise NotImplementedError("Deve ser implementado")