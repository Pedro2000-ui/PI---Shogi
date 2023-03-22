import os
def verificacaoJogadaBispo(tabuleiro, pos1, pos2, jogador_turno, humano, agente, peca):
  # os.system("clear")
  
  #Verificações do Jogador A
  if(jogador_turno == humano):
    if(peca.__contains__("B")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("A")):
      print("Movimento Inválido: Há peças aliadas no caminho")
      return False
      
  #Verificações do Jogador B
  else:
    if(peca.__contains__("A")):
      print("Movimento Inválido: Essa é uma peça adversária")
      return False
    if(tabuleiro[pos2[0]][pos2[1]].__contains__("B")):
      print("Movimento Inválido: Há peças aliadas no caminho")
      return False
  
  #É um movimento válido, mas ainda não sabemos para qual lado    
  if(abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])):
    #Subindo no tabuleiro
    if(pos1[0] > pos2[0]):
      inicio = pos2[0] + 1
      fim = pos1[0]
      #Indo para Direita
      if(pos1[1] < pos2[1]): 
        j = pos2[1] - 1
        decrementa = True
      #Indo para Esquerda
      else: 
        j = pos2[1] + 1
        decrementa = False
    #Descendo no Tabuleiro
    else:
      inicio = pos1[0] + 1
      fim = pos2[0] 
      #Indo para Esquerda
      if(pos1[1] > pos2[1]):
        j = pos1[1] - 1
        decrementa = True
      #Indo para Direita
      else:
        j = pos1[1] + 1
        decrementa = False
    for i in range(inicio, fim):
      if(tabuleiro[i][j] != "00"):
        print("Movimento inválido: Não é possível saltar peças")
        return False
      if(decrementa):
        j = j - 1
      else: 
        j = j + 1  
    print("Movimento Válido")
    return True
  print("O bispo não pode realizar esse movimento")
  return False