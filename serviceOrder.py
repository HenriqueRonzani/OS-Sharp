from utils import cls
from utils import warningBox
from utils import handleNumericInput
from utils import gatherData

def main(data):
  cls()
  
  [ employees, serviceOrders ] = data

  options = {
    "1": creatingOrder,
    "2": selectOrder,
    "3": listOrders,
  }
  while True:
    print("Gerenciar ordens de serviço")
    print("Escolha uma das opções do menu\n")
    print("Digite 1 | Cadastrar nova ordem de serviço")
    print("Digite 2 | Editar/Excluir ordem de serviço")
    print("Digite 3 | Listar ordem de serviço")
    print("Digite X | Voltar ao menu principal\n")
  
    userInput = input()
    if userInput in options:
      toRun = options[userInput]
      serviceOrders = toRun(serviceOrders, employees)
      data = [employees, serviceOrders]
    elif userInput.upper() == "X":
      break
    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")
      
    cls()

  return data

def creatingOrder(orders: dict, employees: dict) -> dict:
  order = gatherData(["nome do cliente",
                      "telefone do cliente",
                      "produto", 
                      "defeito",
                      "data de cadastro",
                      "status do serviço"
                      ])

  if employees:
    cls()
    print("Selecione um funcionário para atender a ordem de serviço")

    for employeeNumber in employees:
      employee = employees[employeeNumber]
      print(f"{employeeNumber}: {employee['Nome']}")

    employeeNumber = handleNumericInput(False, True, False)
    order["employee"] = employeeNumber

  else:
    order["employee"] = "Não atribuído"
  
  if not orders:
    toSave = 1
  else:
    toSave = int(next(reversed(orders), 0)[-1]) + 1

  orders["000" + str(toSave)] = order

  return orders

def selectOrder(orders: dict, employees: dict) -> dict:
  cls()
  if not orders:
    warningBox("Erro", "Não há ordens cadastradas")
    return orders
  while True:
    for orderNumber in orders:
      order = orders[f"{orderNumber}"]
      toPrint = [ f"{orderNumber}", 
                  order["nome do cliente"], 
                  order["produto"],
                  order["status do serviço"],
                ]
      toPrint.append(employees[order["employee"]]["Nome"] if order["employee"] != "Não atribuído" else "Não atribuído"),

      print(f"Ordem {toPrint[0]}: Nome do cliente: {toPrint[1]}, Produto: {toPrint[2]}, Status: {toPrint[3]}, Funcionário: {toPrint[4]}")


    print("Digite o número de qual ordem você deseja editar")
    orderNumber = input()

    if orderNumber not in orders:
      warningBox("Erro", "Ordem não encontrada")
    else:
      orders = modifyOrder(orders, orderNumber, employees)
      break

    cls()

  return orders

def modifyOrder(orders: dict, orderNumber: int, employees: dict) -> dict:
  cls()
  while True:
    print("Ordem " + orderNumber)
    print("\nO que você deseja fazer?")
    print("Editar 1 | Excluir 2\n")

    userInput = input()
    if userInput == "1":
      orders = editOrder(orders, orderNumber, employees)
      break
    elif userInput == "2":
      cls()
      orders.pop(orderNumber, None)
      break

    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")

  return orders

def editOrder(orders: dict, orderNumber: int, employees: dict) -> dict: 
  cls()
  fields = {
    "1": "nome do cliente",
    "2": "telefone do cliente",
    "3": "produto",
    "4": "defeito",
    "5": "data de cadastro",
    "6": "status do serviço",
    "7": "employee",
  }
  while True:
    order = orders[orderNumber]
    toPrint = [ 
                order[fields["1"]],
                order[fields["2"]],
                order[fields["3"]],
                order[fields["4"]],
                order[fields["5"]],
                order[fields["6"]],
              ]
    toPrint.append(employees[order["employee"]]["Nome"] if order["employee"] != "Não atribuído" else "Não atribuído")
    
    print(f"1 | Nome do cliente: {toPrint[0]}\n2 | Telefone do cliente: {toPrint[1]}\n3 | Produto: {toPrint[2]}\n4 | Defeito: {toPrint[3]}\n5 | Data de cadastro: {toPrint[4]}\n6 | Status do serviço: {toPrint[5]}\n7 | Funcionário: {toPrint[6]}\n")
    print("Digite o número do campo que deseja editar")

    fieldNumber = input()

    if fieldNumber in fields:
      cls()
      if fieldNumber == "7":
        if employees:
          print("Selecione um funcionário para atender a ordem de serviço")

          for employeeNumber in employees:
            employee = employees[employeeNumber]
            print(f"{employeeNumber}: {employee['Nome']}")

          employeeNumber = handleNumericInput(False, True, False)
          order["employee"] = employeeNumber
          break

        else:
          warningBox("Erro", "Não há funcionários cadastrados")
          break
      else:
        print(f"Digite o novo valor para {fields[fieldNumber]}")
        newValue = input()
        orders[orderNumber][fields[fieldNumber]] = newValue
        break
    else:
      warningBox("Erro", "Campo inválido, você deve digitar um dos números do menu")
    
    cls()
  return orders

def listOrders(orders: dict, employees: dict) -> dict:
  cls()

  for orderNumber in orders:
    order = orders[f"{orderNumber}"]
    toPrint = [ f"{orderNumber}", 
                order["nome do cliente"],
                order["telefone do cliente"],
                order["produto"],
                order["defeito"],
                order["data de cadastro"],
                order["status do serviço"],
              ]
    toPrint.append(employees[order["employee"]]["Nome"] if order["employee"] != "Não atribuído" else "Não atribuído")

    if "employee" in order and order["employee"] in employees:
        employeeName = employees[order["employee"]]['Nome']
    else:
        employeeName = "Não atribuído"
    toPrint.append(employeeName)

    print(f"Ordem {toPrint[0]}: Nome do cliente: {toPrint[1]}, Telefone: {toPrint[2]}, Produto: {toPrint[3]}, Defeito: {toPrint[4]}, Data: {toPrint[5]}, Status: {toPrint[6]}, Funcionário: {toPrint[7]}")

  input("\nDigite enter para sair")

  return orders