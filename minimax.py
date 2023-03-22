## Minimax sem poda
def minimax(jogo, jogador, profundidade_maxima = 8):
  # se o jogo acabou ou se a profundidade é máxima
  if jogo.venceu() or jogo.empate() or profundidade_maxima == 0:
    return jogo.calcular_utilidade(jogador)

  if jogador.e_max(): # turno do MAX
    melhor_valor = float("-inf") # Menos infinito é o menor valor

    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerar_jogadas_validas():
      utilidade = minimax(jogo.jogar(proximo_jogo), jogador.proximo_turno(), profundidade_maxima - 1)
      melhor_valor = max(utilidade, melhor_valor) # proximo_jogo com o maior valor
    return melhor_valor
  else: # turno no MIN
    pior_valor = float("inf") # Mais infinito é o maior valor

    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerar_jogadas_validas():
      utilidade = minimax(jogo.jogar(proximo_jogo), jogador.proximo_turno(), profundidade_maxima - 1)
      pior_valor = min(utilidade, pior_valor) # proximo_jogo com o menor valor
    return pior_valor

## Minimax com poda
def minimax_alfabeta(jogo, jogador, tabuleiro, timeA, timeB, jogador_turno, humano, agente, alfa = float("-inf"), beta = float("inf"), profundidade_maxima = 1):
  # se o jogo acabou ou se a profundidade é máxima
  if jogo.venceu(timeA, timeB, humano, agente) or profundidade_maxima == 1:
    return jogo.calcular_utilidade(timeA, timeB, humano, agente)

  if jogador.e_max(): # turno do MAX
    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerarJogadasValidas(tabuleiro, timeA, timeB, jogador_turno, humano, agente):
      utilidade = minimax_alfabeta(jogo.jogar(tabuleiro, proximo_jogo["peca"], proximo_jogo["jogada"], timeA, timeB, jogador_turno, humano, agente), jogo.turno(),tabuleiro,timeA, jogador_turno, timeB, humano, agente, alfa, beta, profundidade_maxima - 1)
      alfa = max(utilidade, alfa)
      if alfa >= beta: break
    return alfa
  
  else: # turno no MIN
    # busca todos os possíveis jogos
    for proximo_jogo in jogo.gerarJogadasValidas(tabuleiro, timeA, timeB, jogador_turno, humano, agente):
      utilidade = minimax_alfabeta(jogo.jogar(tabuleiro, proximo_jogo["peca"], proximo_jogo["jogada"], timeA, timeB, jogador_turno, humano, agente), jogo.turno(),tabuleiro,timeA, jogador_turno, timeB, humano, agente, alfa, beta, profundidade_maxima - 1)
      beta = min(utilidade, beta)
      if alfa >= beta: break
    return beta