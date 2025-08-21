import pandas as pd
tabela = pd.read_excel('GincanaPlanilha.csv.xlsx', header=1)
tabela = tabela.rename(columns={'Genêro' : 'Gênero'})
tabela = tabela.rename(columns={"Coluna1": "Faturamento"})

def decidindo():
    print(' (0 para encerrar)')
    print(' -1 para Faturamento Geral\n -2 para Média do Faturamento Geral\n -3 para valor total de cada equipe\n -4 valor médio de cada equipe')
    print(' -5 para Faturamento Alunos\n -6 para Aluno com o maior Faturamento\n -7 para Aluno com o menor Faturamento')
    print(' -8 para Faturamento Estados\n -9 Estado para com maior Faturamento\n -10 para Estado com menor Faturamento')
    print(' -11 para Faturamento de cada Gênero')

def analisando():
    print('---------------------------------------TABELA GERAL---------------------------------------')
    print(tabela)
    decidindo()
    while True:
        escolha = str(input(' opção : '))
        if escolha == '0':
            print('Encerrando o programa...')
            break
        elif escolha == '1':
            print('------Faturamento Geral------')
            valor_total = tabela.groupby('Time')['Faturamento'].sum()
            print(f"Total Geral: R$ {valor_total.sum():,.2f}")
        elif escolha == '2':
            print('------Média do Faturamento Geral')
            media_geral = tabela.groupby('Time')['Faturamento'].mean()
            print(f"Total Geral: R$ {media_geral.mean():,.2f}")
        elif escolha == '3':
            print('------valor total de cada equipe------')
            valor_total_equipe = tabela.groupby('Time')['Faturamento'].sum()
            print(valor_total_equipe)
        elif escolha == '4':
            print('------valor médio de cada equipe------')
            valor_medio_equipe = tabela.groupby('Time')['Faturamento'].mean()
            print(valor_medio_equipe)
        elif escolha == '5':
            print('------Faturamento Alunos-----')
            aluno_maior_valor = tabela.groupby('Nome')['Faturamento'].max()
            aluno_maior = aluno_maior_valor.sort_values(ascending=False)
            print(aluno_maior)
        elif escolha == '6':
            print('------Aluno com o maior Faturamento------')
            print(aluno_maior.head(1))
        elif escolha == '7':
            print('------Aluno com menor Faturamento------')
            print(aluno_maior.tail(1))
        elif escolha == '8':
            print('------Faturamento Estados------')
            estado_faturamento_valor = tabela.groupby('Estado')['Faturamento'].sum()
            estado_faturamento = estado_faturamento_valor.sort_values(ascending=False)
            print(estado_faturamento)
        elif escolha == '9':
            print('------Estado com maior Faturamento------')
            print(estado_faturamento.head(1))
        elif escolha == '10':
            print('------Estado com menor Faturamento------')
            print(estado_faturamento.tail(1))
        elif escolha == '11':
            print('------Faturamento de cada Gênero------')
            genero_faturamento = tabela.groupby('Gênero')['Faturamento'].sum()
            print(genero_faturamento)

analisando()








