from utils import cls
from utils import handleNumericInput
from utils import warningBox

from workOrder import main as manageOrders
from employee import main as manageEmployees
from serviceQueue import main as manageServiceQueue
from generatePDF import main as generatePDF

def main(): 
  cls()
  mainMenu()

def mainMenu():
  options = {
      1: manageOrders,
      2: manageEmployees,
      3: manageServiceQueue,
      4: generatePDF
    }
  
  employees = []
  serviceOrders = {}
  serviceQueue = {}
  
  while True:  

    print("Bem-vindo ao OS#")
    print("Escolha uma das opções do menu\n")
    print("Digite 1 | Gerenciar ordens de serviço")
    print("Digite 2 | Gerenciar gerenciar funcionários e atribuições")
    print("Digite 3 | Filas de atendimento por funcionário")
    print("Digite 4 | Gerar PDF de ordens de serviços")
    print("Digite X | Sair\n")

    userInput = handleNumericInput(False, True, True)

    if userInput in options:
      toRun = options[userInput]
      [ employees, serviceOrders, serviceQueue ] = toRun( [ employees, serviceOrders, serviceQueue ] )

    elif userInput == "quit":
      break

    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")
      
    cls()

main()