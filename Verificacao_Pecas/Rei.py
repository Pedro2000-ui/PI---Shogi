import os
def verificacaoJogadaRei(tabuleiro, pos1, pos2, jogador_turno, humano, agente, peca):
  os.system("clear")
  
  #Verificações para o Jogador A
  if(jogador_turno == humano):
    if(peca.__contains__("B")):
        print("Movimento Inválido: Essa é uma peça adversária")
        return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("A")):
        print("Movimento Inválido: Há peças aliadas no caminho")
        return False
  #Verificações para o Jogador B
  else:
    if(peca.__contains__("A")):
      os.system("clear")
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("B")):
        print("Movimento Inválido: Há peças aliadas no caminho")
        return False
  
  #Verificações de Movimentações Gerais, independente do Jogador
  if(pos2[0] - pos1[0] > 1 or pos2[1] - pos1[1] > 1 or pos2[0] - pos1[0] < -1 or pos2[1] - pos1[1] < -1):
    print("O Rei não pode realizar esse movimento")
    return False
  print("Movimento Válido")
  return True
    