def comePeca(tabuleiro, pos1, pos2, timeA, timeB, vez):
    if vez:
      timeA.append(tabuleiro[pos2[0]][pos2[1]])
    else:
      timeB.append(tabuleiro[pos2[0]][pos2[1]])
    
def movimentacaoPeca(tabuleiro, pos1, pos2, timeA, timeB, vez):
  if(tabuleiro[pos2[0]][pos2[1]] != "00"):
    comePeca(tabuleiro, pos1, pos2, timeA, timeB, vez)
    
  tabuleiro[pos2[0]][pos2[1]] =  tabuleiro[pos1[0]][pos1[1]]
  tabuleiro[pos1[0]][pos1[1]] = "00"
    
  
  
  