n1= int(input('Digite um número:'))
n2= int(input('Digite um número:'))
n3= int(input('Digite um número:'))
n4= int(input('Digite um número:'))
soma=n1+n2+n3+n4
media=soma/4
menor = min(n1, n2, n3, n4)
maior = max(n1, n2, n3, n4)
print(f'A média aritmética é: {media} ')
print(f'A diferença entre o menor e o maior número é: {maior-menor} ')