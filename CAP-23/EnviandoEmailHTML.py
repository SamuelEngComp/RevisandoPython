import smtplib
from email.mime.text import MIMEText

##Enviar email com imgem
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime

import email.message

smtpHostSSL = "smtp.gmail.com"
smtpHostPorta = 465

usuario = "cafezinhonuts@gmail.com"
senha = "cervantes33"

dataDoEvento = datetime.datetime.now()
mes = dataDoEvento.month
ano = dataDoEvento.year
dia = dataDoEvento.day
hora = dataDoEvento.hour
minutos = dataDoEvento.minute




destinoDoEmail = ["samuellima810@gmail.com"] #"thiagosantanadias84@gmail.com","jeffbassan@gmail.com",

conteudoDoEmail = "<html lang='en'><head><meta http-equiv='X-UA-Compatible' content='ie=edge'><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='Content-Type' content='text/html; charset=utf-8'><title>NUTS-COFFE</title><style type='text/css'>a {color: #d80a3e;}body, #header h1, #header h2, p {margin: 0; padding: 0;}#main {border: 1px solid #cfcece;} img {display: block;}#top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }#header h1 {color: #ffffff !important; font-family: 'Lucida Grande', sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }#header p {color: #ffffff !important; font-family: 'Lucida Grande', 'Lucida Sans', 'Lucida Sans Unicode', sans-serif; font-size: 12px;  }h5 {margin: 0 0 0.8em 0;}h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }p {font-size: 12px; color: #444444 !important; font-family: 'Lucida Grande', 'Lucida Sans', 'Lucida Sans Unicode', sans-serif; line-height: 1.5;}</style></head>"\
    "<body><table width='100%' cellpadding='0' cellspacing='0' bgcolor='e4e4e4'><tr><td><table id='main' width='600' align='center' cellpadding='0' cellspacing='15' bgcolor='ffffff'><tr><td><table id='header' cellpadding='10' cellspacing='0' align='center' bgcolor='8fb4e9'><tr><td width='570' align='center'  bgcolor='#0f0f0f'><h1>EU QUERO CAFE</h1></td></tr></table></td></tr><tr><td><table id='content-3' cellpadding='0' cellspacing='0' align='center'><tr><td width='250' valign='top' bgcolor='d0d0d0' style='padding:5px;'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2kCn9W8Ktsk1omhj2gCJwhc08zmzP3IH3mTOTjW9z6I_RJAyfKQ' width='250' height='150' /></td><td width='15'></td></tr></table></td></tr><tr><td><table id='content-4' cellpadding='0' cellspacing='0' align='center'><tr><td width='200' valign='top'><h5>Cafe Crocodilo Dante</h5><p></p></td><td width='15'></td></tr></table></td></tr></table></td></tr> </table></body></html>"

mensagem = email.message.Message()
mensagem['subject'] = "Esta na Hora do Café"
mensagem['from'] = usuario
mensagem['to'] = ', '.join(destinoDoEmail)
mensagem.add_header('Content-Type','text/html')
mensagem.set_payload(conteudoDoEmail + "Parabens - Thiago !!!! Voce foi sorteado")

servidor = smtplib.SMTP_SSL(smtpHostSSL, smtpHostPorta)
servidor.login(usuario, senha)
servidor.sendmail(usuario, destinoDoEmail,mensagem.as_string())
print("E-mail enviado com sucesso !!! ")
servidor.quit()