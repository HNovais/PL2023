import re

def printSaldo():
    global saldo
    novoSaldo = saldo * 100
    euros = novoSaldo // 100
    centimos = novoSaldo % 100
            
    return f"{int(euros)}e{int(centimos)}c"

def receberMoeads(coins):
    global saldo
    global moedas
    if re.match(r"(?i:moeda)", coins) != None:
        moedasInvalidas = []

        valores = re.findall(r"\d+e|\d+c", coins)

        for val in valores:
            if val in moedas:
                if val == "10c":
                    saldo += 0.1
                elif val == "20c":
                    saldo += 0.2
                elif val == "50c":
                    saldo += 0.5
                elif val == "1e":
                    saldo += 1
                else:
                    saldo += 2
            else:
                moedasInvalidas.append(val)

        if moedasInvalidas != None:
            for m in moedasInvalidas:
                print(f"maq: Moeda {m} inválida. Moedas aceites: 10c, 20c, 50c, 1e, 2e")


def pousarAuscultador(comando):
    global estado
    if re.match(r"(?i:pousar)", comando) != None:
        estado = "POUSAR"
        saldoFormatado = printSaldo()
        print(f"maq: O seu troco é {saldoFormatado}, volte sempre!")      


def abortarComando(comando):
    global saldo
    if re.match(r"(?i:abortar)", comando) != None:
        saldoFormatado = printSaldo()
        print(f"maq: A sua ação foi abortada, foram devolvidos {saldoFormatado}")   
        saldo = 0
            

def ligar(num):
    global saldo
    if re.match(r"T=\d", num) != None:
        str = re.findall(r"\d*", num)
        numero = str[2]

        if not re.match(r'^(\d{9}|\d{2}\d+)$', numero):
            print("maq: Número inválido")
    
        else: 
            if (re.match(r"601", numero) != None) or (re.match(r"641", numero) != None):
                print("maq: Chamada bloqueada")

            elif (re.match(r"00", numero) != None):
                if saldo >= 1.5:
                    saldo -= 1.5
                else:
                    print("maq: Saldo insuficiente para chamada internacional.")

            elif (re.match(r"2", numero) != None):
                if saldo >= 0.25:
                    saldo -= 0.25
                else:
                    print("maq: Saldo insuficiente para chamada nacional.")

            elif (re.match(r"800", numero) != None):
                None

            elif (re.match(r"800", numero) != None):
                if saldo >= 0.1:
                    saldo -= 0.1
                else:
                    print("maq: Saldo insuficiente para chamada azul.")
            
            else:
                print("maq: Número não permitido neste telefone.")


def main():
    global estado
    while(True):
        if estado == "INICIO":
            print("maq: Levante o auscultador para começar (LEVANTAR)")
            
            comando = input().strip().upper()

            if comando == "LEVANTAR":
                    estado = comando
            else:
                print("maq: Comando inválido")

        elif estado == "LEVANTAR":
            saldoFormatado = printSaldo()
            print(f"maq: Saldo = {saldoFormatado}")

            comando = input()

            receberMoeads(comando)
            pousarAuscultador(comando)
            abortarComando(comando)
            ligar(comando)

        else:
            break

estado = "INICIO"
saldo = 0
moedas = ["10c", "20c", "50c", "1e", "2e"]

main()

        