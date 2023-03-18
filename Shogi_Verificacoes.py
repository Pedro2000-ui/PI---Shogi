# Importando peças com suas respectivas verificações
from Verificacao_Pecas import General_Prateado
from Verificacao_Pecas import Bispo
from Verificacao_Pecas import Peao
from Verificacao_Pecas import Lanca
from Verificacao_Pecas import Torre
from Verificacao_Pecas import Rei
from Verificacao_Pecas import Cavaleiro
from Verificacao_Pecas import General_Dourado

def verificaJogadaValida(tabuleiro, pos1, pos2, vez, timeA, timeB):
  # Verificar se o usuário está tentando mover uma peça vazia
  if(tabuleiro[pos1[0]][pos1[1]] == "00"):
    print("Não existe uma peça nessa posição!")
    return False
    
  # Retorna qual peça eu estou mexendo
  peca = tabuleiro[pos1[0]][pos1[1]] 

  # Estrutura condicional para verificar jogadas
  if(peca.__contains__("0")):
    return verificacaoJogadaTorrePromovido()
  elif(peca.__contains__("1")):
    return Peao.verificacaoJogadaPeao(tabuleiro, pos1, pos2, vez, peca)
  elif(peca.__contains__("2")):
    return Lanca.verificacaoJogadaLanca(tabuleiro, pos1, pos2, vez, peca)
  elif(peca.__contains__("3")):
    return Cavaleiro.verificacaoJogadaCavaleiro(tabuleiro, pos1, pos2, vez, peca)
  elif(peca.__contains__("4")):
    return General_Prateado.verificacaoJogadaPrata(tabuleiro, pos1, pos2, vez, peca)
  elif(peca.__contains__("5")):
    return General_Dourado.verificacaoJogadaOuro(tabuleiro, pos1, pos2, vez , peca)
  elif(peca.__contains__("6")):
    return Bispo.verificacaoJogadaBispo(tabuleiro, pos1, pos2, vez, peca)
  elif(peca.__contains__("7")):
    return Torre.verificacaoJogadaTorre(tabuleiro, pos1, pos2, vez, peca)
  elif(peca.__contains__("8")):
    return Rei.verificacaoJogadaRei(tabuleiro, pos1, pos2, vez, peca)
  elif(peca.__contains__("9")):
    return verificacaoJogadaBispoPromovido()

def verificacaoJogadaTorrePromovido():
  print("Torre Promovida")
  return False
  
def verificacaoJogadaBispoPromovido():
  print("Bispo Promovido")
  return False

