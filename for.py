print("Quantos vendedores fazem parte da equipe? ")
vendedores = int(input())
print("Quantos dias serão análisados? ")
dias = int(input())
TotalDeVendas = 0
MaiorVendedor = 0
vencedor = ""
MaiorVendaDia = 0

for v in range (vendedores):
    nome = input('Qual o seu nome: ')

    total_vendedor = 0.0
    folga = 0

    for dia in range(dias):
        print("Qual o valor vendido no dia " + str(dia + 1) +":")
        valor = float(input())
        
        

        total_vendedor = total_vendedor + valor
        media = total_vendedor / dias
        if valor == 0:
            folga = folga + 1

        if valor > MaiorVendaDia:
            MaiorVendaDia = valor
 
    TotalDeVendas = TotalDeVendas + total_vendedor
    print('\nSeu nome é: ',nome)
    print('Seu valor total vendido na semana foi: ',total_vendedor)
    print("A sua média de venda diária nessa semana foi: ", media)
    print("Essa semana você folgou: ",folga," dias\n")
    
    if total_vendedor > MaiorVendedor:
        MaiorVendedor = total_vendedor
        vencedor = nome 

print("\nRelátorio da equipe: ")
print("\nTotal de venda da equipe foi: ",TotalDeVendas)
print("O funcionário que mais vendeu na semana foi: ",vencedor)
print("A maior venda em um único dia foi", MaiorVendaDia)
