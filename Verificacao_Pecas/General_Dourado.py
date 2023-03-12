import os

def verificacaoJogadaOuro(tabuleiro, pos1, pos2, vez, peca):
  os.system("clear")
  
  #Verificações para o Jogador A
  if(vez == True):
    if(peca.__contains__("B")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("A")):
      print("Movimento Inválido: Há peças aliadas no caminho")
      return False
    #Verifica se é um movimento diagonal p/ trás
    if(pos2[0] - pos1[0] == 1 and pos2[1] - pos1[1] != 0):
      print("O General Dourado não pode realizar esse movimento")
      return False
  
  #Verificações para o Jogador B
  else:
    if(peca.__contains__("A")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("B")):
      print("Movimento Inválido: Há peças aliadas no caminho")
      return False
    #Verifica se é um movimento diagonal p/ trás
    if(pos2[0] - pos1[0] == -1 and pos2[1] - pos1[1] != 0):
      print("O General Dourado não pode realizar esse movimento")
      return False
  if(pos2[0] - pos1[0] > 1 or pos2[1] - pos1[1] > 1 or pos2[0] - pos1[0] < -1 or pos2[1] - pos1[1] < -1):
    print("O General Dourado não pode realizar esse movimento")
    return False
  print("Movimento Válido")
  return True