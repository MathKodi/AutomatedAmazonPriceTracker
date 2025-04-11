# 🛒 Amazon Price Tracker with Email Alerts
Este script em Python realiza o monitoramento de preços de produtos da Amazon e envia um alerta por e-mail quando o valor de um item fica abaixo do desejado.

## 🔧 Tecnologias utilizadas
BeautifulSoup – Para extração dos dados da página do produto

requests – Para realizar requisições HTTP à Amazon

smtplib – Para envio automático de e-mails com alerta de preço

python-dotenv – Para gerenciar credenciais e variáveis sensíveis com segurança

## 📌 Como funciona
Você informa a URL de um produto da Amazon e o preço máximo que está disposto a pagar.

O script realiza uma requisição à página do produto e, com BeautifulSoup, extrai o preço atual.

O valor é comparado com o preço definido.

Se o preço do produto estiver igual ou inferior ao valor desejado, o script dispara automaticamente um e-mail de notificação.

## ✅ Requisitos
Conta de e-mail (Gmail, Outlook etc.) com autenticação habilitada

Arquivo .env com as seguintes variáveis:

MY_EMAIL – Seu endereço de e-mail

MY_PASSWORD – Senha ou App Password (para Gmail com 2FA)

SMTP_SERVER – Servidor SMTP 

SMTP_PORT – Porta 
