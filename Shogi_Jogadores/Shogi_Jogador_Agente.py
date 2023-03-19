from .Shogi_Jogador import Jogador

class JogadorShogiAgente(Jogador):
  def __init__(self, identificador):
    super().__init__(identificador, "max")

  def jogar(self, jogo):
    profundidade_maxima = 81
    melhor_valor = float("-inf")
    melhor_jogada = -1
    print(jogo.turno().imprimir())
    for proximo_jogo in jogo.gerar_jogadas_validas():
      utilidade = minimax_alfabeta(jogo.jogar(proximo_jogo), jogo.turno(), profundidade_maxima)
      if utilidade > melhor_valor:
        melhor_valor = utilidade
        melhor_jogada = proximo_jogo
    return melhor_jogada