def ler_opcao():
    opcao = input("Escolha: ").strip()
    
    try: 
        opcao = int(opcao)
        return opcao
    
    except ValueError:
        print('Opção inválida! Digite apenas o número correspondete a sua opção')

    
    if isinstance(opcao, float):
        print('Opção inválida! Digite apenas o número correspondete a sua opção')

    else:
        return opcao