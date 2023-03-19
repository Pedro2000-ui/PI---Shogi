import os
def verificacaoJogadaLanca(tabuleiro, pos1, pos2, jogador_turno, humano, agente, peca):
  os.system("clear")
  
  #Verificações do Jogador A
  if(jogador_turno == humano):
    if(peca.__contains__("B")):
        print("Movimento Inválido: Essa é uma peça adversária")
        return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("A")):
        print("Movimento Inválido: Há peças aliadas no caminho")
        return False
    #Verifica um movimento p/ frente
    if(pos1[0] - pos2[0] >= 1 and pos2[1] == pos1[1]):
      for i in range(pos2[0] + 1, pos1[0]): 
        if(tabuleiro[i][pos1[1]] != "00"):
          print("Movimento inválido: Não é possível saltar peças")
          return False
      print("Movimento Válido")
      return True
  
  #Verificações do Jogador B
  else:
    if(peca.__contains__("A")):
        print("Movimento Inválido: Essa é uma peça adversária")
        return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("B")):
        print("Movimento Inválido: Há peças aliadas no caminho")
        return False
    #Verifica um movimento p/ frente
    if(pos1[0] - pos2[0] <= -1 and pos2[1] == pos1[1]):
      for i in range(pos1[0] + 1, pos2[0]):
        if(tabuleiro[i][pos1[1]] != "00"):
          print("Movimento inválido: Não é possível saltar peças")
          return False
      print("Movimento Válido")
      return True
  print("A lança não pode realizar esse movimento")
  return False
