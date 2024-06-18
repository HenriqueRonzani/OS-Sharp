from utils import warningBox
from utils import cls
from utils import handleStringInput
from utils import handleNumericInput


def main(data: list):
  cls()
  options = {
    "1": creatingEmployee,
    "2": selectEmployee,
    "3": listEmployees,
  }

  [ employees, serviceOrders, serviceQueue ] = data

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

  return [ employees, serviceOrders, serviceQueue ]

def creatingEmployee(employees: list) -> list:
  cls()

  print("Digite o nome do funcionário")
  name = handleStringInput(False)

  employees.append(name)

  return employees

def selectEmployee(employees: list)-> list:
  cls()
  while True:
    for i, employee in enumerate(employees):
      print(f"{i + 1}: {employee}")

    print("Digite o número de qual funcionário você deseja editar")
    employeeNumber = handleNumericInput(False, True, False)

    if employeeNumber > len(employees):
      warningBox("Erro", "Funcionário não encontrado")
    else:
      employees = modifyEmployee(employees, employeeNumber - 1)
      break
    
    cls()

  return employees
    
def modifyEmployee(employees, employeeNumber: list) -> list:
  print(employees, employeeNumber, employees[employeeNumber])
  while True:
    print(employees[employeeNumber])
    print("Você deseja editar este funcionário ou deletar?")
    print("Editar 1 | Excluir 2")
    
    userInput = input()
    if userInput == "1":
      print("Digite o novo nome do funcionário")
      newName = handleStringInput(False)
      employees[employeeNumber] = newName
      break
    elif userInput == "2":
      employees.pop(employeeNumber)
      break
    else:
      warningBox("Erro", "Opção inválida, você deve digitar uma das opções do menu")

  return employees

def listEmployees(employees: list) -> None:
  cls()

  for employee in employees:
    print(f"Nome: {employee}")

  input("\nDigite enter para sair")

  return employees