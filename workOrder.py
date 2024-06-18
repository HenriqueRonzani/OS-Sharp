from utils import cls
from utils import warningBox
from utils import handleNumericInput
from utils import gatherData

def main(data):
  cls()
  
  [ employees, serviceOrders, serviceQueue ] = data

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
      data = [employees, serviceOrders, serviceQueue]
    elif userInput.upper() == "X":
      break
    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")
      
    cls()

  cls()

def creatingOrder(orders: dict, employees: dict) -> dict:
  order = gatherData(["nome do cliente",
                      "telefone do cliente",
                      "produto", 
                      "defeito",
                      "data de cadastro",
                      "status do serviço"
                      ])

  if employees:
    print("Selecione um funcionário para atender a ordem de serviço")

    for employeeNumber in employees:
      employee = employees[employeeNumber]
      print(f"{employeeNumber}: {employee['Nome']}")

    employeeNumber = handleNumericInput(False, True, False)
    order["employee"] = employeeNumber

  else:
    order["employee"] = "Não atribuído"
  
  toSave = len(orders) + 1

  orders["000" + str(toSave)] = order

  return orders

def selectOrder(orders: dict, employees: dict) -> dict:
  cls()
  while True:
    for i in range(len(orders)):
      order = orders[f"000{i+1}"]
      if "employee" in order and order["employee"] in employees:
        employeeName = employees[order["employee"]]['Nome']
      else:
        employeeName = "Não atribuído"
      toPrint = [ f"00{i+1}", 
                  order["nome do cliente"], 
                  order["produto"],
                  order["status do serviço"],
                  employeeName
                ]
      print(f"Ordem {toPrint[0]}: Nome do cliente: {toPrint[1]}, Produto: {toPrint[2]}, Status: {toPrint[3]}, Funcionário: {toPrint[4]}")

    print("Digite o número de qual ordem você deseja editar")
    orderNumber = handleNumericInput(False, True, False)

    if orderNumber > len(orders):
      warningBox("Erro", "Ordem não encontrada")
    else:
      orders = modifyOrder(orders, orderNumber - 1, employees)
      break

    cls()

  return orders

def modifyOrder(orders: dict, orderNumber: int, employees: dict) -> dict:
  order = orders[f"000{orderNumber + 1}"]

  print("O que você deseja fazer?")
  print("Digite 1 | Editar ordem")
  print("Digite 2 | Excluir ordem")
  print("Digite X | Voltar")

  userInput = input()

  if userInput == "1":
    order = gatherData(["nome do cliente",
                        "telefone do cliente",
                        "produto", 
                        "defeito",
                        "data de cadastro",
                        "status do serviço"
                        ])
    if employees:
      print("Selecione um funcionário para atender a ordem de serviço")

      for employeeNumber in employees:
        employee = employees[employeeNumber]
        print(f"{employeeNumber}: {employee['Nome']}")

      employeeNumber = handleNumericInput(False, True, False)
      order["employee"] = employeeNumber

    else:
      order["employee"] = "Não atribuído"

    orders[f"000{orderNumber + 1}"] = order
  elif userInput == "2":
    order["employee"] = "Não atribuído"
    del orders[f"000{orderNumber + 1}"]

  return orders

def delete():
  pass

def listOrders(orders: dict, employees: dict) -> dict:
  cls()

  for orderNumber in orders:
    order = orders[f"{orderNumber}"]
    toPrint = [ f"{orderNumber}", 
                order["nome do cliente"], 
                order["produto"],
                order["status do serviço"],
              ]
    if "employee" in order and order["employee"] in employees:
        employeeName = employees[order["employee"]]['Nome']
    else:
        employeeName = "Não atribuído"
    toPrint.append(employeeName)

    print(f"Ordem {toPrint[0]}: Nome do cliente: {toPrint[1]}, Produto: {toPrint[2]}, Status: {toPrint[3]} Funcionário: {toPrint[4]}")

  input("\nDigite enter para sair")

  return orders