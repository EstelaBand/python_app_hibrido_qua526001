# declaração de dicionário
veiculo = {
    'fabricante': "Chevrolet",
    'modelo': "Chevette",
    'ano': 1973,
    'cor': "branco",
    'placa': "DF-1973"
}

# exibe os dados
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

# usuário escolhe o campo que deseja mudar
while True:
    campo = input("Informe o nome do campo que deseja alterar ou digita 'sair' para encerrar o programa: ").strip().lower()
    
    match campo:
        case "fabricante":
            veiculo['fabricante'] = input("Informe o novo valor de 'fabricante': ").strip()
        case "modelo":
            veiculo['modelo'] = input("Informe o novo valor de 'modelo': ").strip()
        case "ano":
            veiculo['ano'] = int(input("Informe o novo valor de 'ano': ").strip())
        case "cor":
            veiculo['cor'] = input("Informe o novo valor de 'cor': ").strip()  
        case "placa":
            veiculo['placa'] = input("Informe o novo valor de 'placa': ").strip()
        case "sair":
            break
        case _:
            print("Valor inválido.")
            continue
    #mostra na tela os novos valores
    for chave in veiculo:
        print(f"{chave.capitalize()}: {veiculo[chave]}")
                 