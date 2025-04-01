from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os

# Encontra o caminho do arquivo .env e carrega as variáveis
env_path = find_dotenv("sql.env")
if env_path:
    load_dotenv(env_path, override=True)

class Geral:
    CAMINHO_ARQUIVO = os.getenv("CAMINHO_ARQUIVO")
    HOST = os.getenv("DB_HOST")
    DATABASE = os.getenv("DB_DATABASE")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    
    MES_COMPETENCIA = "62"  # Não sensível

class Header:
    TIPO_REGISTRO = "0" # 1
    COD_REMESSA = "1" #1
    LIT_REMESSA = ("REMESSA", 7) # 7 caracteres
    COD_SERVICO = "01"  # 2 caracteres
    LIT_SERVICO = ("COBRANCA", 15)  # 15 caracteres
    COD_EMPRESA = ("00000000000003721546", 20)  # 20 caracteres
    RAZAO_SOCIAL = ("GAFOR SA", 30)  # 30 caracteres
    NUM_BANCO = "237"  # 3 caracteres
    NOME_BANCO = ("BRADESCO", 15)  # 15 caracteres
    DATA_GRAVACAO = datetime.now().strftime("%d%m%y")  # 6 caracteres
    BRANCO_ANTES_ID = " " * 8  # 8 caracteres
    ID_SISTEMA = "MX"  # 2 caracteres
    SEQUENCIAL_REMESSA = f"{1:07}"  # 7 caracteres
    BRANCO_DEPOIS_SEQ = " " * 277  # 277 caracteres
    SEQUENCIAL_REGISTRO = f"{1:06}" # 6 caracteres

class Detalhes:
    TIPO_REGISTRO = "1"  # (1 caractere)
    AGENCIA_DEB = (5*"0", 5, "0", False)  # (5 caracteres) - Preencher com zeros se não usado
    DIGITO_AG_DEBITO = ("0", 1, "0", False)  # (opcional) (1 caractere) - Preencher com zeros se não usado
    RAZAO_CONT_COR = (5*"0", 5, "0", False)  # (opcional) (5 caracteres) - Preencher com zeros se não usado
    CONT_COR = (6*"0", 7, "0", False)  # (opcional) (7 caracteres) - Preencher com zeros se não usado
    DIGITO_CONT_COR = ("0", 1, "0", False)  # (1 caractere) - Preencher com zeros se não usado
    EMPRESA_BENEFICIARIA = (17, "0", False)  # (17 caracteres)
    N_CONTROLE_PARTICIPANTES = (25, " ", True)  # (25 caracteres)
    COD_BANCO = "237"  # Código do Banco (3 caracteres)
    MULTA = "0"  # (1 caractere) - Sem multa (0)
    PERC_MULTA = (4*"0", 4, "0", False)  # (4 caracteres)
    IDENT_TITULO = (11, "0", False)  # (11 caracteres)
    DIGITO_AUTOCOF =  "0"  # (1 caractere)
    DESCONTO_BENEF = (10*"0", 10, "0", False)  # (10 caracteres)
    EMISSAO_PAPELETA = "1"  # (1 caractere)
    IDENT_BOLETO_DEB_AUT = "N"  # (1 caractere)
    IDENT_OP_BANCO =  " " * 10  # Identificação da Operação do Banco (10 caracteres)
    INDIC_RATEIO = " "  # (opcional) (1 caractere)
    ENDERE_AVISO_DEB_AUT = " "  # (opcional) (1 caractere)
    QNTD_PAG = ("01", 2, "0", False)  # Quantidade de Pagamentos (2 caracteres)
    IDENT_OCORRENCIA = (2*"0", 2, "0", False)  # Identificação da Ocorrência (2 caracteres)
    N_DOCUMENT = (10, "0", False)  # Nº do Documento (10 caracteres)
    # Data do Vencimento do Título (6 caracteres)
    VALOR_TITULO = (13, "0", False)  # (13 caracteres)
    BANCO_ENCARRE_COBRANCA = 3*"0"  # (3 caracteres)
    AGENCIA_DEP = 5*"0"  # (5 caracteres)
    ESPECIE_TITULO = "01"  # (2 caracteres)
    IDENTIFICACAO = "N"  # (1 caractere)
    # Data da Emissão do Título (6 caracteres)cnab 
    P_INSTRUCAO = 2*"0"  # 1ª Instrução (2 caracteres)
    S_INSTRUCAO = 2*"0"  # 2ª Instrução (2 caracteres)
    COBRANCA_ATRASO = (13, "0", False)  # Valor a ser Cobrado por Dia de Atraso (13 caracteres)
    # Data Limite P/Concessão de Desconto (6 caracteres)
    VALOR_DESCONTO = (13, "0", False)  # (13 caracteres)
    VALOR_IOF = (13*"0", 13, "0", False)  # (13 caracteres)
    VALOR_ABATIMENTO = (13*"0", 13, "0", False)  # (13 caracteres)
    IDENTIFICACAO_TIPO = "01"  # Identificação do Tipo de Inscrição do Pagador (2 caracteres)
    N_INSCRICAO_PAGADOR = (14, "0", False)  # Nº(14 caracteres)
    NOME_PAGADOR = (40, " ", True)  # (40 caracteres)
    ENDERECO_COMPLETO = (40, " ", True)  # (40 caracteres)
    CEP = (5, "0", False)  # (5 caracteres)
    SUFIXO_CEP = (3, "0", False)  # (3 caracteres)
    MENSAGEM = " " * 12  # Mensagem 1 (12 caracteres)
    BENEFICIARIO_FINAL = " " * 60  # Beneficiário Final ou 2ª Mensagem (60 caracteres)
    N_SEQUENCIAL = (6, "0", False)  # Nº Sequencial do Registro (6 caracteres)

class Trailer:
    TIPO_REGISTRO = "9"  # Tipo de Registro (1 caractere)
    ZEROS_FIXOS = "0" * 393  # Zeros (Fixos) (393 caracteres)
    NUM_LINHAS_ARQUIVOS = (6, "0", False)  # Número de Linhas do Arquivo (6 caracteres)

