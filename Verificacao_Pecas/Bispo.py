# Funções do bispo
def verificacaoMovimentoBispos(tabuleiro, vez, pos1, pos2):
  if pos1[0] > pos2[0]:
    for i in range(pos2[0], (pos1[0] + 1)):
      if pos1[1] > pos2[1]:
        if vez:
          if tabuleiro[-i + pos1[0] + pos2[0]][-i + pos1[1] + pos2[0]].__contains__("B") and pos2[0] != (-i + pos1[0] + pos2[0]):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False

          if tabuleiro[-i + pos1[0] + pos2[0]][-i + pos1[1] + pos2[0]].__contains__("A") and pos1[0] != (-i + pos1[0] + pos2[0]):
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
        else:
          if tabuleiro[-i + pos1[0] + pos2[0]][-i + pos1[1] + pos2[0]].__contains__("A") and pos2[0] != (-i + pos1[0] + pos2[0]):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False

          if tabuleiro[-i + pos1[0] + pos2[0]][-i + pos1[1] + pos2[0]].__contains__("B") and pos1[0] != (-i + pos1[0] + pos2[0]):
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
        
      else:
        if vez:
          if tabuleiro[-i + pos1[0] + pos2[0]][i].__contains__("B") and pos2[0] != (-i + pos1[0] + pos2[0]):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False
  
          if tabuleiro[-i + pos1[0] + pos2[0]][i].__contains__("A") and pos1[0] != (-i + pos1[0] + pos2[0]):
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
        else:
          if tabuleiro[-i + pos1[0] + pos2[0]][i].__contains__("A") and pos2[0] != (-i + pos1[0] + pos2[0]):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False
  
          if tabuleiro[-i + pos1[0] + pos2[0]][i].__contains__("B") and pos1[0] != (-i + pos1[0] + pos2[0]):
            print("Erro aqui")
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
        
  elif pos1[0] < pos2[0]:
    for i in range(pos1[0], (pos2[0] + 1)):
      if pos1[1] < pos2[1]:
        if vez:
          if tabuleiro[i][i].__contains__("B") and pos2[0] != (i):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False
  
          if tabuleiro[i][i].__contains__("A") and pos1[0] != (i):
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
        else:
          if tabuleiro[i][i].__contains__("A") and pos2[0] != (i):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False
  
          if tabuleiro[i][i].__contains__("B") and pos1[0] != (i):
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
        
      else:
        if vez:
          if tabuleiro[i][-i + pos1[0] + pos2[0]].__contains__("B") and pos2[0] != (i):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False
  
          if tabuleiro[i][-i + pos1[0] + pos2[0]].__contains__("A") and pos1[0] != (i):
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
        else:
          if tabuleiro[i][-i + pos1[0] + pos2[0]].__contains__("A") and pos2[0] != (i):
            print("Movimento inválido: Não da para pular uma peça inimiga")
            return False
  
          if tabuleiro[i][-i + pos1[0] + pos2[0]].__contains__("B") and pos1[0] != (i):
            print("Movimento inválido: Há peças aliadas no caminho")
            return False
  return True
  
      
def verificacaoJogadaBispos(tabuleiro, vez, pos1, pos2):
  if pos1[0] == pos2[0]:
    print("Movimento inválido: Não pode ficar no mesmo lugar.")
    return False
  if (abs(pos1[0] - pos2[0]) - abs(pos1[1] - pos2[1])) == 0:
    return verificacaoMovimentoBispos(tabuleiro, vez, pos1, pos2)
  return False