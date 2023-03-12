import os
def verificacaoJogadaTorre(tabuleiro, pos1, pos2, vez, peca):
  os.system("clear")

  #Verificações para o Jogador A
  if(vez == True):
    if(peca.__contains__("B")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("A")):
      print("Movimento inválido: Há peças aliadas no caminho")
      return False

  #Verificações para o Jogador B
  else:
    if(peca.__contains__("A")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("B")):
      print("Movimento inválido: Há peças aliadas no caminho")
      return False

  #Movimentação p/ frente Jogador A e p/ trás Jogador B
  if(pos1[0] - pos2[0] > 0 and pos2[1] == pos1[1]): 
    for i in range(pos2[0] + 1, pos1[0]): 
      if(tabuleiro[i][pos1[1]] != "00"):
        print("Movimento inválido: Não é possível saltar peças")
        return False
  #Movimentação p/ trás Jogador A e p/ frente Jogador B
  elif(pos2[0] - pos1[0] > 0 and pos2[1] == pos1[1]): 
    for i in range(pos1[0] + 1, pos2[0]):
      if(tabuleiro[i][pos1[1]] != "00"):
        print("Movimento inválido: Não é possível saltar peças")
        return False
  #Movimentação p/ a Direita Jogador A e p/ esquerda Jogador B
  elif(pos2[1] - pos1[1] > 0 and pos2[0] == pos1[0]): 
    for i in range(pos1[1] + 1, pos2[1]):
      if(tabuleiro[int(pos1[0])][i] != "00"):
        print("Movimento inválido: Não é possível saltar peças")
        return False
  #Movimentação p/ esquerda Jogador A e p/ direita Jogador B
  elif(pos1[1] - pos2[1] > 0 and pos2[0] == pos1[0]): 
    for i in range(pos2[1] + 1, pos1[1]):
      if(tabuleiro[pos1[0]][i] != "00"):
        print("Movimento inválido: Não é possível saltar peças")
        return False
  else:
    print("A Torre não pode realizar esse movimento")
    return False
  print("Movimento Válido")
  return True