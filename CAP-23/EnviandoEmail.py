import smtplib
from email.mime.text import MIMEText

##Enviar email com imgem
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

imagem = open('crocodiloDante.png','rb')
imagemUtilizada = MIMEImage(imagem.read())

smtpHostSSL = "smtp.gmail.com"
smtpHostPorta = 465

usuario = "cafezinhonuts@gmail.com"
senha = "cervantes33"

#destinoDoEmail = ["thiagosantanadias84@gmail.com","jeffbassan@gmail.com"]
destinoDoEmail = 'samuellima810@gmail.com'
#mensagem = MIMEText("Os Senhores foram sorteados para preparar o café.")
mensagem = MIMEMultipart()
# mensagem
mensagem['subject'] = "Café Café"
mensagem['from'] = usuario
mensagem['to'] = ', '.join(destinoDoEmail)
mensagem.attach(imagemUtilizada)


servidor = smtplib.SMTP_SSL(smtpHostSSL, smtpHostPorta)
servidor.login(usuario, senha)
servidor.sendmail(usuario, destinoDoEmail,mensagem.as_string())
servidor.quit()
