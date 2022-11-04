from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

#Padrão para enviar email (assunto, to, from)
from email.mime.multipart import MIMEMultipart 
#Corpo do email (texto)
from email.mime.text import MIMEText
#Recebe uma imagem para anexar no email
from email.mime.image import MIMEImage 
import smtplib


with open('template.html', 'r') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='SeuNome', data=data) # Safe_substitute é usado para não apresentar o erro, mas vai mostrar a variavel
    
    
msg = MIMEMultipart()
# Email que vai enviar
msg['from'] = meu_email 
# Email que vai receber
msg['to'] = 'destino_email'    
# Titulo
msg['subject'] = 'ATENÇÃO: Teste para validar o código' 

corpo = MIMEText(corpo_msg, 'html')
# Envia o corpo do email
msg.attach(corpo) 

with open('guerra.jpg', 'rb') as img:   # rb = modo de leitura de bytes
    img =  MIMEImage(img.read())
    # Envia a imagem
    msg.attach(img) 


with smtplib.SMTP(host='host_smtp', port=porta) as smtp:  # Configure o smtp de acordo com o seu servidor de email
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user=meu_email, password=minha_senha)
    smtp.send_message(msg)
    
    print('E-mail enviado com sucesso')