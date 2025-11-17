def contar_vogais(a):
    vogais = 'aeiouAEIOU'
    soma=0
    for letra in a:
        if letra in vogais:
         soma+=1
    return soma
x=input("Digite a palavra desejada:  ")
conta=contar_vogais(x)
print(f"A palavra {x} contém {conta} vogais")