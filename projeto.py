from tqdm import tqdm
import time

# print("Ligando a máquina...")
# for i in tqdm(range(100)):
#     time.sleep(0.05)

Read = 10  # Ler uma palavra do teclado e armazena na célula do operando
Write = 11  # Escreve o valor armazenado na célula do operando na tela
Load = 20  # Carrega no ACC o conteúdo da célula do operando
Store = 21  # Carrega do ACC o conteúdo para a célula do operando
Add = 30  # Soma o conteúdo salvo na célula do operando com o conteúdo do ACC
Subtract = 31  # Subtraí o conteúdo do ACC com o conteúdo do operando
Divide = 32
Multiply = 33
Branch = 40  # Desvia a leitura das instruções para a instrução de endereço do operando
Branchneg = 41  # Se o conteúdo do ACC for negativa, realiza um Branch
Branchzero = 42  # Se o conteúdo do ACC for 0, realiza um Branch
Halt = 43  # Encerra o programa

MP = [0]*18
ACC = 0
conteudo = 0
endereco = 0
i = 0
print("----------------------------------------------------------------------------------------------------")
print("|      Por favor, escolha uma instrução ou dado por célula, você pode pular essa parte usando      |")
print("|        a opção pré-estabelecida para poupar tempo: Digite -1 para usar a opção já feita          |")
print("|           Digite -99 para encerrar o endereçamento das células e iniciar o programa.             |")
print("----------------------------------------------------------------------------------------------------")

print("CÓDIGOS DE OPERAÇÃO:")
print("10: Read")
print("11: Write")
print("20: Load")
print("21: Store")
print("30: Add")
print("31: Subtract")
print("32: Divide")
print("33: Multiply")
print("40: Branch")
print("41: Branchneg")
print("42: Branchzero")
print("43: Halt")

while conteudo != -99:
    conteudo = int(input(f'Célula de endereço {endereco}: '))
    if conteudo != -99 or conteudo != -1:
        MP[endereco] = conteudo
    endereco += 1
    if conteudo == -1:
        MP[0] = 1017
        MP[1] = 1018
        MP[2] = 1019
        MP[3] = 2018
        MP[4] = 2120
        MP[5] = 3117
        MP[6] = 2121
        MP[7] = 2020
        MP[8] = 3018
        MP[9] = 2120
        MP[10] = 2021
        MP[11] = 3117
        MP[12] = 2121
        MP[13] = 4215
        MP[14] = 4007
        MP[15] = 1120
        MP[16] = 4300
        endereco = endereco + 16
        conteudo = int(input(f'Célula de endereço {endereco}: '))
        if conteudo != -99 or conteudo != -1 or conteudo != -3:
            MP[endereco] = conteudo
            print(MP)
        endereco += 1


# print("INICIANDO SISTEMA...")
# for i in tqdm(range(100)):
#     time.sleep(0.02)

while i != 43:
    codigo = int(MP[i])//100
    Operando = int(MP[i]) % 100
    if codigo == Read:
        MP[Operando] = int(
            input(f'\nDigite um valor para a célula {Operando}: '))
    if codigo == Write:
        print(MP[Operando])
    if codigo == Load:
        ACC = MP[Operando]
    if codigo == Store:
        MP[Operando] = ACC
    if codigo == Add:
        ACC += MP[Operando]
    if codigo == Subtract:
        ACC -= MP[Operando]
    if codigo == Multiply:
        ACC *= MP[Operando]
    if codigo == Divide:
        if MP[Operando] != 0:
            ACC /= MP[Operando]
        else:
            print('Divisão por zero é indefinida')
    if codigo == Branch:
        if 0 <= Operando <= 99:
            i = Operando
            continue
    if codigo == Branchzero:
        if 0 <= Operando <= 99 and ACC == 0:
            i = Operando
            continue
    if codigo == Branchneg:
        if 0 <= Operando <= 99 and ACC < 0:
            i = Operando
            continue
    if codigo == Halt:
        print('Programa Encerrado')
        break
    i += 1
print('Programa Encerrado')


# endereco0 = endereco1 = endereco2 = endereco3 = endereco4 = endereco5 = endereco6 = endereco7 = endereco8 = endereco9 = endereco10 = endereco11 = endereco12 = endereco13 = endereco14 = endereco15 = '000000'

# enderecos = ["0000", "0001", "0010", "0011", "0100", "0101", "0110",
#              "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111", "A", "B", "C", "D", "E", "F"]


# lista = []


# while True:
#     first = input(
#         "Digite L para listar a memória e W para escrever nela e S para iniciar processador: ")
#     if first == "W" or first == "w":
#         end = input(
#             "Escolha um endereço da memória de 0000 até F (1111) ou Esolha a opção de agrupamento já criada (1): ")
#         if end in enderecos:
#             pergunta = input(
#                 "O que deseja gravar neste endereço? OBS: | C. Op. & Endereço |  ou  | Dado |: ")
#             lista.append(pergunta)
#             if end == "0000":
#                 endereco0 = pergunta
#             elif end == "0001":
#                 endereco1 = pergunta
#             elif end == "0010":
#                 endereco2 = pergunta
#             elif end == "0011":
#                 endereco3 = pergunta
#             elif end == "0100":
#                 endereco4 = pergunta
#             elif end == "0101":
#                 endereco5 = pergunta
#             elif end == "0110":
#                 endereco6 = pergunta
#             elif end == "0111":
#                 endereco7 = pergunta
#             elif end == "1000":
#                 endereco8 = pergunta
#             elif end == "1001":
#                 endereco9 = pergunta
#             elif end == "1010" or end == "A":
#                 endereco10 = pergunta
#             elif end == "1011" or end == "B":
#                 endereco11 = pergunta
#             elif end == "1100" or end == "C":
#                 endereco12 = pergunta
#             elif end == "1101" or end == "D":
#                 endereco13 = pergunta
#             elif end == "1110" or end == "E":
#                 endereco14 = pergunta
#             elif end == "1111" or end == "F":
#                 endereco15 = pergunta
#             ordem = [endereco0, endereco1, endereco2, endereco3, endereco4, endereco5, endereco6, endereco7,
#                      endereco8, endereco9, endereco10, endereco11, endereco12, endereco13, endereco14, endereco15]
#         elif end == "1":
#             endereco0 = 1017
#             endereco1 = 1018

#     if first == "L" or first == "l":
#         print(f"0000 = {endereco0}")
#         print(f"0001 = {endereco1}")
#         print(f"0010 = {endereco2}")
#         print(f"0011 = {endereco3}")
#         print(f"0100 = {endereco4}")
#         print(f"0101 = {endereco5}")
#         print(f"0110 = {endereco6}")
#         print(f"0111 = {endereco7}")
#         print(f"1000 = {endereco8}")
#         print(f"1001 = {endereco9}")
#         print(f"1010 = {endereco10}")
#         print(f"1011 = {endereco11}")
#         print(f"1100 = {endereco12}")
#         print(f"1101 = {endereco13}")
#         print(f"1110 = {endereco14}")
#         print(f"1111 = {endereco15}")

#     if first == "S" or first == "s":
#         for valor in ordem:
#             valor = globals()[ordem.len(pergunta)]
#             if valor[0] == '1' and valor[1] == '0':
#                 print("Read")
#             elif valor[0] == '1' and valor[1] == '1':
#                 print("Write")
#             elif valor[0] == '2' and valor[1] == '0':
#                 print("Load")
#             elif valor[0] == '2' and valor[1] == '1':
#                 print("Store")
#             elif valor[0] == '3' and valor[1] == '0':
#                 print("Add")
#             elif valor[0] == '3' and valor[1] == '1':
#                 print("Subtract")
#             elif valor[0] == '3' and valor[1] == '2':
#                 print("Divide")
#             elif valor[0] == '3' and valor[1] == '3':
#                 print("Multiply")
#             elif valor[0] == '4' and valor[1] == '0':
#                 print("Branch")
#             elif valor[0] == '4' and valor[1] == '1':
#                 print("Branchneg")
#             elif valor[0] == '4' and valor[1] == '2':
#                 print("Branchzero")
#             elif valor[0] == '4' and valor[1] == '3':
#                 print("Halt")
#             else:
#                 print("Dado")
