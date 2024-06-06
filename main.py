from utils import cls
from utils import handleNumericInput

def main(): 
   cls()
   mainMenu()

def mainMenu():
  while True:
    options = {
      1: manageOrders,
      2: manageEmployees,
      3: manageServiceQueue,
      4: generatePDF
    }

    print("Bem-vindo ao OS#")
    print("Escolha uma das opções do menu\n")
    print("Digite 1 | Gerenciar ordens de serviço")
    print("Digite 2 | Gerenciar gerenciar funcionários e atribuições")
    print("Digite 3 | Filas de atendimento por funcionário")
    print("Digite 4 | Gerar PDF de oordens de serviços")

    userInput = handleNumericInput(False, True, False)
    if userInput in options:
      newMenu = options[userInput]()
      newMenu
    else:
      cls()
      print("Opção inválida\n")

def manageOrders():
   return

def manageEmployees():
   return

def manageServiceQueue():
   return

def generatePDF():
   return

main()