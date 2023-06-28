from tqdm import tqdm
import time
print("Ligando a máquina...")
for x in tqdm(range(100)):
    time.sleep(0.02)

Read = 10 
Write = 11  
Load = 20  
Store = 21  
Add = 30  
Subtract = 31  
Divide = 32
Multiply = 33
Branch = 40  
Branchneg = 41 
Branchzero = 42  
Halt = 43 

MP = [0]*100
ACC = 0
conteudo = 0
end = 0
i = 0

print("------------------------------------------------------------------------------------------------")
print("|                     Por favor, escolha uma instrução ou dado por célula,                     |")
print("|          Digite -99 para encerrar o endereçamento das células e iniciar o programa.          |")
print("------------------------------------------------------------------------------------------------")
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
    conteudo = int(input(f"Célula {end}: "))
    if conteudo != -99:
        MP[end] = conteudo
    end += 1

print("INICIANDO SISTEMA...")
for x in tqdm(range(100)):
    time.sleep(0.03)


while i != 43:
    codigo_operacao = int(MP[i])//100
    operando = int(MP[i]) % 100
  
    if codigo_operacao == Write:
        print("Escrevendo")
        for x in tqdm(range(100)):
            time.sleep(0.02)
        MP[operando] = int(
            input(f'\nO que deseja escrever na célula {operando}: '))

    if codigo_operacao == Read:
        print("Lendo")
        for x in tqdm(range(100)):
            time.sleep(0.02)
        print(MP[operando])

    if codigo_operacao == Load:
        print(f"Carregando dado da MP para o ACC: {MP[operando]}")
        for x in tqdm(range(100)):
            time.sleep(0.02)
        ACC = MP[operando]
        print(f"ACC = {ACC}")

    if codigo_operacao == Store:
        print(f"Guardando dado do ACC para a célula: {ACC}")
        for x in tqdm(range(100)):
            time.sleep(0.02)
        MP[operando] = ACC
        print(f"Célula {operando} = {MP[operando]}")

    if codigo_operacao == Add:
        print(f"Somando: {ACC} + {MP[operando]}")
        for x in tqdm(range(100)):
            time.sleep(0.01)
        ACC += MP[operando]

    if codigo_operacao == Subtract:
        print(f"Subtraindo: {ACC} - {MP[operando]}")
        for x in tqdm(range(100)):
            time.sleep(0.01)
        ACC -= MP[operando]

    if codigo_operacao == Multiply:
        print(f"Multiplicando: {ACC} * {MP[operando]}")
        for x in tqdm(range(100)):
            time.sleep(0.01)
        ACC *= MP[operando]

    if codigo_operacao == Divide:
        print(f"Dividindo: {ACC} / {MP[operando]}")
        for x in tqdm(range(100)):
            time.sleep(0.01)
        if MP[operando] != 0:
            ACC /= MP[operando]

        else:
            print('Divisão por zero é indefinida')

    if codigo_operacao == Branch:
        if 0 <= operando <= 99:
            print("Fazendo Jump")
            for x in tqdm(range(100)):
                time.sleep(0.01)
            i = operando
            continue

    if codigo_operacao == Branchzero:
        print("Se o conteúdo do ACC = 0, fazer Jump")
        for x in tqdm(range(100)):
            time.sleep(0.01)
        if 0 <= operando <= 99 and ACC == 0:
            i = operando
            continue
        

    if codigo_operacao == Branchneg:
        print("Se o conteúdo do ACC for negativo, fazer Jump")
        for x in tqdm(range(100)):
            time.sleep(0.01) 
        if 0 <= operando <= 99 and ACC < 0:  
            i = operando
            continue
        

    if codigo_operacao == Halt:
        print("FIM DO PROGRAMA")
        break
      
    i += 1