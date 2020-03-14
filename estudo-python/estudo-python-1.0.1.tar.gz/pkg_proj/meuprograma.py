"""
Módulo que contém a classe entrevista

Esta classe será usada para instanciar e guardar cada entrevista
feita pelo programa mas aas entrevistas gurdadas em disco.

curso pela internet

url:
https://www.youtube.com/watch?v=uDW2mbWEQu8&list=PLV7VqBqvsd_3yRYYWrHkziPL6izzrUIkp&index=4
"""
import datetime


class Entrevista():
    """ Classe entrevista """

    def __init__(self, nome="", idade=0, ano_infor=0):
        """
        Entra com valores iniciais.

        Variáveis do sistema:

        Keyword Arguments:
            nome {str} -- [nome informado pelo entrevistado] (default: {""})
            idade {number} -- [idade calculada] (default: {0})
            ano_infor {number} -- [ano nascimento] (default: {0})
        """
        super(Entrevista, self).__init__()
        self.idade = idade
        self.nome = nome
        self.ano_infor = ano_infor

    def pergunta_nome(self):
        """ Pergunta o nome do entrevistado. Retorna String. """
        nome_ok = False
        while not nome_ok:
            self.nome = input("Qual é o seu nome? [p termina] ")
            if self.nome:
                nome_ok = True
                if self.nome.lower() != "p":
                    print(f"Nome: {self.nome}")

        self.nome = self.nome.title()  # pq é variavel de classe
        return self.nome

    def pergunta_idade(self):
        """[Pergunda o ano de nascimento]

        E valida o valoer entre 1900 e a data atual,
        calculado atraves datetime.date.today().year
        se, validado calcula a idade.
        """
        ano_atual = datetime.date.today().year
        ano_ok = False
        while not ano_ok:
            try:
                # Pergunta em que ano você nasceu
                self.ano_infor = int(
                    input(
                        f"Olá {self.nome}, em que ano você nasceu? "
                    )
                )
                ano_ok = True
            except Exception as e:
                print(e)
                continue
            else:
                if self.ano_infor >= 1900 and self.ano_infor <= ano_atual:
                    pass
                else:
                    ano_ok = False

        # Subtrair o ano informado do ano atual
        self.idade = ano_atual - self.ano_infor
        # Imprimir a idade
        print(f"Você tem {self.idade} anos")

    def __str__(self):
        """ Retorna uma descrição amigavel do objeto."""
        return f"{self.nome}/{self.idade}"

    def __repr__(self):
        """ Retorna uma descrição precisa e única do objeto. """
        return f"input()={self.nome} input()=int({self.idade})"
