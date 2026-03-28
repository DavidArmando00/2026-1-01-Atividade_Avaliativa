n1= int(input('Digite um número:'))
n2= int(input('Digite um número:'))
n3= int(input('Digite um número:'))
n4= int(input('Digite um número:'))
soma= n1+n2+n3+n4
media=soma/4
print(f'O valor da média é: {media}')
if media >= 6:
    print(f'Média maior/igual a 6. Aluno aprovado.')
else:
    print(f'Média menor que 6. Aluno reprovado.')
