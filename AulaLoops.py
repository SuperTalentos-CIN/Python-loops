for i in range(5):
   print(f"{i+1}° colocado")

# iterar sobre uma lista com frutas
frutas = ["maçã", "banana", "laranja"]

print(frutas[2])
for fruta in frutas:
   print(f"Eu gosto de {fruta}")

#len = length
for i in range(len(frutas)):
   print(f"Fruta: {frutas[i]}")


print("1.3 Loop for com range() (início, fim, passo)")
range(2, 10, 2) # -> começa no 2, vai até ao 9, saltando de 2 em 2
for i in range(2, 11, 2):
   if i % 2 == 0:
       print(f"Número par: {i}")

   print(f"Número par, que legal\n")


print("1.4 Iterar sobre uma String") # Strings são listas disfarçadas
palavra = "Python" # ['p','y','t','h','o','n']

for letra in palavra:
   print(f"Letra: {letra}")

for i in range(len(palavra) - 3): # length = comprimento
   print(f"Letra: {palavra[i]}")


# ========Loop while=======
print(" LOOP WHILE")

#O loop while executa enquanto a condição for verdadeira
contador = 15
while contador < 20:
  print(f"Contador atual: {contador}")
  contador += 1  # Crucial: atualizar a variável para evitar loops infinitos


print("CONTROLES DE LOOP (break e continue)")

#print("3.1 Uso do 'break'")
# O 'break' serve para sair do loop imediatamente
for numero in range(10):
   if numero == 5:
       print("Encontrei o 5! Interrupção do loop")
       break
   print(f"Número: {numero}")

print(" 3.2 Uso do 'continue' ")

# O 'continue' serve para saltar a iteração atual e passar para a próxima
for numero in range(5):
    if numero == 2:
        print("A saltar o número 2...")
        continue
    print(f"Número: {numero}")




print(" 'ELSE' EM LOOPS")
# Em Python, os loops podem ter um bloco 'else'.
# Ele é executado apenas se o loop terminar normalmente (sem o uso do 'break').

print("--- 4.1 Loop a terminar normalmente ---")
for i in range(3):
    if i == 1:
        break
    print(f"Iteração {i}")
else:
    print("O loop terminou sem interrupções.")

print("4.2 Loop interrompido com break")
for i in range(3):
    if i == 1:
        break
    print(f"Iteração {i}")
else:
    print("Esta mensagem não vai aparecer, pois o loop foi interrompido.")


print(" LOOPS ANINHADOS (conhecido em inglês como Nested Loops)")

# Um loop dentro de outro loop
adjetivos = ["vermelha", "doce"]
frutas = ["maçã", "cereja"]

for adj in adjetivos:
    for fruta in frutas:
        print(f"A {fruta} é {adj}")


