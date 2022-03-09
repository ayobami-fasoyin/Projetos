"""  
Atualmente, os professores do departamento de Ciência da Computação (CIC) da UnB tem estado bastante preocupados
com o alto índice de evasão de seus cursos. Visando diagnosticar o problema, estamos examinando os dados obtidos
através do censo do ensino superior, fornecidos ao público no site do governo federal. Ainda não sabemos a utili-
dade desses dados para diagnosticar evasão, mas certamente eles fornecem informações interessantes ou no mínimo 
curiosas sobre o perfil desses alunos.

Neste trabalho, você deve escrever um programa que explora esses dados, fornecendo algumas informações sobre nossos
alunos. Para tal, serão usados dados do censo mais recente, que foi publicado em 2019 e conta com dados referentes a 
2018.

Para facilitar seu trabalho, a base de dados nacional (que contém mais de 3 GB com informações sobre mais de 12 milhões
de alunos) foi processada para extrair somente algumas informações sobre alunos dos cursos do CIC. Os dados serão forne-
cidos ao seu programa usando o seguinte formato:

T (número inteiro que indica qual tarefa deve desempenhar)
N (número de linhas que serão fornecidas para o programa)
NU_ANO_INGRESSO NU_DIA_NASCIMENTO NU_MES_NASCIMENTO NU_ANO_NASCIMENTO TP_SEXO TP_SITUACAO
    ...
    .
    .
"""


from datetime import date

T = int(input())

lista_alunos = list()

for _ in range(int(input())):
    numero = input().split()

    aluno = {}
    aluno["NU_ANO_INGRESSO"] = int(numero[0]) # ano em que o aluno ingressou na UnB
    aluno["NU_DIA_NASCIMENTO"] = int(numero[1]) # dia de nascimento (expresso com até 2 dígitos)
    aluno["NU_MES_NASCIMENTO"] = int(numero[2]) # mês de nascimento (expresso numericamente com até 2 dígitos)
    aluno["NU_ANO_NASCIMENTO"] = int(numero[3]) # ano de nascimento (expresso com 4 dígitos)
    aluno["TP_SEXO"] = int(numero[4]) # indicador de sexo do aluno
    aluno["TP_SITUACAO"] = int(numero[5]) # situação do aluno no curso

    lista_alunos.append(aluno)

# Porcentagem de alunos regulares e não regulares
if T == 1:
    aluno_regular = 0
    aluno__nao_regular = 0
    for aluno in lista_alunos:
        if aluno["TP_SITUACAO"] == 6 or aluno["TP_SITUACAO"] == 2:
            aluno_regular += 1
        else:
            aluno__nao_regular += 1
    
    total = aluno_regular + aluno__nao_regular
    matriculados = (aluno_regular/total) * 100
    outros = (aluno__nao_regular/total) * 100
    
    print(f'matriculados ou formados:{matriculados:5.1f}')
    print(f'alunos em outras situacoes:{outros:5.1f}')

# Porcentagem de alunos do sexo masculino e feminino
elif T == 2:
    aluno_masculino = 0
    aluno_feminino = 0
    for aluno in lista_alunos:
        if aluno["TP_SEXO"] == 1:
            aluno_feminino += 1
        else:
            aluno_masculino += 1
    
    total = aluno_masculino + aluno_feminino
    aluno_masculino = (aluno_masculino/total) * 100
    aluno_feminino = (aluno_feminino/total) * 100
    
    print(f'sexo masculino:{aluno_masculino:5.1f}')
    print(f'sexo feminino:{aluno_feminino:5.1f}')

# Tempo médio (em anos) desde que o aluno ingressou no curso
elif T == 3:
    N = 0
    total_alunos = 0
    for aluno in lista_alunos:
        tempo_ingresso = 2019 - aluno["NU_ANO_INGRESSO"]
        N = N + tempo_ingresso
        total_alunos += 1
    
    tempo_medio = N/total_alunos
    
    print(f'media de anos desde ingresso:{tempo_medio:5.1f}')        

# Histograma percentual de dia da semana em que os alunos nasceram
elif T == 4:
    alunos_segunda = 0
    alunos_terca = 0
    alunos_quarta = 0
    alunos_quinta = 0
    alunos_sexta = 0
    alunos_sabado = 0
    alunos_domingo = 0
    
    for aluno in lista_alunos:
        data_nascimento = date(aluno["NU_ANO_NASCIMENTO"], aluno["NU_MES_NASCIMENTO"], aluno["NU_DIA_NASCIMENTO"])
        dia_semana = data_nascimento.weekday()
        if dia_semana == 0:
            alunos_segunda += 1
        elif dia_semana == 1:
            alunos_terca += 1
        elif dia_semana == 2:
            alunos_quarta += 1
        elif dia_semana == 3:
            alunos_quinta += 1
        elif dia_semana == 4:
            alunos_sexta += 1
        elif dia_semana == 5:
            alunos_sabado += 1
        else:
            alunos_domingo += 1
    
    total = alunos_domingo + alunos_segunda + alunos_terca + alunos_quarta + alunos_quinta + alunos_sexta + alunos_sabado
    alunos_domingo = (alunos_domingo/total) * 100 
    alunos_segunda = (alunos_segunda/total) * 100
    alunos_terca = (alunos_terca/total) * 100
    alunos_quarta = (alunos_quarta/total) * 100
    alunos_quinta = (alunos_quinta/total) * 100
    alunos_sexta = (alunos_sexta/total) * 100
    alunos_sabado = (alunos_sabado/total) * 100
    
    print(f'domingo:{alunos_domingo:5.1f}')
    print(f'segunda:{alunos_segunda:5.1f}')
    print(f'terca:{alunos_terca:5.1f}')
    print(f'quarta:{alunos_quarta:5.1f}')
    print(f'quinta:{quinta:5.1f}')
    print(f'sexta:{alunos_sexta:5.1f}')
    print(f'sabado:{alunos_sabado:5.1f}')

# Percentuais de alunos regulares e não regulares, separados em alunos masculinos e femininos
elif T == 5:
    feminino_regular = 0
    feminino_nao_regular = 0
    masculino_regular = 0
    masculino_nao_regular = 0
    
    for aluno in lista_alunos:
        if aluno["TP_SEXO"] == 1:
            if aluno["TP_SITUACAO"] == 2 or aluno["TP_SITUACAO"] == 6:
                feminino_regular += 1
            else:
                feminino_nao_regular += 1
        else:
            if aluno["TP_SITUACAO"] == 2 or aluno["TP_SITUACAO"] == 6:
                masculino_regular += 1
            else:
                masculino_nao_regular += 1
    
    print('dentre masculinos:')
    
    total_masculino = masculino_nao_regular + masculino_regular
    porcentagem_masculino_regulares = 100 * (masculino_regular / total_masculino)
    porcentagem_masculino_nao_regulares = 100 * (masculino_nao_regular / total_masculino)
    
    print(f'matriculados ou formados:{porcentagem_masculino_regulares:5.1f}')
    print(f'alunos em outras situacoes:{porcentagem_masculino_nao_regulares:5.1f}')
    
    print('dentre femininos:')
    
    total_feminino = feminino_nao_regular + feminino_regular
    porcentagem_feminino_regulares = (feminino_regular / total_feminino) * 100
    porcentagem_feminino_nao_regulares = (feminino_nao_regular / total_feminino) * 100
    
    print(f'matriculados ou formados:{porcentagem_feminino_regulares:5.1f}')
    print(f'alunos em outras situacoes:{porcentagem_feminino_nao_regulares:5.1f}')

# Tempo médio de curso separado em alunos regulares e não-regulares
elif T == 6:
    alunos_matriculados = 0
    alunos_outros = 0
    total_matriculados = 0
    total_outros = 0
    
    for aluno in lista_alunos:
        if aluno["TP_SITUACAO"] == 2 or aluno["TP_SITUACAO"] == 6:
            tempo_ingresso = 2019 - aluno["NU_ANO_INGRESSO"]
            alunos_matriculados = tempo_ingresso + alunos_matriculados
            total_matriculados += 1
        else:
            tempo_ingresso = 2019 - aluno["NU_ANO_INGRESSO"]
            alunos_outros = tempo_ingresso + alunos_outros
            total_outros += 1
    
    media_alunos_outros = (alunos_outros/total_outros) 
    media_alunos_matriculados = (alunos_matriculados/total_matriculados)
    
    print('dentre matriculados ou formados:')
    print(f'media de anos desde ingresso:{media_alunos_matriculados:5.1f}')
    print(f'dentre alunos em outras situacoes:')
    print(f'media de anos desde ingresso:{alunos_outros:5.1f}')

# Histograma percentual do dia da semana em que os alunos nasceram dividos por sexo            
else:
    feminino_segunda = 0
    feminino_terca = 0
    feminino_quarta = 0
    feminino_quinta = 0
    feminino_sexta = 0
    feminino_sabado = 0
    feminino_domingo = 0
    masculino_segunda = 0
    masculino_terca = 0
    masculino_quarta = 0
    masculino_quinta = 0
    masculino_sexta = 0
    masculino_sabado = 0
    masculino_domingo = 0
    
    for aluno in lista_alunos:
        data_nascimento = date(aluno["NU_ANO_NASCIMENTO"], aluno["NU_MES_NASCIMENTO"], aluno["NU_DIA_NASCIMENTO"])
        dia_semana = data_nascimento.weekday()
        if aluno["TP_SEXO"] == 1:
            if dia_semana == 0:
                feminino_segunda += 1
            elif dia_semana == 1:
                feminino_terca += 1
            elif dia_semana == 2:
                feminino_quarta += 1
            elif dia_semana == 3:
                feminino_quinta += 1
            elif dia_semana == 4:
                feminino_sexta += 1
            elif dia_semana == 5:
                feminino_sabado += 1
            else:
                feminino_domingo += 1
        else:
            if dia_semana == 0:
                masculino_segunda += 1
            elif dia_semana == 1:
                masculino_terca += 1
            elif dia_semana == 2:
                masculino_quarta += 1
            elif dia_semana == 3:
                masculino_quinta += 1
            elif dia_semana == 4:
                masculino_sexta += 1
            elif dia_semana == 5:
                masculino_sabado += 1
            else:
                masculino_domingo += 1
    
    feminino_total = feminino_segunda + feminino_terca + feminino_quarta + feminino_quinta + feminino_sexta + feminino_sabado + feminino_domingo
    masculino_total = masculino_segunda + masculino_terca + masculino_quarta + masculino_quinta + masculino_sexta + masculino_sabado + masculino_domingo
    
    print('dentre masculinos:')
    print(f'domingo:{((masculino_domingo/masculino_total)*100):5.1f}\nsegunda:{((masculino_segunda/masculino_total)*100):5.1f}\nterca:{((masculino_terca/masculino_total)*100):5.1f}\nquarta:{((masculino_quarta/masculino_total)*100):5.1f}\nquinta:{((masculino_quinta/masculino_total)*100):5.1f}\nsexta:{((masculino_sexta/masculino_total)*100):5.1f}\nsabado:{((masculino_sabado/masculino_total)*100):5.1f}')
    print('dentre femininos:')
    print(f'domingo:{((feminino_domingo/feminino_total)*100):5.1f}\nsegunda:{((feminino_segunda/feminino_total)*100):5.1f}\nterca:{((feminino_terca/feminino_total)*100):5.1f}\nquarta:{((feminino_quarta/feminino_total)*100):5.1f}\nquinta:{((feminino_quinta/feminino_total)*100):5.1f}\nsexta:{((feminino_sexta/feminino_total)*100):5.1f}\nsabado:{((feminino_sabado/feminino_total)*100):5.1f}')
