 #input é uma função que permite perguntar algo ao usuário
nome = input("Qual é o seu nome?")

'''
Bloco
de
Comentário
Permite que várias limhas se tornem um comentário
'''

print("Olá", nome, ". Tudo bem com você ?")
print("Alteração depois de clonado")

print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
print("Tipo da var c: ", type(c))
print("Tipo da var d: ", type(d))

a = 20
print("a: ", a)
b = "São Paulo"
print("b: ", b)
print("Tipo de var a: ", type(a))
print("Tipo de var b: ", type(b))

a = input("informe um número: ")
b = input("informe outro número: ")
print("a: ", a, " - b:", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b
print("c:", c)
print("Tipo da var c: ", type(c))
d = int(a)
print("d:", d)
print("Tipo da var d: ", type(d))

a = int(input("informe um número: "))
b = int(input("informe outro número: "))
print("a: ", a, " - b:", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b
print("c:", c)
print("Tipo da var c: ", type(c))

a = float(input("informe um número: "))
b = float(input("informe outro número: "))
print("a: ", a, " - b:", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b
print("c:", c)
print("Tipo da var c: ", type(c))