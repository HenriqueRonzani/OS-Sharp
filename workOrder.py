from utils import cls
from utils import warningBox
from utils import handleStringInput

def main():
  options = {
    "1": creatingOrder,
    "2": edit,
    "3": show,
    "X": lambda: None
  }
  while True:
    print("Gerenciar ordens de serviço")
    print("Escolha uma das opções do menu\n")
    print("Digite 1 | Cadastrar nova ordem de serviço")
    print("Digite 2 | Editar/Excluir ordem de serviço")
    print("Digite 3 | Listar ordem de serviço")
    print("Digite X | Voltar ao menu principal")
  
    userInput = input()
    if userInput in options:
      toRun = options[userInput]
      toRun()
    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")
      
    cls()

def creatingOrder():
  print("Digite o nome do cliente")
  name = handleStringInput(False)

  print("Digite o telefone do cliente")
  telefone = handleStringInput(False)

  print("Digite a descrição do equipamento")
  descricao = handleStringInput(False)

  print("Digite o defeito reclamado")
  defeito = handleStringInput(False)

  print("Digite a data de cadastro")
  data = handleStringInput(False)

  print("Digite o status da ordem de serviço")
  status = handleStringInput(False)
  

def create():
  pass

def edit():
  pass

def delete():
  pass

def show():
  pass