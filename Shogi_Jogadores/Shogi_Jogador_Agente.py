from .Shogi_Jogador import Jogador
from minimax import minimax, minimax_alfabeta

class JogadorShogiAgente(Jogador):
  def __init__(self, identificador):
    super().__init__(identificador, "max")

  def jogar(self, jogo, tabuleiro, timeA, timeB, jogador_turno, humano, agente):
    profundidade_maxima = 9
    melhor_valor = float("-inf")
    melhor_jogada = -1
    
    for proximo_jogo in jogo.gerarJogadasValidas(tabuleiro, timeA, jogo.jogador_turno, timeB, humano, agente):
      
      novo_jogo = jogo.jogar(tabuleiro, proximo_jogo["peca"], proximo_jogo["jogada"], timeA, timeB, jogo.jogador_turno, humano, agente)
      
      utilidade = minimax_alfabeta(novo_jogo, jogo.turno(),tabuleiro, timeA, timeB, jogador_turno, humano, agente)
      if utilidade > melhor_valor:
        melhor_valor = utilidade
        melhor_jogada = proximo_jogo
    return melhor_jogada

