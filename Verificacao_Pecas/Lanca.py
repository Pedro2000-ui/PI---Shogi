# Funções da lança
def verificacaoMovimentoLanca(tabuleiro, vez, pos1, pos2):
  if vez:
    for i in range(pos2[0], (pos1[0] + 1)):
      if tabuleiro[-i + pos1[0] + pos2[0]][pos1[1]].__contains__("B") and pos2[0] != (-i + pos1[0] + pos2[0]):
        print("Movimento inválido: Não da para pular uma peça inimiga")
        return False
    
      if tabuleiro[-i + pos1[0] + pos2[0]][pos1[1]].__contains__("A") and pos1[0] != (-i + pos1[0] + pos2[0]):
        print("Movimento inválido: Há peças aliadas no caminho")
        return False
    return True
  else:
    for i in range(pos1[0], (pos2[0] + 1)):
      if tabuleiro[i][pos1[1]].__contains__("A") and pos2[0] != i:
        print("Movimento inválido: Não da para pular uma peça inimiga")
        return False
    
      if tabuleiro[i][pos1[1]].__contains__("B") and pos1[0] != i:
        print("Movimento inválido: Há peças aliadas no caminho")
        return False
    return True
    
def verificacaoJogadaLanca(tabuleiro, vez, pos1, pos2):
  if pos1[1] != pos2[1]:
    print("Movimento inválido: Coluna diferente")
    return False
    
  if vez:
    if pos1[0] <= pos2[0]:
      print("Movimento inválido: Lança não anda para trás")
      return False
    if verificacaoMovimentoLanca(tabuleiro, vez, pos1, pos2) == False:
      return False
      
    print("Movimento válido")
    return True
  else:
    if pos1[0] >= pos2[0]:
      print("Movimento inválido: Lança não anda para trás")
      return False
    if verificacaoMovimentoLanca(tabuleiro, vez, pos1, pos2) == False:
      return False
      
    print("Movimento válido!")
    return True