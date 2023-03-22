from Verificacao_Movimentacao import Shogi_Verificacoes as verificacoes
import os
from Jogo_Shogi import JogoShogi

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
  
def solicitaPosicoesDeJogada(jogo, timeA, timeB, jogador_turno, humano, agente, tenteNovamente):
  if tenteNovamente:
    print("\nTente novamente.\n")
  print("Situaçãoe do Jogo:")
  print(jogo.imprimir())
  print("=======================================")
  if jogador_turno == humano:
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

def jogo(tabuleiro, estado, timeA, timeB):
  tenteNovamente = False
  jogo = JogoShogi(tabuleiro)
  (humano, agente) = jogo.inicializaJogadores()

  instrucoesJogo()
  while(estado != "Fim"):
    if jogo.jogador_turno == humano:
      pos1, pos2 = solicitaPosicoesDeJogada(jogo, timeA, timeB, jogo.jogador_turno, humano, agente, tenteNovamente)
    else:
      pos1, pos2 = [0, 0], [0, 0]
    if(pos1[0] > 8 or pos1[1] > 8 or pos2[0] > 8 or pos2[1] > 8):
      os.system("clear")
      print("Não é possível sair do tabuleiro!!")
      tenteNovamente = True
    else:
      movimentoValido = verificacoes.verificaJogadaValida(tabuleiro, pos1, pos2, jogo.jogador_turno, humano, agente, timeA, timeB)
      if(movimentoValido): 
        if jogo.jogador_turno == humano:
          jogo = jogo.jogar(tabuleiro, pos1, pos2, timeA, timeB, jogo.jogador_turno, humano, agente)
          tenteNovamente = False
          estado = "Jogando"

          if jogo.venceu(timeA, timeB, humano, agente):
            print(f"{jogador_humano.imprimir()} Venceu!")
            break
        else:
          tabuleiro_aux = [["2B", "3B", "4B", "5B", "8B", "5B", "4B", "3B", "2B"],
                      ["00", "7B", "00", "00", "00", "00", "00", "6B", "00"],
                      ["1B", "1B", "1B", "1B", "1B", "1B", "1B", "1B", "1B"],
                      ["00", "00", "00", "00", "00", "00", "00", "00", "00"],
                      ["00", "00", "00", "00", "00", "00", "00", "00", "00"],
                      ["00", "00", "00", "00", "00", "00", "00", "00", "00"],
                      ["1A", "1A", "1A", "1A", "1A", "1A", "1A", "1A", "1A"],
                      ["00", "6A", "00", "00", "00", "00", "00", "7A", "00"],
                      ["2A", "3A", "4A", "5A", "8A", "5A", "4A", "3A", "2A"]]
          jogada_agente = agente.jogar(jogo, tabuleiro_aux, timeA, timeB, jogo.jogador_turno, humano, agente)
          print("=======================================")
          jogo = jogo.jogar(tabuleiro, jogada_agente["peca"], jogada_agente["jogada"], timeA, timeB, jogo.jogador_turno, humano, agente)
          print(tabuleiro)
      else: 
        tenteNovamente = True