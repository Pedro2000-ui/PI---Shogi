class Jogador:
  def __init__(self, identificador, min_max = None):
    self.identificador = identificador
    self.min_max = min_max

  def define_proximo_turno(self, proximo_turno):
    self.jogador_proximo_turno = proximo_turno

  def imprimir(self):
    return self.identificador
  
  def jogar(self, jogo):
    raise NotImplementedError("Deve ser implementado")
  
  def e_min(self):
    return self.min_max == "min"
  
  def e_max(self):
    return self.min_max == "max"
  
  def proximo_turno(self):
    return self.jogador_proximo_turno