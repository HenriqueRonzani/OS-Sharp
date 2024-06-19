from utils import warningBox
from utils import cls
from utils import handleStringInput
from utils import handleNumericInput
from utils import gatherData


def main(data: list):
  cls()
  options = {
    "1": creatingEmployee,
    "2": selectEmployee,
    "3": listEmployees,
  }

  [ employees, serviceOrders ] = data

  while True:
    print("Gerenciar funcionários")
    print("Escolha uma das opções do menu\n")
    print("Digite 1 | Cadastrar novo funcionário")
    print("Digite 2 | Editar/Excluir funcionário")
    print("Digite 3 | Listar funcionários")
    print("Digite X | Voltar ao menu principal\n")

    userInput = input()
    if userInput in options:
      toRun = options[userInput]
      employees = toRun(employees)
    elif userInput.upper() == "X":
      break
    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")
  
    cls()

  return [ employees, serviceOrders ]

def creatingEmployee(employees: dict) -> list:
  cls()

  employee = gatherData(["Nome"])

  toSave = next(reversed(employees), 0) + 1

  employees[toSave] = employee

  return employees

def selectEmployee(employees: dict) -> dict:
  cls()
  if not employees:
    warningBox("Erro", "Não há funcionários cadastrados")
    return employees
  while True:
    for employeeNumber in employees:
      employee = employees[employeeNumber]
      print(employeeNumber, f": {employee["Nome"]}")

    print("Digite o número de qual funcionário você deseja editar")
    employeeNumber = handleNumericInput(False, True, False)

    if employeeNumber not in employees:
      warningBox("Erro", "Funcionário não encontrado")
    else:
      employees = modifyEmployee(employees, employeeNumber)
      break
    
    cls()

  return employees
    
def modifyEmployee(employees: dict, employeeNumber: str) -> dict:
  cls()
  while True:
    print(employees[employeeNumber]["Nome"])
    print("Você deseja editar este funcionário ou deletar?")
    print("Editar 1 | Excluir 2\n")
    
    userInput = input()
    if userInput == "1":
      cls()
      print("Digite o novo nome do funcionário")
      newName = handleStringInput(False)
      employees[employeeNumber]["Nome"] = newName
      break
    elif userInput == "2":
      cls()
      employees.pop(employeeNumber, None)
      break
    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")

  return employees

def listEmployees(employees: list) -> None:
  cls()

  for employeeNumber in employees:
      employee = employees[employeeNumber]
      print(employeeNumber, f": {employee["Nome"]}")

  input("\nDigite enter para sair")
  
  return employees