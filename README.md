<h1 align="center">CNAB 400 Generator - Bradesco</h1>

<p align="center">
  
![projeto_cnab](https://github.com/user-attachments/assets/c4470bca-a054-474e-a25d-692154669f72)

</p>

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

## 📑 Descrição do Projeto
Sistema de geração de arquivos CNAB 400 para integração com o Banco Bradesco, desenvolvido durante estágio. O projeto automatiza a criação de remessas bancárias seguindo as especificações oficiais do formato CNAB 400, incluindo:

- Geração de headers, detalhes e trailers
- Formatação precisa de campos numéricos e alfabéticos
- Conexão segura com base de dados MySQL
- Tratamento de caracteres especiais e acentuação

## 🛠️ Funcionalidades Principais
- **Geração de Arquivos CNAB 400**
  - Layout completo com Header, Detalhes e Trailer
  - Formatação automática de campos numéricos e datas
  - Validação de tamanho de registros
  - Sequencialização automática de registros

- **Integração com Banco de Dados**
  - Conexão segura usando MySQL Connector
  - Query builder customizado
  - Tratamento de erros de conexão

- **Segurança e Configuração**
  - Gestão de credenciais via .env
  - Validação de dados de entrada
  - Tratamento de caracteres especiais

- **Logs e Monitoramento**
  - Mensagens de status detalhadas
  - Validação de consistência de dados
  - Tratamento de exceções personalizado

## 🧰 Tecnologias Utilizadas
- **Linguagem:** Python 3.8+
- **Bibliotecas:**
  - mysql-connector-python
  - python-dotenv
  - datetime
  - re (Expressões Regulares)
- **Banco de Dados:** MySQL/MariaDB
- **Gestão de Configuração:** Dotenv (.env)

## 🤝 Fork o projeto.
- Crie uma nova branch (git checkout -b feature/nova-funcionalidade). </br>
- Faça commit de suas alterações (git commit -am 'Adicionando nova funcionalidade'). </br>
- Faça push para a branch (git push origin feature/nova-funcionalidade). </br>
- Abra um Pull Request.

## 📄 Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
