from os import system

def cls():
  try:
    system("cls")
  except:
    pass

def newRegister(currentData: list, newData: dict) -> dict:
  currentData.append(newData)
  #make possible validations here
  return newRegister

#
# Usage example:
#
# print("Digite sua idade")
# userInput = handleNumericInput(False, True, True)
# if userInput == "quit": -- handle quit --
# -- handle input --
#

def handleNumericInput(isFloat: bool, onlyPositive: bool, canQuit: bool) -> any:
  while True:
    userInput = input()
    
    if canQuit and userInput.upper() == "X": return "quit"

    try:
      number =  float(userInput) if isFloat else int(userInput)
      if number < 0 and onlyPositive:
        print("Você deve digitar um número positivo")
      else:
        break
    except: 
      type_ = "real" if isFloat else "inteiro"
      print(f"Você deve digitar um número {type_} para prosseguir")
  
  return number

#
# Usage Example
#
# print("Digite seu nome")
# userInput = handleStringInput(True)
# if userInput == "quit": -- handle quit --
# -- handle input --
#

def handleStringInput(canQuit: bool) -> str:

  userInput = input()

  if canQuit and userInput.upper() == "X":
    return "quit"
  
  return userInput