import os
def verificacaoJogadaCavaleiro(tabuleiro, pos1, pos2, vez, peca):
  os.system("clear")
  
  #Verificações para o Jogador A
  if(vez == True):
    if(peca.__contains__("B")):
        print("Movimento Inválido: Essa é uma peça adversária")
        return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("A")):
        print("Movimento Inválido: Há peças aliadas no caminho")
        return False
    if(pos1[0] > 1 and pos2[0] == pos1[0] - 2): 
      if(pos1[1] != 8 and pos2[1] == pos1[1] + 1): #Movimento em L p/ direita
        print("Movimento Válido")
        return True
      if(pos1[1] != 0 and pos2[1] == pos1[1] - 1): #Movimento em L p/ esquerda 
        print("Movimento Válido")
        return True
      print("O cavaleiro não pode realizar esse movimento!")
      return False
    else:
      print("O cavaleiro não pode realizar esse movimento!")
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
    if(pos1[0] < 7 and pos2[0] == pos1[0] + 2): 
      if(pos1[1] != 0 and pos2[1] == pos1[1] - 1): #Movimento em L p/ direita
        print("Movimento Válido")
        return True
      if(pos1[1] != 8 and pos2[1] == pos1[1] + 1): #Movimento em L p/ esquerda 
        print("Movimento Válido")
        return True
      print("O cavaleiro não pode realizar esse movimento!")
      return False
    else:
      print("O cavaleiro não pode realizar esse movimento!")
      return False
  return False