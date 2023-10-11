print("\n---------- CALCULO HORA HOMEM ----------\n")

# Ler a Quantidade de Gastos Mensais
listaGastosMensais = []
print("\n---------- QUANTIDADE DE GASTOS MENSAIS ----------\n")
quantidadeGastosMensais = int(input("Digite a quantidade de gastos mensais: "))
print("\n---------- VALOR DOS GASTOS MENSAIS ----------\n")
for i in range(quantidadeGastosMensais):
    gastoMensal = float(input("Digite o Valor do Gasto Mensal: "))
    listaGastosMensais.append(gastoMensal)

# Somar todos os Gastos Mensais
somaGastosMensais = sum(listaGastosMensais)

# Ler a Quantidade de Gastos Anuais
listaGastosAnuais = []
print("\n---------- QUANTIDADE DE GASTOS ANUAIS ----------\n")
quantidadeGastosAnuais = int(input("\nDigite a quantidade de gastos anuais: "))
print("\n---------- VALOR DOS GASTOS ANUAIS ----------\n")
for j in range(quantidadeGastosAnuais):
    gastoAnual = float(input("Digite o Valor do Gasto Anual: "))
    listaGastosAnuais.append(gastoAnual)

# Somar todos os Gastos Anuais
somaGastosAnuais = sum(listaGastosAnuais)
print(somaGastosAnuais)
resultadoGastosAnuais = somaGastosAnuais / 12

# Capturar as Horas de Trabalho
print("\n---------- HORAS DE TRABALHO ----------\n")
horasTrabalhoDia = int(input("\nQuantas horas você trabalha por dia?: "))
diasSemanas = int(input("Quantos dias na semana?: "))
horasTrabalhoTotal = horasTrabalhoDia * diasSemanas * 4

# Calcular a Hora Homem e Printar na Tela
horaHomem = (resultadoGastosAnuais + somaGastosMensais) / horasTrabalhoTotal
print("\n----------RESULTADO----------\n")
print("O seu valor de Hora Homem é: ", horaHomem, " R$\n")
print("---------- FIM ----------")
