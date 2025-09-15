import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def enviar_email(destinatario, assunto, corpo, caminho_arquivo):
    email = "joao"
    senha = ""

    mensagem = MIMEMultipart()
    mensagem['From'] = email
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEApplication(open(caminho_arquivo, "rb").read(), Name='boleto.pdf'))

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(email, senha)
        servidor.sendmail(email, destinatario, mensagem.as_string())


enviar_email("mazzajp27@gmail.com", "Boleto Mensal", "Segue o boleto em anexo.", "/caminho/do/boleto.pdf")
