print("Quantos vendedores fazem parte da equipe? ")
vendedores = int(input())
print("Quantos dias serão análisados? ")
dias = int(input())



for v in range (vendedores):
    nome = input('Qual o seu nome: ')

    total_vendedor = 0.0
    folga = 0
    TotalDeVendas = 0

    
    for dia in range(dias):
        print("Qual o valor vendido no dia " + str(dia + 1) +":")
        valor = float(input())
        
        total_vendedor = total_vendedor + valor
        media = total_vendedor / dias
        TotalDeVendas = TotalDeVendas + total_vendedor
        if valor == 0:
            folga = folga + 1

    print('\nSeu nome é: ',nome)
    print('Seu valor total vendido na semana foi: ',total_vendedor)
    print("A sua média de venda diária nessa semana foi: ", media)
    print("Essa semana você folgou: ",folga," dias\n")
   
print("\nRelátorio da equipe: ")
print("Total de venda da equipe",TotalDeVendas)
