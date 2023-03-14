import os
def verificacaoJogadaPeao(tabuleiro, pos1, pos2, vez, peca):
  os.system("clear")
  
  #Verificações para o Jogador A
  if(vez == True):
    if(peca.__contains__("B")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("A")):
      print("Movimento inválido: Há peças aliadas no caminho")
      return False
    #Verifica um movimento que não seja uma casa p/ frente
    if(pos1[0] - pos2[0] != 1 or pos2[1] != pos1[1]):
      print("O peão não pode realizar esse movimento")
      return False

  #Verificações para o Jogador B
  else:
    if(peca.__contains__("A")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("B")):
      print("Movimento inválido: Há peças aliadas no caminho")
      return False
    #Verifica um movimento que não seja uma casa p/ frente
    if(pos2[0] - pos1[0] != 1 or pos2[1] != pos1[1]):
      print("O peão não pode realizar esse movimento")
      return False
  print("Movimento Válido")
  return True