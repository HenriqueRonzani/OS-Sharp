from os import system
import ctypes

def cls():
  try:
    system("cls")
  except:
    pass

def warningBox(title: str, message: str):
  try:
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x00001000 | 0x00000000 | 0x00000030)
  except:
    print(f"{title}\n{message}")

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
        warningBox("Erro", "Você deve digitar um número positivo")
      else:
        break
    except: 
      type_ = "real" if isFloat else "inteiro"
      warningBox("Erro", f"Você deve digitar um número {type_} para prosseguir")
  
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

def gatherData(fields: list) -> dict:
  data = {}
  for field in fields:
    print(f"Digite {field}")
    data[field] = handleStringInput(False)
  return data