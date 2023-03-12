import Shogi_Verificacoes as verificacoes
import Shogi_Movimentacoes as movimentacoes
import os
def instrucoesJogo():
  print("\n#Peão - 1")
  print("#Lança - 2") 
  print("#Cavalo - 3") 
  print("#Gen Prata - 4") 
  print("#Gen Ouro - 5") 
  print("#Bispo - 6") 
  print("#Torre - 7") 
  print("#Rei - 8") 
  print("#Bispo Promovido - 9") 
  print("#Torre Promovida - 10") 
  print("\n#Variável -> Peça + Time") 
  print("\n#Exemplo -> 1A - Peão do time A; 8B - Rei do time B; 00 - Casa Vazia") 
  input("\nAperte qualquer tecla para continuar...")
  
def solicitaPosicoesDeJogada(tabuleiro, timeA, timeB, vez, tenteNovamente):
  if tenteNovamente:
    print("\nTente novamente.\n")
  print(tabuleiro)
  if vez:
    print("\nVez do time A")
  else: 
    print("\nVez do time B")
  print()
  print("Capturas A:")
  print(timeA)
  print()
  print("Capturas B:")
  print(timeB)
  print()
  print("Escolha a posição em que se encontra a peça a ser movida:")
  print("Exemplo: 4 2")
  pos1 = input()
  pos1 = pos1.split()
  pos1 = [int(pos1[0]), int(pos1[1])]
  print("Escolha a posição para a qual a peça irá:")
  print("Exemplo: 4 3")
  pos2 = input()
  pos2 = pos2.split()
  pos2 = [int(pos2[0]), int(pos2[1])]
  return pos1, pos2

def alternaVezTime(vez):
  if vez:
    return False
  else:
    return True

def jogo(tabuleiro, estado, vez, timeA, timeB):
  instrucoesJogo()
  tenteNovamente = False
  
  while(estado != "Fim"):
    pos1, pos2 = solicitaPosicoesDeJogada(tabuleiro, timeA, timeB, vez, tenteNovamente)
    if(pos1[0] > 8 or pos1[1] > 8 or pos2[0] > 8 or pos2[1] > 8):
      os.system("clear")
      print("Não é possível sair do tabuleiro!!")
      tenteNovamente = True
    else:
      movimentoValido = verificacoes.verificaJogadaValida(tabuleiro, pos1, pos2, vez, timeA, timeB)
      if(movimentoValido):
        movimentacoes.movimentacaoPeca(tabuleiro, pos1, pos2, timeA, timeB, vez)
        vez = alternaVezTime(vez)
        tenteNovamente = False
        estado = "Jogando"
      else: 
        tenteNovamente = True