from datetime import date

T = int(input())

lista_alunos = list()

for _ in range(int(input())):
    numero = input().split()

    aluno = {}
    aluno["NU_ANO_INGRESSO"] = int(numero[0])
    aluno["NU_DIA_NASCIMENTO"] = int(numero[1])
    aluno["NU_MES_NASCIMENTO"] = int(numero[2])
    aluno["NU_ANO_NASCIMENTO"] = int(numero[3])
    aluno["TP_SEXO"] = int(numero[4])
    aluno["TP_SITUACAO"] = int(numero[5])

    lista_alunos.append(aluno)

if T == 1:
    regular = 0
    irregular = 0
    for aluno in lista_alunos:
        if aluno["TP_SITUACAO"] == 6 or aluno["TP_SITUACAO"] == 2:
            regular += 1
        else:
            irregular += 1
    total = regular + irregular
    matriculados = (regular/total) * 100
    outros = (irregular/total) * 100
    print(f'matriculados ou formados:{matriculados:5.1f}')
    print(f'alunos em outras situacoes:{outros:5.1f}')

elif T == 2:
    masculino = 0
    feminino = 0
    for aluno in lista_alunos:
        if aluno["TP_SEXO"] == 1:
            feminino += 1
        else:
            masculino += 1
    total = masculino + feminino
    masculino = (masculino/total) * 100
    feminino = (feminino/total) * 100
    print(f'sexo masculino:{masculino:5.1f}')
    print(f'sexo feminino:{feminino:5.1f}')

elif T == 3:
    N = 0
    i = 0
    for aluno in lista_alunos:
        a = 2019 - aluno["NU_ANO_INGRESSO"]
        N = N + a
        i += 1
    media = N/i
    print(f'media de anos desde ingresso:{media:5.1f}')        

elif T == 4:
    segunda = 0
    terca = 0
    quarta = 0
    quinta = 0
    sexta = 0
    sabado = 0
    domingo = 0
    for aluno in lista_alunos:
        data = date(aluno["NU_ANO_NASCIMENTO"], aluno["NU_MES_NASCIMENTO"], aluno["NU_DIA_NASCIMENTO"])
        dia_semana = data.weekday()
        if dia_semana == 0:
            segunda += 1
        elif dia_semana == 1:
            terca += 1
        elif dia_semana == 2:
            quarta += 1
        elif dia_semana == 3:
            quinta += 1
        elif dia_semana == 4:
            sexta += 1
        elif dia_semana == 5:
            sabado += 1
        else:
            domingo += 1
    total = domingo+segunda+terca+quarta+quinta+sexta+sabado
    domingo = (domingo/total) * 100
    segunda = (segunda/total) * 100
    terca = (terca/total) * 100
    quarta = (quarta/total) * 100
    quinta = (quinta/total) * 100
    sexta = (sexta/total) * 100
    sabado = (sabado/total) * 100
    print(f'domingo:{domingo:5.1f}')
    print(f'segunda:{segunda:5.1f}')
    print(f'terca:{terca:5.1f}')
    print(f'quarta:{quarta:5.1f}')
    print(f'quinta:{quinta:5.1f}')
    print(f'sexta:{sexta:5.1f}')
    print(f'sabado:{sabado:5.1f}')

elif T == 5:
    feminino_regular = 0
    feminino_irrgular = 0
    masculino_regular = 0
    masculino_irregular = 0
    for aluno in lista_alunos:
        if aluno["TP_SEXO"] == 1:
            if aluno["TP_SITUACAO"] == 2 or aluno["TP_SITUACAO"] == 6:
                feminino_regular += 1
            else:
                feminino_irrgular += 1
        else:
            if aluno["TP_SITUACAO"] == 2 or aluno["TP_SITUACAO"] == 6:
                masculino_regular += 1
            else:
                masculino_irregular += 1
    print('dentre masculinos:')
    total_masculino = masculino_irregular + masculino_regular
    mm = 100 * (masculino_regular / total_masculino)
    mi = 100 * (masculino_irregular / total_masculino)
    print(f'matriculados ou formados:{mm:5.1f}')
    print(f'alunos em outras situacoes:{mi:5.1f}')
    print('dentre femininos:')
    total_feminino = feminino_irrgular + feminino_regular
    fm = (feminino_regular / total_feminino) * 100
    fi = (feminino_irrgular / total_feminino) * 100
    print(f'matriculados ou formados:{fm:5.1f}')
    print(f'alunos em outras situacoes:{fi:5.1f}')
elif T == 6:
    matriculados = 0
    outras = 0
    k = 0
    m = 0
    for aluno in lista_alunos:
        if aluno["TP_SITUACAO"] == 2 or aluno["TP_SITUACAO"] == 6:
            a = 2019 - aluno["NU_ANO_INGRESSO"]
            matriculados = a + matriculados
            k += 1
        else:
            a = 2019 - aluno["NU_ANO_INGRESSO"]
            outras = a + outras
            m += 1
    media_outras = (outras/m) 
    media_matriculados = (matriculados/k)
    print('dentre matriculados ou formados:')
    print(f'media de anos desde ingresso:{media_matriculados:5.1f}')
    print(f'dentre alunos em outras situacoes:')
    print(f'media de anos desde ingresso:{media_outras:5.1f}')
            
else:
    fseg = 0
    fter = 0
    fqua = 0
    fqui = 0
    fsex = 0
    fsab = 0
    fdom = 0
    mseg = 0
    mter = 0
    mqua = 0
    mqui = 0
    msex = 0
    msab = 0
    mdom = 0
    for aluno in lista_alunos:
        data = date(aluno["NU_ANO_NASCIMENTO"], aluno["NU_MES_NASCIMENTO"], aluno["NU_DIA_NASCIMENTO"])
        dia_semana = data.weekday()
        if aluno["TP_SEXO"] == 1:
            if dia_semana == 0:
                fseg += 1
            elif dia_semana == 1:
                fter += 1
            elif dia_semana == 2:
                fqua += 1
            elif dia_semana == 3:
                fqui += 1
            elif dia_semana == 4:
                fsex += 1
            elif dia_semana == 5:
                fsab += 1
            else:
                fdom += 1
        else:
            if dia_semana == 0:
                mseg += 1
            elif dia_semana == 1:
                mter += 1
            elif dia_semana == 2:
                mqua += 1
            elif dia_semana == 3:
                mqui += 1
            elif dia_semana == 4:
                msex += 1
            elif dia_semana == 5:
                msab += 1
            else:
                mdom += 1
    ft = fseg + fter + fqua + fqui + fsex + fsab + fdom
    mt = mseg + mter + mqua + mqui + msex + msab + mdom
    print('dentre masculinos:')
    print(f'domingo:{((mdom/mt)*100):5.1f}\nsegunda:{((mseg/mt)*100):5.1f}\nterca:{((mter/mt)*100):5.1f}\nquarta:{((mqua/mt)*100):5.1f}\nquinta:{((mqui/mt)*100):5.1f}\nsexta:{((msex/mt)*100):5.1f}\nsabado:{((msab/mt)*100):5.1f}')
    print('dentre femininos:')
    print(f'domingo:{((fdom/ft)*100):5.1f}\nsegunda:{((fseg/ft)*100):5.1f}\nterca:{((fter/ft)*100):5.1f}\nquarta:{((fqua/ft)*100):5.1f}\nquinta:{((fqui/ft)*100):5.1f}\nsexta:{((fsex/ft)*100):5.1f}\nsabado:{((fsab/ft)*100):5.1f}')
