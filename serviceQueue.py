from utils import cls
from utils import warningBox
from utils import handleNumericInput

def main(data):
  [employees, serviceOrders] = data
  cls()
  while True:
    print("Você deseja visualizar a fila de atendimento por funcionários ou por ordens de serviço?\n")
    print("Por funcionários 1 | Por ordens de serviço 2")
    print("Digite X | Voltar ao menu principal\n")

    userInput = input()

    if userInput == "1":
      showByEmployee(employees, serviceOrders)

    elif userInput == "2":
      showByOrder(employees, serviceOrders)

    elif userInput.upper() == "X":
      break
    else:
      warningBox("Erro", "Você deve digitar uma das opções do menu")

    cls()
  return [employees, serviceOrders]

def showByEmployee(employees, serviceOrders):
  cls()
  while True:
    ordersByEmployee = {}
    i = 0
    for employeeNumber in employees:
      i += 1
      employee = employees[employeeNumber]
      orders = []

      for orderNumber in serviceOrders:
        order = serviceOrders[orderNumber]
        if order["employee"] == employeeNumber:
          orders.append(orderNumber)

      print(i, f" | O funcionário {employee['Nome']} está responsável pelas ordens: {', '.join(str(order) for order in orders)}")

      ordersByEmployee[employeeNumber] = orders

    print("\nDigite o número de um funcionário para visualizar as ordens de serviço")
    print("Digite X | Voltar ao menu anterior\n")

    userInput = handleNumericInput(False, True, True)

    if userInput == "quit":
      break
    elif userInput in employees:
      cls()
      employeeOrders = ordersByEmployee[userInput]
      for orderNumber in employeeOrders:
        order = serviceOrders[orderNumber]
        print(f"Ordem de serviço {orderNumber}:")
        for key in order:
          if key == "employee":
            print(f"Funcionário responsável: {employees[order[key]]['Nome']}")
          else:
            print(f"{key}: {order[key]}")
        print()
      input("Pressione Enter para continuar")
      break
    else:
      warningBox("Erro", "Você deve digitar um número de funcionário válido")

    cls()

def showByOrder(employees, serviceOrders):
  cls()
  for orderNumber in serviceOrders:
    order = serviceOrders[orderNumber]
    employee = employees[order["employee"]]["Nome"] if order["employee"] != "Não atribuído" else "Não atribuído"
    print(f"Ordem de serviço {orderNumber}: Funcionário responsável: {employee}")
    print()
  
  input("Pressione Enter para continuar")

      