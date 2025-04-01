import mysql.connector
from datetime import datetime
import re
from constantes import Detalhes, Geral, Header, Trailer
from mysql_connect import Connection

def formatar_campo(value, length, pad_char=' ', align_left=True):
    #Formata o campo para o comprimento especificado, preenchendo com pad_char se necessário.
    if align_left:
        return str(value).ljust(length, pad_char)[:length]
    return str(value).rjust(length, pad_char)[:length]

def remover_caracteres_especiais(texto):
    #Remove caracteres especiais acentuados e converte para caracteres ASCII.
    # Mapeamento de caracteres acentuados para seus equivalentes sem acento
    mapeamento = {
        r"(á|à|ã|â|ä)": "a",
        r"(Á|À|Ã|Â|Ä)": "A",
        r"(é|è|ê|ë)": "e",
        r"(É|È|Ê|Ë)": "E",
        r"(í|ì|î|ï)": "i",
        r"(Í|Ì|Î|Ï)": "I",
        r"(ó|ò|õ|ô|ö)": "o",
        r"(Ó|Ò|Õ|Ô|Ö)": "O",
        r"(ú|ù|û|ü)": "u",
        r"(Ú|Ù|Û|Ü)": "U",
        r"(ñ)": "n",
        r"(Ñ)": "N"
    }

    # Para cada padrão no mapeamento, substituímos os caracteres no texto
    for padrao, substituto in mapeamento.items():
        texto = re.sub(padrao, substituto, texto)

    # Retorna o texto sem acentos
    return texto

def criar_zeros():
    raise NotImplementedError()

def formatar_data(data: str) -> str:
    data_formatada = datetime.strptime(str(data), "%Y-%m-%d").strftime("%d%m%y")
    return formatar_campo(data_formatada, 6)  # Garante 6 caracteres

def criar_header():
    #Cria o header do arquivo CNAB 400.

    header = "".join([
        Header.TIPO_REGISTRO,
        Header.COD_REMESSA,
        formatar_campo(*Header.LIT_REMESSA),
        Header.COD_SERVICO,
        formatar_campo(*Header.LIT_SERVICO),
        formatar_campo(*Header.COD_EMPRESA),
        formatar_campo(*Header.RAZAO_SOCIAL),
        Header.NUM_BANCO,
        formatar_campo(*Header.NOME_BANCO),
        Header.DATA_GRAVACAO,
        Header.BRANCO_ANTES_ID,
        Header.ID_SISTEMA,
        Header.SEQUENCIAL_REMESSA,
        Header.BRANCO_DEPOIS_SEQ,
        Header.SEQUENCIAL_REGISTRO
    ])
    return formatar_campo(header, 400, pad_char=' ', align_left=True)

def criar_detalhes(boletos):
    #Cria os registros de detalhe para o arquivo CNAB 400 com base no layout especificado, incluindo o número sequencial.
    detalhes = ""
    numero_sequencial = 1  # Número sequencial inicial

    for boleto in boletos:
        try:
            # Certifique-se de que o valor é um número antes de multiplicar
            valor_titulo = int(float(boleto[9]) * 100)  # Valor do Título em centavos (13 caracteres)
            valor_multa = int(float(boleto[10]) * 100)  # Valor da Multa (12 caracteres)
            
            # Converta as datas para o formato ddmmyy
            data_vencimento = formatar_data(boleto[6])
            data_emissao = formatar_data(boleto[7])
            data_limite_desconto = formatar_data(boleto[8])

            # Separar o CEP e sufixo do CEP
            cep_completo = boleto[15].strip()
            cep = cep_completo[:5]  # primeiros 5 caracteres (CEP)

            sufixo_cep = cep_completo[6:9] if len(cep_completo) >= 8 else cep_completo[5:8]

            # Ajusta o comprimento do CEP e do sufixo
            cep = cep.ljust(5, '0')
            sufixo_cep = sufixo_cep.ljust(3, '0')

            # Remover caracteres especiais dos campos relevantes
            nome_pagador = remover_caracteres_especiais(boleto[12])
            cpf_cnpj_pagador = remover_caracteres_especiais(boleto[13])
            endereco_completo = remover_caracteres_especiais(boleto[14]).upper()

            detalhe = "".join([
                Detalhes.TIPO_REGISTRO,
                formatar_campo(*Detalhes.AGENCIA_DEB),
                formatar_campo(*Detalhes.DIGITO_AG_DEBITO),
                formatar_campo(*Detalhes.RAZAO_CONT_COR),
                formatar_campo(*Detalhes.CONT_COR),
                formatar_campo(*Detalhes.DIGITO_CONT_COR),
                formatar_campo(boleto[0],*Detalhes.EMPRESA_BENEFICIARIA),
                formatar_campo(boleto[1],*Detalhes.N_CONTROLE_PARTICIPANTES),
                Detalhes.COD_BANCO,
                Detalhes.MULTA,
                formatar_campo(*Detalhes.PERC_MULTA),
                formatar_campo(boleto[0],*Detalhes.IDENT_TITULO),
                Detalhes.DIGITO_AUTOCOF,
                formatar_campo(*Detalhes.DESCONTO_BENEF),
                Detalhes.EMISSAO_PAPELETA,
                Detalhes.IDENT_BOLETO_DEB_AUT,
                Detalhes.IDENT_OP_BANCO,
                Detalhes.INDIC_RATEIO,
                Detalhes.ENDERE_AVISO_DEB_AUT,
                formatar_campo(*Detalhes.QNTD_PAG),
                formatar_campo(*Detalhes.IDENT_OCORRENCIA),
                formatar_campo(boleto[0],*Detalhes.N_DOCUMENT),
                data_vencimento,
                formatar_campo(valor_titulo,*Detalhes.VALOR_TITULO),
                Detalhes.BANCO_ENCARRE_COBRANCA,
                Detalhes.AGENCIA_DEP,
                Detalhes.ESPECIE_TITULO,
                Detalhes.IDENTIFICACAO,
                data_emissao,
                Detalhes.P_INSTRUCAO,
                Detalhes.S_INSTRUCAO,
                formatar_campo(valor_multa,*Detalhes.COBRANCA_ATRASO),
                data_limite_desconto,
                formatar_campo(int(float(boleto[11]) * 100),*Detalhes.VALOR_DESCONTO),
                formatar_campo(*Detalhes.VALOR_IOF),
                formatar_campo(*Detalhes.VALOR_ABATIMENTO),
                Detalhes.IDENTIFICACAO_TIPO,
                formatar_campo(cpf_cnpj_pagador,*Detalhes.N_INSCRICAO_PAGADOR),
                formatar_campo(nome_pagador,*Detalhes.NOME_PAGADOR),
                formatar_campo(endereco_completo,*Detalhes.ENDERECO_COMPLETO),
                formatar_campo(cep,*Detalhes.CEP),
                formatar_campo(sufixo_cep,*Detalhes.SUFIXO_CEP),
                Detalhes.MENSAGEM,
                Detalhes.BENEFICIARIO_FINAL,
                formatar_campo(str(numero_sequencial),*Detalhes.N_SEQUENCIAL)
            ])

            detalhe = formatar_campo(detalhe, 400) + "\n"
            detalhes += detalhe

            numero_sequencial += 1  # Incrementa o número sequencial para o próximo registro

        except Exception as e:
            if len(detalhe) != 400:
                raise ValueError(f"Tamanho do detalhe inválido: {len(detalhe)}")
            raise ValueError(f"Erro ao processar o boleto: {boleto}. Erro: {e}") 
    return detalhes

def criar_trailer(num_detalhes):
    # Cria o trailer do arquivo CNAB 400.
    trailer = "".join([
        Trailer.TIPO_REGISTRO,
        Trailer.ZEROS_FIXOS,
        formatar_campo(num_detalhes + 1, *Trailer.NUM_LINHAS_ARQUIVOS)  # +1 para incluir o trailer
    ])

    if len(trailer) != 400:
        raise ValueError(f"Tamanho do trailer inválido: {len(trailer)}")
    return trailer

def gerar_cnab400_bradesco():
    try:
        # Conectar ao banco de dados MySQL
        conect = Connection(Geral.HOST, Geral.DATABASE, Geral.USER, Geral.PASSWORD)
        
        # Consultar os dados do banco de dados para o ciclo específico
        conect.SELECT("*").FROM("tab_boletos").WHERE(f"id_ciclos = {Geral.MES_COMPETENCIA}").EXECUTE()
        
        boletos = conect.cursor.fetchall()
        if not boletos:
            print(f"Não foram encontrados boletos para o ciclo {Geral.MES_COMPETENCIA}.")
            return

        header = criar_header()
        detalhes = criar_detalhes(boletos)
        trailer = criar_trailer(len(boletos))

        # Geração do arquivo
        with open(Geral.CAMINHO_ARQUIVO, "w", encoding='ascii') as arquivo:
            str_final = f"{header}\n{detalhes}{trailer}"
            arquivo.write(str_final)

        print(f"Arquivo CNAB 400 para o ciclo {Geral.MES_COMPETENCIA} gerado com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco de dados: {err}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        # Fechar a conexão com o banco de dados
        if conect.connection.is_connected():
            conect.connection.close()

# Executa a função para gerar o arquivo
gerar_cnab400_bradesco()
# -https://www.ne12.bradesconetempresa.b.br/ibpjlogin/login.jsf?nscnn=2-
