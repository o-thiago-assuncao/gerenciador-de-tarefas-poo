dicionario={}
ct=0
soma=0
for n in range(4):
    chave=input("Digite o nome do produto :  ")
    valor=float(input("Digite o preço do produto digitado: "))
    dicionario[chave]=valor
    ct+=1
    soma=soma+valor
    if valor>=valor:
        print(f"O produto mais caro custa: {valor} e sua chave é {chave}")

media=soma/ct
print(f"O ticket médio dos produtos é: {media} ")
print(dicionario)