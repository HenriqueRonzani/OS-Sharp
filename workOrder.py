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
    "3": show,
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
      serviceOrders = toRun(serviceOrders, employees)
    elif userInput.upper() == "X":
      break
    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")
      
    cls()

  return [ employees, serviceOrders, serviceQueue ]

def creatingOrder(orders: dict, employees: list, ) -> dict:
  order = gatherData(["nome do cliente",
                      "telefone do cliente",
                      "produto", 
                      "defeito",
                      "data de cadastro",
                      "status do serviço"
                      ])

  if employees:
    print("Selecione um funcionário para atender a ordem de serviço")

    for i, employee in enumerate(employees):
      print(f"{i + 1}: {employee}")
    employeeNumber = handleNumericInput(False, True, False)
    order["employee"] = int(employeeNumber - 1)

  else:
    order["employee"] = "Não atribuído"
  
  toSave = len(orders) + 1

  orders["000" + str(toSave)] = order

  return orders

def selectOrder(orders, employees: list) -> dict:
  for i in range(len(orders)):
    order = orders[f"000{i+1}"]
    toPrint = [ f"00{i+1}", 
                order["nome do cliente"], 
                order["produto"],
                order["status do serviço"],
                employees[order["employee"]],
              ]
    print(f"Ordem {toPrint[0]}: Nome do cliente: {toPrint[1]}, Produto: {toPrint[2]}, Status: {toPrint[3]} Funcionário: {toPrint[4]}")

  input()
  return orders
  

def delete():
  pass

def show(orders: dict, employees: list) -> dict:
  cls()

  for i in range(len(orders)):
    order = orders[f"000{i+1}"]
    toPrint = [ f"00{i+1}", 
                order["nome do cliente"], 
                order["produto"],
                order["status do serviço"],
                employees[order["employee"]],
              ]
    print(f"Ordem {toPrint[0]}: Nome do cliente: {toPrint[1]}, Produto: {toPrint[2]}, Status: {toPrint[3]} Funcionário: {toPrint[4]}")

  input("\nDigite enter para sair")

  return orders