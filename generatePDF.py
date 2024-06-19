from utils import cls
from utils import warningBox
from reportlab.pdfgen import canvas

def main(data):
  [employees, orders] = data
  cls()
  if not orders:
    warningBox("Erro", "Não há ordens de serviço cadastradas")
    return [employees, orders]
  while True:
    for orderNumber in orders:
      print(f"Ordem de serviço: {orderNumber}")
    print("\nDigite o número da ordem de serviço que deseja gerar o PDF")
    print("Digite X para voltar ao menu principal")
    userInput = input()

    if userInput in orders:
      order = orders[userInput]
      dataToPrint = [
        order["nome do cliente"],
        order["telefone do cliente"],
        order["produto"],
        order["defeito"],
        order["data de cadastro"],
        order["status do serviço"],
                    ]
      dataToPrint.append(employees[order["employee"]]["Nome"] if order["employee"] != "Não atribuído" else "Não atribuído");
      dataToPrint.append(userInput)

      generatePdf(dataToPrint)
      warningBox("Sucesso", "PDF gerado com sucesso na pasta pdfs")

    elif userInput.upper() == "X":
      break
    else:
      warningBox("Erro", "Ordem de serviço não encontrada")
    
    cls()

  return [employees, orders]

def generatePdf(dataToPrint):
  route = "./pdfs/"
  otherSide = 420.945

  c = canvas.Canvas(route+dataToPrint[7]+".pdf")
  
  c.setFont("Helvetica", 12)

  c.drawString(50, 350, f"Nome do cliente: {dataToPrint[0]}")
  c.drawString(50, 350+otherSide, f"Nome do cliente: {dataToPrint[0]}")

  c.drawString(350, 350, f"Telefone do cliente: {dataToPrint[1]}")
  c.drawString(350, 350+otherSide, f"Telefone do cliente: {dataToPrint[1]}")

  c.drawString(50, 300, f"Produto: {dataToPrint[2]}")
  c.drawString(50, 300+otherSide, f"Produto: {dataToPrint[2]}")

  c.drawString(350, 300, f"Defeito: {dataToPrint[3]}")
  c.drawString(350, 300+otherSide, f"Defeito: {dataToPrint[3]}")

  c.drawString(50, 250, f"Data de cadastro: {dataToPrint[4]}")
  c.drawString(50, 250+otherSide, f"Data de cadastro: {dataToPrint[4]}")

  c.drawString(350, 250, f"Status do serviço: {dataToPrint[5]}")
  c.drawString(350, 250+otherSide, f"Status do serviço: {dataToPrint[5]}")

  c.drawString(50, 200, f"Funcionário responsável: {dataToPrint[6]}")
  c.drawString(50, 200+otherSide, f"Funcionário responsável: {dataToPrint[6]}")

  c.setFont("Helvetica", 20)

  c.drawString(175, 80, f"Ordem de Serviço: {dataToPrint[7]}")
  c.drawString(175, 80+otherSide, f"Ordem de Serviço: {dataToPrint[7]}")

  c.line(0, 420.945, 595.276, 420.945)
  c.save()
