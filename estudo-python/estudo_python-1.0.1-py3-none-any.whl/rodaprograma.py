"""
Entrevistas e calculos de estatisticas.

Código em 4 partes:
1a.parte: ler arquivo json
2a.parte: entrevistas
3a.parte: IO disco
4a.parte: estatisticas e views
"""
from pkg_proj import meuprograma
import statistics
import json
from sh import gedit


def carrega_dados():
    """
    Carrega as informações do arquivo JSON.

    Popula a lista lista_entrevistados co instancias da classe
    entrevista com valores que vem do arquivo JSON.
    """
    global lista_entrevistados

    def pega_dados(obj):
        """
        Cria uma instancia uma nova entrevista

        Usa os dados vindos do JSON atraves do objeto 'obj'
        para nome, idade e ano_informado
        retorna a instancia Entrevista()
        """
        instancia = meuprograma.Entrevista(
            ano_infor=obj['ano'],
            idade=obj['idade'],
            nome=obj['nome']
        )
        return instancia

    # Ler arquivo JSON
    try:
        arquivo_json = open('dados.json', 'r')
        dados_json = json.load(arquivo_json)  # dict
        entrevistas = dados_json['Entrevistas']  # list
        lista_entrevistados = [
            pega_dados(entrevista) for entrevista in entrevistas
        ]

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def novos_dados():
    """
    Pergunta novos nomes e anos de nascimento.

    Enquanto o usúario não digitar 'p' ao perguntado pelo nome
    o programa perguntara o ano nascimento e calculara a idade.
    """
    pode_parar = False

    while not pode_parar:
        entrevistado = meuprograma.Entrevista()
        if entrevistado.pergunta_nome().lower() == "p":
            pode_parar = True
        else:
            try:
                entrevistado.pergunta_idade()
                # x = 1000 / 0
            except ZeroDivisionError:
                print("Lista foi salva")
                lista_entrevistados.append(entrevistado)
            except Exception as e:
                print(f"Ocorreu um erro a lista NÃO foi salva.")
                print(f"Ocorreu um erro tipo {type(e)}")
                print(f"A msg foi: {e}")
            else:
                lista_entrevistados.append(entrevistado)


def salvar_dados():
    """
    Salva as informações geradas IO disco em JSON.

    Converter o dicionario python para JSON e salva
    as informações da lista_entrevistados

    """

    lista_salvar = [
        dict(nome=obj.nome, ano=obj.ano_infor, idade=obj.idade)
        for obj in lista_entrevistados
    ]
    dic_salvar = {"Entrevistas": lista_salvar}
    dic_salvar = json.dumps(dic_salvar, indent=4, sort_keys=False)

    try:
        arquivo_json = open('dados.json', 'w')
        arquivo_json.write(dic_salvar)
        arquivo_json.close()

    except Exception as e:
        print(f"Erro: {e}")


def calcular_dados():
    """
    Calcula as estastisticas de idade

    Mostra a menor idade calculada
    Mostra a maior idade calculada
    Mostra a media das idades dos adultos
    """

    menor_idade = min([obj.idade for obj in lista_entrevistados])
    maior_idade = max([obj.idade for obj in lista_entrevistados])
    media_adultos = statistics.median_high(
        [obj.idade for obj in lista_entrevistados if obj.idade >= 18]
    )
    lista_decadas = [
        int(obj.ano_infor / 10) * 10 for obj in lista_entrevistados
    ]
    # dicionario que não se repete
    set_decadas = set(lista_decadas)
    # Dicionario compreesion
    qtd_nascimentos = {
        decadas: lista_decadas.count(decadas) for decadas in set_decadas
    }

    print(f"\nResultados:")
    print("-" * 40)
    print(f"""
        A quantidade de entrevistas: {len(lista_entrevistados)}
        A menor idade informadas : {menor_idade},
        A maior idade informadas : {maior_idade},
        A média das idades dos adultos (> 18): {media_adultos},
        \nA quantidade de nascimento por decadas: """)
    print("-" * 40)
    for decada, qtd in qtd_nascimentos.items():
        print(f"Decada {decada}: {qtd} nascimentos.")
    print('\n')

    resposta_ok = False
    while not resposta_ok:
        try:
            xpto = input("Deseja mostrar o arquivo? (s/n)")
            xpto = xpto[0].lower()
            if xpto == 's' or xpto == 'n':
                resposta_ok = True

        except Exception as e:
            print(e)
            continue

    if xpto == 's':
        gedit('dados.json')


def main():
    carrega_dados()
    novos_dados()
    salvar_dados()
    calcular_dados()

# python -m pip install twine
# python setup.py sdist
