## Variável resposável por abrir o arquivo 'dados_usuário.txt' com autoridade de modificá-lo
coleta_dado = open('dados_usuario.txt', 'a')

## Varável resposável pela condição do while
loop = True

##Mensagem convidativa no terminal
print("Olá! Gostaria de coletar seus dados inutilmente")

while(loop):

    ##Responsável por coletar os dados do usuário
    print("Qual seu nome?")
    nome = input("Resposta: ")

    print("Quantos anos você tem?")
    idade = input("Resposta: ")

    print("Qual seu número de telefone?")
    telefone = input("Resposta: ")

    print("Muito obrigado pelas informações!\nGostaria de nos fornecer mais dados? (sim/nao)")
    ask_continua = input("Resposta: ")

## Escreve no arquivo 'dados_clientes.txt' os dados coletados
    coleta_dado.write(f"\nNome: {nome} | Idade= {idade} | Telefone: {telefone}")

## Finaliza o loop, ou não, dependendo da resposta do usuário
    if(ask_continua == 'nao'):
        loop = False
        coleta_dado.close()

## Variável resposável por abrir o arquivo com autoridade de apenas ler
dados = open('dados_usuario.txt', 'r')

## Conta a quantidade de linhas no arquivo - 1 (o programa cria uma linha vazia no início do documento)
## e retorna a quantidade de linha de dados no terminal
print("Linhas totais de dados:", len(dados.readlines()) - 1)